"""
boards for tic tac toe agent to play on

1) 3X3 board
2) 4*4 board
3) 5*5 board
"""

BOARD1 = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

BOARD2 = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

BOARD3 = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

"""
    win_state = [
        [state[0][0], state[0][1], state[0][2]],  # Row 1
        [state[1][0], state[1][1], state[1][2]],  # Row 2
        [state[2][0], state[2][1], state[2][2]],  # Row 3
        [state[0][0], state[1][0], state[2][0]],  # Col 1
        [state[0][1], state[1][1], state[2][1]],  # Col 2
        [state[0][2], state[1][2], state[2][2]],  # Col 3
        [state[0][0], state[1][1], state[2][2]],  # Diag 1
        [state[2][0], state[1][1], state[0][2]],  # Diag 2
    ]

    win_state = [
        [state[0][0], state[0][1], state[0][2], state[0][3]],  # Row 1
        [state[1][0], state[1][1], state[1][2], state[1][3]],  # Row 2
        [state[2][0], state[2][1], state[2][2], state[2][3]],  # Row 3
        [state[3][0], state[3][1], state[3][2], state[3][3]],  # Row 4
        [state[0][0], state[1][0], state[2][0], state[3][0]],  # Col 1
        [state[0][1], state[1][1], state[2][1], state[3][1]],  # Col 2
        [state[0][2], state[1][2], state[2][2], state[3][2]],  # Col 3
        [state[0][3], state[1][3], state[2][3], state[3][3]],  # Col 4
        [state[0][0], state[1][1], state[2][2], state[3][3]],  # Diag 1
        [state[0][3], state[1][2], state[2][1], state[3][0]],  # Diag 2
    ]

    win_state = [
        [state[0][0], state[0][1], state[0][2], state[0][3], state[0][4]],  # Row 1
        [state[1][0], state[1][1], state[1][2], state[1][3], state[1][4]],  # Row 2
        [state[2][0], state[2][1], state[2][2], state[2][3], state[2][4]],  # Row 3
        [state[3][0], state[3][1], state[3][2], state[3][3], state[3][4]],  # Row 4
        [state[4][0], state[4][1], state[4][2], state[4][3], state[4][4]],  # Row 5
        [state[0][0], state[1][0], state[2][0], state[3][0], state[4][0]],  # Col 1
        [state[0][1], state[1][1], state[2][1], state[3][1], state[4][1]],  # Col 2
        [state[0][2], state[1][2], state[2][2], state[3][2], state[4][2]],  # Col 3
        [state[0][3], state[1][3], state[2][3], state[3][3], state[4][3]],  # Col 4
        [state[0][4], state[1][4], state[2][4], state[3][4], state[4][4]],  # Col 5
        [state[0][0], state[1][1], state[2][2], state[3][3], state[4][4]],  # Diag 1
        [state[0][4], state[1][3], state[2][2], state[3][1], state[4][0]],  # Diag 2
    ]
"""
