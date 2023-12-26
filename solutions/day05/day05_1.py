from typing import List, Dict

def readInput(file: str) -> List[str]:
    inputFile = "solutions/day05/"+file
    with open(inputFile) as f:
        lines = [line.strip() for line in f]

    return lines

def splitWhiteSpaceInt(lst):
    newLst = list(filter(lambda x: x != '', lst.strip().split(" ")))
    return list(map(int, newLst))


def getSeed(rawInput):
    seeds = rawInput[0]
    _, seeds = seeds.split(": ")
    return splitWhiteSpaceInt(seeds)

def getMapping(rawInput):
    rawInput = rawInput[1:]
    i = 1
    allMapping = {}
    conversion = {}
    while i < len(rawInput):
        title = rawInput[i]
        title, _ = title.split(' ')
        prevTitle, _, title = title.split('-')
        conversion[prevTitle] = title
        currMapping = []
        while True:
            i += 1
            if i >= len(rawInput) or rawInput[i] == "":
                allMapping[title] = currMapping
                i += 1
                break
            curr = splitWhiteSpaceInt(rawInput[i])
            currMapping.append(curr)
    return allMapping, conversion
        
def getSeedLocation(data, type, mapping, conversion):
    if type == "location":
        return data

    nextType = conversion[type]
    mappingData = mapping[nextType]

    found = False

    for mapVals in mappingData:
        if data >= mapVals[1] and data < mapVals[1] + mapVals[2]:
            diff = data - mapVals[1] 
            newData = mapVals[0] + diff
            found = True
            break
    if not found:
        newData = data
    return getSeedLocation(newData, nextType, mapping, conversion)

def analyze(seeds, mappings, conversion):
    minLocation = float('inf')
    for seed in seeds:
        location = getSeedLocation(seed, "seed", mappings, conversion)
        if location < minLocation:
            minLocation = location
    return minLocation

def main():
    inputData = readInput('puzzleInput.txt')
    seed = getSeed(inputData)
    mappings, conversion = getMapping(inputData)
    location = analyze(seed, mappings, conversion)
    print(location)
    
    

if __name__ == "__main__":
    main()