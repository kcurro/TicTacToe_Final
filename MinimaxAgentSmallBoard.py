from math import inf as infinity
from random import choice, random
import random
import time

# play on a 3x3 board
AGENT = -1
COMP = +1
board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
]


def evaluate(state):
    if winState(state, COMP):
        #score = +1
        score = 100
        return score

    elif winState(state, AGENT):
        #score = -1
        score = -100
        return score

    else:
        score = 0
        return score


def winState(state, player):
    win_state = [
        [state[0][0], state[0][1], state[0][2]],
        [state[1][0], state[1][1], state[1][2]],
        [state[2][0], state[2][1], state[2][2]],
        [state[0][0], state[1][0], state[2][0]],
        [state[0][1], state[1][1], state[2][1]],
        [state[0][2], state[1][2], state[2][2]],
        [state[0][0], state[1][1], state[2][2]],
        [state[2][0], state[1][1], state[0][2]],
    ]
    if [player, player, player] in win_state:
        return True
    else:
        return False


def checkWin(state):
    if winState(state, AGENT):
        return True
    elif winState(state, COMP):
        return True
    else:
        return False


def availablePositions(state):
    #spots available for agent or computer to play
    l = []
    for first in enumerate(state):
        for second in enumerate(first[1]):
            if second[1] == 0:
                l.append([first[0], second[0]])
    return l


def validMove(x, y, player):
    if [x, y] in availablePositions(board):
        board[x][y] = player
        return True

    if [x, y] not in availablePositions(board):
        return False


def minimax(state, depth, player, expanded):
    if player == AGENT:
        best = [-1, -1, -infinity, expanded]
        for cell in availablePositions(state):
            x, y = cell[0], cell[1]
            state[x][y] = player
            score = minimax(state, depth - 1, changePlayer(player), expanded)
            state[x][y] = 0
            score[0], score[1] = x, y
            if score[2] > best[2]:
                temp = max(score, best)
                best = temp
            expanded += 1
            best[3] = expanded
        return best

    if player == COMP:
        best = [-1, -1, infinity, expanded]
        for cell in availablePositions(state):
            x, y = cell[0], cell[1]
            state[x][y] = player
            score = minimax(state, depth - 1, changePlayer(player), expanded)
            state[x][y] = 0
            score[0], score[1] = x, y
            if score[2] < best[2]:
                temp = min(score, best)
                best = temp
            expanded += 1
            best[3] = expanded

        return best

    if depth == 0 or checkWin(state):
        score = evaluate(state)
        return [-1, -1, score, expanded]


def changePlayer(player):
    if player == AGENT:
        return 1
    else:
        return -1


def loadBoard(state, computerSymbol, agentSymbol):
    chars = {
        -1: agentSymbol,
        +1: computerSymbol,
        0: ' '
    }
    str_line = '---------------'

    print('\n' + str_line)
    for row in state:
        for cell in row:
            symbol = chars[cell]
            print(f'| {symbol} |', end='')
        print('\n' + str_line)


def ai_turn(computerSymbol, agentSymbol, expanded):
    # agent plays choosing random selection choice
    openPositions = len(availablePositions(board))
    depth = openPositions

    if depth == 0 or checkWin(board):
        return

    else:
        print('Computer turn\n')
        loadBoard(board, computerSymbol, agentSymbol)

        if depth == 9:
            x = choice([0, 1, 2])
            y = choice([0, 1, 2])

        else:
            l = []

            for first in range(len(board)):
                for second in range(len(board)):
                    if board[first][second] == 0:
                        l.append((first, second))

            move = random.choice(l)
            expanded = 1
            x, y = move[0], move[1]

        validMove(x, y, COMP)
        time.sleep(1)

        return expanded


def agent_turn(computerSymbol, agentSymbol, expanded):
    openPositions = len(availablePositions(board))
    depth = openPositions

    if depth == 0 or checkWin(board):
        return
    else:

        print('Agent turn\n')
        loadBoard(board, computerSymbol, agentSymbol)

        if depth == 9:
            x = choice([0, 1, 2])
            y = choice([0, 1, 2])
        else:
            move = minimax(board, depth, AGENT, expanded)
            x, y = move[0], move[1]
            expanded = move[3]

        validMove(x, y, AGENT)
        time.sleep(1)
        return expanded


def main():
    start_time = time.time()
    agentSymbol = ''
    computerSymbol = ''
    expanded_comp = 0
    expanded_agent = 0
    expanded = 0

    agentSymbol = input('\nChoose the Agents symbol X or O\nUser Selected: ').upper()

    if agentSymbol == 'X':
        computerSymbol = 'O'

    if agentSymbol == 'O':
        computerSymbol = 'X'

    # AGENT starts first
    while len(availablePositions(board)) > 0 and not checkWin(board):
        expanded_agent = agent_turn(computerSymbol, agentSymbol, expanded_agent)
        expanded_comp = ai_turn(computerSymbol, agentSymbol, expanded_comp)
        #print(expanded_agent)
        #print(expanded_comp)
        if expanded_agent is None or expanded_comp is None:
            if expanded_agent is None:
                expanded_agent = 0
            if expanded_comp is None:
                expanded_comp = 0
        expanded = expanded + int(expanded_agent) + int(expanded_comp)
        #print(f'loop {expanded}')

    # Game over message with number nodes expanded, and time to execute
    if winState(board, COMP):
        print(f'COMPUTER turn')
        loadBoard(board, computerSymbol, agentSymbol)
        print('AGENT LOSES - COMPUTER WINS!')
        print(f'Expanded {expanded} nodes')
        print("Execution time in %s seconds" % (time.time() - start_time))

    elif winState(board, AGENT):
        print(f'AGENT turn')
        loadBoard(board, computerSymbol, agentSymbol)
        print('AGENT WON!')
        print(f'Expanded {expanded} nodes')
        print("Execution time in %s seconds" % (time.time() - start_time))
    else:
        loadBoard(board, computerSymbol, agentSymbol)
        print('TIE!')
        print(f'Expanded {expanded} nodes')
        print("Execution time in %s seconds" % (time.time() - start_time))

    exit()


if __name__ == '__main__':
    print("Minimax Tic-Tac-Toe Board 3x3 Board")
    main()
