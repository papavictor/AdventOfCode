#!/usr/bin/env python

import json
import math
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
                size = l[0]
                if size == "dir":
                    continue
                if cwd in dirs:
                    dirs[cwd] += int(size)
                else:
                    dirs[cwd] = int(size)
                parent_dir = cwd
                while True:
                    if parent_dir == "/":
                        break
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
                    cwd = "/".join(cwd.rstrip("/").split("/")[:-1]) or "/"
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
                size = l[0]
                if size == "dir":
                    continue
                if cwd in dirs:
                    dirs[cwd] += int(size)
                else:
                    dirs[cwd] = int(size)
                parent_dir = cwd
                while True:
                    if parent_dir == "/":
                        break
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
                    cwd = "/".join(cwd.rstrip("/").split("/")[:-1]) or "/"
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

def puzzle_9_1():
    with open("9.txt") as fp:
        data = fp.read().strip().splitlines()
    h = [0, 0]
    t = [0, 0]
    visited_positions = []
    for line in data:
        (direction, distance) = line.split()
        for i in range(int(distance)):
            if direction == "R":
                h[0] += 1
            elif direction == "L":
                h[0] -= 1
            elif direction == "U":
                h[1] += 1
            elif direction == "D":
                h[1] -= 1
            if abs(h[0] - t[0]) > 1:
                if t[0] > h[0]:
                    t[0] += h[0] - t[0] + 1
                else:
                    t[0] += h[0] - t[0] - 1
                if abs(h[1] - t[1]) > 1:
                    if t[1] > h[1]:
                        t[1] += h[1] - t[1] + 1
                    else:
                        t[1] += h[1] - t[1] - 1
                elif abs(h[1] - t[1]) == 1:
                    t[1] += h[1] - t[1]
            if abs(h[1] - t[1]) > 1:
                if t[1] > h[1]:
                    t[1] += h[1] - t[1] + 1
                else:
                    t[1] += h[1] - t[1] - 1
                if abs(h[0] - t[0]) == 1:
                    t[0] += h[0] - t[0]
            visited_positions.append(tuple(t))
    return len(set(visited_positions))

def puzzle_9_2():
    with open("9.txt") as fp:
        data = fp.read().strip().splitlines()
    pos = {} # H = 0
    for k in range(10):
        pos[k] = [0, 0]
    visited_positions = []
    for line in data:
        (direction, distance) = line.split()
        for i in range(int(distance)):
            if direction == "R":
                pos[0][0] += 1
            elif direction == "L":
                pos[0][0] -= 1
            elif direction == "U":
                pos[0][1] += 1
            elif direction == "D":
                pos[0][1] -= 1
            for i in range(1, 10):
                if abs(pos[i-1][0] - pos[i][0]) > 1:
                    if pos[i][0] > pos[i-1][0]:
                        pos[i][0] += pos[i-1][0] - pos[i][0] + 1
                    else:
                        pos[i][0] += pos[i-1][0] - pos[i][0] - 1
                    if abs(pos[i-1][1] - pos[i][1]) > 1:
                        if pos[i][1] > pos[i-1][1]:
                            pos[i][1] += pos[i-1][1] - pos[i][1] + 1
                        else:
                            pos[i][1] += pos[i-1][1] - pos[i][1] - 1
                    elif abs(pos[i-1][1] - pos[i][1]) == 1:
                        pos[i][1] += pos[i-1][1] - pos[i][1]
                if abs(pos[i-1][1] - pos[i][1]) > 1:
                    if pos[i][1] > pos[i-1][1]:
                        pos[i][1] += pos[i-1][1] - pos[i][1] + 1
                    else:
                        pos[i][1] += pos[i-1][1] - pos[i][1] - 1
                    if abs(pos[i-1][0] - pos[i][0]) == 1:
                        pos[i][0] += pos[i-1][0] - pos[i][0]
            visited_positions.append(tuple(pos[9]))
    return len(set(visited_positions))

