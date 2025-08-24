def print_mat_row_Wise(matrix,m,n):
    for i in range(m):
        for j in range(n):
            print(matrix[i][j],end=" ")
        print()


# column wise pritning matrix....
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# 1 4 7
# 2 5 8
# 3 6 9
def print_mat(matrix,m,n):
    for i in range(n):
        for j in range(m):
            print(matrix[j][i],end=" ")
        print()
mat=[]
m=int(input("rows:"))
n=int(input("cols:"))
for i in range(m):
    mat.append(list(map(int,input(f'row {i}:').split())))
print(mat)
print_mat(mat,m,n)
print()
print_mat_row_Wise(mat,m,n)