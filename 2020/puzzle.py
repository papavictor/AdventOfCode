#!/usr/bin/env python

from copy import deepcopy
from functools import reduce
from itertools import combinations, permutations
import json
import re
import regex
import string
import sys
from time import sleep

def puzzle_1_1():
    with open("1.txt", "r") as fp:
        data = fp.read().strip().splitlines()
    for i in range(len(data)-1):
        a = data[i]
        for b in data[i:]:
            print(i, a, b, int(a)+int(b))
            if int(a) + int(b) == 2020:
                return int(a)*int(b)

def puzzle_1_2():
    with open("1.txt", "r") as fp:
        data = list(map(int, fp.read().strip().splitlines()))
    for i in range(len(data)-1):
        for j in range(i+1, len(data)-1):
            for k in range(j+1, len(data)-1):
                print(data[i], data[j], data[k])
                if data[i] + data[j] + data[k] == 2020:
                    return data[i] * data[j] * data[k]

def puzzle_2_1():
    with open("2.txt") as fp:
        data = fp.read().strip().splitlines()
    valid_count = 0
    for line in data:
        m = re.match("([0-9]+)-([0-9]+) ([a-z]): ([a-z]+)", line)
        if m:
            (minc, maxc, c, passwd) = m.groups()
            if int(minc) <= passwd.count(c) <= int(maxc):
                valid_count += 1
    return valid_count

def puzzle_2_2():
    with open("2.txt") as fp:
        data = fp.read().strip().splitlines()
    valid_count = 0
    for line in data:
        m = re.match("([0-9]+)-([0-9]+) ([a-z]): ([a-z]+)", line)
        if m:
            (pos1, pos2, c, passwd) = m.groups()
            print(pos1, pos2, c, passwd)
            if (passwd[int(pos1)-1] == c or \
              passwd[int(pos2)-1] == c) and not \
              (passwd[int(pos1)-1] == c and passwd[int(pos2)-1] == c):
                valid_count += 1
    return valid_count

def puzzle_3_1():
    with open("3.txt") as fp:
        data = fp.read().strip().splitlines()
    x = 0
    tree_count = 0
    for line in data:
        upd_line = list(line)
        if line[x] == "#":
            tree_count += 1
            upd_line[x] = "X"
        else:
            upd_line[x] = "O"
        print("".join(upd_line))
        x = (x+3) % len(line)
    return tree_count

def puzzle_3_2():
    with open("3.txt") as fp:
        data = fp.read().strip().splitlines()
    attempts = ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))
    product_trees = 1
    for attempt in attempts:
        x = 0
        tree_count = 0
        for i in range(0, len(data), attempt[1]):
            upd_line = list(data[i])
            if data[i][x] == "#":
                tree_count += 1
                upd_line[x] = "X"
            else:
                upd_line[x] = "O"
            print("".join(upd_line))
            x = (x+attempt[0]) % len(data[i])
        print(tree_count)
        product_trees *= tree_count
    return product_trees

def puzzle_4_1():
    with open("4.txt") as fp:
        data = fp.read().splitlines()
    mandatory_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    optional_fields = ["cid"]
    buf = ""
    valid_count = 0
    for line in data:
        print(line)
        if not re.match("^\s*$", line):
            buf += "{} ".format(line)
        else:
            tmpdict = {}
            print(buf.strip())
            for e in buf.strip().split(" "):
                tmpdict[e.split(":")[0]] = e.split(":")[1]
            print(tmpdict)
            for f in mandatory_fields:
                if f not in tmpdict:
                    break
            else:
                valid_count += 1
            buf = ""
    return valid_count

def puzzle_4_2():
    with open("4.txt") as fp:
        data = fp.read().splitlines()
    mandatory_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    optional_fields = ["cid"]
    buf = ""
    valid_count = 0
    for line in data:
        print(line)
        if not re.match("^\s*$", line):
            buf += "{} ".format(line)
        else:
            tmpdict = {}
            print(buf.strip())
            for e in buf.strip().split(" "):
                tmpdict[e.split(":")[0]] = e.split(":")[1]
            print(tmpdict)
            for f in mandatory_fields:
                if f not in tmpdict:
                    break
            else:
                if 1920 <= int(tmpdict["byr"]) <= 2002 and \
                   2010 <= int(tmpdict["iyr"]) <= 2020 and \
                   2020 <= int(tmpdict["eyr"]) <= 2030 and \
                   ((tmpdict["hgt"].endswith("cm") and 150 <= int(tmpdict["hgt"].split("c")[0]) <= 193) or \
                   (tmpdict["hgt"].endswith("in") and 59 <= int(tmpdict["hgt"].split("i")[0]) <= 76)) and \
                   re.fullmatch("\#[0-9a-f]{6}", tmpdict["hcl"]) and \
                   tmpdict["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"] and \
                   len(tmpdict["pid"]) == 9 and tmpdict["pid"].isdigit():
                    valid_count += 1
            buf = ""
    return valid_count

def puzzle_5_1():
    with open("5.txt") as fp:
        data = fp.read().strip().splitlines()
    #data = ["FBFBBFFRLR", "BFFFBBFRRR", "FFFBBBFRRR", "BBFFBBFRLL"]
    max_id = 0
    for line in data:
        row = int(line[0:7].replace("F", "0").replace("B", "1"), 2)
        column = int(line[7:].replace("L", "0").replace("R", "1"), 2)
        uid = row * 8 + column
        if uid > max_id:
            max_id = uid
        print(line, row, column, uid)
    return max_id

def puzzle_5_2():
    with open("5.txt") as fp:
        data = fp.read().strip().splitlines()
    #data = ["FBFBBFFRLR", "BFFFBBFRRR", "FFFBBBFRRR", "BBFFBBFRLL"]
    max_id = 0
    min_id = 100
    seen_seats = []
    for line in data:
        row = int(line[0:7].replace("F", "0").replace("B", "1"), 2)
        column = int(line[7:].replace("L", "0").replace("R", "1"), 2)
        uid = row * 8 + column
        seen_seats.append(uid)
        if uid > max_id:
            max_id = uid
        if uid < min_id:
            min_id = uid
        print(line, row, column, uid)
    print(min_id, max_id)
    for i in range(min_id, max_id):
        if i not in seen_seats:
            return i

def puzzle_6_1():
    with open("6.txt") as fp:
        data = fp.read().splitlines()
    buf = ""
    sum = 0
    for line in data:
        print(line)
        if not re.match("^\s*$", line):
            buf += line
        else:
            count = len(set(buf))
            sum += count
            print(buf, set(buf), len(set(buf)), sum)
            buf = ""
    return sum

def puzzle_6_2():
    with open("6.txt") as fp:
        data = fp.read().splitlines()
    buf = ""
    sum = 0
    begin_group = True
    for line in data:
        print(line)
        if not re.match("^\s*$", line):
            if not begin_group:
                buf2 = set(buf) & set(line)
                buf = buf2
            else:
                buf = line
                begin_group = False
        else:
            count = len(buf)
            sum += count
            print(buf, count, sum)
            buf = ""
            begin_group = True
    return sum

def puzzle_7_1():
    with open("7.txt") as fp:
        data = fp.read().strip().splitlines()
    containers = {}
    for line in data:
        #m = re.match("([a-z]+) ([a-z]+) bags contain ((([0-9]) ([a-z]+) ([a-z]+)|no other) bags?(.|,)\s?)+", line)
        #if m:
        #    print(m.groups())
        #    #if m.groups()[2] == "no other":
        #    #    print(line)
        (subj, pred) = line.split("s contain ")
        containers[subj] = {}
        for p in map(lambda x: x.strip("s."), pred.split(", ")):
            if p != "no other bag":
                (count, inner_container) = p.split(" ", 1)
                containers[subj][inner_container] = count
    print(json.dumps(containers))
    look = "shiny gold bag"
    def _find_parent_bags(bag, containers):
        total_bags = []
        for (k, v) in containers.items():
            if bag in v:
                print(bag, k)
                total_bags += [k] + _find_parent_bags(k, containers)
        return list(set(total_bags))
    outer_bags = _find_parent_bags(look, containers)
    print(outer_bags)
    return len(outer_bags)

