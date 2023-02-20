import os
import random
import requests
import binascii
import threading

from colorama import Fore

invite = "2OO618j2"
created = 0

def get_rstr(lenght: int) -> str:
    return str(binascii.b2a_hex(os.urandom(lenght)).decode('utf-8'))


def Gen():
    try:
        global created
        proxy = random.choice(open('proxies.txt', 'r').read().splitlines())
        proxies = {'http': f'http://{proxy}', 'https': f'http://{proxy}'}

        name     = ''.join(random.choices('poiuytrewqlkjhgfdsamnbvcxz098765431', k=7))
        email    = ''.join(random.choices('poiuytrewqlkjhgfdsamnbvcxz098765431', k=8)) + '@gmail.com'
        password = ''.join(random.choices('poiuytrewqlkjhgfdsamnbvcxz098765431', k=12))
        headers = {
            'authority'              : 'www.guilded.gg',
            'accept'                 : 'application/json, text/javascript, */*; q=0.01',
            'accept-language'        : 'en-GB,en;q=0.9',
            'content-type'           : 'application/json',
            'guilded-client-id'      : f'{get_rstr(8)}-{get_rstr(4)}-{get_rstr(4)}-{get_rstr(4)}-{get_rstr(12)}',
            'guilded-stag'           : get_rstr(32),
            'guilded-viewer-platform': 'desktop',
            'origin'                 : 'https://www.guilded.gg',
            'referer'                : 'https://www.guilded.gg/',
            'sec-ch-ua'              : '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile'       : '?0',
            'sec-ch-ua-platform'     : '"Windows"',
            'sec-fetch-dest'         : 'empty',
            'sec-fetch-mode'         : 'cors',
            'sec-fetch-site'         : 'same-origin',
            'user-agent'             : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
            'x-requested-with'       : 'XMLHttpRequest',
        }

        json = {
            'extraInfo': {
                'registrationSource': 'search',
                'platform': 'desktop',
            },
            'name'    : name,
            'email'   : email,
            'password': password,
            'fullName': name,
        }

        response = requests.post('https://www.guilded.gg/api/users?type=email', json=json, headers=headers, proxies=proxies)
        if response.status_code == 200:
            created += 1
            print(f"{Fore.BLUE}[ {Fore.GREEN}+ {Fore.BLUE}]{Fore.RESET} Generated ({created})")
            hmac         = response.cookies['hmac_signed_session']
            with open('cookies.txt', 'a') as cookieOpen:
                cookieOpen.write(f'{hmac}\n')
            with open('accounts.txt', 'a') as accountOpen:
                accountOpen.write(f'{email}:{name}:{password}\n')

                __headers__ = {
                    'authority': 'www.guilded.gg',
                    'accept': 'application/json, text/javascript, */*; q=0.01',
                    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
                    'content-type': 'application/json',
                    'cookie': f'hmac_signed_session={hmac}',
                    'guilded-client-id': f'{get_rstr(8)}-{get_rstr(4)}-{get_rstr(4)}-{get_rstr(4)}-{get_rstr(12)}',
                    'guilded-viewer-platform': 'desktop',
                    'origin': 'https://www.guilded.gg',
                    'referer': 'https://www.guilded.gg/',
                    'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-platform': '"Windows"',
                    'sec-fetch-dest': 'empty',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-site': 'same-origin',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
                    'x-requested-with': 'XMLHttpRequest',
                }

                params_ = {'teamId': f'{invite}','includeLandingChannel': 'true',}

                __json = {'type': 'consume',}
                response = requests.put(f'https://www.guilded.gg/api/invites/{invite}', params=params_, headers=__headers__, json=__json, proxies=proxies)

        else:
            print(f"{Fore.BLUE}[ {Fore.RED}x {Fore.BLUE}]{Fore.RESET} Error")
    except Exception as e:
        pass


os.system('cls')
thread = int(input("threads: "))
if __name__ == '__main__':
    for i in range(thread):
        threading.Thread(target=Gen).start()
