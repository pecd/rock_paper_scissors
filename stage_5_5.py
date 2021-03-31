import sys

matrix = ['#', ['#', ' ', ' ', ' '], ['#', ' ', ' ', ' '], ['#', ' ', ' ', ' ']]

print('---------')
print(f'| {matrix[1][3]} {matrix[2][3]} {matrix[3][3]} |')
print(f'| {matrix[1][2]} {matrix[2][2]} {matrix[3][2]} |')
print(f'| {matrix[1][1]} {matrix[2][1]} {matrix[3][1]} |')
print('---------')

def status():
    line3 = [matrix[1][3], matrix[2][3], matrix[3][3]]
    line2 = [matrix[1][2], matrix[2][2], matrix[3][2]]
    line1 = [matrix[1][1], matrix[2][1], matrix[3][1]]
    column1 = [matrix[1][3], matrix[1][2], matrix[1][1]]
    column2 = [matrix[2][3], matrix[2][2], matrix[2][1]]
    column3 = [matrix[3][3], matrix[3][2], matrix[3][1]]
    dia1 = [matrix[1][1], matrix[2][2], matrix[3][3]]
    dia2 = [matrix[1][3], matrix[2][2], matrix[3][1]]
    return [line1, line2, line3, column1, column2, column3, dia1, dia2]

def condition():
    res = status()
    # print(res)

    empty_check = [x for three in matrix for x in three if x == ' ']
    # print(f'Empty check: {empty_check}')

    win_check = [x for three in res for x in three[0] if len(set(three)) == 1]
    # print(f'Win check: {win_check}')

    if len(win_check) == 1 and win_check[0] != ' ':
        print('---------')
        print(f'| {matrix[1][3]} {matrix[2][3]} {matrix[3][3]} |')
        print(f'| {matrix[1][2]} {matrix[2][2]} {matrix[3][2]} |')
        print(f'| {matrix[1][1]} {matrix[2][1]} {matrix[3][1]} |')
        print('---------')
        print(f'{win_check[0]} wins')
        sys.exit()
    elif len(empty_check) == 0 and len(win_check) == 0:
        print('---------')
        print(f'| {matrix[1][3]} {matrix[2][3]} {matrix[3][3]} |')
        print(f'| {matrix[1][2]} {matrix[2][2]} {matrix[3][2]} |')
        print(f'| {matrix[1][1]} {matrix[2][1]} {matrix[3][1]} |')
        print('---------')
        print('Draw')
        sys.exit()



turn = []

while True:
    if len(turn) % 2 == 0:
        player = 'X'
    else:
        player = 'O'
    inp_coord = input('Enter the coordinates: ')
    if ' ' not in list(inp_coord):
        print('You should enter numbers!')
    else:
        x, y = inp_coord.split()
        if x.isdigit() == False or y.isdigit() == False:
            print('You should enter numbers!')
            continue
        if x not in ['1', '2', '3'] or y not in ['1', '2', '3']:
            print('Coordinates should be from 1 to 3!')
            continue
        if matrix[int(x)][int(y)] == 'X' or matrix[int(x)][int(y)] == 'O':
            print('This cell is occupied! Choose another one!')
        else:
            matrix[int(x)][int(y)] = player
            status()
            condition()
            turn.append(player)
            print('---------')
            print(f'| {matrix[1][3]} {matrix[2][3]} {matrix[3][3]} |')
            print(f'| {matrix[1][2]} {matrix[2][2]} {matrix[3][2]} |')
            print(f'| {matrix[1][1]} {matrix[2][1]} {matrix[3][1]} |')
            print('---------')




