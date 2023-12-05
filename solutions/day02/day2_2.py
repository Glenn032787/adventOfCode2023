from day2_1 import readInput, parse

def minCube(game):
    maxCubes = {'red': 0, 'blue': 0, 'green': 0}
    for gameSet in game:
        for color in gameSet:
            if int(gameSet[color]) > maxCubes[color]:
                maxCubes[color] = int(gameSet[color])
    return maxCubes["red"] * maxCubes["blue"] * maxCubes["green"]


def main():
    inputData = readInput('puzzleInput.txt')
    powerSum = 0 
    for line in inputData:
        _, game = parse(line)
        power = minCube(game)
        powerSum += power
    print(powerSum)

if __name__ == "__main__":
    main()