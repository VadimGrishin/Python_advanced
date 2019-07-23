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
    sock.connect((host, port))
    print(f'Client was started at {host}: {port}')

    data = input('Введите сообщение: \n')

    sock.send(data.encode())
    print(f'сообщение {data} отправлено')

    b_response = sock.recv(bs)
    print(f'Ответ сервера: {b_response.decode()}')
except KeyboardInterrupt:
    print('user shutdown')