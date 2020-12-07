def getTreesHit(terrain, xSlope, ySlope=1):
    trees_hit = 0
    currentX = 0
    rowLength = len(terrain[0])
    for rowIndex in range(0, len(terrain), ySlope):
        if terrain[rowIndex][currentX] == '#':
            trees_hit += 1
        currentX = (currentX + xSlope) % rowLength
    return trees_hit


with open("input3.txt") as f:
    dumb = list(f)
    terrain = [x.strip() for x in dumb]
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    results = [getTreesHit(terrain, x[0], x[1]) for x in slopes]
    print(results[1])
    print(results[0] * results[1] * results[2]
          * results[3] * results[4])
