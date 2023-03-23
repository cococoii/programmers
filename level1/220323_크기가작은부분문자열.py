def solution(t, p):
    answer = 0
    p_l = len(p)
    for i in range(len(t)-p_l+1):
        if int(t[i:i+p_l])<=int(p):
            answer+=1
    return answer

solution("3141592","271")
solution("500220839878","7")
solution("10203","15")