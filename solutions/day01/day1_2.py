from day1_1 import readInput, calibrate

num = {
    'one': 'o1e',
    'two': 't2o',
    'three': 't3e',
    'four': 'f4r',
    'five': 'f5e', 
    'six': 's6x', 
    'seven': 's7n', 
    'eight': 'e8t', 
    'nine': 'n9e'
}

def convert2num(line):
    for digit in num.keys():
        line = line.replace(digit, num[digit])
    return line


def main():
    inputLines = readInput()
    inputConvert = [convert2num(line) for line in inputLines]
    result = calibrate(inputConvert)
    print(result)

if __name__ == "__main__":
    main()
