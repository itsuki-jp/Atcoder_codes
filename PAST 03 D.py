n = int(input())
s = [input() for _ in range(5)]
ans = []
num8 = ["###","#.#","###","#.#"]
num9 = ["###","#.#","###","..#"]
num0 = ["###","#.#","#.#","#.#"]
num2 = ["###","..#","###","#.."]
num3 = ["###","..#","###","..#"]
num7 = ["###","..#","..#","..#"]
num5 = ["###","#..","###","..#"]
num6 = ["###","#..","###","#.#"]
nun4 = ["#.#","#.#","###","..#"]
num1 = [".#.","##.",".#.",".#."]
for i in range(1,n+1):
    if s[0][4*i-3:4*i] == "###":
        if s[1][4*i-3:4*i] == "#.#":
            if s[2][4*i-3:4*i] == "###":
                if s[3][4*i-3:4*i] == "#.#":
                    ans.append("8")
                else:
                    ans.append("9")
            else:
                ans.append("0")
        elif s[1][4*i-3:4*i] == "..#":
            if s[3][4*i-3:4*i] == "#..":
                ans.append("2")
            elif s[2][4*i-3:4*i] == "..#":
                ans.append("7")
            else:
                ans.append("3")
        else:
            if s[3][4*i-3:4*i] == "..#":
                ans.append("5")
            else:
                ans.append("6")
    else:
        if s[0][4*i-3:4*i] == "#.#":
            ans.append("4")
        else:
            ans.append("1")
print("".join(ans))
