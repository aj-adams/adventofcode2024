import os
import requests

cookie = os.environ.get('AoC_SESSION')
cookies={'session': cookie}
headers = {'User-Agent': 'Mozilla/5.0'}
response = requests.get('https://adventofcode.com/2024/day/1/input', cookies=cookies, headers=headers)
input = response.text

exit()

left = []
right = []
distances = []

path = os.path.dirname(os.path.realpath(__file__))
input = os.path.join(path, "input.txt")

with open(input, 'r') as reader:

    locations = [list(map(int,line.rstrip().split())) for line in reader.readlines()]
    """
    for location in locations:
        left.append(location[0])
        right.append(location[1])"""

    lefts, rights = zip(*locations)
    
    left = sorted(lefts)
    right = sorted(rights)

    distances = [abs(l - r) for l,r in zip(left,right)]
    
    print("Answer to part 1: " + str(sum(distances)))

    similarity_scores = [l*right.count(l) for l in left]
    
    print("Answer to part 2: " + str(sum(similarity_scores)))