def puzzle_10_1():
    with open("10.txt") as fp:
        data = fp.read().rstrip().splitlines()
    add_cycles = list(map(lambda x: x.startswith("addx "), data)).count(True) * 2
    noop_cycles = list(map(lambda x: x.startswith("noop"), data)).count(True)
    total_cycles = add_cycles + noop_cycles
    cycles = [20, 60, 100, 140, 180, 220]
    X = 1
    signal = 0
    in_prog = False
    instr = ""
    signal_sums = 0
    for c in range(1, total_cycles + 1):
        signal = c * X
        if in_prog:
            in_prog = False
            if c in cycles:
                signal_sums += signal
            X += int(instr.split()[1])
        else:
            instr = data.pop(0)
            if instr.startswith("addx "):
                in_prog = True
            if c in cycles:
                signal_sums += signal
    return signal_sums

def puzzle_10_2():
    with open("10.txt") as fp:
        data = fp.read().rstrip().splitlines()
    add_cycles = list(map(lambda x: x.startswith("addx"), data)).count(True) * 2
    noop_cycles = list(map(lambda x: x.startswith("noop"), data)).count(True)
    total_cycles = add_cycles + noop_cycles
    X = 1
    crt = [['.' for i in range(40)] for j in range(6)]
    signal = 0
    in_prog = False
    instr = ""
    for c in range(1, total_cycles + 1):
        crt_row = int((c - 1)/40)
        crt_col = int((c - 1)%40)
        signal = c * X
        if in_prog:
            in_prog = False
            if X - 1 <= crt_col <= X + 1:
                crt[crt_row][crt_col] = '#'
            X += int(instr.split()[1])
        else:
            instr = data.pop(0)
            if instr.startswith("addx "):
                in_prog = True
            if X - 1 <= crt_col <= X + 1:
                crt[crt_row][crt_col] = '#'
    output = "\n".join(["".join(line) for line in crt])
    return output

def puzzle_11_1():
    with open("11.txt") as fp:
        data = fp.read().strip().splitlines()
    monkeys = {}
    cur_monk = 0
    for line in data:
        if line.startswith("Monkey "):
            cur_monk = int(line.strip(":").split()[1])
            monkeys[cur_monk] = {}
        elif line.startswith("  Starting items: "):
            monkeys[cur_monk]["items"] = list(map(int, line.split(":")[1].strip().split(", ")))
        elif line.startswith("  Operation: "):
            monkeys[cur_monk]["operation"] = line.split(":")[1].strip()
        elif line.startswith("  Test:"):
            monkeys[cur_monk]["test"] = int(line.split()[-1])
        elif line.startswith("    If true"):
            monkeys[cur_monk]["test_true"] = int(line.split()[-1])
        elif line.startswith("    If false"):
            monkeys[cur_monk]["test_false"] = int(line.split()[-1])
    counted = dict.fromkeys(monkeys.keys(), 0)
    for r in range(20):
        for m in sorted(monkeys.keys()):
            for i in monkeys[m]["items"]:
                counted[m] += 1
                new = eval(monkeys[m]["operation"].split("= ")[1].replace("old", str(i)))
                level = int(new / 3)
                if not level % monkeys[m]["test"]:
                    monkeys[monkeys[m]["test_true"]]["items"].append(level)
                else:
                    monkeys[monkeys[m]["test_false"]]["items"].append(level)
            monkeys[m]["items"] = []
    return math.prod(sorted(counted.values(), reverse=True)[0:2])

def puzzle_11_2():
    with open("11.txt") as fp:
        data = fp.read().strip().splitlines()
    monkeys = {}
    cur_monk = 0
    for line in data:
        if line.startswith("Monkey "):
            cur_monk = int(line.strip(":").split()[1])
            monkeys[cur_monk] = {}
        elif line.startswith("  Starting items: "):
            monkeys[cur_monk]["items"] = list(map(int, line.split(":")[1].strip().split(", ")))
        elif line.startswith("  Operation: "):
            monkeys[cur_monk]["operation"] = line.split("=")[1].strip()
        elif line.startswith("  Test:"):
            monkeys[cur_monk]["test"] = int(line.split()[-1])
        elif line.startswith("    If true"):
            monkeys[cur_monk]["test_true"] = int(line.split()[-1])
        elif line.startswith("    If false"):
            monkeys[cur_monk]["test_false"] = int(line.split()[-1])
    test_product = math.prod([monkeys[m]["test"] for m in monkeys])
    counted = dict.fromkeys(monkeys.keys(), 0)
    smk = sorted(monkeys.keys())
    for r in range(10000):
        for m in smk:
            for i in monkeys[m]["items"]:
                counted[m] += 1
                op_l = monkeys[m]["operation"].replace("old", str(i)).split()
                if op_l[1] == '*':
                    new = int(op_l[0]) * int(op_l[2]) % test_product
                else:
                    new = int(op_l[0]) + int(op_l[2]) % test_product
                if not new % monkeys[m]["test"]:
                    monkeys[monkeys[m]["test_true"]]["items"].append(new)
                else:
                    monkeys[monkeys[m]["test_false"]]["items"].append(new)
            monkeys[m]["items"] = []
    return math.prod(sorted(counted.values(), reverse=True)[0:2])

