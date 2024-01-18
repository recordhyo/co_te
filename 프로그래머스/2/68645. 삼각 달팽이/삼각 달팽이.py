def solution(n):
    answer = []
    temp = [[0] * i for i in range(1,n+1)]
    num = 1
    x, y = 0, -1

    for i in range(n) :
        for j in range(i,n) :
            a = i % 3
            if a == 0 : y += 1
            elif a == 1 : x +=1
            elif a == 2 : y -=1; x -= 1
            
            temp[y][x] = num
            num += 1
    
    return [i for j in temp for i in j]