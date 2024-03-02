import sys
import httpx
import json
from time import sleep


def main(args: list):
    len_args = len(args)
    data = json.dumps({'urls': args[1:len_args]})
    r = httpx.post('http://localhost:8888/api/v1/tasks/', data=data)
    print('Res:', r.text, r)
    id = r.json()['id']
    print(id)
    for _ in range(5):
        r = httpx.get(f'http://localhost:8888/api/v1/tasks/{id}')
        print('Res:', r.text, r)
        sleep(5)


if __name__ == '__main__':
    main(sys.argv)
