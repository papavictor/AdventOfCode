#!/usr/bin/env python

import math
import re

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

def puzzle_4_1():
    with open("4.txt") as fp:
        data = fp.read().strip().splitlines()
    score = 0
    for line in data:
        card_score = 0
        winning_numbers = line.split(":")[1].split("|")[0].strip().split(" ")
        my_numbers = line.split("|")[1].strip().split(" ")
        while '' in my_numbers:
            my_numbers.remove('')
        while '' in winning_numbers:
            winning_numbers.remove('')
        winners = set(winning_numbers).intersection(set(my_numbers))
        card_score = 2**(len(winners)-1)
        score += int(card_score)
    return score

def puzzle_4_2():
    with open("4.txt") as fp:
        data = fp.read().strip().splitlines()
    copies = {}
    for line in data:
        card_num = int("".join(line.split(":")[0].split(" ")[1:]).strip())
        if card_num not in copies:
            copies[card_num] = 1
        else:
            copies[card_num] += 1
        winning_numbers = line.split(":")[1].split("|")[0].strip().split(" ")
        my_numbers = line.split("|")[1].strip().split(" ")
        while '' in my_numbers:
            my_numbers.remove('')
        while '' in winning_numbers:
            winning_numbers.remove('')
        winners = set(winning_numbers).intersection(set(my_numbers))
        for i in range(copies[card_num]):
            for j in range(card_num+1, card_num+len(winners)+1):
                if j not in copies:
                    copies[j] = 1
                else:
                    copies[j] += 1
    return sum(copies.values())

def puzzle_5_1():
    with open("5.txt") as fp:
        data = fp.read().strip().splitlines()
    seeds = list(map(int, data[0].split(":")[1].strip().split()))
    maps = {}
    query = "([a-z]+-to-[a-z]+)\ map:\n(([0-9\ ]+\n?)+\n?)"
    parsed = re.findall(query, "\n".join(data[1:]))
    for m in parsed:
        maps[m[0]] = list(map(lambda x: list(map(int, x.split())), m[1].strip().splitlines()))
    min_loc = 9999999999
    for s in seeds:
        cur_word = "seed"
        while cur_word != "location":
            for m in maps:
                if m.startswith(f"{cur_word}-to-"):
                    dest_word = re.match(f"{cur_word}-to-([a-z]+)", m).groups()[0]
                    for c in maps[m]:
                        if c[1] <= s <= c[1]+c[2]-1:
                            dest_num = c[0]+(s-c[1])
                            break
                    else:
                        dest_num = s
            cur_word = dest_word
            s = dest_num
        if s < min_loc:
            min_loc = s
    return min_loc

def puzzle_5_2():
    with open("5.txt") as fp:
        data = fp.read().strip().splitlines()
    sl = list(map(int, data[0].split(":")[1].strip().split()))
    maps = {}
    query = "([a-z]+-to-[a-z]+)\ map:\n(([0-9\ ]+\n?)+\n?)"
    parsed = re.findall(query, "\n".join(data[1:]))
    for m in parsed:
        maps[m[0]] = list(map(lambda x: list(map(int, x.split())), m[1].strip().splitlines()))
    min_loc = 0
    for s in range(0, len(sl), 2):
        distance_from_end = -1
        seed = sl[s]
        s2 = sl[s]
        cur_word = "seed"
        while cur_word != "location":
            for m in maps:
                if m.startswith(f"{cur_word}-to-"):
                    dest_word = re.match(f"{cur_word}-to-([a-z]+)", m).groups()[0]
                    for c in maps[m]:
                        if c[1] <= s2 <= c[1]+c[2]-1:
                            dest_num = c[0]+(s2-c[1])
                            if distance_from_end == -1 or (c[1] + c[2] - s2) < distance_from_end:
                                distance_from_end = c[1] + c[2] - s2
                            break
                    else:
                        dest_num = s2
            cur_word = dest_word
            s2 = dest_num
        if min_loc == 0 or dest_num < min_loc:
            min_loc = dest_num
        s2 = seed+distance_from_end
        seed = s2
        cur_word = "seed"
        while cur_word != "location":
            for m in maps:
                if m.startswith(f"{cur_word}-to-"):
                    dest_word = re.match(f"{cur_word}-to-([a-z]+)", m).groups()[0]
                    for c in maps[m]:
                        if c[1] <= s2 <= c[1]+c[2]-1:
                            dest_num = c[0]+(s2-c[1])
                            break
                    else:
                        dest_num = s2
            cur_word = dest_word
            s2 = dest_num
        if s2 < min_loc:
            min_loc = s2
        elif min_loc == 0:
            min_loc = s2
    return min_loc

def main():
    print(f"Puzzle 1, part 1: {puzzle_1_1()}")
    print(f"Puzzle 1, part 2: {puzzle_1_2()}")
    print(f"Puzzle 2, part 1: {puzzle_2_1()}")
    print(f"Puzzle 2, part 2: {puzzle_2_2()}")
    print(f"Puzzle 3, part 1: {puzzle_3_1()}")
    print(f"Puzzle 3, part 2: {puzzle_3_2()}")
    print(f"Puzzle 4, part 1: {puzzle_4_1()}")
    print(f"Puzzle 4, part 2: {puzzle_4_2()}")
    print(f"Puzzle 5, part 1: {puzzle_5_1()}")
    print(f"Puzzle 5, part 2: {puzzle_5_2()}")

if __name__ == '__main__':
    main()