def puzzle_7_2():
    with open("7.txt") as fp:
        data = fp.read().strip().splitlines()
        containers = {} 
    for line in data:
        #m = re.match("([a-z]+) ([a-z]+) bags contain ((([0-9]) ([a-z]+) ([a-z]+)|no other) bags?(.|,)\s?)+", line)
        #if m:
        #    print(m.groups())
        #    #if m.groups()[2] == "no other": 
        #    #    print(line)
        (subj, pred) = line.split("s contain ")
        containers[subj] = {}
        for p in map(lambda x: x.strip("s."), pred.split(", ")): 
            if p != "no other bag":
                (count, inner_container) = p.split(" ", 1) 
                containers[subj][inner_container] = count  
    print(json.dumps(containers))
    look = "shiny gold bag"
    def _find_inner_bags(bag, containers):
        total_bags = []
        total_count = 0
        for inner_bag in containers[bag]:
            total_bags += [[inner_bag, containers[bag][inner_bag]]]
            total_count += int(containers[bag][inner_bag])
            (bags, count) = _find_inner_bags(inner_bag, containers)
            for bag2 in bags:
                print(bag2)
                bag2[1] = str(int(bag2[1]) * int(containers[bag][inner_bag]))
            #total_bags += int(containers[bag][inner_bag]) * bags
            #total_bags += map(lambda x: x[1] *= int(containers[bag][inner_bag]))
            total_bags += bags
            total_count += int(containers[bag][inner_bag]) * count
        return [total_bags, total_count]
    [inner_bags, total_count] = _find_inner_bags(look, containers)
    print(inner_bags)
    return(total_count)

def puzzle_8_1():
    with open("8.txt") as fp:
        data = fp.read().strip().splitlines()
    accumulator = 0
    ptr = 0
    seen_instrs = []
    while ptr not in seen_instrs:
        seen_instrs.append(ptr)
        instr = data[ptr]
        (op, arg) = instr.split()
        #(sign, count) = (arg[0], int(arg[1:]))
        if op == "acc":
            accumulator = eval("{}{}".format(accumulator, arg))
            ptr += 1
        elif op == "jmp":
            ptr = eval("{}{}".format(ptr, arg))
        elif op == "nop":
            ptr += 1
        print(instr, accumulator, ptr)
    return accumulator

def puzzle_8_2():
    with open("8.txt") as fp:
        data = fp.read().strip().splitlines()
    accumulator = 0
    ptr = 0
    seen_instrs = []
    updated_instrs = []
    flipped_bit = False
    while ptr not in seen_instrs and ptr != len(data):
        seen_instrs.append(ptr)
        instr = data[ptr]
        (op, arg) = instr.split()
        if op == "acc":
            accumulator = eval("{}{}".format(accumulator, arg))
            ptr += 1
        elif op == "jmp":
            if not flipped_bit and ptr not in updated_instrs:
                flipped_bit = True
                updated_instrs.append(ptr)
                op = "nop"
                ptr += 1
            else:
                ptr = eval("{}{}".format(ptr, arg))
        elif op == "nop":
            if not flipped_bit and ptr not in updated_instrs:
                flipped_bit = True
                updated_instrs.append(ptr)
                op = "jmp"
                ptr = eval("{}{}".format(ptr, arg))
            else:
                ptr += 1
        if flipped_bit == True and updated_instrs[-1] == ptr:
            print("{}* {} {} {}".format(op, arg, accumulator, ptr))
        else:
            print(instr, accumulator, ptr)
        if ptr > len(data) or ptr < 0 or ptr in seen_instrs:
            print("Instruction out of range or stuck in an infinite loop, resetting!")
            print(updated_instrs)
            accumulator = 0
            ptr = 0
            flipped_bit = False
            seen_instrs = []
    print("Success")
    return accumulator

def puzzle_9_1():
    with open("9.txt") as fp:
        data = list(map(int, fp.read().strip().splitlines()))
    preamble_len = 25
    weakness = 0
    for i in range(len(data)):
        preamble = data[i-preamble_len:i]
        print(i, data[i], preamble)
        if i >= preamble_len:
            for j in range(len(preamble) - 1):
                for k in range(j+1, len(preamble)):
                    if preamble[j] + preamble[k] == data[i]:
                        #print(preamble[j], preamble[k], data[i])
                        break
                else:
                    continue
                break
            else:
                weakness = data[i]
                print("ran out of numbers on {}...".format(weakness))
                break
    return weakness

def puzzle_9_2():
    with open("9.txt") as fp:
        data = list(map(int, fp.read().strip().splitlines()))
    #weakness = 127
    weakness = 36845998
    for i in range(len(data) - 1):
        for j in range(i+1, len(data)):
            if sum(data[i:j]) > weakness:
                break
            elif sum(data[i:j]) == weakness:
                print("found the sum: {}".format(data[i:j]))
                sum_weak2 = min(data[i:j]) + max(data[i:j])
                return sum_weak2

def puzzle_10_1():
    with open("10.txt") as fp:
        data = sorted(map(int, fp.read().strip().splitlines()))
    dev_jolt_rating = max(data) + 3
    data = [0] + data + [dev_jolt_rating]
    print(data)
    print(dev_jolt_rating)
    diffs = {}
    for i in range(len(data)-1):
        diff = data[i+1] - data[i]
        if diff in diffs:
            diffs[diff] += 1
        else:
            diffs[diff] = 1
    print(diffs)
    return(diffs[1] * diffs[3])

def puzzle_10_2():
    with open("10.test2.txt") as fp:
        data = sorted(map(int, fp.read().strip().splitlines()))
    dev_jolt_rating = max(data) + 3
    #data = [0] + data + [dev_jolt_rating]
    #print(data)
    count = 0
    for i in range(int(dev_jolt_rating/3), len(data)+1):
        for l in combinations(data, i):
            #print(l)
            l = [0] + list(l) + [dev_jolt_rating]
            #if l and l[0] == 0 and l[-1] == dev_jolt_rating:
            if l:
                for j in range(len(l)-1):
                    if not l[j+1] - l[j] <= 3:
                        break
                else:
                    count += 1
                    print(l)
    return count

def puzzle_10_2_redux():
    with open("10.txt") as fp:
        data = sorted(map(int, fp.read().strip().splitlines()))
    dev_jolt_rating = data[-1]+3
    data = [0] + data + [dev_jolt_rating]
    print(data)
    removable = []
    for i in range(1, len(data)-1):
        (a, b, c) = (data[i-1], data[i], data[i+1])
        if b - a < 3 and c - b < 3:
            removable.append(b)
    print(removable)
    count = 1
    for i in range(len(removable)+1):
        for j in list(combinations(removable, i)):
            if not j:
                continue
            tmplist = data.copy()
            for k in j:
                m = tmplist.index(k)
                if not tmplist[m+1] - tmplist[m-1] <= 3:
                    break
                tmplist.remove(k)
            else:
                #print(list(sorted(set(tmplist)-set(j))))
                count += 1
            #for l in range(len(tmplist) - 1):
            #    #print(tmplist[l], tmplist[l+1])
            #    if not tmplist[l+1] - tmplist[l] <= 3:
            #        #print("{} not viable".format(tmplist))
            #        break
            #else:
            #    #print(j, tmplist)
            #    count += 1
    print(data)
    print(count)

def puzzle_11_1():
    with open("11.test2.txt") as fp:
        data = list(map(list, fp.read().strip().splitlines()))
    prev_step = deepcopy(data)
    next_step = deepcopy(prev_step)
    start = True
    while start or next_step != prev_step:
        prev_step = deepcopy(next_step)
        if start:
            start = False
        for l in range(len(prev_step)):
            for c in range(len(prev_step[l])):
                #for line in prev_step:
                #    print("".join(line))
                adjacent_seats = []
                if l > 0:
                    if c > 0:
                        adjacent_seats.append(prev_step[l-1][c-1])
                    adjacent_seats.append(prev_step[l-1][c])
                    if c < len(prev_step[l]) - 1:
                        adjacent_seats.append(prev_step[l-1][c+1])
                if c > 0:
                    adjacent_seats.append(prev_step[l][c-1])
                if c < len(prev_step[l]) - 1:
                    adjacent_seats.append(prev_step[l][c+1])
                if l < len(prev_step) - 1:
                    if c > 0:
                        adjacent_seats.append(prev_step[l+1][c-1])
                    adjacent_seats.append(prev_step[l+1][c])
                    if c < len(prev_step[l]) - 1:
                        adjacent_seats.append(prev_step[l+1][c+1])
                #print(c, l, adjacent_seats)
                if prev_step[l][c] == "L" and adjacent_seats.count("#") == 0:
                    print("Updating {},{} to '#'".format(l, c))
                    next_step[l][c] = "#"
                    #print(next_step[l][c], prev_step[l][c])
                if prev_step[l][c] == "#" and adjacent_seats.count("#") >= 4:
                    print("Updating {},{} to 'L'".format(l, c))
                    next_step[l][c] = "L"
                    #print(next_step[l][c], prev_step[l][c])
                #print(data[l][c], end="")
                
            #print(list(map(str, next_step)))
        occupied_count = 0
        for row in next_step:
            occupied_count += row.count("#")
            print("".join(row))
        print(occupied_count)
    return occupied_count

