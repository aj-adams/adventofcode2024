import os, requests

cookie = os.environ.get('AoC_SESSION')
cookies={'session': cookie}
headers = {'User-Agent': 'Mozilla/5.0'}
response = requests.get('https://adventofcode.com/2024/day/2/input', cookies=cookies, headers=headers)
input = response.text