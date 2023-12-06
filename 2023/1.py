"""
--- Day 1: Trebuchet?! ---

Obtain the calibration value
Can be found by combining the first digit and the last digit (in that order) to form single two-digit number

1abc2 -> 12
pqr3stu8vwx -> 38
a1b2c3d4e5f -> 15
treb7uchet  -> 77
Sum = 142
"""

def part_1(line):
    num = [c for c in line if c.isdigit()]
    num = int(num[0] + num[-1]) 
    return num
print(sum(map(part_1, open("puzzleinput.txt").readlines())))

number_map = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5",
              "six": "6", "seven": "7", "eight": "8", "nine": "9"}

# Important, here eighthree is 83 and not eigh3. So we can replace 3 with t3e
# Then we get eighthree -> eight3e -> e8t3e -> 83
def part_2(line):
    for n, s in number_map.items():
        if n in line:
            line = line.replace(n, n[0] + s + n[-1])
    return part_1(line)
print(sum(map(part_2, open("puzzleinput.txt").readlines())))