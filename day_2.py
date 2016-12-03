instructions = [
        "LDUDDRUDRRURRRRDRUUDULDLULRRLLLUDDULRDLDDLRULLDDLRUURRLDUDDDDLUULUUDDDDLLLLLULLRURDRLRLRLLURDLLDDUULUUUUDLULLRLUUDDLRDRRURRLURRLLLRRDLRUDURRLRRRLULRDLUDRDRLUDDUUULDDDDDURLDULLRDDRRUDDDDRRURRULUDDLLRRDRURDLLLLLUUUDLULURLULLDRLRRDDLUDURUDRLRURURLRRDDLDUULURULRRLLLDRURDULRDUURRRLDLDUDDRLURRDRDRRLDLRRRLRURDRLDRUDLURRUURDLDRULULURRLDLLLUURRULUDDDRLDDUDDDRRLRDUDRUUDDULRDDULDDURULUDLUDRUDDDLRRRRRDLULDRLRRRRUULDUUDRRLURDLLUUDUDDDLUUURDRUULRURULRLLDDLLUDLURRLDRLDDDLULULLURLULRDLDRDDDLRDUDUURUUULDLLRDRUDRDURUUDDLRRRRLLLUULURRURLLDDLDDD",
        "DRURURLLUURRRULURRLRULLLURDULRLRRRLRUURRLRRURRRRUURRRLUDRDUDLUUDULURRLDLULURRLDURLUUDLDUDRUURDDRDLLLDDRDDLUUDRDUDDRRDLDUDRLDDDRLLDDLUDRULRLLURLDLURRDRUDUDLDLULLLRDLLRRDULLDRURRDLDRURDURDULUUURURDLUDRRURLRRLDULRRDURRDRDDULLDRRRLDRRURRRRUURDRLLLRRULLUDUDRRDDRURLULLUUDDRLDRRDUDLULUUDRDDDDLRLRULRLRLLDLLRRDDLDRDURRULLRLRRLULRULDDDRDRULDRUUDURDLLRDRURDRLRDDUDLLRUDLURURRULLUDRDRDURLLLDDDRDRURRDDRLRRRDLLDDLDURUULURULRLULRLLURLUDULDRRDDLRDLRRLRLLULLDDDRDRU",
        "URUUDUDRDDRDRRRDLLUDRUDRUUUURDRRDUDUULDUDLLUDRRUDLLRDLLULULDRRDDULDRLDLDDULLDDRDDDLRLLDLLRDUUDUURLUDURDRRRRLRRLDRRUULLDLDLRDURULRURULRRDRRDDUUURDURLLDDUUDLRLDURULURRRDRRUUUDRDDLRLRRLLULUDDRRLRRRRLRDRUDDUULULRRURUURURRLRUDLRRUUURUULLULULRRDDULDRRLLLDLUDRRRLLRDLLRLDUDDRRULULUDLURLDRDRRLULLRRDRDLUURLDDURRLDRLURULDLDRDLURRDRLUUDRUULLDRDURLLDLRUDDULLLLDLDDDLURDDUDUDDRLRDDUDDURURLULLRLUDRDDUDDLDRUURLDLUUURDUULRULLDDDURULDDLLD",
        "LRRLLRURUURRDLURRULDDDLURDUURLLDLRRRRULUUDDLULLDLLRDLUDUULLUDRLLDRULDDURURDUUULRUDRLLRDDDURLRDRRURDDRUDDRRULULLLDLRLULLDLLDRLLLUDLRURLDULRDDRDLDRRDLUUDDLURDLURLUDLRDLDUURLRRUULDLURULUURULLURLDDURRURDRLUULLRRLLLDDDURLURUURLLLLDLLLUDLDLRDULUULRRLUUUUDLURRURRULULULRURDDRRRRDRUDRURDUDDDDUDLURURRDRRDRUDRLDLDDDLURRRURRUDLDURDRLDLDLDDUDURLUDUUDRULLRLLUUDDUURRRUDURDRRUURLUDRRUDLUDDRUUDLULDLLDLRUUDUULLDULRRLDRUDRRDRLUUDDRUDDLLULRLULLDLDUULLDRUUDDUDLLLLDLDDLDLURLDLRUUDDUULLUDUUDRUDLRDDRDLDRUUDUDLLDUURRRLLLLRLLRLLRLUUDULLRLURDLLRUUDRULLULRDRDRRULRDLUDDURRRRURLLRDRLLDRUUULDUDDLRDRD",
        "DDLRRULRDURDURULLLLRLDDRDDRLLURLRDLULUDURRLUDLDUDRDULDDULURDRURLLDRRLDURRLUULLRUUDUUDLDDLRUUDRRDDRLURDRUDRRRDRUUDDRLLUURLURUDLLRRDRDLUUDLUDURUUDDUULUURLUDLLDDULLUURDDRDLLDRLLDDDRRDLDULLURRLDLRRRLRRURUUDRLURURUULDURUDRRLUDUDLRUDDUDDRLLLULUDULRURDRLUURRRRDLLRDRURRRUURULRUDULDULULUULULLURDUDUDRLDULDRDDULRULDLURLRLDDDDDDULDRURRRRDLLRUDDRDDLUUDUDDRLLRLDLUDRUDULDDDRLLLLURURLDLUUULRRRUDLLULUUULLDLRLDLLRLRDLDULLRLUDDDRDRDDLULUUR"
    ]

# instructions = [
#     "ULL",
#     "RRDDD",
#     "LURDL",
#     "UUUUD"
# ]

keypad = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

keypad_2 = [
      [0, 0, 1, 0, 0],
      [0, 2, 3, 4, 0],
      [5, 6, 7, 8, 9],
      [0, "A", "B", "C", 0],
      [0, 0, "D", 0, 0],
]

valid_matrix = [
    [0, 0, 1, 0, 0],
    [0, 1, 1, 1, 0],
    [1, 1, 1, 1, 1],
    [0, 1, 1, 1, 0],
    [0, 0, 1, 0, 0]
]

move = {
    "L": [0, -1],
    "R": [0, 1],
    "U": [-1, 0],
    "D": [1, 0]
}

curr_pos = [2, 0]

result = ""


def first():
    for key in instructions:
        for each in key:
            next_i = curr_pos[0] + move[each][0]
            next_j = curr_pos[1] + move[each][1]
            if 0 <= next_i < 3 and 0 <= next_j < 3:
                curr_pos[0], curr_pos[1] = next_i, next_j
                print(curr_pos, each)
        result += str(keypad[curr_pos[0]][curr_pos[1]])
        print(result)


def second():
    result = ""
    for key in instructions:
        for each in key:
            next_i = curr_pos[0] + move[each][0]
            next_j = curr_pos[1] + move[each][1]
            if 0 <= next_i < 5 and 0 <= next_j < 5:
                if valid_matrix[next_i][next_j]:
                    curr_pos[0], curr_pos[1] = next_i, next_j
                    print(curr_pos, each)
        result += str(keypad_2[curr_pos[0]][curr_pos[1]])
        print(result)

second()