def puzzle_11_2():
    with open("11.txt") as fp:
        data = list(map(list, fp.read().strip().splitlines()))
    prev_step = deepcopy(data)
    next_step = deepcopy(prev_step)
    start = True
    while start or prev_step != next_step:
        if start:
            start = False
        prev_step = deepcopy(next_step)
        for l in range(len(prev_step)):
            for c in range(len(prev_step[l])):
                adjacent_seats = []
                found_seats = {"n": False, "ne": False, "e": False, "se": False, \
                               "s": False, "sw": False, "w": False, "nw": False}
                for nl in range(l-1, -1, -1):
                    if not found_seats["n"] and prev_step[nl][c] != ".":
                        adjacent_seats.append(prev_step[nl][c])
                        found_seats["n"] = True
                    if not found_seats["nw"] and c - (l-nl) >= 0:
                        if prev_step[nl][c-(l-nl)] != ".":
                            adjacent_seats.append(prev_step[nl][c-(l-nl)])
                            found_seats["nw"] = True
                    if not found_seats["ne"] and c + (l-nl) < len(prev_step[l]):
                        if prev_step[nl][c+(l-nl)] != ".":
                            adjacent_seats.append(prev_step[nl][c+(l-nl)])
                            found_seats["ne"] = True
                for wc in range(c-1, -1, -1):
                    if not found_seats["w"] and prev_step[l][wc] != ".":
                        adjacent_seats.append(prev_step[l][wc])
                        found_seats["w"] = True
                for ec in range(c+1, len(prev_step[l])):
                    if not found_seats["e"] and prev_step[l][ec] != ".":
                        adjacent_seats.append(prev_step[l][ec])
                        found_seats["e"] = True
                for sl in range(l+1, len(prev_step)):
                    if not found_seats["s"] and prev_step[sl][c] != ".":
                        adjacent_seats.append(prev_step[sl][c])
                        found_seats["s"] = True
                    if not found_seats["sw"] and c - (sl-l) >= 0:
                        if prev_step[sl][c-(sl-l)] != ".":
                            adjacent_seats.append(prev_step[sl][c-(sl-l)])
                            found_seats["sw"] = True
                    if not found_seats["se"] and c + (sl-l) < len(prev_step[l]):
                        if prev_step[sl][c+(sl-l)] != ".":
                            adjacent_seats.append(prev_step[sl][c+(sl-l)])
                            found_seats["se"] = True
                #if prev_step[l][c] == "L":
                #    print(adjacent_seats)
                #print(prev_step[l][c], end="")
                
                if prev_step[l][c] == "L" and adjacent_seats.count("#") == 0:
                    print("Updating {},{} to '#'".format(l, c))
                    print(adjacent_seats)
                    next_step[l][c] = "#"
                    #print(next_step[l][c], prev_step[l][c])
                if prev_step[l][c] == "#" and adjacent_seats.count("#") >= 5:
                    print("Updating {},{} to 'L'".format(l, c))
                    print(adjacent_seats)
                    next_step[l][c] = "L"
                    #print(next_step[l][c], prev_step[l][c])
                #print(data[l][c], end="")
        occupied_count = 0
        for row in next_step:
            occupied_count += row.count("#")
            print("".join(row))
        print(occupied_count)
        #break
    return occupied_count

def puzzle_12_1():
    with open("12.txt") as fp:
        data = fp.read().strip().splitlines()
    directions = ["E", "S", "W", "N"]
    facing = "E"
    coords = [0, 0] # (-W/+E, -S/+N)
    def _turn_dir(start, direction, degrees):
        start_degrees = directions.index(start)*90
        if direction == "R":
            sym = "+"
        else:
            sym = "-"
        new_dir = directions[int(eval("(({}+360{}{})%360)/90".format(start_degrees, sym, degrees)))]
        return new_dir
    for instr in data:
        [act, val] = [instr[0], int("".join(instr[1:]))]
        print(act, val)
        if act == "F":
            act = facing
        if act == "N":
            coords[1] += val
        elif act == "S":
            coords[1] -= val
        elif act == "E":
            coords[0] += val
        elif act == "W":
            coords[0] -= val
        elif act == "L" or act == "R":
            facing = _turn_dir(facing, act, val)
            print("now facing {}".format(facing))
        print("new coords: {}".format(coords))
    return abs(coords[0]) + abs(coords[1])

def puzzle_12_2():
    with open("12.txt") as fp:
        data = fp.read().strip().splitlines()
    def _rotate_waypoint(direction, degrees, coords):
        if degrees == 180:
            new_coords = list(map(lambda x: 0-x, coords))
        elif (degrees == 90 and direction == "R") or (degrees == 270 and direction == "L"):
            # (-12, 10) -> (10, 12)
            # (13, 3) -> (3, -13)
            # (4, -7) -> (-7, -4)
            # (-5, -6) -> (-6, 5)
            new_coords = [coords[1], 0-coords[0]]
        elif (degrees == 270 and direction == "R") or (degrees == 90 and direction == "L"):
            # (-12, 10) -> (-10, -12)
            # (13, 3) -> (-3, 13)
            # (4, -7) -> (7, 4)
            # (-5, -6) -> (6, -5)
            new_coords = [0-coords[1], coords[0]]
        return new_coords
    waypoint_coords = [10, 1]
    ship_coords = [0, 0]
    print("Ship coords: {}\nWaypoint coords: {}".format(ship_coords, waypoint_coords))
    for instr in data:
        [act, val] = [instr[0], int("".join(instr[1:]))]
        print(act, val)
        if act == "F":
            ship_coords = [sum(x) for x in zip(*[ship_coords, list(map(lambda x: val*x, waypoint_coords))])]
            print("new ship coords: {}".format(ship_coords))
        elif act == "N":
            waypoint_coords[1] += val
        elif act == "S":
            waypoint_coords[1] -= val
        elif act == "E":
            waypoint_coords[0] += val
        elif act == "W":
            waypoint_coords[0] -= val
        elif act == "R" or act == "L":
            waypoint_coords = _rotate_waypoint(act, val, waypoint_coords)
        print("new waypoint coords: {}".format(waypoint_coords))
    return abs(ship_coords[0]) + abs(ship_coords[1])

def puzzle_13_1():
    with open("13.txt") as fp:
        data = fp.read().strip().splitlines()
    earliest_departure = int(data[0])
    buses = data[1].split(",")
    print(buses)
    closest_bus = 0
    closest_bus_id = 0
    for b in buses:
        if b == "x":
            continue
        bus_sched = int(b)
        while bus_sched < earliest_departure:
            bus_sched += int(b)
        if bus_sched < closest_bus or closest_bus == 0:
            print("Bus {} is closest with time {}, prev sched: {}".format(b, bus_sched, closest_bus))
            closest_bus = bus_sched
            closest_bus_id = int(b)
    return (closest_bus - earliest_departure) * closest_bus_id

def puzzle_13_2():
    with open("13.txt") as fp:
        data = fp.read().strip().splitlines()
    buses = data[1].split(",")
    #buses = ["67","7","59","61"]
    #buses = ["67","x", "7","59","61"]
    #buses = ["67","7","x", "59","61"]
    #buses = ["1789","37","47","1889"]
    bus_ints = list(map(int, [x for x in buses if x.isdigit()]))
    for b in bus_ints:
        print("{}, {}".format(b, buses.index(str(b))))
    #print(len(buses))
    product = reduce(lambda x, y: x*y, bus_ints)
    indx = max(bus_ints) + buses.index(str(max(bus_ints)))
    cont = True
    max_bus_idx = buses.index(str(max(bus_ints)))
    #indx = max(bus_ints) * 2 + max_bus_idx 
    #indx = 1068788
    indx = 0
    #indx = 3393583190
    indx = 100000000000282
    while True:
        #print("\nNew run..indx: {}".format(indx))
        for bus in bus_ints:
            bus_indx = indx - (max_bus_idx - buses.index(str(bus))) # correct so far...
            #print("Bus: {}, bus_idx: {}".format(bus, bus_indx))
            pos = int(bus_indx / bus) * bus
            #print(pos) # correct so far...?
            if pos == bus_indx:
                pass
                #print("Bus {} in place".format(bus))
                #print("Found a match!, bus: {}, pos_in_scope: {}".format(bus, bus_indx))
                #break
                if bus in [19, 463, 37]:
                    print("\nFound a match!, bus: {}, pos_in_scope: {}".format(bus, bus_indx))
                #    return
            else:
                #print("Bus {} not in place, cur_pos: {}, should_be: {}".format(bus, bus_indx, pos))
                break
            #pos_in_scope = pos + (buses.index(str(max(bus_ints))) - buses.index(str(bus)))
            #print(pos_in_scope)
            #print(max(bus_ints))
            #if pos_in_scope != max(bus_ints):
            #    print("Not a match, bus {} would be at {} rather than {}!".format(bus, pos_in_scope, indx+buses.index(str(bus))))
            #    break
            #return False
            #cont = False
        else:
            print("Found all matches!")
            return indx - max_bus_idx
        indx += max(bus_ints)
    """
    Found all matches!
    741745043105674
    
    real	9363m47.586s
    user	9362m49.425s
    sys	0m11.229s
    
    Holy shit! 6.5 days of 100% cpu.. that poor core..
    """

        #break
    #print(product)
    #bus_times = {}
    #for b in bus_ints:
    #    bt = b
    #    btl = [bt]
    #    while bt <= product:
    #        bt += b
    #        btl.append(bt)
    #    print(len(btl))
    #    
    #    bus_times[buses.index(str(b))] = btl
    #print(bus_times.keys())

