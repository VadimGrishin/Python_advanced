import yaml
from argparse import ArgumentParser
import socket

# настройки сокета по умолчанию:
config = {
    'host': 'localhost',
    'port': 8000,
    'buffer_size': 1024
}

# обновление настроек из файла-параметра командной строки
parser = ArgumentParser()
parser.add_argument(
    '-c', '--config', type=str, required=False, help='Config file path'
)

args = parser.parse_args()
if args.config:
    with open(args.config) as file:
        file_config = yaml.load(file, Loader=yaml.Loader)
        config.update(file_config)

host = config.get('host')
port = config.get('port')
bs = config.get('buffer_size')

# работа с сокетом
try:
    sock = socket.socket()
    sock.bind((host, port))
    sock.listen(4)
    print(f'Server started at {host}: {port}')
    while True:
        client, address = sock.accept()
        print(f'Client was detected at {address[0]}: {address[1]}')

        b_request = client.recv(bs)
        print(f'Client has sent message: {b_request.decode()}')

        client.send(b'Your message: "' + b_request + b'" received')

        client.close()

except KeyboardInterrupt:
    print('user shutdown')


