#!/usr/bin/env python

import string

def puzzle_1_1():
    with open("1.txt") as fp:
        data = fp.read().strip().splitlines()
    maxsum = 0
    ssum = 0
    for s in data:
        if s == '':
            if ssum > maxsum:
                maxsum = ssum
            ssum = 0
        else:
            ssum += int(s)
    if ssum > maxsum:
        maxsum = ssum
    return maxsum

def puzzle_1_2():
    with open("1.txt") as fp:
        data = fp.read().strip().splitlines()
    sums = []
    ssum = 0
    for s in data:
        if s == '':
            sums.append(ssum)
            ssum = 0
        else:
            ssum += int(s)
    sums.append(ssum)
    return sum(sorted(sums)[-3:])

def puzzle_2_1():
    with open("2.txt") as fp:
        data = fp.read().strip().splitlines()
    scores = {"X": 1, "Y": 2, "Z": 3}
    total = 0
    wld = {"A": {"X": 3, "Y": 6, "Z": 0}, "B": {"X": 0, "Y": 3, "Z": 6}, "C": {"X": 6, "Y": 0, "Z": 3}}
    for line in data:
        (op, my) = line.split(" ")
        total += scores[my] + wld[op][my]
    return total

def puzzle_2_2():
    with open("2.txt") as fp:
        data = fp.read().strip().splitlines()
    shapes = {"A": {"X": 3, "Y": 1, "Z": 2}, "B": {"X": 1, "Y": 2, "Z": 3}, "C": {"X": 2, "Y": 3, "Z": 1}}
    wld_score = {"X": 0, "Y": 3, "Z": 6}
    total = 0
    for line in data:
        (op, end) = line.split(" ")
        total += wld_score[end] + shapes[op][end]
    return total

def puzzle_3_1():
    with open("3.txt") as fp:
        data = fp.read().strip().splitlines()
    total = 0
    for line in data:
        (fh, lh) = (line[:int(len(line)/2)], line[int(len(line)/2):])
        for c in fh:
            if c in lh:
                total += string.ascii_letters.index(c) + 1
                break
    return total

def puzzle_3_2():
    with open("3.txt") as fp:
        data = fp.read().strip().splitlines()
    total = 0
    while data:
        (elf1, elf2, elf3) = data.pop(0), data.pop(0), data.pop(0)
        for c in elf1:
            if c in elf2 and c in elf3:
                total += string.ascii_letters.index(c) + 1
                break
    return total

def puzzle_4_1():
    with open("4.txt") as fp:
        data = fp.read().strip().splitlines()
    c = 0
    for line in data:
        e1, e2 = map(lambda x: x.split("-"), line.split(","))
        e1l = list(range(int(e1[0]), int(e1[1]) + 1))
        e2l = list(range(int(e2[0]), int(e2[1]) + 1))
        if list(set(e1l) - set(e2l)) == [] or list(set(e2l) - set(e1l)) == []:
            c += 1
    return c

def puzzle_4_2():
    with open("4.txt") as fp:
        data = fp.read().strip().splitlines()
    c = 0
    for line in data:
        e1, e2 = map(lambda x: x.split("-"), line.split(","))
        e1l = list(range(int(e1[0]), int(e1[1]) + 1))
        e2l = list(range(int(e2[0]), int(e2[1]) + 1))
        if e1l[0] in e2l or e1l[:-1] in e2l or \
           e2l[0] in e1l or e2l[:-1] in e1l:
            c += 1
    return c

def puzzle_5_1():
    with open("5.txt") as fp:
        data = fp.read().rstrip().splitlines()
    stacks = {}
    moves = []
    instack = True
    for line in data:
        if not line:
            instack = False
        elif instack:
            for r in range(int(len(line)/4)+1):
                if line[(r*4)+1] in string.ascii_letters:
                    if r+1 in stacks:
                        stacks[r+1].append(line[(r*4)+1])
                    else: 
                        stacks[r+1] = [line[(r*4)+1]]
        else:
            l = line.split()
            moves.append([int(l[1]), int(l[3]), int(l[5])])
    for m in moves:
        for c in range(m[0]):
            stacks[m[2]].insert(0, stacks[m[1]].pop(0))
    result = ""
    for i in range(len(stacks)):
        result += stacks[i+1][0]
    return result