def puzzle_14_1():
    with open("14.txt") as fp:
        data = fp.read().strip().splitlines()
    cur_mask = ""
    ferry_mem = {}
    for line in data:
        if line.startswith("mask = "):
            cur_mask = line.split("=")[1].strip()
        elif line.startswith("mem["):
            mem_pos = int(line.split("[")[1].split("]")[0])
            mem_val = "{0:036b}".format(int(line.split("=")[1].strip()))
            upd_mem_val = ""
            for c in range(len(cur_mask)):
                if cur_mask[c] == "X":
                    upd_mem_val += mem_val[c]
                else:
                    upd_mem_val += cur_mask[c]
            print(cur_mask, mem_val, upd_mem_val, int(mem_val, 2), int(upd_mem_val, 2))
            ferry_mem[mem_pos] = int(upd_mem_val, 2)
    print(ferry_mem)
    return sum(ferry_mem.values())

def puzzle_14_2():
    with open("14.txt") as fp:
        data = fp.read().strip().splitlines()
    cur_mask = ""
    ferry_mem = {}
    for line in data:
        if line.startswith("mask = "):
            cur_mask = line.split("=")[1].strip()
        elif line.startswith("mem["):
            mem_pos = int(line.split("[")[1].split("]")[0])
            mem_val = "{0:036b}".format(int(line.split("=")[1].strip()))
            mem_addr = "{0:036b}".format(mem_pos)
            x_count = cur_mask.count("X")
            num_perms = 2**x_count
            perms = ["{{0:0{}b}}".format(x_count).format(x) for x in range(num_perms)] # SO MUCH FASTER
            #perms = sorted(list(set(permutations("0"*x_count+"1"*x_count, x_count)))) # SLOOOOOOOOOOOOW
            print(cur_mask, x_count, mem_pos, mem_addr, int(mem_addr, 2))
            for p in perms:
                perm_val = ""
                xc = 0
                for c in range(len(cur_mask)):
                    if cur_mask[c] == "0":
                        perm_val += mem_addr[c]
                    elif cur_mask[c] == "1":
                        perm_val += "1"
                    elif cur_mask[c] == "X":
                        perm_val += p[xc]
                        xc += 1
                print(perm_val, int(perm_val, 2))
                ferry_mem[int(perm_val, 2)] = int(mem_val,2)
    return sum(ferry_mem.values())

def puzzle_15_1():
    with open("15.txt") as fp:
        data = fp.read().strip().split(",")
    #print(data)
    data = [1, 3, 2]
    #data = [2, 1, 3]
    #data = [1, 2, 3]
    #data = [2, 3, 1]
    #data = [3, 2, 1]
    #data = [3, 1, 2]
    cur_turn = 0
    seen_nums = {}
    cur_num = None
    next_num = None
    while cur_turn < 2020:
        if cur_turn < len(data):
            cur_num = int(data[cur_turn])
        else:
            cur_num = next_num
        if cur_num in seen_nums:
            next_num = cur_turn - seen_nums[cur_num]
            print("Cur_num: {} in seen_nums: {}, {} ago.  Next num: {}".format(cur_num, seen_nums[cur_num], cur_turn - seen_nums[cur_num], next_num))
        else:
            next_num = 0
            print("Cur_num: {} not in seen_nums.  Next num: {}".format(cur_num, next_num))
        seen_nums[cur_num] = cur_turn
        #print(cur_num, cur_turn, next_num)
        #print(seen_nums)
        cur_turn += 1
    return cur_num

def puzzle_15_1():  
    with open("15.txt") as fp:
        data = fp.read().strip().split(",")
    #print(data)
    data = [1, 3, 2]
    #data = [2, 1, 3]
    #data = [1, 2, 3]
    #data = [2, 3, 1]
    #data = [3, 2, 1]
    #data = [3, 1, 2]
    cur_turn = 0    
    seen_nums = {}  
    cur_num = None
    next_num = None
    #while cur_turn < 2020:
    while cur_turn < 30000000:
        if cur_turn < len(data):
            cur_num = int(data[cur_turn])
        else:
            cur_num = next_num
        if cur_num in seen_nums:
            next_num = cur_turn - seen_nums[cur_num]
            #print("Cur_num: {} in seen_nums: {}, {} ago.  Next num: {}".format(cur_num, seen_nums[cur_num], cur_turn - seen_nums[cur_num], next_num))
        else:
            next_num = 0
            #print("Cur_num: {} not in seen_nums.  Next num: {}".format(cur_num, next_num))
        seen_nums[cur_num] = cur_turn
        #print(cur_num, cur_turn, next_num)
        #print(seen_nums)
        cur_turn += 1 
    return cur_num

def puzzle_16_1():
    with open("16.txt") as fp:
        data = fp.read().strip().splitlines()
    myticket = ""
    myt = False
    nearby_tickets = []
    nbt = False
    fields = {}
    for line in data:
        if line.startswith("your ticket"):
            myt = True
        elif myt:
            myticket = line
            myt = False
        elif line.startswith("nearby tickets"):
            nbt = True
        elif nbt:
            nearby_tickets.append(line)
        elif not line:
            continue
        else:
            m = re.match("([a-z ]+): ([0-9]+)-([0-9]+) or ([0-9]+)-([0-9]+)", line)
            (field, min1, max1, min2, max2) = m.groups()
            fields[field] = [(int(min1), int(max1)), (int(min2), int(max2))]
    print(fields)
    print(myticket)
    print(nearby_tickets)
    valid_tickets = []
    invalid_tickets = []
    invalid_fields = 0
    for ticket in nearby_tickets:
        for field in map(int, ticket.split(",")):
            for f2 in fields:
                print(fields[f2], field)
                if fields[f2][0][0] <= field <= fields[f2][0][1] or fields[f2][1][0] <= field <= fields[f2][1][1]:
                    break
            else:
                print("Ticket does not match!, {}".format(ticket))
                invalid_fields += field
                break
        else:
            print("Ticket matches. {}".format(ticket))
            valid_tickets.append(ticket)
            continue
        invalid_tickets.append(ticket)
    print("Valid tickets: {}".format(valid_tickets))
    print("Invalid tickets: {}".format(invalid_tickets))
    return invalid_fields

def puzzle_16_2():
    with open("16.txt") as fp:
        data = fp.read().strip().splitlines()
    myticket = []
    myt = False
    nearby_tickets = []
    nbt = False
    fields = {}
    valid_fields = {} # map
    invalid_fields = {}
    for line in data:
        if line.startswith("your ticket"):
            myt = True
        elif myt:
            myticket = line.split(",")
            myt = False
        elif line.startswith("nearby tickets"):
            nbt = True
        elif nbt:
            nearby_tickets.append(line)
        elif not line:
            continue
        else:
            m = re.match("([a-z ]+): ([0-9]+)-([0-9]+) or ([0-9]+)-([0-9]+)", line)
            (field, min1, max1, min2, max2) = m.groups()
            fields[field] = [(int(min1), int(max1)), (int(min2), int(max2))]
    print(fields)
    print(myticket)
    print(nearby_tickets)
    valid_tickets = []
    invalid_tickets = []
    for ticket in nearby_tickets:
        tmp_invalid_fields = {}
        tmp_valid_fields = {}
        for ticket_field in range(len(ticket.split(","))):
            field = int(ticket.split(",")[ticket_field])
            fm = False
            for f2 in fields:
                #print(fields[f2], field)
                if fields[f2][0][0] <= field <= fields[f2][0][1] or fields[f2][1][0] <= field <= fields[f2][1][1]:
                    if f2 in tmp_valid_fields:
                        tmp_valid_fields[f2].append(ticket_field)
                    else:
                        tmp_valid_fields[f2] = [ticket_field]
                    #print("Field: {} matches {}".format(field, f2))
                    #print(tmp_valid_fields)
                    fm = True
                else:
                    if f2 in tmp_invalid_fields:
                        tmp_invalid_fields[f2].append(ticket_field)
                    else:
                        tmp_invalid_fields[f2] = [ticket_field]
            if not fm:
                #print("Ticket does not match!, {}".format(ticket))
                #invalid_fields += field
                break
        else:
            #print("Ticket matches. {}".format(ticket))
            valid_tickets.append(ticket)
            for k, v in tmp_invalid_fields.items():
                if k in invalid_fields:
                    invalid_fields[k] += v
                else:
                    invalid_fields[k] = v
            for k, v in tmp_valid_fields.items():
                if k in valid_fields:
                    valid_fields[k] += v
                else:
                    valid_fields[k] = v
            continue
        invalid_tickets.append(ticket)
    print("Valid tickets: {}".format(valid_tickets))
    print("Invalid tickets: {}".format(invalid_tickets))
    print("Valid fields: {}".format(valid_fields))
    print("Invalid fields: {}".format(invalid_fields))
    field_map = {}
    for f in valid_fields:
        if f in valid_fields and f in invalid_fields:
            print("{} valid fields = {}".format(f, list(set(valid_fields[f]) - set(invalid_fields[f]))))
            valid_fields[f] = list(set(valid_fields[f]) - set(invalid_fields[f]))
        else:
            print("{} valid fields = {}".format(f, list(set(valid_fields[f]))))
            valid_fields[f] = list(set(valid_fields[f]))
    print("Valid fields: {}".format(valid_fields))
    print("sorted valid fields: {}".format(sorted(valid_fields.items(), key=lambda item: len(item[1]))))
    sorted_fields = dict(sorted(valid_fields.items(), key=lambda item: len(item[1])))
    print("sorted valid fields: {}".format(sorted_fields))
    for k in sorted_fields:
        for v in sorted_fields[k]:
            for k2 in sorted_fields:
                if k != k2 and v in sorted_fields[k2]:
                    sorted_fields[k2].remove(v)
    print(sorted_fields)
    product = 1
    for k, v in sorted_fields.items():
        if k.startswith("departure"):
            product *= int(myticket[v[0]])
    return product

