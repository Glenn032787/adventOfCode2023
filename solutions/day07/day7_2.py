from math import sqrt, ceil, floor
from typing import List, Dict
from collections import Counter

def readInput(file: str) -> List[str]:
    inputFile = "solutions/day07/"+file
    with open(inputFile) as f:
        lines = [line.strip().split() for line in f]
    return lines

class pokerHand:
    
    def __init__(self, hand, bid):
        self.hand = hand
        self.bid = bid
    
    def _convertWildType(self):
        hand = self.hand.replace("J", "")
        if len(hand) == 0:
            # All wildcard
            return "KKKKK"
        mostCommonCard = Counter(hand).most_common(1)[0][0]
        newHand = self.hand.replace('J', mostCommonCard)
        return newHand

    def typeRank(self):
        newHand = self._convertWildType()
        uniqCard = set(newHand)
        numCard = Counter([newHand.count(card) for card in uniqCard])
        
        if numCard == Counter([5]):
            # 5 of a kind
            return 7 
        elif numCard == Counter([4, 1]):
            # 4 of a kind
            return 6
        elif numCard == Counter([2, 3]):
            # Full house
            return 5
        elif numCard == Counter([1, 1, 3]):
            # Three of a kind
            return 4
        elif numCard == Counter([2, 2, 1]):
            # Two pair
            return 3
        elif numCard == Counter([2, 1, 1, 1]):
            # One pair
            return 2
        else: 
            # High card
            return 1

    def largerNum(self, other):
        RANKING = {
        'A': 14,
        'K': 13,
        'Q': 12,
        'J': 1,
        'T': 10,
        }  
        for i in range(len(self.hand)):
            if self.hand[i] != other.hand[i]:
                if self.hand[i] in RANKING:
                    curr = RANKING[self.hand[i]]
                else:
                    curr = int(self.hand[i])
                if other.hand[i] in RANKING:
                    currOther = RANKING[other.hand[i]]
                else:
                    currOther = int(other.hand[i])
                return curr > currOther
                
    def __lt__(self, other):
        selfRank = self.typeRank()
        otherRank = other.typeRank()
        if selfRank == otherRank:
            return not self.largerNum(other)
        return selfRank < otherRank

    def __gt__(self, other):
        selfRank = self.typeRank()
        otherRank = other.typeRank()
        if selfRank == otherRank:
            return self.largerNum(other)
        return selfRank > otherRank

    def __eq__(self, other):
        return Counter(self.hand) == Counter(other.hand)

    def __str__(self):
        return self.hand
    
    def __repr__(self):
        return self.hand


def main():
    puzzleInput = readInput("puzzleInput.txt")
    game = []
    for card in puzzleInput:
        game.append(pokerHand(card[0], int(card[1])))
    game = sorted(game)
    winning = 0
    for i in range(len(game)):
        winning += game[i].bid * (i + 1)
    print(winning)
        
if __name__ == "__main__":
    main()