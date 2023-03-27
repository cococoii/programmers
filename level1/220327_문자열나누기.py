def solution(s):
    answer = 0
    f = s[0]
    eq = 1
    neq = 0

    for i in range(1,len(s)):
        if f==s[i]:#같은 경우
            eq+=1
        else:#다른 경우
            neq+=1
        if eq==neq:
            answer+=1
            if i!=len(s)-1:
                f= s[i+1]
            eq =0
            neq = 0
        if i==len(s)-1 and eq!=neq:
            answer+=1
    #'a'인 경우 > answer=1로 나오게 만들기
    if len(s)==1:
        answer+=1
    return answer

print(solution('a'))
print('------')
print(solution('banana'))
print('------')
print(solution('abracadabra'))
print('------')
print(solution('aaabbaccccabba'))