def puzzle_17_1():
    with open("17.test.txt") as fp:
        data = [fp.read().strip().splitlines()]
    print("\n".join(data[0]))
    print("======")
    cur_status = deepcopy(data)
    next_status = []
    #next_status = [['.'*(len(data[0][0])+2)]*(len(data[0])+2)]*(len(data)+2)
    #print(next_status)
    for i in range(6):
        if next_status:
            cur_status = deepcopy(next_status)
        print(cur_status)
        next_status = []
        for j in range(len(cur_status)+2):
            new_col = []
            for k in range(len(cur_status[0])+2):
                new_row = []
                for l in range(len(cur_status[0][0])+2):
                    new_row.append(".")
                new_col.append(new_row)
            next_status.append(new_col)
        #next_status = [[['.']*(len(cur_status[0][0])+2)]*(len(cur_status[0])+2)]*(len(cur_status)+2)
        for z in range(len(next_status)):
            #print(z)
            #print("\n".join(data[0]))
            for y in range(len(next_status[z])):
                for x in range(len(next_status[z][y])):
                    #print("ZYX: {}".format((z, y, x)))
                    neighbors = []
                    # looks good
                    if z >= 2 and z < (len(cur_status)+2):
                        if y >= 2 and y < (len(cur_status[z-2])+2):
                            if x >= 2 and x < (len(cur_status[z-2][y-2])+2):
                                neighbors.append(cur_status[z-2][y-2][x-2])
                            if x >= 1 and x < (len(cur_status[z-2][y-2]) +1):
                                neighbors.append(cur_status[z-2][y-2][x-1])
                            if x < len(cur_status[z-2][y-2]):
                              neighbors.append(cur_status[z-2][y-2][x])
                        if y >= 1 and y < (len(cur_status[z-2])+1):
                            if x >= 2 and x < (len(cur_status[z-2][y-1])+2):
                                neighbors.append(cur_status[z-2][y-1][x-2])
                            if x >= 1 and x < (len(cur_status[z-2][y-1])+1):
                                neighbors.append(cur_status[z-2][y-1][x-1])
                            if x < len(cur_status[z-2][y-1]):
                                neighbors.append(cur_status[z-2][y-1][x])
                        if x >= 2 and y < len(cur_status[z-2]):
                            neighbors.append(cur_status[z-2][y][x-2])
                        if x >= 1 and y < len(cur_status[z-2]) and x < (len(cur_status[z-2][y])+1):
                            neighbors.append(cur_status[z-2][y][x-1])
                        if y < len(cur_status[z-2]) and x < len(cur_status[z-2][y]):
                            neighbors.append(cur_status[z-2][y][x])
                    # how to exclude self from neighbors (?) done (?)
                    # seems correct in this section
                    if z >= 1 and z < (len(cur_status)+1):
                        if y >= 2 and y < (len(cur_status[z-1])+2):
                            if x >= 2 and x < (len(cur_status[z-1][y-2])+2):
                                neighbors.append(cur_status[z-1][y-2][x-2])
                            if x >= 1 and x < (len(cur_status[z-1][y-2])+1):
                                neighbors.append(cur_status[z-1][y-2][x-1])
                            if x < len(cur_status[z-1][y-2]):
                                neighbors.append(cur_status[z-1][y-2][x])
                        if y >= 1 and y < (len(cur_status[z-1])+1):
                            if x >= 2 and x < (len(cur_status[z-1][y-1])+2):
                                neighbors.append(cur_status[z-1][y-1][x-2])
                            #if x >= 1 and x < (len(cur_status[z-1][y-1])+1):
                            #    neighbors.append(cur_status[z-1][y-1][x-1])
                            if x < len(cur_status[z-1][y-1]):
                                neighbors.append(cur_status[z-1][y-1][x])
                        if x >= 2 and y < len(cur_status[z-1]):
                            neighbors.append(cur_status[z-1][y][x-2])
                        if x >= 1 and y < len(cur_status[z-1]) and x < (len(cur_status[z-1][y])+1):
                            neighbors.append(cur_status[z-1][y][x-1])
                        if y < len(cur_status[z-1]) and x < len(cur_status[z-1][y]):
                            neighbors.append(cur_status[z-1][y][x])
                    # everything below here is correct
                    if z < len(cur_status):
                        if y >= 2 and y < len(cur_status[z])+2:
                            if x >= 2 and x < (len(cur_status[z][y-2])+2):
                                neighbors.append(cur_status[z][y-2][x-2])
                            if x >= 1 and x < (len(cur_status[z][y-2])+1):
                                neighbors.append(cur_status[z][y-2][x-1])
                            if x < len(cur_status[z][y-2]):
                                neighbors.append(cur_status[z][y-2][x])
                        if y >= 1 and y < len(cur_status[z]) + 1:
                            if x >= 2 and x < (len(cur_status[z][y-1])+2):
                                neighbors.append(cur_status[z][y-1][x-2])
                            if x >= 1 and x < (len(cur_status[z][y-1])+1):
                                neighbors.append(cur_status[z][y-1][x-1])
                            if x < len(cur_status[z][y-1]):
                                neighbors.append(cur_status[z][y-1][x])
                        if x >= 2 and y < len(cur_status[z]):
                            neighbors.append(cur_status[z][y][x-2])
                        if x >= 1 and y < len(cur_status[z]) and x < (len(cur_status[z][y])+1):
                            neighbors.append(cur_status[z][y][x-1])
                        if y < len(cur_status[z]) and x < len(cur_status[z][y]):
                            neighbors.append(cur_status[z][y][x])
                    print("{} neighbors: {}".format((z, y, x), neighbors))
                    #print(z, y, x)
                    #print(cur_status)
                    #print(len(cur_status), len(cur_status[0]), len(cur_status[0][1]))
                    print(next_status)
                    if x > 0 and y > 0 and z > 0 and \
                      z <= len(cur_status) and y <= len(cur_status[0]) and x <= len(cur_status[0][0]):
                        prev_pos = cur_status[z-1][y-1][x-1]
                        if prev_pos == "#" and 2 <= neighbors.count("#") <= 3:
                            next_status[z][y][x] = '#'
                            print("Updating next status at {}".format((z, y, x)))
                        elif neighbors.count("#") == 3:
                            next_status[z][y][x] = '#'
                            print("Updating next status at {}".format((z, y, x)))
                    elif neighbors.count("#") == 3:
                        next_status[z][y][x] = '#'
                        print("Updating next status at {}".format((z, y, x)))
                    print(next_status)
                    #print(next_status[z][y][x], end="")
                #print()
            #print()
        #print("======")
        #print(next_status)
        total_live = 0
        for z in next_status:
            for y in z:
                for x in y:
                    print(x, end="")
                    if x == '#':
                        total_live += 1
                print()
            print()
        print(total_live)

def puzzle_17_2():
    with open("17.test.txt") as fp:
        data = fp.read().strip().splitlines()
    print(data)
    nb = [0, 1, 2]
    neighbors = sorted(list(set([(o, tw, th, f) for o in nb for tw in nb for th in nb for f in nb]) - set([(1, 1, 1, 1)])))
    print(neighbors)


