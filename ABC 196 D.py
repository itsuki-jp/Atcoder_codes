def solve( a, b, lst_solve,x,y ):
    for i in range(4):
        if i == 0:# 1*1
            if a =! 0 and lst_solve[x][y] == 0:
                lst_solve[x][y] = 1
                solve(a-1,b,lst_solve,)
    print(h, w)


h, w, a, b = map(int, input().split())
lst = [[0 for _ in range(w)] for _ in range(h)]
print(solve(a, b, lst,0,0))
