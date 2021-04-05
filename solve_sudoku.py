import numpy as np

def possible(row,col,num):
    for ele in range(9):
        if grid[row][ele]==num:
            return False
        if grid[ele][col]==num:
            return False
    row1=(row//3)*3
    col1=(col//3)*3
    for ele1 in range(row1,(row1+3)):
        for ele2 in range(col1,(col1+3)):
            if grid[ele1][ele2]==num:
                return False
    return True
            
def solve_puzzle(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col]==0:
                for num in range(1,10):
                    if possible(row,col,num):
                        grid[row][col]=num
                        solve_puzzle(grid)
                        grid[row][col]=0
                return
    print("\nThe Solution To The Puzzle\n")
    print(np.matrix(grid))

if __name__=="__main__":
    grid=[]
    print("Enter Sudoku Puzzle\n")
    try:
        for num in range(9):
            list_of_num=[int(x) for x in input().split()]
            if len(list_of_num) != 9:
                raise "Invalid Lenght"
            grid.append(list_of_num)
    except:
        print("Error Occured")
    else:
        solve_puzzle(grid)
    
    
        
                        
            
            
