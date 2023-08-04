def solution(strings, n):
    answer = []
    str1 = []
    for i in strings :
        str1.append(i[n]+i)
    str1.sort()
    return [i[1:] for i in str1]