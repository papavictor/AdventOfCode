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
        for j in range(card_num+1, card_num+len(winners)+1):
            if j not in copies:
                copies[j] = copies[card_num]
            else:
                copies[j] += copies[card_num]
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

def puzzle_6_1():
    with open("6.txt") as fp:
        data = fp.read().strip().splitlines()
    times = list(map(int, data[0].split(":")[1].strip().split()))
    distances = list(map(int, data[1].split(":")[1].strip().split()))
    wins = {}
    for i in range(len(times)):
        wins[times[i]] = []
        for j in range(times[i]):
            ttm = times[i] - j
            dm = j * ttm
            if dm > distances[i]:
                wins[times[i]].append(j)
    prod = math.prod([len(x) for x in wins.values()])
    return prod

def puzzle_6_2():
    with open("6.txt") as fp:
        data = fp.read().strip().splitlines()
    time = int("".join(data[0].split(":")[1].strip().split()))
    distance = int("".join(data[1].split(":")[1].strip().split()))
    wins = []
    for i in range(time):
        ttm = time - i
        dm = i * ttm
        if dm > distance:
            wins.append(i)
    return len(wins)

def puzzle_7_1():
    def _sorter(i):
        s = {"A":"a", "K":"b", "Q":"c", "J":"d", "T":"e", "9":"f", "8":"g", "7":"h", "6":"i", "5":"j", "4":"k", "3":"l", "2":"m"}
        sn = f"{s[i[0]]}{s[i[1]]}{s[i[2]]}{s[i[3]]}{s[i[4]]}"
        return(sn)
    with open("7.txt") as fp:
        data = fp.read().strip().splitlines()
    hands_rank = {1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[]}
    bets = {}
    sorted_hands = []
    for line in data:
        (hand, bet) = line.split()
        bets[hand] = int(bet)
        hc = {}
        for card in hand:
            if card in hc:
                hc[card] += 1
            else:
                hc[card] = 1
        if 5 in hc.values():
            hands_rank[1].append(hand)
        elif 4 in hc.values():
            hands_rank[2].append(hand)
        elif 3 in hc.values():
            if 2 in hc.values():
                hands_rank[3].append(hand)
            else:
                hands_rank[4].append(hand)
        elif list(hc.values()).count(2) == 2:
            hands_rank[5].append(hand)
        elif 2 in hc.values():
            hands_rank[6].append(hand)
        else:
            hands_rank[7].append(hand)
    for rank in range(1, 8):
        for hand in sorted(hands_rank[rank], key=_sorter):
            sorted_hands.append(hand)
    total_winnings = 0
    sorted_hands.reverse()
    for hand in range(len(sorted_hands)):
        total_winnings += bets[sorted_hands[hand]] * (hand+1)
    return total_winnings

def puzzle_7_2():
    def _sorter(i):
        s = {"A":"a", "K":"b", "Q":"c", "T":"d", "9":"e", "8":"f", "7":"g", "6":"h", "5":"i", "4":"j", "3":"k", "2":"l", "J":"m"}
        sn = f"{s[i[0]]}{s[i[1]]}{s[i[2]]}{s[i[3]]}{s[i[4]]}"
        return(sn)
    with open("7.txt") as fp:
        data = fp.read().strip().splitlines()
    hands_rank = {1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[]}
    bets = {}
    sorted_hands = []
    for line in data:
        (hand, bet) = line.split()
        bets[hand] = int(bet)
        hc = {}
        for card in hand:
            if card in hc:
                hc[card] += 1
            else:
                hc[card] = 1
        if "J" in hc:
            mv = 0
            bc = ""
            for k,v in hc.items():
                if k == "J":
                    continue
                if v > mv:
                    mv = v
                    bc = k
            if bc:
                hc[bc] += hc["J"]
                del hc["J"]
        if 5 in hc.values():
            hands_rank[1].append(hand)
        elif 4 in hc.values():
            hands_rank[2].append(hand)
        elif 3 in hc.values():
            if 2 in hc.values():
                hands_rank[3].append(hand)
            else:
                hands_rank[4].append(hand)
        elif list(hc.values()).count(2) == 2:
            hands_rank[5].append(hand)
        elif 2 in hc.values():
            hands_rank[6].append(hand)
        else:
            hands_rank[7].append(hand)
    for rank in range(1, 8):
        for hand in sorted(hands_rank[rank], key=_sorter):
            sorted_hands.append(hand)
    total_winnings = 0
    sorted_hands.reverse()
    for hand in range(len(sorted_hands)):
        total_winnings += bets[sorted_hands[hand]] * (hand+1)
    return total_winnings

