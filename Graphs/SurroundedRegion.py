# 130. Surrounded Regions
# DFS
# try again BFS
class Solution:
    def solve(self, m):
        """
        Do not return anything, modify board in-place instead.
        """
        def check(i,j):
            if m[i][j]=="O":
                m[i][j]="#"
            else:
                return
            d=[[0,1],[1,0],[-1,0],[0,-1]]
            for x,y in d:
                if 0<=x+i<len(m) and 0<=y+j<len(m[0]) and m[x+i][y+j]=="O":
                    check(x+i,y+j)
        for i in range(len(m)):
            check(i,0)
        for i in range(len(m)):
            check(i,len(m[0])-1)
        for i in range(len(m[0])):
            check(len(m)-1,i)
        for i in range(len(m[0])):
            check(0,i)
        # traverse again
        for i in range(len(m)):
            for j in range(len(m[0])):
                if m[i][j]=="O":
                    m[i][j]="X"
                elif m[i][j]=="#":
                    m[i][j]="O"
