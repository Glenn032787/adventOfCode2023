from typing import List

def readInput(file: str) -> List[str]:
    inputFile = "solutions/day03/"+file
    with open(inputFile) as f:
        lines = [line.strip() for line in f]
    return lines

def findSymbol(engine: List[str]):
    coords = []
    for y in range(len(engine)):
        row = engine[y]
        for x in range(len(row)):
            if not row[x].isdigit() and row[x] != ".":
                coords.append((x, y))
    return coords

def getAdjacent(startX, endX, Y):
    allAdjacent = []
    for x in range(startX, endX):
        allAdjacent += [(i,j) for i in (x-1,x,x+1) for j in (Y-1,Y,Y+1) if i >= 0 and j >= 0] 
    return list(set(allAdjacent))
    

def findEngine(engine, coord):
    result = 0 
    for y in range(len(engine)):
        x = 0 
        while x < len(engine[y]):
            if engine[y][x].isdigit():
                start = end = x
                while end < len(engine[y]) and engine[y][end].isdigit():
                    end += 1
                number = engine[y][start:end]
                adjacent = getAdjacent(start, end, y)
                if len(set(adjacent).intersection(coord)) != 0:
                    result += int(number)
                x = end 
            else:
                x += 1
    return result

def main():
    engine = readInput("puzzleInput.txt")
    symbolCoords = findSymbol(engine)
    result = findEngine(engine, symbolCoords)
    print(result)

if __name__ == "__main__":
    main()