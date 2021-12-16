#!/usr/bin/env python

from copy import deepcopy
from functools import reduce

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

def puzzle_4_1():
    with open("4.txt") as fp:
        data = fp.read().strip().splitlines()
    numbers_called = data[0].strip().split(",")
    boards = []
    newboard = []
    for line in range(2, len(data)):
        #print(data[line])
        if line == 0:
            numbers_called = data[line].split(",")
        if not data[line] and newboard:
            boards.append(newboard)
            newboard = []
        else:
            newboard.append(data[line].strip().split())
    boards.append(newboard)
    #### Helper function ####
    def _player_wins(boards):
        ''' Checks if any player wins '''
        for board in range(len(boards)):
            columns = {0:0, 1:0, 2:0, 3:0, 4:0}
            # Check the X
            for line in boards[board]:
                if line.count("X") == 5: # 5 in a row, board wins!
                    return board
                for c in range(len(line)): # keep a column count
                    if line[c] == "X":
                        columns[c] += 1
            # Check the Y
            for c in columns:
               if columns[c] == 5: # 5 in a column, board wins!
                   return board
        return False
    ### END of helper function ###
    for number_called in numbers_called:
        for board in range(len(boards)):
            for line in range(len(boards[board])):
                for num in range(len(boards[board][line])):
                    if boards[board][line][num].isdigit() and int(boards[board][line][num]) == int(number_called):
                        boards[board][line][num] = "X" # board has it at (x=num, y=line)
        pw = _player_wins(boards) # check if a board has won
        if str(pw).isdigit():
            uncalled_sum = 0
            for row in boards[pw]:
                for c in row:
                    if c.isdigit():
                        uncalled_sum += int(c)
            return uncalled_sum * int(number_called)

def puzzle_4_2():
    with open("4.txt") as fp:
        data = fp.read().strip().splitlines()
    numbers_called = data[0].strip().split(",")
    boards = []
    newboard = []
    for line in range(2, len(data)):
        if line == 0:
            numbers_called = data[line].split(",")
        if not data[line] and newboard:
            boards.append(newboard)
            newboard = []
        else:
            newboard.append(data[line].strip().split())
    boards.append(newboard)
    #### Helper function ####
    def _players_wins(boards, uwb):
        ''' Checks if any player(s) wins '''
        winning_boards = []
        for board in range(len(boards)):
            if board not in uwb:
                continue
            columns = {0:0, 1:0, 2:0, 3:0, 4:0}
            # Check the X
            for line in boards[board]:
                if line.count("X") == 5:
                    winning_boards.append(board)
                for c in range(len(line)):
                    if line[c] == "X":
                        columns[c] += 1
            # Check the Y
            for c in columns:
               if columns[c] == 5:
                   winning_boards.append(board)
        return winning_boards
    ### END of helper function ###
    unwinning_boards = [i for i in range(len(boards))]
    for number_called in numbers_called:
        for board in range(len(boards)):
            if board not in unwinning_boards:
                continue
            for line in range(len(boards[board])):
                for num in range(len(boards[board][line])):
                    if boards[board][line][num].isdigit() and int(boards[board][line][num]) == int(number_called):
                        boards[board][line][num] = "X"
        pws = _players_wins(boards, unwinning_boards)
        for pw in list(set(pws)):
            unwinning_boards.remove(pw)
            if len(unwinning_boards) == 0 or numbers_called.index(number_called) == len(numbers_called) - 1:
                uncalled_sum = 0
                for row in boards[pw]:
                    for c in row:
                        if c.isdigit():
                            uncalled_sum += int(c)
                return uncalled_sum * int(number_called)

