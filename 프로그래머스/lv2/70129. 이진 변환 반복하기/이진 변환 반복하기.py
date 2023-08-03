def solution(s):
    answer = []
    cnt = 0
    cnt0 = 0
    while (s.count("1")>=1) :
        cnt += 1
        cnt0 += s.count("0")
        if s.count("1")==1 :
            break
        else :
            s = str(bin(s.count("1")))[2:]
        
    answer = [cnt, cnt0]
    return answer