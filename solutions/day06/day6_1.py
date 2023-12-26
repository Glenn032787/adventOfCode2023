from math import sqrt, ceil, floor
from typing import List, Dict

def readInput(file: str) -> List[str]:
    inputFile = "solutions/day06/"+file
    with open(inputFile) as f:
        lines = [line.strip().split() for line in f]
    return lines


def analyze(totalTime: int, maxDistance: int) -> int:
    criticalPointsA = ((-totalTime) + sqrt(totalTime**2 - 4*maxDistance)) / -2
    criticalPointsB = ((-totalTime) - sqrt(totalTime**2 - 4*maxDistance)) / -2 
    
    if criticalPointsA > criticalPointsB:
        minVal = ceil(criticalPointsB)
        maxVal = floor(criticalPointsA)
    else:
        minVal = ceil(criticalPointsA)
        maxVal = floor(criticalPointsB)

    if (totalTime - minVal) * minVal == maxDistance:
        minVal += 1
    if (totalTime - maxVal) * maxVal == maxDistance:
        maxVal -= 1

    return maxVal - minVal + 1


def main():
    puzzleInput = readInput("puzzleInput.txt")
    final = 1
    for i in range(1, len(puzzleInput[0])):
        totalTime = int(puzzleInput[0][i])
        maxDistance = int(puzzleInput[1][i])
        currResults = analyze(totalTime, maxDistance)
        final = final * currResults
    print(final)
        
if __name__ == "__main__":
    main()