def puzzle_5_1():
    with open("5.txt") as fp:
        data = fp.read().strip().splitlines()
    lines = []
    max_x = 0
    max_y = 0
    for line in data:
        (x1, y1) = map(int, line.split(" -> ")[0].split(","))
        (x2, y2) = map(int, line.split(' -> ')[1].split(","))
        if x1 == x2 or y1 == y2:
            lines.append((x1, y1, x2, y2))
        if x1 > max_x:
            max_x = x1
        if x2 > max_x:
            max_x = x2
        if y1 > max_y:
            max_y = y1
        if y2 > max_y:
            max_y = y2
    board = [[0 for i in range(max_x+1)] for j in range(max_y+1)]
    for line in lines:
        if line[1] == line[3]: # horizontal
            for seg in range(min(line[0], line[2]), max(line[0], line[2]) + 1):
                board[line[1]][seg] += 1
        else: # vertical (line[0] = line[2])
            for seg in range(min(line[1], line[3]), max(line[1], line[3])+1): 
                board[seg][line[0]] += 1
    gto = 0
    for line in board:
        for c in line:
            if c > 1:
                gto += 1
    return gto

def puzzle_5_2():
    with open("5.txt") as fp:
        data = fp.read().strip().splitlines()
    lines = []
    max_x = 0
    max_y = 0
    diag_lines = []
    for line in data:
        (x1, y1) = map(int, line.split(" -> ")[0].split(","))
        (x2, y2) = map(int, line.split(' -> ')[1].split(","))
        if x1 == x2 or y1 == y2:
            lines.append((x1, y1, x2, y2))
        elif abs(x1-x2) == abs(y1-y2):
            diag_lines.append((x1, y1, x2, y2))
        if x1 > max_x:
            max_x = x1
        if x2 > max_x:
            max_x = x2
        if y1 > max_y:
            max_y = y1
        if y2 > max_y:
            max_y = y2
    board = [[0 for i in range(max_x+1)] for j in range(max_y+1)]
    for line in lines:
        if line[1] == line[3]: # horizontal
            for seg in range(min(line[0], line[2]), max(line[0], line[2]) + 1):
                board[line[1]][seg] += 1
        else: # vertical (line[0] = line[2])
            for seg in range(min(line[1], line[3]), max(line[1], line[3])+1):
                board[seg][line[0]] += 1
    for line in diag_lines:
        ux = True if line[0] < line[2] else False
        uy = True if line[1] < line[3] else False
        xx = max(line[0], line[2])
        nx = min(line[0], line[2])
        xy = max(line[1], line[3])
        ny = max(line[1], line[3])
        rx = list(range(line[0], line[2] - 1 if not ux else line[2]+1, 1 if ux else - 1))
        ry = list(range(line[1], line[3] - 1 if not uy else line[3]+1, 1 if uy else - 1))
        for (x, y) in list(zip(rx, ry)):
            board[y][x] += 1
    gto = 0
    for line in board:
        for c in line:
            if c > 1:
                gto += 1
    return gto

def puzzle_6_1():
    with open("6.txt") as fp:
        data = list(map(int, fp.read().strip().split(",")))
    nxtdayapd = []
    for day in range(80):
        data += nxtdayapd
        nxtdayapd = []
        for num in range(len(data)):
            data[num] -= 1
            if data[num] == 0:
                nxtdayapd.append(9)
            if data[num] < 0:
                data[num] = 6
    return len(data)

def puzzle_6_2():
    with open("6.txt") as fp:
        data = list(map(int, fp.read().strip().split(",")))
    nxtdayapd = []
    fish = {0: 0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0}
    next_fish = {0: 0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0}
    for f in data:
        fish[f] += 1
    days = 256
    for day in range(days):
        next_fish = {0: 0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0}
        for (f,c) in fish.items():
            if f == 0:
                if c:
                    next_fish[6] = c
                    next_fish[8] = c
            elif f == 7:
                next_fish[6] += c
            elif c > 0:
                next_fish[f-1] = c
        fish = next_fish
    return sum(fish.values())

def puzzle_7_1():
    with open("7.txt") as fp:
        data = list(map(int, fp.read().strip().split(",")))
    minpos = data[0]
    maxpos = data[0]
    for line in data:
        if line > maxpos:
            maxpos = line
        if line < minpos:
            minpos = line
    min_sum = 0
    for c in range(minpos, maxpos+1):
        sumc = 0
        for d in data:
            sumc += abs(d - c)
        if not min_sum or sumc < min_sum:
            min_sum = sumc
    return min_sum

