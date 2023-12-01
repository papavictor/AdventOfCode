#!/usr/bin/env python

def puzzle_1_1():
    with open("1.txt") as fp:
        data = fp.read().strip().splitlines()
    total = 0
    for line in data:
        d = ""
        for c in line:
            if c.isdigit():
                d += c
                break
        for c in line[::-1]:
            if c.isdigit():
                d += c
                break
        total += int(d)
    return total

def puzzle_1_2():
    with open("1.txt") as fp:
        data = fp.read().strip().splitlines()
    nums = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5",
            "six": "6", "seven": "7", "eight": "8", "nine": "9"}
    total = 0
    for line in data:
        d = ""
        for c in range(len(line)):
            if line[c].isdigit():
                d += line[c]
                break
            for num in nums:
                if line[c:].startswith(num):
                    d += nums[num]
                    break
            else:
                continue
            break
        for c in range(len(line)):
            if line[::-1][c].isdigit():
                d += line[::-1][c]
                break
            for num in nums:
                if line[::-1][c:].startswith(num[::-1]):
                    d += nums[num]
                    break
            else:
                continue
            break
        total += int(d)
    return total

def main():
    print(f"Puzzle 1, part 1: {puzzle_1_1()}")
    print(f"Puzzle 1, part 2: {puzzle_1_2()}")

if __name__ == '__main__':
    main()
