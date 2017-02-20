import time

def main():
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

                                        # Checks if any queen is diagonal to another queen. If so, prints the solution.
                                        checks = 0
                                        top = 0
                                        queens = [q1, q2, q3, q4, q5, q6, q7, q8]
                                        while top < 8:
                                            next = 0
                                            while next < 8:
                                                if not (abs(queens[top] - queens[next]) == abs(top - next)):
                                                    checks += 1
                                                next += 1
                                            top += 1
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


start_time = time.clock()
main()

print "Total CPU Time:", time.clock() - start_time, "seconds."
