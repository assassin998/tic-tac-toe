p1 = 'p1'
p2 = 'p2'
p3 = 'p3'
p4 = 'p4'
p5 = 'p5'
p6 = 'p6'
p7 = 'p7'
p8 = 'p8'
p9 = 'p9'

turn = 'x'
win =  False
end = False

while end == False:
    print(' ')
    print(' ')
    print(' ')
    print(' ')
    print(' ')
    print(' ')
    print(' ')
    print(' ')
    print(' ')
    print(' ')
    print(' ')
    print(' ')
    print(p1, '|', p2, '|', p3)
    print('____________________')
    print(p4, '|', p5, '|', p6)
    print('____________________')
    print(p7, '|', p8, '|', p9)

    if win == False:
        while str(turn) == 'x':
            print("player1 turn(X) chose a square")
            sq = input('square (ex p1) ')

            if str(sq) == 'p1' and not p1 == '0':
                p1 = "x"
            if str(sq) == 'p2' and not p2 == '0':
                p2 = "x"
            if str(sq) == 'p3' and not p3 == '0':
                p3 = "x"
            if str(sq) == 'p4' and not p4 == '0':
                p4 = "x"
            if str(sq) == 'p5' and not p5 == '0':
                p5 = "x"
            if str(sq) == 'p6' and not p6 == '0':
                p6 = "x"
            if str(sq) == 'p7' and not p7 == '0':
                p7 = "x"
            if str(sq) == 'p8' and not p8 == '0':
                p8 = "x"
            if str(sq) == 'p9' and not p9 == '0':
                p9 = "x"
            print(' ')
            print(' ')
            print(' ')
            print(' ')
            print(' ')
            print(' ')
            print(' ')
            print(' ')
            print(' ')
            print(' ')
            print(' ')
            print(' ')
            print(p1, '|', p2, '|', p3)
            print('____________________')
            print(p4, '|', p5, '|', p6)
            print('____________________')
            print(p7, '|', p8, '|', p9)

            turn = '0'
            if str(p1) == str(p2) and str(p2) == str(p3):
                win = True
                end = True
                print(turn, "won!")
            if str(p1) == str(p5) and str(p5) == str(p9):
                win = True
                end = True
                print(turn, "won!")
            if str(p1) == str(p4) and str(p4) == str(p7):
                win = True
                end = True
                print(turn, "won!")
            if str(p2) == str(p5) and str(p5) == str(p8):
                win = True
                end = True
                print(turn, "won!")
            if str(p3) == str(p5) and str(p5) == str(p7):
                win = True
                end = True
                print(turn, "won!")
            if str(p3) == str(p6) and str(p6) == str(p9):
                win = True
                end = True
                print(turn, "won!")
            if str(p4) == str(p5) and str(p5) == str(p6):
                win = True
                end = True
                print(turn, "won!")
            if str(p7) == str(p8) and str(p8) == str(p9):
                win = True
                end = True
                print(turn, "won!")

        if win == False:
            while str(turn) == 'x':
                print("player1 turn(X) chose a square")
                sq = input('square (ex p1) ')

                if str(sq) == 'p1' and not p1 == '0':
                    p1 = "x"
                if str(sq) == 'p2' and not p2 == '0':
                    p2 = "x"
                if str(sq) == 'p3' and not p3 == '0':
                    p3 = "x"
                if str(sq) == 'p4' and not p4 == '0':
                    p4 = "x"
                if str(sq) == 'p5' and not p5 == '0':
                    p5 = "x"
                if str(sq) == 'p6' and not p6 == '0':
                    p6 = "x"
                if str(sq) == 'p7' and not p7 == '0':
                    p7 = "x"
                if str(sq) == 'p8' and not p8 == '0':
                    p8 = "x"
                if str(sq) == 'p9' and not p9 == '0':
                    p9 = "x"
                print(' ')
                print(' ')
                print(' ')
                print(' ')
                print(' ')
                print(' ')
                print(' ')
                print(' ')
                print(' ')
                print(' ')
                print(' ')
                print(' ')
                print(p1, '|', p2, '|', p3)
                print('____________________')
                print(p4, '|', p5, '|', p6)
                print('____________________')
                print(p7, '|', p8, '|', p9)

            while str(turn) == '0':
                print("player1 turn(X) chose a square")
                sq = input('square (ex p1) ')

                if str(sq) == 'p1' and not p1 == 'x':
                    p1 = "0"
                if str(sq) == 'p2' and not p2 == 'x':
                    p2 = "0"
                if str(sq) == 'p3' and not p3 == 'x':
                    p3 = "0"
                if str(sq) == 'p4' and not p4 == 'x':
                    p4 = "0"
                if str(sq) == 'p5' and not p5 == 'x':
                    p5 = "0"
                if str(sq) == 'p6' and not p6 == 'x':
                    p6 = "0"
                if str(sq) == 'p7' and not p7 == 'x':
                    p7 = "0"
                if str(sq) == 'p8' and not p8 == 'x':
                    p8 = "0"
                if str(sq) == 'p9' and not p9 == 'x':
                    p9 = "0"
                print(' ')
                print(' ')
                print(' ')
                print(' ')
                print(' ')
                print(' ')
                print(' ')
                print(' ')
                print(' ')
                print(' ')
                print(' ')
                print(' ')
                print(p1, '|', p2, '|', p3)
                print('____________________')
                print(p4, '|', p5, '|', p6)
                print('____________________')
                print(p7, '|', p8, '|', p9)
        if str(p1) == str(p2) and str(p2) == str(p3):
            win = True
            end = True
            print(turn, "won!")
        if str(p1) == str(p5) and str(p5) == str(p9):
            win = True
            end = True
            print(turn, "won!")
        if str(p1) == str(p4) and str(p4) == str(p7):
            win = True
            end = True
            print(turn, "won!")
        if str(p2) == str(p5) and str(p5) == str(p8):
            win = True
            end = True
            print(turn, "won!")
        if str(p3) == str(p5) and str(p5) == str(p7):
            win = True
            end = True
            print(turn, "won!")
        if str(p3) == str(p6) and str(p6) == str(p9):
            win = True
            end = True
            print(turn, "won!")
        if str(p4) == str(p5) and str(p5) == str(p6):
            win = True
            end = True
            print(turn, "won!")
        if str(p7) == str(p8) and str(p8) == str(p9):
            win = True
            end = True
            print(turn, "won!")
        turn = 'x'
input(' ')