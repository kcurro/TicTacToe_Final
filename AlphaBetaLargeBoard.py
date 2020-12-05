from math import inf as infinity
from random import choice, random
import random
import time

# play on a 5x5 board
AGENT = -1
COMP = +1
board = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
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
    win_state_large_board = [
        [state[0][0], state[0][1], state[0][2], state[0][3], state[0][4]],
        [state[1][0], state[1][1], state[1][2], state[1][3], state[1][4]],
        [state[2][0], state[2][1], state[2][2], state[2][3], state[2][4]],
        [state[3][0], state[3][1], state[3][2], state[3][3], state[3][4]],
        [state[4][0], state[4][1], state[4][2], state[4][3], state[4][4]],
        [state[0][0], state[1][0], state[2][0], state[3][0], state[4][0]],
        [state[0][1], state[1][1], state[2][1], state[3][1], state[4][1]],
        [state[0][2], state[1][2], state[2][2], state[3][2], state[4][2]],
        [state[0][3], state[1][3], state[2][3], state[3][3], state[4][3]],
        [state[0][4], state[1][4], state[2][4], state[3][4], state[4][4]],
        [state[0][0], state[1][1], state[2][2], state[3][3], state[4][4]],
        [state[0][4], state[1][3], state[2][2], state[3][1], state[4][0]],
    ]
    if [player, player, player, player, player] in win_state_large_board:
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


def alphaBeta(state, depth, player, alpha, beta, expanded):
    current_depth = min(5, depth)

    if player == AGENT:
        best = [-1, -1, -infinity, expanded]
    if player == COMP:
        best = [-1, -1, +infinity, expanded]

    if depth == 0 or checkWin(state):
        score = evaluate(state)
        return [-1, -1, score, expanded]

    for cell in availablePositions(state):
        x, y = cell[0], cell[1]
        state[x][y] = player
        score = alphaBeta(state, current_depth - 1, changePlayer(player), alpha, beta, expanded)
        state[x][y] = 0
        score[0], score[1] = x, y

        if player == AGENT:
            if score[2] > best[2]:
                score[2] = max(score[2], best[2])
                temp = [score[0], score[1], score[2], score[3]]
                best = temp

            expanded += 1
            best[3] = expanded

            if score[2] > beta:
                return best
            alpha = max(alpha, best[2])

        else:
            if score[2] < best[2]:
                score[2] = min(score[2], best[2])
                temp = [score[0], score[1], score[2], score[3]]
                best = temp

            expanded += 1
            best[3] = expanded

            if score[2] < alpha:
                return best

            beta = min(beta, best[2])

    return best


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
    str_line = '-------------------------'

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

        if depth == 25:
            x = choice([0, 1, 2, 3, 4])
            y = choice([0, 1, 2, 3, 4])

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
    expanded = 0
    alpha, beta = float('-inf'), float('inf')

    if depth == 0 or checkWin(board):
        return
    else:

        print('Agent turn\n')
        loadBoard(board, computerSymbol, agentSymbol)

        if depth == 25:
            x = choice([0, 1, 2, 3, 4])
            y = choice([0, 1, 2, 3, 4])
        else:
            move = alphaBeta(board, depth, AGENT, alpha, beta, expanded)
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
        # print(expanded_agent)
        # print(expanded_comp)
        if expanded_agent is None or expanded_comp is None:
            if expanded_agent is None:
                expanded_agent = 0
            if expanded_comp is None:
                expanded_comp = 0
        expanded = expanded + int(expanded_agent) + int(expanded_comp)
        # print(f'loop {expanded}')

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
    print("Alpha Beta Tic-Tac-Toe Board 5x5 Board")
    main()