def puzzle_7_2():
    with open("7.txt") as fp:
        data = list(map(int, fp.read().strip().split(",")))
    minpos = data[0]
    maxpos = data[0]
    for line in data:
        if line > maxpos:
            maxpos = line
        if line < minpos:
            minpos = line
    min_sum = 0
    def _sum_torial(i):
        sumt = i
        for x in range(0, i):
            sumt += x
        return sumt
    for c in range(minpos, maxpos+1):
        sumc = 0
        for d in data:
            sumc += _sum_torial(abs(d - c))
        if not min_sum or sumc < min_sum:
            min_sum = sumc
    return min_sum

def puzzle_8_1():
    with open("8.txt") as fp:
        data = fp.read().strip().splitlines()
    count = 0
    for line in data:
        (sig_pat, output_val) = line.split(" | ")
        for word in output_val.split():
            if len(word) in [2, 3, 4, 7]:
                count += 1
    return count

def puzzle_8_2():
    with open("8.txt") as fp:
        data = fp.read().strip().splitlines()
    #data = ["acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"]
    sum_d = 0
    for line in data:
        segments = {0:False, 1:False, 2:False, 3:False, 4:False, 5:False, 6:False, 7:False, 8:False, 9:False}
        (sig_pat, output_val) = line.split(" | ")
        len_fives = []
        len_sixes = []
        for word in sig_pat.split():
            if len(word) == 2:
                segments[1] = word
            elif len(word) == 3:
                segments[7] = word
            elif len(word) == 4:
                segments[4] = word
            elif len(word) == 7:
                segments[8] = word
            elif len(word) == 5:
                len_fives += [word]
            elif len(word) == 6:
                len_sixes += [word]
        for word in len_fives:
            if len(set(list(word)) - set(list(segments[1]))) == 3:
                segments[3] = word
            elif len(set(list(word)) - set(list(segments[4]))) == 2:
                segments[5] = word
            elif len(set(list(word)) - set(list(segments[4]))) == 3:
                segments[2] = word
        for word in len_sixes:
            if len(set(list(word)) - set(list(segments[4]))) == 2:
                segments[9] = word
            elif len(set(list(segments[5])) - set(list(word))) == 0:
                segments[6] = word
            else:
                segments[0] = word
        val = ""
        for word in output_val.split():
             for k,v in segments.items():
                 if sorted(word) == sorted(v):
                     val += str(k)
                     break
        sum_d += int(val)
    return sum_d

def puzzle_9_1():
    with open("9.test.txt") as fp:
        data = fp.read().strip().splitlines()
    heights = []
    for line in data:
        heights.append(list(map(int, list(line))))
    # helper function #
    def _get_lower_neighbors(x, y, h):
        nu = []
        nd = []
        nl = []
        nr = []
        lower_neighbors = []
        if y > 0:
            nl = heights[y-1][x]
            if nl <= h:
                lower_neighbors.append([x,y-1])
        if y < len(heights) - 1:
            nr = heights[y+1][x]
            if nr <= h:
                lower_neighbors.append([x,y+1])
        if x > 0:
            nu = heights[y][x-1]
            if nu <= h:
                lower_neighbors.append([x-1,y])
        if x < len(heights[y]) - 1:
            nd = heights[y][x+1]
            if nd <= h:
                lower_neighbors.append([x+1,y])
        return lower_neighbors
    # end helper function #
    total_risk_level = 0
    for y in range(len(heights)):
        for x in range(len(heights[y])):
            lower_neighbors = _get_lower_neighbors(x, y, heights[y][x])
            if not lower_neighbors:
                total_risk_level += (1 + heights[y][x])
    return total_risk_level