def puzzle_5_2():
    with open("5.txt") as fp:
        data = fp.read().rstrip().splitlines()
    stacks = {}
    moves = []
    instack = True
    for line in data:
        if not line:
            instack = False
        elif instack:
            for r in range(int(len(line)/4)+1):
                if line[(r*4)+1] in string.ascii_letters:
                    if r+1 in stacks:
                        stacks[r+1].append(line[(r*4)+1])
                    else: 
                        stacks[r+1] = [line[(r*4)+1]]
        else:
            l = line.split()
            moves.append([int(l[1]), int(l[3]), int(l[5])])
    for m in moves:
        boxes = stacks[m[1]][0:m[0]]
        for i in range(m[0]):
            stacks[m[1]].pop(0)
        stacks[m[2]] = boxes + stacks[m[2]]
    result = ""
    for i in range(len(stacks)):
        result += stacks[i+1][0]
    return result

def puzzle_6_1():
    with open("6.txt") as fp:
        data = fp.read().strip()
    buffer = []
    buf_point = 0
    for c in data:
        if len(buffer) < 4:
            buffer.append(c)
            buf_point += 1
        else:
            if len(set(buffer)) == 4:
                break
            else:
                buffer.pop(0)
                buffer.append(c)
                buf_point += 1
    return buf_point

def puzzle_6_2():
    with open("6.txt") as fp:
        data = fp.read().strip()
    buffer = []
    buf_point = 0
    for c in data:
        if len(buffer) < 14:
            buffer.append(c)
            buf_point += 1
        else:
            if len(set(buffer)) == 14:
                break
            else:
                buffer.pop(0)
                buffer.append(c)
                buf_point += 1
    return buf_point

def puzzle_7_1():
    with open("7.txt") as fp:
        data = fp.read().rstrip().splitlines()
    dirs = {}
    cwd = "/"
    in_ls = False
    for line in data:
        l = line.split()
        if in_ls:
            if l[0] == "$":
                in_ls = False
            else:
                (size, file) = l
                if size == "dir":
                    continue
                if cwd in dirs:
                    dirs[cwd] += int(size)
                    if cwd != "/":
                        parent_dir = "/".join(cwd.split("/")[:-1]) or "/"
                        if parent_dir in dirs:
                            dirs[parent_dir] += int(size)
                        else:
                            dirs[parent_dir] = int(size)
                        while parent_dir != "/":
                            parent_dir = "/".join(parent_dir.split("/")[:-1]) or "/"
                            if parent_dir in dirs:
                                dirs[parent_dir] += int(size)
                            else:
                                dirs[parent_dir] = int(size)
                else:
                    dirs[cwd] = int(size)
                    if cwd != "/":
                        parent_dir = "/".join(cwd.split("/")[:-1]) or "/"
                        if parent_dir in dirs:
                            dirs[parent_dir] += int(size)
                        else:
                            dirs[parent_dir] = int(size)
                        while parent_dir != "/":
                            parent_dir = "/".join(parent_dir.split("/")[:-1]) or "/"
                            if parent_dir in dirs:
                                dirs[parent_dir] += int(size)
                            else:
                                dirs[parent_dir] = int(size)
        if not in_ls and l[0] == "$":
            if l[1] == "cd":
                if l[2].startswith("/"):
                    cwd = l[2]
                elif l[2].startswith(".."):
                    cwd = "/".join(cwd.rstrip("/").split("/")[:-1])
                    if cwd == "":
                        cwd = "/"
                else:
                    cwd = cwd.rstrip("/") + "/" + l[2]
            elif l[1] == "ls":
                in_ls = True
    tot = 0
    for d in dirs:
        if dirs[d] <= 100000:
            tot += dirs[d]
    return tot

