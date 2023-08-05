#!/usr/bin/env python

import sys
import json
from uuid import uuid4
from subprocess import check_output, CalledProcessError, DEVNULL
from os.path import isfile, isdir, exists, join, getsize
from os import environ as env
from pathlib import Path
from glob import glob
import logging
import asyncio
import webbrowser

import websockets
from websockets.exceptions import ConnectionClosedOK
import colorama
from tqdm import tqdm


logger = logging.getLogger('websockets')
logger.setLevel(logging.DEBUG if '--debug' in sys.argv else logging.INFO)
logger.addHandler(logging.StreamHandler())

MEGA_BYTE = 1024 ** 2
MINUTE = 60


class WebSocketClient:

    async def loop(self):
        try:
            async with websockets.connect(
                    self.websocket_url,
                    max_size=2 * MEGA_BYTE,
                    ping_interval=5 * MINUTE,
                    ping_timeout=5 * MINUTE,
                    ) as ws:
                self.ws = ws
                await self.on_open()
                while await self.on_message():
                    pass
        finally:
            await self.on_close()

    async def on_open(self):
        pass

    async def on_message(self):
        try:
            message = await self.ws.recv()
        except ConnectionClosedOK:
            return False

        message = json.loads(message)
        message_type = message.pop('type', None)
        handler = getattr(self, 'receive_' + message_type, None)
        if handler:
            await handler(**message)
            return True
        else:
            await self.receive_print(
                [
                    'Did not understand message from server:',
                    message_type,
                    message
                ],
                {'color': 'RED'}
            )
            return False

    async def on_close(self):
        pass

    # Data transmission

    async def send(self, **kwargs):
        await self.ws.send(json.dumps(kwargs))

    async def send_bytes(self, data):
        await self.ws.send(data)

    async def receive(self):
        return json.loads(await self.ws.recv())

    # Receivers

    async def receive_print(self, args, kwargs):
        color = kwargs.pop('color', None)
        if color:
            color = color and getattr(colorama.Fore, color, None)
            print(
                color + colorama.Style.BRIGHT + ':: ',
                end=colorama.Style.RESET_ALL
            )
        print(*args, **kwargs)


class Iskra(WebSocketClient):
    def __init__(self):
        self.read_configuration()
        self.argv = sys.argv[1:]
        self.websocket_url = env.get('ISKRA_API', 'wss://app.iskra.ml/api/cli')

    async def loop(self):
        command = self.argv[:1]

        # If first argument is a file run training
        if command and Path(command[0]).is_file():
            self.argv.insert(0, 'train')

        # Dispatch local command
        if command:
            command_handler = getattr(self, 'cmd_' + command[0], None)
            if command_handler:
                await command_handler(*sys.argv[2:])
                return

        await super().loop()

    # Configuration

    def get_config(self, keys, defalut=None):
        value = self.config
        for key in keys.split('.'):
            value = value.get(key) or {}
        return value or defalut

    def read_configuration(self):
        self.config_dir = Path.home().joinpath('.iskra')
        self.config_dir.mkdir(exist_ok=True)
        self.config_file = self.config_dir.joinpath('config.json')
        self.config_file.touch()
        self.config = json.loads(self.config_file.read_text() or '{}')

    def write_configuration(self, **kwargs):
        self.config.update(kwargs)
        self.config_file.write_text(json.dumps(self.config, indent=4))

    # WebSocket event handlers

    async def on_open(self):
        await self.run_command()

    async def run_command(self, *argv):
        await self.send(type='command', argv=self.argv)

    # Local commands

    async def cmd_logout(self):
        self.config.pop('jwt', None)
        self.write_configuration()
        await self.receive_print(['Bye bye...'], {'color': 'GREEN'})

    # Receivers

    async def receive_jwt(self, refresh, access):
        self.write_configuration(jwt={
            'refresh': refresh,
            'access': access,
        })

    async def receive_machine(self, host, command, argv):
        access_token = self.get_config('jwt.access', '')
        self.talk_to_server = TrainingServer(host, command, access_token, argv)

    async def receive_open_browser(self, url):
        webbrowser.open(url)

    # Responders

    async def receive_prompt(self, request_id, msg):
        await self.send(request_id=request_id, value=input(msg + ': '))

    async def receive_send_access_token(self, request_id):
        access_token = self.get_config('jwt.access', '')
        await self.send(access_token=access_token, request_id=request_id)

    async def receive_send_refresh_token(self, request_id):
        refresh_token = self.get_config('jwt.refresh', '')
        await self.send(refresh_token=refresh_token, request_id=request_id)

    async def receive_send_project_metadata(self, request_id):
        conf = self.read_project_config()
        await self.send(**dict(conf, request_id=request_id))

    def read_project_config(self):
        conf_file = Path.cwd().joinpath('.iskra.json')
        if not conf_file.exists():
            conf_file.write_text(json.dumps({
                'id': str(uuid4()),
                'name': Path.cwd().name,
            }))
        return json.loads(conf_file.read_text())