def puzzle_12_1():
    with open("12.txt") as fp:
        data = list(map(lambda x: list(x), fp.read().strip().splitlines()))
    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] == 'S':
                start = (x, y)
            elif data[y][x] == 'E':
                end = (x, y)
    data[end[1]][end[0]] = 'z'
    data[start[1]][start[0]] = 'a'
    path_found = False
    seen_cells = [end]
    last_seen_cells = [end]
    cur_count = 1
    while not path_found:
        marked_cells = []
        for cell in last_seen_cells:
            neighbor_cells = []
            for i in range(cell[1] - 1, cell[1]+2):
                for j in range(cell[0] - 1, cell[0] + 2):
                    if i >= 0 and i < len(data) and j >= 0 and j < len(data[0]) and \
                      (i != cell[1] and j == cell[0] or i == cell[1] and j != cell[0]):
                        neighbor_cells.append((j, i))
            for c in set(neighbor_cells) - set(seen_cells) - set(marked_cells):
                if ord(data[c[1]][c[0]]) >= ord(data[cell[1]][cell[0]]) - 1:
                    marked_cells.append(c)
                    if c == start:
                        path_found = True
                        break
            if path_found:
                break
        seen_cells += marked_cells
        last_seen_cells = marked_cells
        if not path_found:
            cur_count += 1
    return cur_count

def puzzle_12_2():
    with open("12.txt") as fp:
        data = list(map(lambda x: list(x), fp.read().strip().splitlines()))
    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] == 'E':
                end = (x, y)
    data[end[1]][end[0]] = 'z'
    path_found = False
    seen_cells = [end]
    last_seen_cells = [end]
    cur_count = 1
    while not path_found:
        marked_cells = []
        for cell in last_seen_cells:
            neighbor_cells = []
            for i in range(cell[1] - 1, cell[1]+2):
                for j in range(cell[0] - 1, cell[0] + 2):
                    if i >= 0 and i < len(data) and j >= 0 and j < len(data[0]) and \
                      (i != cell[1] and j == cell[0] or i == cell[1] and j != cell[0]):
                        neighbor_cells.append((j, i))
            for c in set(neighbor_cells) - set(seen_cells) - set(marked_cells):
                if ord(data[c[1]][c[0]]) >= ord(data[cell[1]][cell[0]]) - 1:
                    marked_cells.append(c)
                    if data[c[1]][c[0]] == 'a':
                        path_found = True
                        break
            if path_found:
                break
        if not path_found:
            seen_cells += marked_cells
            last_seen_cells = marked_cells
            cur_count += 1
    return cur_count

def puzzle_13_1():
    def _compare(l, r):
        if type(l) == int and type(r) == int:
            if l < r:
                return True
            elif l > r:
                return False
            return None
        elif type(l) == list and type(r) == int:
            return _compare(l, [r])
        elif type(l) == int and type(r) == list:
            return _compare([l], r)
        elif type(l) == list and type(r) == list:
            while l and r:
                l1 = l.pop(0)
                r1 = r.pop(0)
                result = _compare(l1, r1)
                if result == False:
                    return False
                elif result == True:
                    return True
            if r and not l:
                return True
            if l and not r:
                return False
            return None
    with open("13.txt") as fp:
        data = fp.read().strip().splitlines()
    pairs = {}
    pc = 1
    while data:
        left = json.loads(data.pop(0))
        right = json.loads(data.pop(0))
        if data:
            blank = data.pop(0)
        pairs[pc] = _compare(left, right)
        pc += 1
    sumt = 0
    for k, v in pairs.items():
        if v == True:
            sumt += k
    return sumt

