from typing import List, Dict

def readInput(file: str) -> List[str]:
    inputFile = "solutions/day04/"+file
    with open(inputFile) as f:
        lines = [line.strip() for line in f]
    return lines

def splitWhiteSpace(lst):
    return list(filter(lambda x: x != '', lst.strip().split(" ")))

def parse(data: List[str]) -> Dict[str, List[int]]:
    parsedData = {}

    for gameSet in data:
        game, card = gameSet.split(": ")
        winningNum, cardNum = card.split(" | ")
        winningNum = list(map(int, splitWhiteSpace(winningNum)))
        cardNum = list(map(int, splitWhiteSpace(cardNum)))

        _, gameNum = splitWhiteSpace(game)
        parsedData[int(gameNum)] = [winningNum, cardNum]
    return parsedData

def getWinning(winNum: List[int], cardNum: List[int]) -> int:
    numWin = 0 
    for num in cardNum:
        if num in winNum:
            numWin += 1
    if numWin == 0:
        return 0
    else:
        numWin -= 1
    return 2**numWin

def getTotalWinning(data: Dict[str, List[int]]) -> int:
    total = 0 
    for game in data:
        winNum = data[game][0]
        cardNum = data[game][1]
        total += getWinning(winNum, cardNum)
    return total

def main():
    inputData = readInput("puzzleInput.txt")
    parsedData = parse(inputData)
    winning = getTotalWinning(parsedData)
    print(winning)

if __name__ == "__main__":
    main()