def puzzle_18_1():
    with open("18.txt") as fp:
        data = fp.read().strip().splitlines()
    sum_tot = 0
    for line in data:
        print(line)
        total = 0
        num_stack = []
        op_active = False
        op_level = 0
        op_stack = []
        arg = 0
        for elem in line.split(" "):
            print(elem)
            if elem.startswith("("):
                print("inside parens")
                for c in range(1, elem.count("(")):
                    num_stack.append(1)
                    op_stack.append("*")
                    op_level += 1
                num_stack.append(int(elem.split("(")[-1]))
            elif elem.endswith(")"):
                print("ends parens")
                a = num_stack.pop(-1)
                b = op_stack.pop(-1)
                c = int(elem.split(")")[0])
                val = eval("{}{}{}".format(a, b, c))
                print("{}{}{} = {}".format(a, b, c, val))
                num_stack.append(val)
                op_level -= 1
                if not op_level:
                    op_active = False
                else:
                    for c in range( elem.count(")")):
                        if len(op_stack):
                            c = num_stack.pop(-1)
                            b = op_stack.pop(-1)
                            a = num_stack.pop(-1)
                            val = eval("{}{}{}".format(a, b, c))
                            print("{}{}{} = {}".format(a, b, c, val))
                            num_stack.append(val)
                            op_level -= 1
                            if not op_level:
                                op_active = False
            elif elem in ["+", "-", "*", "%"]:
                op_stack.append(elem)
                op_active = True
                op_level += 1
            else:
                if op_active:
                    a = num_stack.pop(-1)
                    b = op_stack.pop(-1)
                    c = int(elem)
                    val = eval("{}{}{}".format(a, b, c))
                    print("{}{}{} = {}".format(a, b, c, val))
                    num_stack.append(val)
                    op_level -= 1
                    if not op_level:
                        op_active = False
                else:
                    num_stack.append(int(elem))
            print(num_stack, op_stack)
        if op_level:
            c = num_stack.pop(-1)
            b = op_stack.pop(-1)
            a = num_stack.pop(-1)
            op_level -= 1
            tot = eval("{}{}{}".format(a, b, c))
        else:
            tot = num_stack.pop(0)
        print(tot)
        print("done.\n")
        sum_tot += tot
        #break
    return sum_tot

def puzzle_18_2():
    pass

def puzzle_19_1():
    with open("19.txt") as fp:
        data = fp.read().strip().splitlines()
    rules = {}
    messages = []
    for line in data:
        #m = re.match("([0-9]+): (?:\"([ab])\"|(?:([0-9]+)(?:|\s([0-9]+))(?:(?:|\s\|\s([0-9]+)(?:|\s([0-9]+))))))$", line)
        m = re.match("([0-9]+): (?:\"([ab])\"|(?:([0-9]+)(\s[0-9]+)?(?:|\s([0-9]+))(?:(?:|\s\|\s([0-9]+)(?:|\s([0-9]+))))))$", line)
        if m:
            (rule_num, letter, uno, dos, tres, cuatro, cinco) = m.groups()
            print(line, m.groups())
            if letter:
                rules[int(rule_num)] = letter
                print("Letter match: {}: {}".format(rule_num, letter))
            else:
                rules[int(rule_num)] = [False if not uno else int(uno), False if not dos else int(dos), False if not tres else int(tres), \
                                   False if not cuatro else int(cuatro), False if not cinco else int(cinco)]
                print(rules[int(rule_num)])
        else:
            messages.append(line)
    print(rules)
    def _get_children(rule):
        if type(rules[rule]) == str:
            return rules[rule]
        rs = rules[rule]
        rule_set = ""
        if rs[0]:
            rs0 = _get_children(rs[0])
            rule_set += rs0
        if rs[1]:
            rs1 = _get_children(rs[1])
            rule_set += rs1
        if rs[2]:
            rs2 = _get_children(rs[2])
            rule_set += rs2
        if rs[3]:
            rs3 = _get_children(rs[3])
            rule_set += "|" + rs3
        if rs[4]:
            rs4 = _get_children(rs[4])
            rule_set += rs4
        return "({})".format(rule_set)
    rule_set = "^{}$".format(_get_children(0))
    matches = 0
    for message in messages:
        if re.match(rule_set, message):
            print("{} matches {}".format(message, rule_set))
            matches += 1
    return matches
    
def puzzle_19_2():
    with open("19.2.txt") as fp:
        data = fp.read().strip().splitlines()
    # not 280, not 315, not 82, not 224, not 253
    # answer is 294
    rules = {}
    messages = []
    for line in data:
        m = re.match("([0-9]+): (?:\"([ab])\"|(?:([0-9]+)(\s[0-9]+)?(?:|\s([0-9]+))(?:(?:|\s\|\s([0-9]+)(?:|\s([0-9]+))(?:|\s([0-9]+))))))$", line)
        if m:
            (rule_num, letter, uno, dos, tres, quattro, cinco, seis) = m.groups()
            if letter:
                rules[int(rule_num)] = letter
            else:
                rules[int(rule_num)] = [False if not uno else int(uno), False if not dos else int(dos), False if not tres else int(tres), \
                                   False if not quattro else int(quattro), False if not cinco else int(cinco), False if not seis else int(seis)]
        else:
            messages.append(line)
    def _get_children(rule):
        if type(rules[rule]) == str: 
            return rules[rule]
        rs = rules[rule]
        rule_set = ""
        if rule == 8:
            rs0 = _get_children(rs[0])
            print("({})+".format(rs0))
            return "({})+".format(rs0)
        elif rule == 11:
            rs0 = _get_children(rs[0])
            rs1 = _get_children(rs[1])
            print(rs0)
            print(rs1)
            #match = "({}(?1)?{})".format(rs0, rs1) # would prefer to get this to work, but alas...
            # this is a cheesy way to do it, but it works, thx https://github.com/mariothedog/Advent-of-Code-2020/blob/main/Day%2019/day_19.py#L53-L60 :-(
            match = "(({}){{1}}({}){{1}}|".format(rs0, rs1)
            match += "({}){{2}}({}){{2}}|".format(rs0, rs1)
            match += "({}){{3}}({}){{3}}|".format(rs0, rs1)
            match += "({}){{4}}({}){{4}})".format(rs0, rs1)
            #match += "({}){{5}}({}){{5}}|".format(rs0, rs1)
            #match += "({}){{6}}({}){{6}}|".format(rs0, rs1)
            #match += "({}){{7}}({}){{7}}|".format(rs0, rs1)
            #match += "({}){{8}}({}){{8}})".format(rs0, rs1)
            print("11 regex: {}".format(match))
            return match
        if rs[0]:
            rs0 = _get_children(rs[0])
            rule_set += rs0
        if rs[1]:
            rs1 = _get_children(rs[1])
            rule_set += rs1
        if rs[2]:
            rs2 = _get_children(rs[2])
            rule_set += rs2
        if rs[3]:
            rs3 = _get_children(rs[3])
            rule_set += "|" + rs3
        if rs[4]:
            rs4 = _get_children(rs[4])
            rule_set += rs4
        if rs[5]:
            rs5 = _get_children(rs[5])
            rule_set += rs5
        return "({})".format(rule_set)
    print(_get_children(42))
    print(_get_children(31))
    rule_set = "^{}$".format(_get_children(0))
    print(rule_set)
    matches = 0
    for message in messages:
        m = regex.match(rule_set, message)
        if m:
            print("{} matches {}".format(message, rule_set))
            #print(m.groups())
            matches += 1
        else:
            print("no match")
    return matches

def puzzle_20_1():
    with open("20.txt") as fp:
        data = fp.read().strip().splitlines()
    tiles = {}
    buf = []
    for line in data:
        if line.startswith("Tile"):
            tile_num = int(re.match("Tile ([0-9]+)", line).groups()[0])
        elif not line:
            tiles[tile_num] = buf
            buf = []
        else:
            buf.append(list(line))
    tiles[tile_num] = buf
    borders = {}
    matches = {}
    for tile in tiles:
        print(tile)
        print("\n".join(["".join(t) for t in tiles[tile]]))
        tbf = [pos for (pos, char) in enumerate(tiles[tile][0]) if char == "#"]
        tbr = [pos for (pos, char) in enumerate(tiles[tile][0][::-1]) if char == "#"]
        bbf = [pos for (pos, char) in enumerate(tiles[tile][-1]) if char == "#"]
        bbr = [pos for (pos, char) in enumerate(tiles[tile][-1][::-1]) if char == "#"]
        lbf = [pos for (pos, char) in enumerate([l[0] for l in tiles[tile]]) if char == '#']
        lbr = [pos for (pos, char) in enumerate([l[0] for l in tiles[tile]][::-1]) if char == '#']
        rbf = [pos for (pos, char) in enumerate([l[-1] for l in tiles[tile]]) if char == '#']
        rbr = [pos for (pos, char) in enumerate([l[-1] for l in tiles[tile]][::-1]) if char == '#']
        borders[tile] = [tbf, rbf, bbf, lbf, tbr, rbr, bbr, lbr]
        print(borders[tile])
    corner_product = 1
    for tile in borders:
        match_count = 0
        for t2 in borders:
            if tile == t2:
                continue
            for side in range(len(borders[tile])):
                for side2 in range(len(borders[t2])):
                    if borders[tile][side] == borders[t2][side2]:
                        print("{} side {} and {} side {} match!".format(tile, side, t2, side2))
                        match_count += 1
        if match_count == 4: # cheat ;-)
            print("Corner: {} found!".format(tile))
            corner_product *= tile
    return corner_product

