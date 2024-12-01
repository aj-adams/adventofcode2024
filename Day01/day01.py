import os.path

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

    similarity_scores = []