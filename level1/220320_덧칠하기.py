def solution(n, m, section):
    answer = 0
    sec = [True]*(n+1)
    for i in section:
        sec[i]=False
    index = section[0]
    while index<n+1:
        if not sec[index]:
            answer+=1
            index+=(m-1)
        index+=1
    return answer

print(solution(8,4,[2,4,6]))
print(solution(5,4,[1,3]))