def puzzle_20_2():
    pass

def puzzle_21_1():
    with open("21.test.txt") as fp:
        data = fp.read().strip().splitlines()
    recipes = {} #map allergens -> [[ingredients], [...]]
    not_an_allergen = []
    for line in data:
        ingredients = []
        allergens = []
        (ing, aller) = line.split("(")
        for i in ing.strip().split():
            if i not in ingredients:
                ingredients.append(i)
        for a in aller.split(")")[0].split("contains ")[1].split(", "):
            if a not in allergens:
                allergens.append(a)
        print(ingredients)
        print(allergens)
        for a2 in allergens:
            if a2 not in recipes:
                recipes[a2] = []
            recipes[a2].append(ingredients)
    print(recipes)
    possible_allergens = {}
    for allergen in recipes:
        possible_allergens[allergen] = []
        allergen_ingredients_to_remove = []
        #print(allergen)
        #print(recipes[allergen])
        for r1 in recipes[allergen]:
            #print(r1)
            for a1 in r1:
                if a1 in allergen_ingredients_to_remove:
                    continue
                for r2 in recipes[allergen]:
                    if r2 == r1 or r2 in allergen_ingredients_to_remove:
                        continue
                    if a1 not in r2:
                        print("Allergen {} recipe {}, ingredient {} not a cause of this allergen.".format(allergen, r1, a1))
                        if a1 not in not_an_allergen:
                            print("appending {} to naa".format(a1))
                            not_an_allergen.append(a1)
                        allergen_ingredients_to_remove.append(a1)
        #print(allergen_ingredients_to_remove)
        for r1 in recipes[allergen]:
            for a1 in r1:
                if a1 not in allergen_ingredients_to_remove and a1 not in possible_allergens[allergen]:
                    possible_allergens[allergen].append(a1)
        #while True:
        for allergen in possible_allergens:
            if len(possible_allergens[allergen]) == 1:
                for oa in possible_allergens:
                    if oa == allergen:
                        continue
                    if possible_allergens[allergen][0] in possible_allergens[oa]:
                        print(allergen, oa, possible_allergens[allergen][0], possible_allergens[oa])
                        possible_allergens[oa].remove(possible_allergens[allergen][0])
                        print("removed {} from {}'s allergens".format(possible_allergens[allergen][0], oa))
                print("found")
            #break
        print(possible_allergens.values())
        for v in possible_allergens.values():
            print(v[0])
            if v[0] in not_an_allergen:
                print("removing {} from naa".format(v[0]))
                not_an_allergen.remove(v[0])
    print(sorted(possible_allergens))
    print(not_an_allergen)
    un_allergen_count = 0
    for ua in not_an_allergen:
        for line in data:
            un_allergen_count += line.count(ua)
    return un_allergen_count
        #print(list(map(lambda x: recipes[allergen].count(x), [x for x in recipes[allergen]])))
        #count_allergens = list(set(zip(recipes[allergen], list(map(lambda x: recipes[allergen].count(x), [x for x in recipes[allergen]])))))
        #allergen_count[allergen] = count_allergens
    #for a in allergen_count:
    #    for b in allergen_count[a]:
    #        if b[1] == 2:
    #            pass
    #    print(a, allergen_count[a])

def puzzle_21_2():
    with open("21.txt") as fp:
        data = fp.read().strip().splitlines()
    recipes = {} #map allergens -> [[ingredients], [...]]
    for line in data:
        ingredients = []
        allergens = []
        (ing, aller) = line.split("(")
        for i in ing.strip().split():
            if i not in ingredients:
                ingredients.append(i)
        for a in aller.split(")")[0].split("contains ")[1].split(", "):
            if a not in allergens:
                allergens.append(a)
        print(ingredients)
        print(allergens)
        for a2 in allergens:
            if a2 not in recipes:
                recipes[a2] = []
            recipes[a2].append(ingredients)
    print(recipes)
    possible_allergens = {}
    for allergen in recipes:
        possible_allergens[allergen] = []
        allergen_ingredients_to_remove = []
        #print(allergen)
        #print(recipes[allergen])
        for r1 in recipes[allergen]:
            #print(r1)
            for a1 in r1:
                if a1 in allergen_ingredients_to_remove:
                    continue
                for r2 in recipes[allergen]:
                    if r2 == r1 or r2 in allergen_ingredients_to_remove:
                        continue
                    if a1 not in r2:
                        print("Allergen {} recipe {}, ingredient {} not a cause of this allergen.".format(allergen, r1, a1))
                        allergen_ingredients_to_remove.append(a1)
        for r1 in recipes[allergen]:
            for a1 in r1:
                if a1 not in allergen_ingredients_to_remove and a1 not in possible_allergens[allergen]:
                    possible_allergens[allergen].append(a1)
        for allergen in possible_allergens:
            if len(possible_allergens[allergen]) == 1:
                for oa in possible_allergens:
                    if oa == allergen:
                        continue
                    if possible_allergens[allergen][0] in possible_allergens[oa]:
                        print(allergen, oa, possible_allergens[allergen][0], possible_allergens[oa])
                        possible_allergens[oa].remove(possible_allergens[allergen][0])
                        print("removed {} from {}'s allergens".format(possible_allergens[allergen][0], oa))
                print("found")
            #break
    print(possible_allergens)
    return ",".join([possible_allergens[x][0] for x in sorted(possible_allergens)])

def puzzle_22_1():
    with open("22.txt") as fp:
        data = fp.read().strip().splitlines()
    hands = {}
    buf = []
    for line in data:
        if line.startswith("Player"):
            player = int(line.split(" ")[1].split(":")[0])
        elif line == "":
            hands[player] = buf
            buf = []
        else:
            buf.append(int(line.strip()))
    hands[player] = buf
    
    print(hands)
    while hands[1] and hands[2]:
        p1 = hands[1].pop(0)
        p2 = hands[2].pop(0)
        if p1 > p2:
            hands[1].append(p1)
            hands[1].append(p2)
        else:
            hands[2].append(p2)
            hands[2].append(p1)
    if len(hands[1]) == 0:
        winner = 2
    else:
        winner = 1
    print(hands)
    score = 0
    for card in range(1, len(hands[winner])+1):
         score += (card * hands[winner].pop(-1))
    return score

def puzzle_22_2():
    with open("22.txt") as fp:
        data = fp.read().strip().splitlines()
    hands = {}
    buf = []
    for line in data:
        if line.startswith("Player"):
            player = int(line.split(" ")[1].split(":")[0])
        elif line == "":
            hands[player] = buf
            buf = []
        else:
            buf.append(int(line.strip()))
    hands[player] = buf
    #configs = [] # keep track of previous game states
    #winner = None
    #print(hands)
    global game_count
    game_count = 1
    global recurse_depth
    recurse_depth = 0
    def _play_game(hands):
        global game_count
        global recurse_depth
        gc = 0 + game_count
        round_count = 1
        #if gc % 10000 == 0:
        print(" ==== Game {} Depth {} ==== ".format(gc, recurse_depth))
        #if gc > 1000 and recurse_depth <= 5:
        #    sleep(10)
        configs = []
        while hands[1] and hands[2]:
            #if recurse_depth <=4:
            print("\n-- Round {} (Game {}, Depth {}) --".format(round_count, gc, recurse_depth))
            if list(hands.values()) in configs:
                print("Duplicate play! Player 1 wins game {}.".format(gc))
                game_winner = 1
                return game_winner
            configs.append(deepcopy(list(hands.values())))
            #if recurse_depth <=4:
            print("Player 1's deck: {}\nPlayer 2's deck: {}".format(", ".join(map(str, hands[1])), ", ".join(map(str, hands[2]))))
            p1 = hands[1].pop(0)
            p2 = hands[2].pop(0)
            print("Player 1 plays {}.\nPlayer 2 plays {}.".format(p1, p2))
            if p1 <= len(hands[1]) and p2 <= len(hands[2]):
                print("Playing a sub-game to determine the winner...\n")
                game_count += 1
                recurse_depth += 1
                h1 = deepcopy(hands[1])[:p1]
                h2 = deepcopy(hands[2])[:p2]
                if max(h1) > max(h2):
                    round_winner = 1
                    print("Skipping play, P1 wins this round")
                else:
                    round_winner = _play_game({1: h1, 2: h2})
                print("\n...anyway, back to game {}.".format(gc))
                recurse_depth -= 1
            elif p1 > p2:
                round_winner = 1
            else:
                round_winner = 2
            print("Player {} wins round {} of game {}!".format(round_winner, round_count, gc))
            if round_winner == 1:
                hands[1].append(p1)
                hands[1].append(p2)
            else:
                hands[2].append(p2)
                hands[2].append(p1)
            #print("Deck as of now: {}".format(hands))
            round_count += 1
        if len(hands[1]) == 0:
            game_winner = 2
        else:
            game_winner = 1
        print("The winner of game {} is player {}!".format(gc, game_winner))
        return game_winner
    game_winner = _play_game(hands)
    print(game_winner, hands)
    score = 0
    for card in range(1, len(hands[game_winner])+1):
        score += (card * hands[game_winner].pop(-1))
    return score

