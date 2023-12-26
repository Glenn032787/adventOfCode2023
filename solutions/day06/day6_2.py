from day6_1 import analyze
from typing import List, Dict
import re

def readInput(file: str) -> List[str]:
    inputFile = "solutions/day06/"+file
    with open(inputFile) as f:
        lines = [re.sub("[^0-9]", "", line) for line in f]
    return lines

def main():
    puzzleInput = readInput("puzzleInput.txt")
    finalResult = analyze(int(puzzleInput[0]), int(puzzleInput[1]))
    print(finalResult)
        
if __name__ == "__main__":
    main()