def puzzle_9_2():
    with open("9.txt") as fp:
        data = fp.read().strip().splitlines()
    heights = []
    for line in data:
        heights.append(list(map(int, list(line))))
    # helper functions #
    def _get_lower_neighbors(x, y, h):
        lower_neighbors = []
        if y > 0 and heights[y-1][x] <= h:
            lower_neighbors.append([x,y-1])
        if y < len(heights) - 1 and heights[y+1][x] <= h:
            lower_neighbors.append([x,y+1])
        if x > 0 and heights[y][x-1] <= h:
            lower_neighbors.append([x-1,y])
        if x < len(heights[y]) - 1 and heights[y][x+1] <= h:
            lower_neighbors.append([x+1,y])
        return lower_neighbors
    def _get_neighbors_lt_9(x, y):
        neighbors = []
        if y > 0 and heights[y-1][x] < 9:
            neighbors.append([x,y-1])
        if y < len(heights) - 1 and heights[y+1][x] < 9:
            neighbors.append([x,y+1])
        if x > 0 and heights[y][x-1] < 9:
            neighbors.append([x-1,y])
        if x < len(heights[y]) - 1 and heights[y][x+1] < 9:
            neighbors.append([x+1,y])
        return neighbors
    # end helper functions #
    lowest_points = []
    for y in range(len(heights)):
        for x in range(len(heights[y])):
            lower_neighbors = _get_lower_neighbors(x, y, heights[y][x])
            if not lower_neighbors:
                lowest_points.append([x, y])
    three_largest_basins = []
    for point in lowest_points:
        basin = [point]
        unseen_neighbors = _get_neighbors_lt_9(point[0], point[1])
        while unseen_neighbors:
            new_nb = unseen_neighbors.pop()
            basin.append(new_nb)
            new_nbs = _get_neighbors_lt_9(new_nb[0], new_nb[1])
            for nb in new_nbs:
               if nb not in basin + unseen_neighbors:
                   unseen_neighbors.append(nb)
        if len(three_largest_basins) < 3:
            three_largest_basins.append(len(basin))
        elif len(basin) > min(three_largest_basins):
            three_largest_basins.append(len(basin))
            three_largest_basins.remove(min(three_largest_basins))
    return reduce(lambda x, y: x*y, three_largest_basins)

def puzzle_10_1():
    with open("10.txt") as fp:
        data = fp.read().strip().splitlines()
    openers = ['{', '[', '(', '<']
    closers = {'}': '{', ']':'[', ')':'(', '>':'<'}
    points = {')': 3, ']': 57, '}': 1197, '>': 25137}
    score = 0
    for line in data:
        stack = []
        for c in line:
            if c in openers:
                stack.append(c)
            else:
                prev_tok = stack.pop()
                if prev_tok != closers[c]:
                    score += points[c]
                    break
    return score

def puzzle_10_2():
    with open("10.txt") as fp:
        data = fp.read().strip().splitlines()
    openers = {'{':'}', '[':']', '(':')', '<':'>'}
    closers = {'}': '{', ']':'[', ')':'(', '>':'<'}
    points = {')': 1, ']': 2, '}': 3, '>': 4}
    scores = []
    for line in data:
        score = 0
        stack = []
        for c in line:
            if c in openers:
                stack.append(c)
            else:
                prev_tok = stack.pop()
                if prev_tok != closers[c]:
                    #corrupt
                    break
        else:
            closing_chars = ""
            while stack:
                c = stack.pop()
                score = score * 5 + points[openers[c]]
            scores.append(score)
    return sorted(scores)[0-(int(len(scores)/2)+1)]

