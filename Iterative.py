import time

def EightQueen():
    """
    count: counts the number of solutions
    first: a boolean used to determine the time it takes to calculate the first solution
    first_time: will be set to the time it takes to find the first solution
    q1 - q9 : will hold the 'y' position of each queen, since no queen is allowed to exist on the same row

    """
    count = 0
    first = "true"
    first_time = 0
    q1 = 0
# Exhaustively tries all placements for queens
    while (q1 < 8):
        q2 = 0
        while (q2 < 8):
            q3 = 0
            while (q3 < 8):
                q4 = 0
                while (q4 < 8):
                    q5 = 0
                    while (q5 < 8):
                        q6 = 0
                        while (q6 < 8):
                            q7 = 0
                            while (q7 < 8):
                                q8 = 0
                                while (q8 < 8):
                                    # Checks if any queen is in the same column as another queen
                                    if (not (q1 == q2 or q1 == q3
                                             or q1 == q4 or q1 == q5 or q1 == q6 or q1 == q7
                                             or q1 == q8 or q2 == q3 or q2 == q4 or q2 == q5
                                             or q2 == q6 or q2 == q7 or q2 == q8 or q3 == q4
                                             or q3 == q5 or q3 == q6 or q3 == q7 or q3 == q8
                                             or q4 == q5 or q4 == q6 or q4 == q7 or q4 == q8
                                             or q5 == q6 or q5 == q7 or q5 == q8 or q6 == q7
                                             or q6 == q8 or q7 == q8 )):

                                        """
                                    checks: counts the number of valid placements. This checking is redundant over each queen,
                                            so when the number of of valid placements is exactly 56 (8 * 7), we have found a solution
                                    queenA: A cursor that points to a specific queen
                                    queenB: A cursor that points to another specific queen
                                    queen[]: An array that holds the values of the queens. The index represents row,
                                             while the value represents the column of a queen

                                    Checks if there is any queens diagonal to one another by comparing the difference
                                    to row values and column values

                                    """
                                        checks = 0
                                        queenA = 0
                                        queens = [q1, q2, q3, q4, q5, q6, q7, q8]
                                        while queenA < 8:
                                            queenB = 0
                                            while queenB < 8:
                                                if not (abs(queens[queenA] - queens[queenB]) == abs(queenA - queenB)):
                                                    checks += 1
                                                queenB += 1
                                            queenA += 1
                                            # This is a calculated constant (7*8) where each queen checks
                                            # compares itself to each other queen
                                            if checks == 56:
                                                count += 1
                                                if first:
                                                    first = "false"
                                                    first_time = time.clock() - start_time

                                                print "-----------------------------------------"
                                                board = [[0 for x in range(8)] for y in range(8)]
                                                board[0][q1] = 1
                                                board[1][q2] = 1
                                                board[2][q3] = 1
                                                board[3][q4] = 1
                                                board[4][q5] = 1
                                                board[5][q6] = 1
                                                board[6][q7] = 1
                                                board[7][q8] = 1
                                                for row in board:
                                                    for val in row:
                                                        print '{:4}'.format(val),
                                                    print

                                    q8 += 1
                                q7 += 1
                            q6 += 1
                        q5 += 1
                    q4 += 1
                q3 += 1
            q2 += 1
        q1 += 1
    print count, " solutions"
    print "CPU Time till first solution: ", first_time, "seconds."

def NineQueen():
    """
    count: counts the number of solutions
    first: a boolean used to determine the time it takes to calculate the first solution
    first_time: will be set to the time it takes to find the first solution
    q1 - q9 : will hold the 'y' position of each queen, since no queen is allowed to exist on the same row

    """
    count = 0
    first = "true"
    first_time = 0
    q1 = 0
    
    # Exhaustively tries all placements for queens on a 9x9 board. Each placement will be evaluated to see if it is valid.
    while (q1 < 9):
        q2 = 0
        while (q2 < 9):
            q3 = 0
            while (q3 < 9):
                q4 = 0
                while (q4 < 9):
                    q5 = 0
                    while (q5 < 9):
                        q6 = 0
                        while (q6 < 9):
                            q7 = 0
                            while (q7 < 9):
                                q8 = 0
                                while (q8 < 9):
                                    q9 = 0
                                    while (q9 < 9):

                                        # Checks if any queen is in the same column as another queen
                                        if (not (q1 == q2 or q1 == q3
                                                 or q1 == q4 or q1 == q5 or q1 == q6 or q1 == q7
                                                 or q1 == q8 or q1 == q9 or q2 == q3 or q2 == q4 or q2 == q5
                                                 or q2 == q6 or q2 == q7 or q2 == q8 or q2 == q9 or q3 == q4
                                                 or q3 == q5 or q3 == q6 or q3 == q7 or q3 == q8 or q3 == q9
                                                 or q4 == q5 or q4 == q6 or q4 == q7 or q4 == q8 or q4 == q9
                                                 or q5 == q6 or q5 == q7 or q5 == q8 or q5 == q9 or q6 == q7
                                                 or q6 == q8 or q6 == q9 or q7 == q8 or q7 == q9 or q8 == q9 )):

                                            """
                                        checks: counts the number of valid placements. This checking is redundant over each queen,
                                                so when the number of of valid placements is exactly 72 (8 * 9), we have found a solution
                                        queenA: A cursor that points to a specific queen
                                        queenB: A cursor that points to another specific queen
                                        queen[]: An array that holds the values of the queens. The index represents row, while the value
                                                 represents the column of a queen
                                        
                                        Checks if there is any queens diagonal to one another by comparing the difference
                                        to row values and column values
                                        
                                        """
                                            checks = 0
                                            queenA = 0
                                            queen = [q1, q2, q3, q4, q5, q6, q7, q8, q9]
                                            while queenA < 9:
                                                queenB = 0
                                                while queenB < 9:
                                                    if not (abs(queen[queenA] - queen[queenB]) == abs(queenA - queenB)):
                                                        checks += 1
                                                    queenB += 1
                                                queenA += 1
                                                if checks == 72:
                                                    count += 1
                                                    if first:
                                                        first = "false"
                                                        first_time = time.clock() - start_time

                                                    print "-----------------------------------------------"
                                                    board = [[0 for x in range(9)] for y in range(9)]
                                                    board[0][q1] = 1
                                                    board[1][q2] = 1
                                                    board[2][q3] = 1
                                                    board[3][q4] = 1
                                                    board[4][q5] = 1
                                                    board[5][q6] = 1
                                                    board[6][q7] = 1
                                                    board[7][q8] = 1
                                                    board[8][q9] = 1
                                                    for row in board:
                                                        for val in row:
                                                            print '{:4}'.format(val),
                                                        print
                                        q9 += 1
                                    q8 += 1
                                q7 += 1
                            q6 += 1
                        q5 += 1
                    q4 += 1
                q3 += 1
            q2 += 1
        q1 += 1
    print count, " solutions"
    print "CPU Time till first solution: ", first_time, "seconds."


start_time = time.clock()
NineQueen()

print "Total CPU Time:", time.clock() - start_time, "seconds."