def puzzle_23_1():
    with open("23.txt") as fp:
        data = fp.read().strip()
    cups = list(map(int, list(data)))
    for i in range(100):
        print("Move {}".format(i))
        print("cups: {}".format(cups))
        pickup = [cups.pop(1), cups.pop(1), cups.pop(1)]
        print("pickup: {}".format(", ".join(map(str, pickup))))
        destination = cups[0] - 1
        if destination == 0:
            destination = 9
        while destination in pickup:
            destination = destination - 1
            if destination == 0:
                destination = 9
        print("destination: {}".format(destination))
        dest_pos = cups.index(destination)
        for i in range(3):
            cups.insert(dest_pos+1+i, pickup.pop(0))
        rot = cups.pop(0)
        cups.append(rot)
    while(cups[0] != 1):
        cups.append(cups.pop(0))
    return int("".join(map(str, cups))[1:])

def puzzle_23_2():
    # too slow, didn't want to wait
    # https://www.reddit.com/r/adventofcode/comments/kiyxim/2020_day_23_part_2_when_the_brute_force_approach/ggu2xoe/
    # you only need an array where arr[cup] = next_cup and everything will be very fast
    with open("23.txt") as fp:
        data = fp.read().strip()
    cups = list(map(int, list(data)))
    next_cups = [0] * 1000001
    for c in range(len(cups)-1):
        next_cups[cups[c]] = cups[c+1]
    next_cups[cups[-1]] = 10
    for i in range(10, 1000001):
        cups.append(i)
        next_cups[i] = i+1
    next_cups[-1] = cups[0]
    pos = 0
    cur_num = cups[pos]
    max_cup = max(cups)
    for i in range(1, 10000001):
        next_one = next_cups[cur_num]
        next_two = next_cups[next_one]
        next_three = next_cups[next_two]
        next_four = next_cups[next_three]
        destination = cur_num - 1
        if destination == 0: 
            destination = max_cup
        while destination in [next_one, next_two, next_three]:
            destination = destination - 1
            if destination == 0:
                destination = max_cup
        dest_next = next_cups[destination]
        next_cups[cur_num] = next_four
        next_cups[next_three] = dest_next
        next_cups[destination] = next_one
        cur_num = next_four
        pos = (pos + 1) % max_cup
    #print(next_cups[1], next_cups[next_cups[1]])
    return next_cups[1] * next_cups[next_cups[1]]

def puzzle_24_1():
    with open("24.txt") as fp:
        data = fp.read().strip().splitlines()
    tiles = []
    #data = ["nwwswee", "neeseww", "nenenwnwswswswswee", "neswswswese", "sesesw", "swseesw"]
    # [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, -3, -2], [-2, -1, 0], [-1, -2, -1]]
    # [swswswee], [sesesw], [seswswe]
    # s3w3e2, s3e2w1, s3e2w2
    # [sw: 3, e: 2], [se: 2, sw: 1], [se: 1, sw: 2, e: 1]
    for line in data:
        #print(line)
        (ne, se, sw, nw) = (line.count("ne"), line.count("se"), line.count("sw"), line.count("nw"))
        (e, w) = (line.count("e") - ne - se, line.count("w") - nw - sw)
        #print("ne: {}, nw: {}, se: {}, sw: {}, e: {}, w: {}".format(ne, nw, se, sw, e, w))
        ew = float(0.5 * ne + 0.5 * se + e - w - 0.5 * nw - 0.5 * sw)
        ns = ne + nw - se - sw
        #print("ns: {}, ew: {}".format(ns, ew))
        tiles.append((ns, ew))
    tiles_flipped = 0
    for tile in set(tiles):
        #print(tile, tiles.count(tile))
        if tiles.count(tile) % 2:
            tiles_flipped += 1
    print(tiles)
    return tiles_flipped

def puzzle_24_2():
    with open("24.test.txt") as fp:
        data = fp.read().strip().splitlines()
    tiles = []
    for line in data:
        (ne, se, sw, nw) = (line.count("ne"), line.count("se"), line.count("sw"), line.count("nw"))
        (e, w) = (line.count("e") - ne - se, line.count("w") - nw - sw)
        ew = float(0.5 * ne + 0.5 * se + e - w - 0.5 * nw - 0.5 * sw)
        ns = ne + nw - se - sw
        tiles.append((ns, ew))
    tiles_flipped = []
    for tile in set(tiles):
        print(tile, tiles.count(tile))
        if tiles.count(tile) % 2:
            tiles_flipped += [tile]
    print(tiles_flipped)
    for i in range(1):
        neighbors = []
        for t in tiles_flipped:
            print(t)
            n1 = (t[0]-1, t[1]-0.5)
            n2 = (t[0]-1, t[1]+0.5)
            n3 = (t[0], t[1]-1)
            n4 = (t[0], t[1]+1)
            n5 = (t[0]+1, t[1]-0.5)
            n6 = (t[0]+1, t[1]+0.5)
            print("tile: {}, neighbors: {}".format(t, [n1, n2, n3, n4, n5, n6]))
            neighbors += [n1, n2, n3, n4, n5, n6]
        print(set(neighbors))
        tta = []
        ttr = []
        for n in set(neighbors):
            print("neighbor: {}, count: {}, black? {}".format(n, neighbors.count(n), n in tiles_flipped))
            
            if n in tiles_flipped and (neighbors.count(n) == 0 or neighbors.count(n) > 2):
                print("{} flips to white, {}, {}".format(n, n in tiles_flipped, neighbors.count(n)))
                ttr += [n]
            elif n not in tiles_flipped and neighbors.count(n) == 2:
                print("{} flips to black.  {}, {}".format(n, n not in tiles_flipped, neighbors.count(n)))
                tta += [n]
        tiles_flipped = list(set(tiles_flipped) - set(ttr)) + tta
        print(tiles_flipped, len(tiles_flipped))
    return len(tiles_flipped)


def main():
    #print(puzzle_1_1())
    #print(puzzle_1_2())
    #print(puzzle_2_1())
    #print(puzzle_2_2())
    #print(puzzle_3_1())
    #print(puzzle_3_2())
    #print(puzzle_4_1())
    #print(puzzle_4_2())
    #print(puzzle_5_1())
    #print(puzzle_5_2())
    #print(puzzle_6_1())
    #print(puzzle_6_2())
    #print(puzzle_7_1())
    #print(puzzle_7_2())
    #print(puzzle_8_1())
    #print(puzzle_8_2())
    #print(puzzle_9_1())
    #print(puzzle_9_2())
    #print(puzzle_10_1())
    #print(puzzle_10_2_redux())
    #print(puzzle_11_1())
    #print(puzzle_11_2())
    #print(puzzle_12_1())
    #print(puzzle_12_2())
    #print(puzzle_13_1())
    #print(puzzle_13_2()) # caution, takes 6.5 days currently
    #print(puzzle_14_1())
    #print(puzzle_14_2())
    #print(puzzle_15_1())
    #print(puzzle_15_2())
    #print(puzzle_16_1())
    #print(puzzle_16_2())
    #print(puzzle_17_1())
    #print(puzzle_17_2())
    #print(puzzle_18_1())
    #print(puzzle_18_2())
    #print(puzzle_19_1())
    #print(puzzle_19_2())
    #print(puzzle_20_1())
    #print(puzzle_20_2())
    #print(puzzle_21_1())
    #print(puzzle_21_2())
    #print(puzzle_22_1())
    #print(puzzle_22_2())
    #print(puzzle_23_1())
    #print(puzzle_23_2())
    #print(puzzle_24_1())
    print(puzzle_24_2())
    

if __name__ == '__main__':
    main()
