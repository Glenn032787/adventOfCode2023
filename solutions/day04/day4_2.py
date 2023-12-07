from day4_1 import readInput, parse
from typing import List

def calcWinning(winNum: List[int], cardNum: List[int]) -> int:
    numWin = 0 
    for num in cardNum:
        if num in winNum:
            numWin += 1
    return numWin


def getTotalWinning(cards):
    dynamic = {}
    total = 0 
    currentCards = list(cards.keys())
    while len(currentCards) != 0:
        cardNum = currentCards.pop()
        total += 1
        if cardNum in dynamic:
            winning = dynamic[cardNum]
        else:
            winNum = cards[cardNum][0]
            cardNumber = cards[cardNum][1]
            winning = calcWinning(winNum, cardNumber)
            dynamic[cardNum] = winning
        currentCards += list(range(cardNum + 1,cardNum + winning + 1))       
    return total 

def main():
    inputData = readInput("puzzleInput.txt")
    parseData = parse(inputData)
    numScratchcard = getTotalWinning(parseData)
    print(numScratchcard)
    

if __name__ == "__main__":
    main()