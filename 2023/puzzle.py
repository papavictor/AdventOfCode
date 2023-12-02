#!/usr/bin/env python

import math

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

def puzzle_2_1():
    with open("2.txt") as fp:
        data = fp.read().strip().splitlines()
    allowed = {"red": 12, "green": 13, "blue": 14}
    count = 0
    for line in data:
        (game, games) = line.split(":")
        game = game.split(" ")[1]
        for g in games.split(";"):
            for color in g.split(","):
                if allowed[color.strip().split(" ")[1]] < int(color.strip().split(" ")[0]):
                    break
            else:
                continue
            break
        else:
            count += int(game)
    return count

def puzzle_2_2():
    with open("2.txt") as fp:
        data = fp.read().strip().splitlines()
    allowed = {"red": 12, "green": 13, "blue": 14}
    count = 0
    for line in data:
        (game, games) = line.split(":")
        game = game.split(" ")[1]
        max_colors = {"red": 0, "green": 0, "blue": 0}
        for g in games.split(";"):
            for color in g.split(","):
                if max_colors[color.strip().split(" ")[1]] < int(color.strip().split(" ")[0]):
                    max_colors[color.strip().split(" ")[1]] = int(color.strip().split(" ")[0])
        product = math.prod(max_colors.values())
        count += product
    return count

def main():
    print(f"Puzzle 1, part 1: {puzzle_1_1()}")
    print(f"Puzzle 1, part 2: {puzzle_1_2()}")
    print(f"Puzzle 2, part 1: {puzzle_2_1()}")
    print(f"Puzzle 2, part 2: {puzzle_2_2()}")

if __name__ == '__main__':
    main()