def puzzle_11_1():
    with open("11.txt") as fp:
        data = fp.read().strip().splitlines()
    octopi = []
    for line in data:
        octopi.append(list(map(int, line)))
    sum_flashed = 0
    for step in range(100):
        for y in range(len(octopi)):
            for x in range(len(octopi[y])):
                octopi[y][x] += 1
        flash_count = sum([list(map(lambda x: x>9, l)).count(True) for l in octopi])
        num_flashed = 0
        flashed = []
        while(flash_count):
            for y in range(len(octopi)):
                for x in range(len(octopi[y])):
                    if octopi[y][x] > 9:
                        flashed.append((x,y))
                        num_flashed += 1
                        octopi[y][x] = 0
                        for y2 in range(y-1, y+2):
                            for x2 in range(x-1, x+2):
                                if 0 <= y2 < len(octopi) and 0 <= x2 < len(octopi[y2]) and (x2, y2) not in flashed:
                                    octopi[y2][x2] += 1
            flash_count = sum([list(map(lambda x: x>9, l)).count(True) for l in octopi])
        sum_flashed += num_flashed
    return sum_flashed

def puzzle_11_2():
    with open("11.txt") as fp:
        octopi = [list(map(int,  line)) for line in fp.read().strip().splitlines()]
    num_flashed = 0
    step = 0
    while num_flashed != 100:
        step += 1
        for y in range(len(octopi)):
            for x in range(len(octopi[y])):
                octopi[y][x] += 1
        flash_count = sum([list(map(lambda x: x>9, l)).count(True) for l in octopi])
        num_flashed = 0
        flashed = []
        while(flash_count):
            for y in range(len(octopi)):
                for x in range(len(octopi[y])):
                    if octopi[y][x] > 9:
                        flashed.append((x,y))
                        num_flashed += 1
                        octopi[y][x] = 0
                        for y2 in range(y-1, y+2):
                            for x2 in range(x-1, x+2):
                                if 0 <= y2 < len(octopi) and 0 <= x2 < len(octopi[y2]) and (x2, y2) not in flashed:
                                    octopi[y2][x2] += 1
            flash_count = sum([list(map(lambda x: x>9, l)).count(True) for l in octopi])
    return step

def puzzle_12_1():
    with open("12.txt") as fp:
        data = fp.read().strip().splitlines()
    paths = []
    connections = {}
    for line in data:
        (a,b) = line.split("-")
        if a in connections:
            connections[a].append(b)
        else:
            connections[a] = [b]
    def _rec_find_paths(p, thus_far):
        paths = []
        for c in connections:
            if c == "end":
                if p in connections[c]:
                    paths.append("{},{}".format(thus_far, c))
            elif (c == c.upper() or c not in thus_far.split(",")) and p in connections[c]:
                paths += _rec_find_paths(c, "{},{}".format(thus_far, c))
        if p in connections:
            for c in connections[p]:
                if c == c.lower() and c in thus_far.split(","):
                    continue
                if c == "end":
                    paths.append("{},{}".format(thus_far, c))
                else:
                    paths += _rec_find_paths(c, "{},{}".format(thus_far, c))
        return paths
    paths = (_rec_find_paths("start", "start"))
    return len(paths)

def puzzle_12_2():
    with open("12.txt") as fp:
        data = fp.read().strip().splitlines()
    connections = {}
    for line in data:
        (a,b) = line.split("-")
        if a in connections:
            connections[a].append(b)
        else:
            connections[a] = [b]
    def _rec_find_paths(p, thus_far):
        paths = []
        small_caves = [x for x in thus_far.split(",") if x.lower() == x]
        for c in connections:
            if c == "end":
                if p in connections[c]:
                    paths.append("{},{}".format(thus_far, c))
            elif c == "start":
                continue
            elif c == c.upper() and p in connections[c]:
                paths += _rec_find_paths(c, "{},{}".format(thus_far, c))
            elif [small_caves.count(x) for x in small_caves].count(1) == len(small_caves) and p in connections[c]:
                paths += _rec_find_paths(c, "{},{}".format(thus_far, c))
            elif [small_caves.count(x) for x in small_caves].count(1) == len(small_caves) - 2 and p in connections[c] and c not in small_caves:
                if small_caves.count(c) != 2:
                    paths += _rec_find_paths(c, "{},{}".format(thus_far, c))
        if p in connections:
            for c in connections[p]:
                if c == c.lower():
                    if c == "start":
                        continue
                    if [small_caves.count(x) for x in small_caves].count(1) == len(small_caves) - 2 and \
                      small_caves.count(c) >= 1:
                        continue
                if c == "end":
                    paths.append("{},{}".format(thus_far, c))
                else:
                    paths += _rec_find_paths(c, "{},{}".format(thus_far, c))
        return paths
    paths = (_rec_find_paths("start", "start"))
    return len(paths)

