from typing import Dict, List, Tuple

maxCube = {
    'red': 12,
    'green': 13,
    'blue': 14
}

def readInput(file: str) -> List[str]:
    inputFile = "solutions/day02/"+file
    with open(inputFile) as f:
        lines = [line.strip() for line in f]
    return lines

def parse(line: str) -> Tuple[str, Dict]:
    game, cubes = line.split(":")
    _, gameNum = game.split(" ")

    cubes = cubes.split(';')
    gameDicts = []
    for cubeSet in cubes:
        cubeSet = cubeSet.split(', ')
        setDict = {}
        for cube in cubeSet:
            cubeNum, color = cube.strip().split(' ')
            setDict[color] = cubeNum
        gameDicts.append(setDict)
    return gameNum, gameDicts
    

def validate(game: Dict) -> bool:
    for gameSet in game:
        for color in gameSet.keys():
            if int(gameSet[color]) > maxCube[color]:
                return False
    return True


def main():
    data = readInput("puzzleInput.txt")
    indexSum = 0 
    for line in data:
        line = parse(line)
        if validate(line[1]):
            indexSum += int(line[0])
    print(indexSum)
    
    

if __name__ == "__main__":
    main()