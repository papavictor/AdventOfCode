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

def puzzle_3_1():
    with open("3.txt") as fp:
        data = fp.read().strip().splitlines()
    parts = []
    for line in range(len(data)):
        buf = ""
        adj_sqrs = []
        for c in range(len(data[line])):
            if data[line][c].isdigit():
                buf += data[line][c]
                if line > 0:
                    if c > 0:
                        adj_sqrs.append((line-1, c-1))
                    adj_sqrs.append((line-1, c))
                    if c < len(data[line])-2:
                        adj_sqrs.append((line-1, c+1))
                if c > 0:
                    adj_sqrs.append((line, c-1))
                if c < len(data[line])-2:
                    adj_sqrs.append((line, c+1))
                if line < len(data) - 1:
                    if c > 0:
                        adj_sqrs.append((line+1, c-1))
                    adj_sqrs.append((line+1, c))
                    if c < len(data[line]) - 1:
                        adj_sqrs.append((line+1, c+1))
            elif buf:
                for s in set(adj_sqrs):
                    if data[s[0]][s[1]] != "." and not data[s[0]][s[1]].isdigit():
                        parts.append(int(buf))
                        break
                adj_sqrs = []
                buf = ""
            if c == len(data[line]) - 1:
                for s in adj_sqrs:
                    if data[s[0]][s[1]] != "." and not data[s[0]][s[1]].isdigit():
                        parts.append(int(buf))
                        break
                adj_sqrs = []
                buf = ""
    return sum(parts)

def puzzle_3_2():
    with open("3.txt") as fp:
        data = fp.read().strip().splitlines()
    parts = []
    all_gears = {}
    for line in range(len(data)):
        buf = ""
        adj_sqrs = []
        for c in range(len(data[line])):
            if data[line][c].isdigit():
                buf += data[line][c]
                if line > 0:
                    if c > 0:
                        adj_sqrs.append((line-1, c-1))
                    adj_sqrs.append((line-1, c))
                    if c < len(data[line])-2:
                        adj_sqrs.append((line-1, c+1))
                if c > 0:
                    adj_sqrs.append((line, c-1))
                if c < len(data[line])-2:
                    adj_sqrs.append((line, c+1))
                if line < len(data) - 1:
                    if c > 0:
                        adj_sqrs.append((line+1, c-1))
                    adj_sqrs.append((line+1, c))
                    if c < len(data[line]) - 1:
                        adj_sqrs.append((line+1, c+1))
            elif buf:
                for s in adj_sqrs:
                    if data[s[0]][s[1]] == "*":
                        parts.append(int(buf))
                        if s in all_gears:
                            if int(buf) not in all_gears[s]:
                                all_gears[s].append(int(buf))
                        else:
                            all_gears[s] = [int(buf)]
                adj_sqrs = []
                buf = ""
            if c == len(data[line]) - 1:
                for s in adj_sqrs:
                    if data[s[0]][s[1]] == "*":
                        parts.append(int(buf))
                        if s in all_gears:
                            if int(buf) not in all_gears[s]:
                                all_gears[s].append(int(buf))
                        else:
                            all_gears[s] = [int(buf)]
                adj_sqrs = []
                buf = ""
    total = 0
    for g in all_gears:
        if len(all_gears[g]) == 2:
            total += math.prod(all_gears[g])
    return total

def main():
    print(f"Puzzle 1, part 1: {puzzle_1_1()}")
    print(f"Puzzle 1, part 2: {puzzle_1_2()}")
    print(f"Puzzle 2, part 1: {puzzle_2_1()}")
    print(f"Puzzle 2, part 2: {puzzle_2_2()}")
    print(f"Puzzle 3, part 1: {puzzle_3_1()}")
    print(f"Puzzle 3, part 2: {puzzle_3_2()}")

if __name__ == '__main__':
    main()
