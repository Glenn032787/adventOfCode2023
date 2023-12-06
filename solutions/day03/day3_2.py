from day3_1 import readInput, findSymbol, getAdjacent

def findNumber(engine): 
    result = {}
    for y in range(len(engine)):
        x = 0 
        while x < len(engine[y]):
            if engine[y][x].isdigit():
                start = end = x
                while end < len(engine[y]) and engine[y][end].isdigit():
                    end += 1
                number = engine[y][start:end]
                adjacent = getAdjacent(start, end, y)
                result[(start, y, int(number))] = adjacent
                x = end
            else:
                x += 1
    return result

def analyze(symbols, numbers):
    result = 0
    for symbolCoord in symbols:
        curr = []
        for number in numbers:
            if symbolCoord in numbers[number]:
                curr.append(number[2])
        if len(curr) == 2:
            gearRatio = curr[0] * curr[1]
            result += gearRatio
    return result
            

def main():
    engine = readInput("puzzleInput.txt")
    symbolCoords = findSymbol(engine)
    number = findNumber(engine)
    result = analyze(symbolCoords, number)
    print(result)


if __name__ == "__main__":
    main()