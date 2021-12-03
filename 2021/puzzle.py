#!/usr/bin/env python

from copy import deepcopy

def puzzle_1_1():
    with open("1.txt") as fp:
        data = fp.read().strip().splitlines()
    prev_depth = int(data[0])
    inc_count = 0
    for line in data[1:]:
        diff = int(line) - prev_depth
        prev_depth = int(line)
        if diff > 0:
            inc_count += 1
    return inc_count

def puzzle_1_2():
    with open("1.txt") as fp:
        data = fp.read().strip().splitlines()
    depths = []
    prev_sumd = 0
    sumd_inc = 0
    for line in data:
        depths.append(int(line))
        if len(depths) > 3:
            depths.pop(0)
        if len(depths) == 3:
            sumd = sum(depths)
            #print(sumd)
            if prev_sumd and sumd > prev_sumd:
                sumd_inc += 1
            prev_sumd = sumd
        #print(depths)
    return sumd_inc

def puzzle_2_1():
    with open("2.txt") as fp:
        data = fp.read().strip().splitlines()
    xpos = 0
    ypos = 0
    for line in data:
        amt = int(line.split(" ")[1])
        if line.startswith("forward"):
            xpos += amt
        elif line.startswith("down"):
            ypos += amt
        elif line.startswith("up"):
            ypos -= amt
    return (xpos * ypos)

def puzzle_2_2():
    with open("2.txt") as fp:
        data = fp.read().strip().splitlines()
    hpos = 0
    aim = 0
    depth = 0
    for line in data:
        amt = int(line.split(" ")[1])
        if line.startswith("forward"):
            hpos += amt
            depth += aim * amt
        elif line.startswith("down"):
            aim += amt
        elif line.startswith("up"):
            aim -= amt
    return (hpos * depth)

def puzzle_3_1():
    with open("3.txt") as fp:
        data = fp.read().strip().splitlines()
    bits = {}
    for line in data:
        for c in range(len(line)):
            if c not in bits:
                bits[c] = {'0': 0, '1': 0}
            bits[c][line[c]] += 1
    maxm = ""
    minm = ""
    for b in bits:
        if bits[b]['0'] > bits[b]['1']:
            maxm += "0"
            minm += "1"
        else:
            maxm += "1"
            minm += "0"
    return int(maxm, 2) * int(minm, 2)

def puzzle_3_2():
    with open("3.txt") as fp:
        data = fp.read().strip().splitlines()
    maxdata = deepcopy(data)
    mindata = deepcopy(data)
    while len(maxdata) > 1:
        for c in range(len(maxdata[0])):
            newmaxdata = deepcopy(maxdata)
            bits = {"0": 0, "1": 0}
            maxm = ""
            for line in maxdata:
                bits[line[c]] += 1
            if bits["0"] > bits["1"]:
                maxm = "0"
            else:
                maxm = "1"
            for line in maxdata:
                if not line[c] == maxm:
                    newmaxdata.remove(line)
                    if len(newmaxdata) == 1:
                        maxdata = newmaxdata
                        break
            else:
                maxdata = newmaxdata
                continue
            break
    while len(mindata) > 1:
        for c in range(len(mindata[0])):
            newmindata = deepcopy(mindata)
            bits = {"0": 0, "1": 0}
            minm = ""
            for line in mindata:
                bits[line[c]] += 1
            if bits["0"] > bits["1"]:
                minm = "1"
            else:
                minm = "0"
            for line in mindata:
                if not line[c] == minm:
                    newmindata.remove(line)
                    if len(newmindata) == 1:
                        mindata = newmindata
                        break
            else:
                mindata = newmindata
                continue
            break
    return int(mindata[0], 2) * int(maxdata[0], 2)

def main():
    print(puzzle_1_1())
    print(puzzle_1_2())
    print(puzzle_2_1())
    print(puzzle_2_2())
    print(puzzle_3_1())
    print(puzzle_3_2())

if __name__ == '__main__':
    main()
