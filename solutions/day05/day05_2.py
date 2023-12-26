## UNSOLVE

from day05_1 import readInput, getMapping, analyze, splitWhiteSpaceInt, getSeed


def analyze(startSeed, endSeed, mapping, conversion):
    curr = [(startSeed, endSeed)]
    type = "seed"
    
    while type != "location":
        nextType = conversion[type]
        mappingData = mapping[nextType]

        nextData = []
        while len(curr) != 0:
            data = curr.pop()
            dataStart = data[0]
            dataEnd = data[1]
            found = False
            for mapVals in mappingData:
                mapStart =  mapVals[1]
                mapEnd = mapVals[1] + mapVals[2] - 1
                mapDiff = mapVals[0] - mapVals[1]
            
                # No overlap
                if dataEnd < mapStart or  dataStart > mapEnd:
                    continue
                ## Check seed interval within  map interval 
                elif dataStart > mapStart and dataEnd < mapEnd:
                    nextData.append(dataStart + mapDiff)
                    nextData.append(dataEnd + mapDiff)
                    found=True
                    break
                ## Check map interval within seed interval (add three interval)
                elif dataStart <= mapStart and dataEnd >= mapEnd:
                    curr.append((dataStart, mapStart-1))
                    curr.append((mapEnd+1, dataEnd))
                    nextData.append(mapStart + mapDiff)
                    nextData.append(mapEnd + mapDiff)
                    found=True
                    break
                ## Check partial overlap (Need to add two interval)
                elif dataStart >= mapStart and dataEnd >= mapEnd:
                    found=True
                    curr.append((mapEnd+1, dataEnd))
                    nextData.append(dataStart + mapDiff)
                    nextData.append(mapEnd + mapDiff)
                    break
                elif dataStart <= mapStart and dataEnd <= mapEnd:
                    curr.append((dataStart, mapStart-1))
                    nextData.append(mapStart + mapDiff)
                    nextData.append(dataEnd + mapDiff)
                    found=True
                    break

            if not found:
                nextData.append(dataStart)
                nextData.append(dataEnd)

        nextData = list(set(nextData))
        nextData.sort()
        curr = [(nextData[i], nextData[i+1])for i in range(len(nextData)-1)] 
        type = nextType
    return min(nextData)

        


def main():
    inputData = readInput('testInput1.txt')
    seed = getSeed(inputData)
    mappings, conversion = getMapping(inputData)
    result = analyze(55, 55+13, mappings, conversion)
    print(result)

if __name__ == "__main__":
    main()