def puzzle_7_2():
    with open("7.txt") as fp: 
        data = fp.read().rstrip().splitlines()
    dirs = {}
    cwd = "/"
    in_ls = False
    for line in data:
        l = line.split()
        if in_ls:
            if l[0] == "$":
                in_ls = False
            else:
                (size, file) = l
                if size == "dir":
                    continue
                if cwd in dirs:
                    dirs[cwd] += int(size)
                    if cwd != "/":
                        parent_dir = "/".join(cwd.split("/")[:-1]) or "/"
                        if parent_dir in dirs:
                            dirs[parent_dir] += int(size)
                        else:
                            dirs[parent_dir] = int(size)
                        while parent_dir != "/":
                            parent_dir = "/".join(parent_dir.split("/")[:-1]) or "/"
                            if parent_dir in dirs:
                                dirs[parent_dir] += int(size)
                            else:
                                dirs[parent_dir] = int(size)
                else:
                    dirs[cwd] = int(size)
                    if cwd != "/":
                        parent_dir = "/".join(cwd.split("/")[:-1]) or "/"
                        if parent_dir in dirs:
                            dirs[parent_dir] += int(size)
                        else:
                            dirs[parent_dir] = int(size)
                        while parent_dir != "/":
                            parent_dir = "/".join(parent_dir.split("/")[:-1]) or "/"
                            if parent_dir in dirs:
                                dirs[parent_dir] += int(size)
                            else:
                                dirs[parent_dir] = int(size)
        if not in_ls and l[0] == "$":
            if l[1] == "cd":
                if l[2].startswith("/"):
                    cwd = l[2] 
                elif l[2].startswith(".."):
                    cwd = "/".join(cwd.rstrip("/").split("/")[:-1])
                    if cwd == "":
                        cwd = "/"
                else:
                    cwd = cwd.rstrip("/") + "/" + l[2]
            elif l[1] == "ls":
                in_ls = True
    total_space = 70000000
    update_space = 30000000
    needed_space = update_space - (total_space - dirs["/"])
    min_dir = update_space
    for d in dirs:
        if dirs[d] > needed_space and dirs[d] < min_dir:
            min_dir = dirs[d]
    return min_dir

def puzzle_8_1():
    with open("8.txt") as fp:
        data = fp.read().rstrip().splitlines()
    grid = []
    visible_count = 0
    for line in data:
        grid.append(list(map(int, line)))
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if row == 0 or row == len(grid) - 1 or \
              col == 0 or col == len(grid[row]) - 1:
                visible_count += 1
            else:
                for i in range(row): # look up
                    if grid[i][col] >= grid[row][col]:
                        break
                else:
                    visible_count += 1
                    continue
                for i in range(col): # look left
                    if grid[row][i] >= grid[row][col]:
                        break
                else:
                    visible_count += 1
                    continue
                for i in range(col + 1, len(grid[row])): # look right
                    if grid[row][i] >= grid[row][col]:
                        break
                else:
                    visible_count += 1
                    continue
                for i in range(row + 1, len(grid)): # look down
                    if grid[i][col] >= grid[row][col]:
                        break
                else:
                    visible_count += 1
                    continue
    return visible_count

def puzzle_8_2():
    with open("8.txt") as fp:
        data = fp.read().rstrip().splitlines()
    grid = []
    best_view_score = 0
    for line in data:
        grid.append(list(map(int, line)))
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            (u, d, l, r) = (0, 0, 0, 0)
            for i in range(row - 1, -1, -1): # look up
                u += 1
                if grid[i][col] >= grid[row][col]:
                    break
            for i in range(col - 1, -1, -1): # look left
                l += 1
                if grid[row][i] >= grid[row][col]:
                    break
            for i in range(row + 1, len(grid)): # look down
                d += 1
                if grid[i][col] >= grid[row][col]:
                    break
            for i in range(col + 1, len(grid[row])): # look right
                r += 1
                if grid[row][i] >= grid[row][col]:
                    break
            if u * d * l * r > best_view_score:
                best_view_score = u * d * l * r
    return best_view_score

def main():
    print(puzzle_1_1())
    print(puzzle_1_2())
    print(puzzle_2_1())
    print(puzzle_2_2())
    print(puzzle_3_1())
    print(puzzle_3_2())
    print(puzzle_4_1())
    print(puzzle_4_2())
    print(puzzle_5_1())
    print(puzzle_5_2())
    print(puzzle_6_1())
    print(puzzle_6_2())
    print(puzzle_7_1())
    print(puzzle_7_2())
    print(puzzle_8_1())
    print(puzzle_8_2())


if __name__ == '__main__':
    main()