def puzzle_13_1():
    with open("13.txt") as fp:
        data = fp.read().strip().splitlines()
    points = []
    folds = []
    for line in data:
        if line.count(",") == 1:
            points.append(list(map(int, line.split(","))))
        elif line.startswith("fold"):
            folds.append(line.split()[2])
    max_x = max([p[0] for p in points])
    max_y = max([p[1] for p in points])
    grid = [["." for i in range(max_x+1)] for j in range(max_y+1)]
    for p in points:
        grid[p[1]][p[0]] = '#'
    for instr in folds:
        (hv, pos) = instr.split("=")
        if hv == "y":
            for y in range(int(pos), len(grid)):
                for x in range(len(grid[0])):
                    if grid[y][x] == '#':
                        grid[int(pos) - (y-int(pos))][x] = '#'
            grid = grid[:int(pos)]
        if hv == "x":
            for y in range(len(grid)):
                for x in range(int(pos), len(grid[y])):
                    if grid[y][x] == '#':
                        grid[y][int(pos) - (x-int(pos))] = '#'
                grid[y] = grid[y][:int(pos)]
        break
    dotcount = 0
    for line in grid:
        dotcount += line.count("#")
    return dotcount

def puzzle_13_2():
    with open("13.txt") as fp:
        data = fp.read().strip().splitlines()
    points = []
    folds = []
    for line in data:
        if line.count(",") == 1:
            points.append(list(map(int, line.split(","))))
        elif line.startswith("fold"):
            folds.append(line.split()[2])
    max_x = max([p[0] for p in points])
    max_y = max([p[1] for p in points])
    grid = [["." for i in range(max_x+1)] for j in range(max_y+1)]
    for p in points:
        grid[p[1]][p[0]] = '#'
    for instr in folds:
        (hv, pos) = instr.split("=")
        if hv == "y":
            for y in range(int(pos), len(grid)):
                for x in range(len(grid[0])):
                    if grid[y][x] == '#':
                        grid[int(pos) - (y-int(pos))][x] = '#'
            grid = grid[:int(pos)]
        if hv == "x":
            for y in range(len(grid)):
                for x in range(int(pos), len(grid[y])):
                    if grid[y][x] == '#':
                        grid[y][int(pos) - (x-int(pos))] = '#'
                grid[y] = grid[y][:int(pos)]
    for line in grid:
        print("".join(line))

def puzzle_14_1():
    with open("14.txt") as fp:
        data = fp.read().strip().splitlines()
    polymer = data[0]
    ins_rules = {}
    for line in data[2:]:
        ins_rules[line.split(" -> ")[0]] = line.split(" -> ")[1]
    for step in range(10):
        next_polymer = ""
        for c in range(len(polymer)-1):
            (a, b) = (polymer[c], polymer[c+1])
            if "{}{}".format(a, b) in ins_rules:
                next_polymer += "{}{}".format(a, ins_rules["{}{}".format(a,b)])
        next_polymer += polymer[-1]
        polymer = list(next_polymer)
    cvals = list(set(polymer))
    cvd = {}
    minc = 0
    maxc = 0
    for c in cvals:
       cvd[c] = polymer.count(c)
       if polymer.count(c) > maxc:
           maxc = polymer.count(c)
       elif not minc or polymer.count(c) < minc:
           minc = polymer.count(c)
    return maxc - minc

