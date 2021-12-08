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
    with open("8.ms.txt") as fp:
        data = fp.read().strip().splitlines()
    count = 0
    for line in data:
        (sig_pat, output_val) = line.split(" | ")
        for word in output_val.split():
            if len(word) in [2, 3, 4, 7]:
                count += 1
    return count

def puzzle_8_2():
    with open("8.ms.txt") as fp:
        data = fp.read().strip().splitlines()
    #data = ["acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"]
    sum_d = 0
    for line in data:
        positions = {0:False, 1:False, 2:False, 3:False, 4:False, 5:False, 6:False}
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
            if len(list(set(list(word)) - set(list(segments[1])))) == 3:
                segments[3] = word
            elif len(list(set(list(word)) - set(list(segments[4])))) == 2:
                segments[5] = word
            elif len(list(set(list(word)) - set(list(segments[4])))) == 3:
                segments[2] = word
        for word in len_sixes:
            if len(list(set(list(word)) - set(list(segments[4])))) == 2:
                segments[9] = word
            elif len(list(set(list(segments[5])) - set(list(word)))) == 0:
                segments[6] = word
            else:
                segments[0] = word
        positions[0] = list(set(list(segments[7])) - set(list(segments[1])))[0]
        positions[1] = list(set(list(segments[4])) - set(list(segments[3])))[0]
        positions[2] = list(set(list(segments[9])) - set(list(segments[5])))[0]
        positions[3] = list(set(list(segments[8])) - set(list(segments[6])))[0]
        positions[4] = list(set(list(segments[8])) - set(list(segments[9])))[0]
        positions[5] = list(set(list(segments[6])) - set(list(segments[5])))[0]
        positions[6] = list(set(list(segments[1])) - set(list(segments[2])))[0]
        positions[7] = list(set(list(segments[3])) - set(list(segments[7])) - set(list(segments[4])))[0]
        val = ""
        for word in output_val.split():
             for k,v in segments.items():
                 if sorted(word) == sorted(v):
                     val += str(k)
        sum_d += int(val)
    return sum_d
        

def main():
    #print("Day 1 Puzzle 1:", puzzle_1_1())
    #print("Day 1 Puzzle 2:", puzzle_1_2())
    #print("Day 2 Puzzle 1:", puzzle_2_1())
    #print("Day 2 Puzzle 2:", puzzle_2_2())
    #print("Day 3 Puzzle 1:", puzzle_3_1())
    #print("Day 3 Puzzle 2:", puzzle_3_2())
    #print("Day 4 Puzzle 1:", puzzle_4_1())
    #print("Day 4 Puzzle 2:", puzzle_4_2())
    #print("Day 5 Puzzle 1:", puzzle_5_1())
    #print("Day 5 Puzzle 2:", puzzle_5_2())
    #print("Day 6 Puzzle 1:", puzzle_6_1())
    #print("Day 6 Puzzle 2:", puzzle_6_2())
    #print("Day 7 Puzzle 1:", puzzle_7_1())
    #print("Day 7 Puzzle 2:", puzzle_7_2())
    print("Day 8 Puzzle 1:", puzzle_8_1())
    print("Day 8 Puzzle 2:", puzzle_8_2())

if __name__ == '__main__':
    main()
