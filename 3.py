"""
Part 1:

Given a string of jumbled letters, parse out mul instructions.
They must be of the format
    mul(X, Y)
where X and Y are 1 to 3 digit positive integers.

Add up the result of all the mul instructions

Solution 1:
State machine for parsing

Part 2:

You also have do and don't() 
"""
from enum import Enum

class ParsingState(Enum):
    INVALID = 1
    M = 2
    U = 3
    L = 4
    MUL_OPEN_PAREN = 5
    X = 6
    MUL_COMMA = 7
    Y = 8
    D = 9
    O = 10
    N = 11
    APOSTROPHE = 12
    T = 13
    DO_OPEN_PAREN = 14
    DONT_OPEN_PAREN = 15




def main():
    ans = 0
    with open('./3_input.txt') as f:
        should_do = True
        for line in f:
            state = ParsingState.INVALID
            curr_x, curr_y = -1, -1
            str_x, str_y = "", ""
            for i, c in enumerate(line):
                # This could be optimized with reading more characters at a time,
                # but this makes the code simple to read as it processes one char at a time.
                print("________________")
                print("char:", c)
                print("before:", state, "(", str_x, ", ", str_y + ")", should_do, ans)
                if state == ParsingState.INVALID and c == 'm':
                    state = ParsingState.M
                elif state == ParsingState.M and c == 'u':
                    state = ParsingState.U
                elif state == ParsingState.U and c == 'l':
                    state = ParsingState.L
                elif state == ParsingState.L and c == '(':
                    state = ParsingState.MUL_OPEN_PAREN
                elif state == ParsingState.MUL_OPEN_PAREN and c.isnumeric():
                    state = ParsingState.X
                    str_x += c
                elif state == ParsingState.X and c.isnumeric() and len(str_x) < 3:
                    str_x += c
                elif state == ParsingState.X and c == ',':
                    state = ParsingState.MUL_COMMA
                    curr_x = int(str_x)
                elif state == ParsingState.MUL_COMMA and c.isnumeric():
                    state = ParsingState.Y
                    str_y += c
                elif state == ParsingState.Y and c.isnumeric() and len(str_y) < 3:
                    str_y += c
                elif state == ParsingState.Y and c == ')':
                    # ParsingState.CLOSE_PAREN is the same as ParsingState.INVALID
                    # since we are no longer in a valid instruction
                    state = ParsingState.INVALID
                    curr_y = int(str_y)
                    str_x = ""
                    str_y = ""
                    if should_do:
                        ans += curr_x * curr_y
                        print("multiplying", curr_x, curr_y)
                elif state == ParsingState.INVALID and c == 'd':
                    state = ParsingState.D
                elif state == ParsingState.D and c == 'o':
                    state = ParsingState.O
                elif state == ParsingState.O and c == 'n':
                    state = ParsingState.N
                elif state == ParsingState.N and c == '\'':
                    state = ParsingState.APOSTROPHE
                elif state == ParsingState.APOSTROPHE and c == 't':
                    state = ParsingState.T
                elif state == ParsingState.T and c == '(':
                    state = ParsingState.DONT_OPEN_PAREN
                elif state == ParsingState.O and c == '(':
                    state = ParsingState.DO_OPEN_PAREN
                elif state == ParsingState.DO_OPEN_PAREN and c == ')':
                    should_do = True
                    print("\t> should do")
                    state = ParsingState.INVALID
                elif state == ParsingState.DONT_OPEN_PAREN and c == ')':
                    should_do = False
                    print("\t> should NOT do")
                    state = ParsingState.INVALID
                else:
                    state = ParsingState.INVALID
                    str_x = ""
                    str_y = ""
                print("after:", state, "(", str_x, ", ", str_y + ")", should_do, ans)
    print("ans", ans)
                


if __name__ == '__main__':
    main()