def puzzle_14_2():
    with open("14.txt") as fp:
        data = fp.read().strip().splitlines()
    polymer = data[0]
    ins_rules = {}
    for line in data[2:]:
        ins_rules[line.split(" -> ")[0]] = line.split(" -> ")[1]
    pairs = {}
    for char in range(len(polymer)-1):
        (a, b) = (polymer[char], polymer[char+1])
        c = ins_rules["{}{}".format(a, b)]
        if "{}{}".format(a, c) not in pairs:
            pairs["{}{}".format(a,c)] = 1
        else:
            pairs["{}{}".format(a,c)] += 1
        if "{}{}".format(c, b) not in pairs:
            pairs["{}{}".format(c, b)] = 1
        else:
            pairs["{}{}".format(c, b)] += 1
    for step in range(40):
        nsc = {}
        sums = {}
        for p in pairs:
            [a,b] = list(p)
            c = ins_rules["{}{}".format(a, b)]
            (ac, cb) = ("{}{}".format(a, c), "{}{}".format(c, b))
            if ac not in nsc:
                nsc[ac] = pairs[p]
            else:
                nsc[ac] += pairs[p]
            if cb not in nsc:
                nsc[cb] = pairs[p]
            else:
                nsc[cb] += pairs[p]
            # count letters
            if b == polymer[-1]:
                if b in sums:
                    sums[b] += pairs[p]
                else:
                    sums[b] = pairs[p]
            if a != polymer[-1]:
                if a in sums:
                    sums[a] += pairs[p]
                else:
                    sums[a] = pairs[p]
        pairs = nsc
    return max(list(sums.values())) - min(list(sums.values()))

def puzzle_15_1():
    with open("15.txt") as fp:
        data = fp.read().strip().splitlines()
    grid = []
    for line in data:
        grid.append(list(map(int, list(line))))
    newgrid = [[0 for x in range(len(grid[0]))] for y in range(len(grid))]
    def _get_min_neighbor(y, x, newgrid):
        if y == 0 and x == 0:
            return 0
        mn = 0
        if y > 0:
            if newgrid[y-1][x] and (newgrid[y-1][x] < mn or not mn):
                mn = newgrid[y-1][x]
        if y < len(newgrid) - 1:
            if newgrid[y+1][x] and (newgrid[y+1][x] < mn or not mn):
                mn = newgrid[y+1][x]
        if x > 0:
            if newgrid[y][x-1] and (newgrid[y][x-1] < mn or not mn):
                mn = newgrid[y][x-1]
        if x < len(newgrid[0]) - 1:
            if newgrid[y][x+1] and (newgrid[y][x+1] < mn or not mn):
                mn = newgrid[y][x+1]
        return mn
    def _get_exposed_neighbors(newgrid):
        exposed = []
        for row in range(len(newgrid)):
            for col in range(len(newgrid[row])):
                if newgrid[row][col] == 0:
                    mn = _get_min_neighbor(row, col, newgrid)
                    if mn:
                        exposed.append((row, col))
        return exposed
    count = 1
    newgrid[1][0] = grid[1][0]
    newgrid[0][1] = grid[0][1]
    while newgrid[-1][-1] == 0:
        en = _get_exposed_neighbors(newgrid)
        for nb in en:
            mn = _get_min_neighbor(nb[0], nb[1], newgrid)
            point_val = mn + grid[nb[0]][nb[1]]
            if point_val <= count:
                newgrid[nb[0]][nb[1]] = point_val
        count += 1
    return newgrid[-1][-1]

