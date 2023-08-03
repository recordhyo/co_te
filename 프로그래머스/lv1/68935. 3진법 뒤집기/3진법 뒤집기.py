def solution(n):
    string = []
    answer = 0
    while(n > 0) :
        string.append(str(n%3))
        n = int(n/3)
    answer = int(''.join(string),3)
    return answer