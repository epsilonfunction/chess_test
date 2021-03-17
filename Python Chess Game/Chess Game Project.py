def createZeroMatrix(r,c):
    output = [[0 for i in range(c)]for i in range(r)]
    return output

def mTightPrint(m):
    for i in range(len(m)):
        line = ''
        for j in range(len(m[0])):
            line += str(m[i][j]) +' '
        print(line)

abc = 'abcdefghijklmnopgqrstuvwxyz'

def gamesetup():
    game = createZeroMatrix(9,9)
    for i in range(1,9):
        game[0][i] = i
        game[-i][0] = abc[i-1]
    game[1][1]=game[1][8]=game[8][1]=game[8][8] = 'R'
    mTightPrint(game)
    return

gamesetup()