def puzzle_8_1():
    with open("8.txt") as fp:
        data = fp.read().strip().splitlines()
    instructions = [e for e in data[0]]
    network = {}
    for line in data[2:]:
        network[line.split("=")[0].strip()] = list(map(lambda x: x.strip(), line.split("=")[1].strip(" ()").split(",")))
    node = "AAA"
    counter = 0
    while node != "ZZZ":
        for i in instructions:
            if i == "L":
                node = network[node][0]
            else:
                node = network[node][1]
            counter += 1
    return counter

def puzzle_8_2():
    with open("8.txt") as fp:
        data = fp.read().strip().splitlines()
    instructions = [e for e in data[0]]
    paths = []
    network = {}
    for line in data[2:]:
        start_point = line.split("=")[0].strip()
        [endpoint_L, endpoint_R] = list(map(lambda x: x.strip(), line.split("=")[1].strip(" ()").split(",")))
        network[start_point] = [endpoint_L, endpoint_R]
        if start_point.endswith("A"):
            paths.append(start_point)
    counts = []
    for p in paths:
        count = 0
        pos = p
        while not pos.endswith("Z"):
            i = instructions[count%len(instructions)]
            if i == "L":
                pos = network[pos][0]
            else:
                pos = network[pos][1]
            count += 1
        counts.append(count)
    divisors = []
    for c in counts:
        divs = []
        for n in range(2, int(math.sqrt(c))):
            if (c / n).is_integer():
                divs += [n, int(c/n)]
        divisors.append(list(set(divs)))
    gcd = 0
    for d in divisors[0]:
        for d2 in divisors:
            if d in d2 and d > gcd:
                gcd = d
    lcm = int(math.prod([e/gcd for e in counts]) * gcd)
    return lcm

def puzzle_9_1():
    with open("9.txt") as fp:
        data = fp.read().strip().splitlines()
    sequences = []
    for line in data:
        sequences.append(list(map(int, line.split())))
    total = 0
    for seq in sequences:
        history = [seq]
        h1 = []
        while not (len(h1) > 0 and h1.count(0) == len(h1)):
            h1 = []
            for i in range(len(seq) - 1):
                diff = seq[i+1] - seq[i]
                h1.append(diff)
            history.append(h1)
            seq = h1
        for i in range(1, len(history)+1):
            h2 = history[-i]
            if h2.count(0) == len(h2):
                h2.append(0)
            else:
                h2.append(h2[-1]+history[-i+1][-1])
        total += h2[-1]
    return total

def puzzle_9_2():
    with open("9.txt") as fp:
        data = fp.read().strip().splitlines()
    sequences = []
    for line in data:
        sequences.append(list(map(int, line.split())))
    total = 0
    for seq in sequences:
        history = [seq]
        h1 = []
        while not (len(h1) > 0 and h1.count(0) == len(h1)):
            h1 = []
            for i in range(len(seq) - 1):
                diff = seq[i+1] - seq[i]
                h1.append(diff)
            history.append(h1)
            seq = h1
        for i in range(1, len(history)+1):
            h2 = history[-i]
            if h2.count(0) == len(h2):
                h2.insert(0, 0)
            else:
                h2.insert(0, h2[0]-history[-i+1][0])
        total += h2[0]
    return total

def puzzle_10_1():
    def _nbs(p):
        [x, y] = p
        nbs = []
        nbs.append([x-1, y])
        nbs.append([x+1, y])
        nbs.append([x, y-1])
        nbs.append([x, y+1])
        return nbs
    with open("10.txt") as fp:
        data = fp.read().strip().splitlines()
        grid_height = len(data)
        grid_width = len(data[0])
    sp = [0, 0]
    for line in range(len(data)):
        if 'S' in data[line]:
            sp = [line, data[line].index('S')]
            break
    newgrid = [['.' for e in range(len(data[0]))] for l in data]
    newgrid[sp[0]][sp[1]] = 0
    nbs = _nbs(sp)
    step = 0
    if nbs[3][1] > grid_width or data[nbs[3][0]][nbs[3][1]] not in ["7", "J", "-"]:
        nbs.pop(3)
    if nbs[2][1] < 0 or data[nbs[2][0]][nbs[2][1]] not in ["L", "F", "-"]:
        nbs.pop(2)
    if nbs[1][0] > grid_height or data[nbs[1][0]][nbs[1][1]] not in ["L", "J", "|"]:
        nbs.pop(1)
    if nbs[0][0] < 0 or data[nbs[0][0]][nbs[0][1]] not in ["F", "7", "|"]:
        nbs.pop(0)
    while nbs:
        step += 1
        nnbs = []
        for n in nbs:
            newgrid[n[0]][n[1]] = step
            tnbs = _nbs(n)
            if tnbs[3][1] >= grid_width or data[tnbs[3][0]][tnbs[3][1]] not in ["7", "J", "-"] or newgrid[tnbs[3][0]][tnbs[3][1]] != '.':
                tnbs.pop(3)
            if tnbs[2][1] < 0 or data[tnbs[2][0]][tnbs[2][1]] not in ["L", "F", "-"] or newgrid[tnbs[2][0]][tnbs[2][1]] != '.':
                tnbs.pop(2)
            if tnbs[1][0] >= grid_height or data[tnbs[1][0]][tnbs[1][1]] not in ["L", "J", "|"] or newgrid[tnbs[1][0]][tnbs[1][1]] != '.':
                tnbs.pop(1)
            if tnbs[0][0] < 0 or data[tnbs[0][0]][tnbs[0][1]] not in ["F", "7", "|"] or newgrid[tnbs[0][0]][tnbs[0][1]] != '.':
                tnbs.pop(0)
            nnbs += tnbs
        nbs = nnbs
    return step

