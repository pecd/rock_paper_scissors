matrix = ['#', ['#', ' ', ' ', ' '], ['#', ' ', ' ', ' '], ['#', ' ', ' ', ' ']]
turn = []
player = ''

def status():
    global matrix
    row3 = [matrix[1][3], matrix[2][3], matrix[3][3]]
    row2 = [matrix[1][2], matrix[2][2], matrix[3][2]]
    row1 = [matrix[1][1], matrix[2][1], matrix[3][1]]
    column1 = [matrix[1][3], matrix[1][2], matrix[1][1]]
    column2 = [matrix[2][3], matrix[2][2], matrix[2][1]]
    column3 = [matrix[3][3], matrix[3][2], matrix[3][1]]
    dia1 = [matrix[1][1], matrix[2][2], matrix[3][3]]
    dia2 = [matrix[1][3], matrix[2][2], matrix[3][1]]
    return [row3, row2, row1, column1, column2, column3, dia1, dia2]

def condition():
    global player
    res = status()
    #print(res)

    empty_check = [x for three in matrix for x in three if x == ' ']
    #print(f'Empty check: {empty_check}')

    win_check = [x for three in res for x in three[0] if len(set(three)) == 1]
    #print(f'Win check: {win_check}')

    if 'X' in win_check or 'O' in win_check:
        draw_field()
        print(f'{player} wins')
        exit()
    elif len(empty_check) == 0:
        draw_field()
        print('Draw')
        exit()

def player_conf():
    global turn, player
    if len(turn) % 2 == 0:
        player = 'X'
    else:
        player = 'O'

def draw_field():
    print('---------')
    print(f'| {matrix[1][3]} {matrix[2][3]} {matrix[3][3]} |')
    print(f'| {matrix[1][2]} {matrix[2][2]} {matrix[3][2]} |')
    print(f'| {matrix[1][1]} {matrix[2][1]} {matrix[3][1]} |')
    print('---------')

while True:
    draw_field()
    player_conf()
    inp_coord = input(f'Enter the coordinates for {player}: ')
    if ' ' not in list(inp_coord) or len(inp_coord) > 4:
        print('You should enter two numbers separated by whitespace!')
    else:
        x, y = inp_coord.split()
        if x.isdigit() is False or y.isdigit() is False:
            print('You should enter numbers!')
            continue
        if x not in ['1', '2', '3'] or y not in ['1', '2', '3']:
            print('Coordinates should be from 1 to 3!')
            continue
        if matrix[int(x)][int(y)] != ' ':
            print('This cell is occupied! Choose another one!')
        else:
            matrix[int(x)][int(y)] = player
            status()
            condition()
            turn.append(player)