def puzzle_13_2():
    def _compare(l, r):
        if type(l) == int and type(r) == int:
            if l < r:
                return True
            elif l > r:
                return False
            return None
        elif type(l) == list and type(r) == int:
            return _compare(l, [r])
        elif type(l) == int and type(r) == list:
            return _compare([l], r)
        elif type(l) == list and type(r) == list:
            while l and r:
                l1 = l.pop(0)
                r1 = r.pop(0)
                result = _compare(l1, r1)
                if result == False:
                    return False
                elif result == True:
                    return True
            if r and not l:
                return True
            if l and not r:
                return False
            return None
    def _quick_sort(l):
        if len(l) < 2:
            return l
        partition = l[-1]
        ltl = []
        gtl = []
        for e in range(len(l) - 1):
            if _compare(json.loads(l[e]), json.loads(partition)):
                ltl.append(l[e])
            else:
                gtl.append(l[e])
        ltl = _quick_sort(ltl)
        gtl = _quick_sort(gtl)
        return ltl + [partition] + gtl
    with open("13.txt") as fp:
        data = fp.read().strip().splitlines()
    sorted_list = ['[[2]]', '[[6]]']
    while data:
        left = data.pop(0)
        right = data.pop(0)
        if data:
            blank = data.pop(0)
        sorted_list += [left, right]
    sorted_list = _quick_sort(sorted_list)
    return (sorted_list.index('[[2]]') + 1) * (sorted_list.index('[[6]]') + 1)

def puzzle_14_1():
    with open("14.txt") as fp:
        data = fp.read().strip().splitlines()
    rock_lines = []
    minxs, maxxs, maxys = [], [], []
    for line in data:
        points = line.split(" -> ")
        minxs.append(int(min(list(map(lambda x: x.split(","), points)), key=lambda x: x[0])[0]))
        maxxs.append(int(max(list(map(lambda x: x.split(","), points)), key=lambda x: x[0])[0]))
        maxys.append(int(max(list(map(lambda x: x.split(","), points)), key=lambda x: x[1])[1]))
        for i in range(len(points)-1):
            rock_lines.append((list(map(int, points[i].split(","))), list(map(int, points[i+1].split(",")))))
    (maxx, maxy, minx, miny) = (max(maxxs) + 1, max(maxys) + 1, min(minxs), 0)
    # design the cave #
    cave = [['.' for i in range(maxx - minx)] for j in range(maxy - miny)]
    for line in rock_lines:
        (s, e) = line
        for x in range(min([s[0], e[0]]), max([s[0], e[0]])+1):
            for y in range(min([s[1], e[1]]), max([s[1], e[1]])+1):
                cave[y-miny][x-minx] = '#'
    # drip the sand #
    c = 0
    end_of_game = False
    while not end_of_game:
        fsp = (500 - minx, 1-miny)
        while not end_of_game:
            if fsp[1]+ 1 < len(cave) and cave[fsp[1]+1][fsp[0]] == '.':
                fsp = (fsp[0], fsp[1]+1)
            elif fsp[0]-1 >= 0 and fsp[1] + 1 < len(cave) and cave[fsp[1]+1][fsp[0]-1] == '.':
                if fsp[0]-1 == 0 and cave[fsp[1]+1][fsp[0]-1] == '.':
                    end_of_game = True # at left edge on a diagonal with no wall
                    break
                fsp = (fsp[0]-1, fsp[1]+1)
            elif fsp[0]+1 < len(cave[0]) and fsp[1] + 1 < len(cave) and cave[fsp[1]+1][fsp[0]+1] == '.':
                if fsp[0]+1 == len(cave[0]) -1 and cave[fsp[1]+1][fsp[0]+1] == '.':
                    end_of_game = True # at right edge on a diagonal with no wall
                    break
                fsp = (fsp[0]+1, fsp[1]+1)
            else:
                if fsp[1] + 1 == len(cave):
                    end_of_game = True # reached the bottom
                    break
                break
        if not end_of_game:
            cave[fsp[1]][fsp[0]] = 'o'
            c += 1
    return c