def puzzle_15_2():
    with open("15.txt") as fp:
        data = fp.read().strip().splitlines()
    grid = []
    for line in data:
        grid.append(list(map(int, list(line))))
    def _get_min_neighbor(y, x, newgrid):
        if y == 0 and x == 0:
            return 0
        mn = 0
        if y > 0:
            if newgrid[y-1][x] and (newgrid[y-1][x] < mn or not mn):
                mn = newgrid[y-1][x]
        if y < len(newgrid) - 1:
            if newgrid[y+1][x] and (newgrid[y+1][x] < mn or not mn):
                mn = newgrid[y+1][x]
        if x > 0:
            if newgrid[y][x-1] and (newgrid[y][x-1] < mn or not mn):
                mn = newgrid[y][x-1]
        if x < len(newgrid[0]) - 1:
            if newgrid[y][x+1] and (newgrid[y][x+1] < mn or not mn):
                mn = newgrid[y][x+1]
        return mn
    def _get_exposed_neighbors(newgrid):
        exposed = []
        for row in range(len(newgrid)):
            for col in range(len(newgrid[row])):
                if newgrid[row][col] == 0:
                    mn = _get_min_neighbor(row, col, newgrid)
                    if mn:
                        exposed.append((row, col))
        return exposed
    newgrid2 = [[0 for x in range(len(grid[0]) * 5)] for y in range(len(grid) * 5)]
    for x in range(5):
        row = []
        for y in range(5):
            dist = x+y
            newlistappd = list(map(lambda l: list(map(lambda k: (k + dist) % 9 if (k + dist) > 9 else k + dist, l)), grid))
            for y1 in range(len(newlistappd)):
                for x1 in range(len(newlistappd[y1])):
                    newgrid2[y1 + len(newlistappd)*y][x1 + len(newlistappd[0]) * x] = newlistappd[y1][x1]
    grid = newgrid2
    newgrid = [[0 for x in range(len(grid[0]))] for y in range(len(grid))]
    newgrid[1][0] = grid[1][0]
    newgrid[0][1] = grid[0][1]
    count = 1
    while newgrid[-1][-1] == 0:
        en = _get_exposed_neighbors(newgrid)
        for nb in en:
            mn = _get_min_neighbor(nb[0], nb[1], newgrid)
            point_val = mn + grid[nb[0]][nb[1]]
            if point_val <= count:
                newgrid[nb[0]][nb[1]] = point_val
        count += 1
    return newgrid[-1][-1]

def main():
    print("Day 1 Puzzle 1:", puzzle_1_1())
    print("Day 1 Puzzle 2:", puzzle_1_2())
    print("Day 2 Puzzle 1:", puzzle_2_1())
    print("Day 2 Puzzle 2:", puzzle_2_2())
    print("Day 3 Puzzle 1:", puzzle_3_1())
    print("Day 3 Puzzle 2:", puzzle_3_2())
    print("Day 4 Puzzle 1:", puzzle_4_1())
    print("Day 4 Puzzle 2:", puzzle_4_2())
    print("Day 5 Puzzle 1:", puzzle_5_1())
    print("Day 5 Puzzle 2:", puzzle_5_2())
    print("Day 6 Puzzle 1:", puzzle_6_1())
    print("Day 6 Puzzle 2:", puzzle_6_2())
    print("Day 7 Puzzle 1:", puzzle_7_1())
    print("Day 7 Puzzle 2:", puzzle_7_2())
    print("Day 8 Puzzle 1:", puzzle_8_1())
    print("Day 8 Puzzle 2:", puzzle_8_2())
    print("Day 9 Puzzle 1:", puzzle_9_1())
    print("Day 9 Puzzle 2:", puzzle_9_2())
    print("Day 10 Puzzle 1:", puzzle_10_1())
    print("Day 10 Puzzle 2:", puzzle_10_2())
    print("Day 11 Puzzle 1:", puzzle_11_1())
    print("Day 11 Puzzle 2:", puzzle_11_2())
    print("Day 12 Puzzle 1:", puzzle_12_1())
    print("Day 12 Puzzle 2:", puzzle_12_2())
    print("Day 13 Puzzle 1:", puzzle_13_1())
    print("Day 13 Puzzle 2:", puzzle_13_2())
    print("Day 14 Puzzle 1:", puzzle_14_1())
    print("Day 14 Puzzle 2:", puzzle_14_2())
    print("Day 15 Puzzle 1:", puzzle_15_1())
    print("Day 15 Puzzle 2:", puzzle_15_2())

if __name__ == '__main__':
    main()
