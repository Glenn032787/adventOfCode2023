from typing import List

def readInput(input: str = "input2.txt") -> List[str]:
    inputFile = "solutions/day01/"+input
    with open(inputFile) as f:
        lines = [line.strip() for line in f]
    return lines


def calibrate(calibration: List[str]) -> int:
    final = 0 
    for line in calibration:
        curr = [str(letter) for letter in line if letter.isdigit()]
        final += int(curr[0] + curr[-1])
    return final 

def main():
    input = readInput()
    result = calibrate(input)
    print(result)

if __name__ == "__main__":
    main()