class TrainingServer(WebSocketClient):
    def __init__(self, host, command, jwt_access_token, argv):
        if host.startswith('localhost'):
            schema = 'ws://'
        else:
            schema = 'wss://'
        self.websocket_url = schema + host + '/cli/' + command
        self.jwt_access_token = jwt_access_token
        self.argv = argv

    async def on_open(self):
        await self.send(jwt_access_token=self.jwt_access_token)

    # Receivers

    async def receive_send_argv(self):
        await self.send(argv=self.argv)

    async def receive_send_metadata(self):
        await self.send(**get_metadata())

    async def receive_start_file_transfer(self):
        checksums, total_size = self.get_local_files_checksum()
        progress = tqdm(
            total=total_size,
            desc='Uploading',
            unit='b',
            unit_scale=True,
            unit_divisor=1024,
        )
        for file_path, (checksum, size) in checksums.items():
            await self.send(type='file', path=file_path, checksum=checksum)
            message = await self.receive()
            if message['type'] == 'transmit':
                with open(file_path, 'rb') as f:
                    chunk = True
                    while chunk:
                        chunk = f.read(MEGA_BYTE)
                        progress.update(len(chunk))
                        await self.send_bytes(chunk)
            elif message['type'] == 'omit':
                progress.update(size)
            else:
                assert False
        await self.send(type='end_of_transmission')

    def get_local_files_checksum(self):
        checksums_size = {}
        total_size = 0
        paths = glob('**', recursive=True)
        dirs_to_ignore = set()
        for path in tqdm(paths, desc="Checksum", unit='file'):
            ignore_this = (
                isdir(path) and (
                    path == '__pycache__' or
                    exists(join(path, 'bin', 'activate'))
                )
            )
            if ignore_this:
                dirs_to_ignore.add(path)

            if (isfile(path) and
                    not any(path.startswith(d) for d in dirs_to_ignore)):
                size = getsize(path)
                checksums_size[path] = (file_checksum(path), size)
                total_size += size

        return checksums_size, total_size


# Introspection

def get_metadata():
    try:
        return {
            'conda': check_output(
                ['conda', 'env', 'export'],
                stderr=DEVNULL
            ).decode()
        }
    except (FileNotFoundError, CalledProcessError):
        major, minor, *_ = sys.version_info
        return {
            'pip': {
                'python': str(major) + '.' + str(minor),
                'requirements': check_output(['pip', 'freeze']).decode(),
            }
        }


def file_checksum(path):
    import hashlib
    md5 = hashlib.md5()
    with open(path, 'rb') as f:
        chunk = True
        while chunk:
            chunk = f.read(4096)
            md5.update(chunk)
    return md5.hexdigest()


async def main():
    iskra = Iskra()
    await iskra.loop()
    talk_to_server = getattr(iskra, 'talk_to_server', None)
    if talk_to_server:
        await talk_to_server.loop()


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
