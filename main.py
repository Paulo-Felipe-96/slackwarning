import requests

from time import sleep
from environments.envs import _url, _headers, _payload
from messenger.messenger import post_message_feature_slack
from messenger.notify import notifier


def try_status():
    counter = 0
    tries = 0
    SUCCESS = False

    while True:
        r = requests.post(_url, headers=_headers, json=_payload)
        counter += 1
        tries += 1

        if r.status_code == 200:
            SUCCESS = True
            notifier(SUCCESS)
            post_message_feature_slack()
            break
        else:
            print(f"Resposta da API: {r.status_code} \n"
                  f"Tentativas: {tries}")
            if counter == 10:
                notifier(SUCCESS)
                counter = 0
        sleep(30)


if __name__ == '__main__':
    try_status()
