puzzle = [
    [5,3,4,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]
]

sol = [
    [5,3,4,6,7,8,9,1,2],
    [6,7,2,1,9,5,3,4,8],
    [1,9,8,3,4,2,5,6,7],
    [8,5,9,7,6,1,4,2,3],
    [4,2,6,8,5,3,7,9,1],
    [7,1,3,9,2,4,8,5,6],
    [9,6,1,5,3,7,2,8,4],
    [2,8,7,4,1,9,6,3,5],
    [3,4,5,2,8,6,1,7,9]
]

while True:
    print("\n")
    for i in range(9):
        if i%3==0 and i!=0:
            print("-" * 25)

        for j in range(9):
            if j%3==0 and j!=0:
                print("|",end=" ")

            if puzzle[i][j] == 0:
                print(".", end=" ")
            else:
                print(puzzle[i][j], end=" ")
        print()

    row=int(input("Enter row(0-8):"))
    col=int(input("Enter column(0-8):"))

    if puzzle[row][col]!=0:
        print("Cell already filled")
        continue
    n=int(input("Enter the number(1-9):"))

    if n==sol[row][col]:
        puzzle[row][col]=n
        print("Correct")
    else:
        print("Wrong")


    complete=True
    for i in range(9):
        for j in range(9):
            if puzzle[i][j]==0:
                complete=False
    if complete:
        print("\nCongratulations!! You solved.")
        break