def puzzle_14_2():
    with open("14.txt") as fp:
        data = fp.read().strip().splitlines()
    rock_lines = []
    minxs, maxxs, maxys = [], [], []
    for line in data:
        points = line.split(" -> ")
        minxs.append(int(min(list(map(lambda x: x.split(","), points)), key=lambda x: x[0])[0]))
        maxxs.append(int(max(list(map(lambda x: x.split(","), points)), key=lambda x: x[0])[0]))
        maxys.append(int(max(list(map(lambda x: x.split(","), points)), key=lambda x: x[1])[1]))
        for i in range(len(points)-1):
            rock_lines.append((list(map(int, points[i].split(","))), list(map(int, points[i+1].split(",")))))
    (maxx, maxy, minx, miny) = (max(maxxs) + 1, max(maxys) + 1, min(minxs), 0)
    maxw = maxy * 2 + 4
    rock_lines.append(((500-int(maxw/2)-1, maxy+1), (500+int(maxw/2)+1, maxy+1)))
    maxy += 2
    minx = 500-int(maxw/2)-1
    maxx = 500+int(maxw/2)+2
    # design the cave #
    cave = [['.' for i in range(maxx - minx)] for j in range(maxy - miny)]
    for line in rock_lines:
        (s, e) = line
        for x in range(min([s[0], e[0]]), max([s[0], e[0]])+1):
            for y in range(min([s[1], e[1]]), max([s[1], e[1]])+1):
                cave[y-miny][x-minx] = '#'
    # drip the sand #
    c = 0
    end_of_game = False
    while not end_of_game:
        fsp = (500 - minx, 0)
        while not end_of_game:
            if cave[fsp[1]+1][fsp[0]] == '.':
                fsp = (fsp[0], fsp[1]+1)
            elif cave[fsp[1]+1][fsp[0]-1] == '.':
                fsp = (fsp[0]-1, fsp[1]+1)
            elif cave[fsp[1]+1][fsp[0]+1] == '.':
                fsp = (fsp[0]+1, fsp[1]+1)
            else:
                if fsp[1] == 0:
                    end_of_game = True # reached the top
                break
        cave[fsp[1]][fsp[0]] = 'o'
        c += 1
    return c

def puzzle_15_1():
    with open("15.txt") as fp:
        data = fp.read().strip().splitlines()
    check = 2000000
    sensors = {}
    for line in data:
        sens = tuple(map(lambda x: int(x.split("=")[1]), " ".join(line.split()[2:4]).rstrip(":").split(", ")))
        beacon = tuple(map(lambda x: int(x.split("=")[1]), " ".join(line.split()[-2:]).split(", ")))
        sensors[sens] = beacon
    occupied = [b for a in list(sensors.items()) for b in a]
    minx = min(occupied, key=lambda x: x[0])[0]
    miny = min(occupied, key=lambda x: x[1])[1]
    grid = []
    mds = {}
    for s, b in sensors.items():
        manhattan_distance = abs(s[0]-b[0]) + abs(s[1]-b[1])
        mds[s] = manhattan_distance
    for s, md in mds.items():
        j = check - miny
        if abs(s[1] - j) > md:
            continue
        for i in range(s[0]-md, s[0]+md+1):
            if abs(s[0] - i) + abs(s[1] - j) <= md:
                if (i-minx, check) not in occupied:
                    grid.append(i-minx)
    return len(set(grid))

