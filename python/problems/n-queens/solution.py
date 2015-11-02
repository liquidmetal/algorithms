#!/usr/bin/python

def place(positions, row, col):
    # Loop from 0 to row-1
    for i in xrange(row):
        if positions[i] == col or abs(i-row) == abs(positions[i]-col):
            return False

    return True

sol_count = 0
def place_queens(positions, row, num_rows, num_cols):
    global sol_count
    for col in xrange(num_cols):
        if place(positions, row, col):
            positions[row] = col

            if row == num_rows-1:
                print("Found a solution")
                disp(positions, num_cols)
                sol_count += 1
                break
            else:
                place_queens(positions, row+1, num_rows, num_cols)
    return


def main():
    global sol_count
    num_rows = 8
    num_cols = 8
    positions = [0] * num_rows
    place_queens(positions, 0, num_rows, num_cols)

    print("numbwer of solutions: %d" % sol_count)

                

def disp(positions, num_cols):
    for i in positions:
        print("."*i + "Q" + "."*(num_cols - i - 1))
            
    return

if __name__ == '__main__':
    main()
