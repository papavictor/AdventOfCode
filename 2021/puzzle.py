#!/usr/bin/env python

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
            if prev_sumd and sumd > prev_sumd:
                sumd_inc += 1
            prev_sumd = sumd
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

def main():
    print(puzzle_1_1())
    print(puzzle_1_2())
    print(puzzle_2_1())
    print(puzzle_2_2())

if __name__ == '__main__':
    main()