def puzzle_15_2():
    with open("15.txt") as fp:
        data = fp.read().strip().splitlines()
    max_coord = 4000000
    mds = {}
    for line in data:
        s = tuple(map(lambda x: int(x.split("=")[1]), " ".join(line.split()[2:4]).rstrip(":").split(", ")))
        b = tuple(map(lambda x: int(x.split("=")[1]), " ".join(line.split()[-2:]).split(", ")))
        manhattan_distance = abs(s[0]-b[0]) + abs(s[1]-b[1])
        mds[s] = manhattan_distance
    for i in range(max_coord + 1):
        row_overlap = []
        for k, v in mds.items():
            offset = abs(i - k[1])
            if offset > v:
                continue
            row_width = (abs(v - offset)) * 2 + 1
            left_edge = k[0] - int(row_width / 2)
            right_edge = k[0] + int(row_width / 2)
            row_overlap += [(left_edge, right_edge)]
        row_overlap = sorted(row_overlap, key=lambda x: x[0])
        for r in range(len(row_overlap)-1):
            if row_overlap[r][1] < row_overlap[r+1][0]:
                r_min = row_overlap[0][0]
                r_max = row_overlap[0][1]
                for rp in range(1, len(row_overlap)):
                    if row_overlap[rp][0] <= r_max and row_overlap[rp][1] > r_max:
                        r_max = row_overlap[rp][1]
                        if r_max >= max_coord:
                            break
                else:
                    if r_max < max_coord:
                        return (r_max + 1) * 4000000 + i
                continue

def puzzle_16_1():
    round_count = 30
    valves = {}
    tunnels = {}
    memoization_score = {}
    open_valves = []
    with open("16.txt") as fp:
        data = fp.read().strip().splitlines()
    for line in data:
        v = line.split()[1]
        valves[v] = int(line.split(";")[0].split("=")[1])
        tunnels[v] = list(map(lambda x: x.strip(","), line.split()[9:]))
    def _dfs(cur_pos, count):
        loc_score = 0
        max_child_score = 0
        if cur_pos.endswith("o"):
            loc_score += (count * valves[cur_pos[:2]])
            open_valves.append(cur_pos[:2])
        count -= 1
        if count == 0:
            if cur_pos.endswith('o'):
                return valves[cur_pos[:2]]
            return 0
        children = tunnels[cur_pos[:2]]
        if cur_pos[:2] not in open_valves and valves[cur_pos]:
            children = ["%so" % cur_pos] + children
        for child in children:
            if "".join([child, str(count-1), *sorted(open_valves)]) in memoization_score:
                score = memoization_score["".join([child, str(count-1), *sorted(open_valves)])]
            else:
                score = _dfs(child, count)
            if score > max_child_score:
                max_child_score = score
            if child.endswith("o"):
                open_valves.pop(-1)
        loc_score += max_child_score
        memoization_score["".join([cur_pos, str(count), *sorted(open_valves)])] = loc_score
        return loc_score
    return _dfs("AA", round_count)

def puzzle_16_2():
    with open("16.test.txt") as fp:
        data = fp.read().strip().splitlines()
    for line in data:
        print(line)
    return 0

def puzzle_17_1():
    with open("17.txt") as fp:
        data = list(fp.read().strip())
    grid = ['-------']
    blocks = ["@@@@", ".@.\n@@@\n.@.", "..@\n..@\n@@@", "@\n@\n@\n@", "@@\n@@"]
    for count in range(2022):
        block = blocks[count % len(blocks)]
        nbotb = []
        for line in block.splitlines():
            nbotb.append(f'..{line:5}'.replace(" ", "."))
        nbotb += ['.......'  for j in range(3)]
        grid = nbotb + grid
        can_move_down = True
        while can_move_down:
            move = data.pop(0)
            data.append(move)
            for line in grid:
                if "@" in line:
                    if move == '<' and line.index('@') > 0 and line[line.index('@')-1] == '.':
                        continue
                    elif move == '>' and line[::-1].index('@') > 0 and line[::-1][line[::-1].index('@')-1] == '.':
                        continue
                    else:
                        break
            else:
                for line in range(len(grid)):
                    if '@' in grid[line]:
                        if move == '<':
                            for c in range(len(grid[line])):
                                if grid[line][c] == '@':
                                    grid[line] = grid[line][:c-1] + '@.' + grid[line][c+1:]
                        elif move == '>':
                            for c in range(len(grid[line])-2, -1, -1):
                                if grid[line][c] == '@':
                                    grid[line] = grid[line][:c] + '.@' + grid[line][c+2:]
            for line in range(len(grid)):
                for c in range(len(grid[line])):
                    if grid[line][c] == '@':
                        if grid[line+1][c] == '.' or grid[line+1][c] == '@':
                            continue
                        else:
                            can_move_down = False
                            break
                else:
                    continue
            if can_move_down:
                for line in range(len(grid)-2, -1, -1):
                    for c in range(len(grid[line])):
                        if grid[line][c] == '@':
                            grid[line+1] = grid[line+1][:c] + '@' + grid[line+1][c+1:]
                            grid[line] = grid[line][:c] + '.' + grid[line][c+1:]
            else:
                for line in range(len(grid)):
                    if '@' in grid[line]:
                        grid[line] = grid[line].replace("@", "#")
                break
            if grid[0].count(".") == 7:
                grid.pop(0)
    return len(grid) - 1

