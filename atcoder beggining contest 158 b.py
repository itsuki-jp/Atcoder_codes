n, blue, red = map(int, input().split())

number = n // (blue + red)          #セットの数を数える
count_blue = number * blue          #セットの中に青が何個あるか
number2 = n - number * (blue + red) #セットの余り
if blue ==0:
    print("0")
    exit()
if number2 > blue:
    count_blue += blue
else:
    count_blue += number2

print(count_blue)