def puzzle_10_2():
    def _nbs(p):
        [x, y] = p
        nbs = []
        nbs.append([x-1, y])
        nbs.append([x+1, y])
        nbs.append([x, y-1])
        nbs.append([x, y+1])
        return nbs
    with open("10.txt") as fp:
        data = fp.read().strip().splitlines()
        grid_height = len(data)
        grid_width = len(data[0])
    sp = [0, 0]
    for line in range(len(data)):
        if 'S' in data[line]:
            sp = [line, data[line].index('S')]
            break
    newgrid = [['.' for e in range(len(data[0]))] for l in data]
    newgrid[sp[0]][sp[1]] = 0
    nbs = _nbs(sp)
    step = 0
    if nbs[3][1] > grid_width or data[nbs[3][0]][nbs[3][1]] not in ["7", "J", "-"]:
        nbs.pop(3)
    if nbs[2][1] < 0 or data[nbs[2][0]][nbs[2][1]] not in ["L", "F", "-"]:
        nbs.pop(2)
    if nbs[1][0] > grid_height or data[nbs[1][0]][nbs[1][1]] not in ["L", "J", "|"]:
        nbs.pop(1)
    if nbs[0][0] < 0 or data[nbs[0][0]][nbs[0][1]] not in ["F", "7", "|"]:
        nbs.pop(0)
    while nbs:
        step += 1
        nnbs = []
        for n in nbs:
            newgrid[n[0]][n[1]] = step
            tnbs = _nbs(n)
            if tnbs[3][1] >= grid_width or data[tnbs[3][0]][tnbs[3][1]] not in ["7", "J", "-"] or \
              newgrid[tnbs[3][0]][tnbs[3][1]] != '.' or data[n[0]][n[1]] not in ["F", "L", "-", "S"]:
                tnbs.pop(3)
            if tnbs[2][1] < 0 or data[tnbs[2][0]][tnbs[2][1]] not in ["L", "F", "-"] or \
              newgrid[tnbs[2][0]][tnbs[2][1]] != '.' or data[n[0]][n[1]] not in ["J", "7", "-", "S"]:
                tnbs.pop(2)
            if tnbs[1][0] >= grid_height or data[tnbs[1][0]][tnbs[1][1]] not in ["L", "J", "|"] or \
              newgrid[tnbs[1][0]][tnbs[1][1]] != '.' or data[n[0]][n[1]] not in ["|", "F", "7", "S"]:
                tnbs.pop(1)
            if tnbs[0][0] < 0 or data[tnbs[0][0]][tnbs[0][1]] not in ["F", "7", "|"] or \
              newgrid[tnbs[0][0]][tnbs[0][1]] != '.' or data[n[0]][n[1]] not in ["|", "J", "L", "S"]:
                tnbs.pop(0)
            nnbs += tnbs
        nbs = nnbs
    int_count = 0
    for row in range(len(newgrid)):
        for col in range(len(newgrid[row])):
            if newgrid[row][col] == '.' and row > 0 and col > 0 and row < len(newgrid)-1 and col < len(newgrid[row])-1:
                count = 0
                for c in range(col):
                    if data[row][c] in ["S", "L", "J", "|"] and data[row-1][c] in ["S", "7", "F", "|"] \
                      and type(newgrid[row][c]) == int and type(newgrid[row-1][c]) == int:
                        count += 1
                if count % 2:
                    newgrid[row][col] = "I"
                    int_count += 1
    return int_count

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
    print(f"Puzzle 6, part 1: {puzzle_6_1()}")
    print(f"Puzzle 6, part 2: {puzzle_6_2()}")
    print(f"Puzzle 7, part 1: {puzzle_7_1()}")
    print(f"Puzzle 7, part 2: {puzzle_7_2()}")
    print(f"Puzzle 8, part 1: {puzzle_8_1()}")
    print(f"Puzzle 8, part 2: {puzzle_8_2()}")
    print(f"Puzzle 9, part 1: {puzzle_9_1()}")
    print(f"Puzzle 9, part 2: {puzzle_9_2()}")
    print(f"Puzzle 10, part 1: {puzzle_10_1()}")
    print(f"Puzzle 10, part 2: {puzzle_10_2()}")

if __name__ == '__main__':
    main()