def puzzle_21_1():
    with open("21.txt") as fp:
        data = fp.read().strip().splitlines()
    monkeys = {}
    for line in data:
        m = line.split(":")[0]
        op = line.split(": ")[1]
        if op.isnumeric():
            monkeys[m] = int(op)
        else:
            monkeys[m] = op
    def _sum_monks(m):
        if type(monkeys[m]) == int:
            return monkeys[m]
        else:
            ms = monkeys[m].split()
            if ms[1] == '*':
                return int(_sum_monks(ms[0])) * int(_sum_monks(ms[2]))
            elif ms[1] == '+':
                return int(_sum_monks(ms[0])) + int(_sum_monks(ms[2]))
            elif ms[1] == '/':
                return int(_sum_monks(ms[0])) / int(_sum_monks(ms[2]))
            elif ms[1] == '-':
                return int(_sum_monks(ms[0])) - int(_sum_monks(ms[2]))
    return _sum_monks("root")

def puzzle_21_2():
    with open("21.txt") as fp:
        data = fp.read().strip().splitlines()
    monkeys = {}
    for line in data:
        m = line.split(":")[0]
        op = line.split(": ")[1]
        if op.isnumeric():
            monkeys[m] = int(op)
        else:
            monkeys[m] = op
    def _sum_monks(m, i):
        if type(monkeys[m]) == int:
            if m == 'humn':
                return i
            return monkeys[m]
        else:
            ms = monkeys[m].split()
            if ms[1] == '*':
                return int(_sum_monks(ms[0], i)) * int(_sum_monks(ms[2], i))
            elif ms[1] == '+':
                return int(_sum_monks(ms[0], i)) + int(_sum_monks(ms[2], i))
            elif ms[1] == '/':
                return int(_sum_monks(ms[0], i)) / int(_sum_monks(ms[2], i))
            elif ms[1] == '-':
                return int(_sum_monks(ms[0], i)) - int(_sum_monks(ms[2], i))
    i = 1
    switch_count = 0
    plus = True
    while True:
        if int(_sum_monks(monkeys['root'].split()[0], i)) > int(_sum_monks(monkeys['root'].split()[2], i)):
            i *= 10
        else:
            switch_count += 1
            break
    while True:
        a = int(_sum_monks(monkeys['root'].split()[0], i))
        b = int(_sum_monks(monkeys['root'].split()[2], i))
        if a < b:
            if plus:
                switch_count += 1
                plus = False
            i -= int(i/10**switch_count)
        elif a > b:
            if not plus:
                switch_count += 1
                plus = True
            i += int(i/10**switch_count)
        elif a == b:
            break
    while _sum_monks(monkeys['root'].split()[0], i) == _sum_monks(monkeys['root'].split()[2], i):
        i -= 1
    return i+1

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
    print(puzzle_9_1())
    print(puzzle_9_2())
    print(puzzle_10_1())
    print(puzzle_10_2())
    print(puzzle_11_1())
    print(puzzle_11_2())
    print(puzzle_12_1())
    print(puzzle_12_2())
    print(puzzle_13_1())
    print(puzzle_13_2())
    print(puzzle_14_1())
    print(puzzle_14_2())
    print(puzzle_15_1())
    print(puzzle_15_2())
    print(puzzle_16_1())
    print(puzzle_16_2())
    print(puzzle_17_1())
    print(puzzle_21_1())
    print(puzzle_21_2())


if __name__ == '__main__':
    main()
