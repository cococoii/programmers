# 내가 한 풀이 -- 너무 비효율적임
# def solution(n, m, section):
#     answer = 0
#     sec = [True]*(n+1)
#     for i in section:
#         sec[i]=False
#     index = section[0]
#     while index<n+1:
#         if not sec[index]:
#             answer+=1
#             index+=(m-1)
#         index+=1
#     return answer

#이런식으로 풀면 n을 쓸일이 없음
def solution(n, m, section):
    answer = 1
    prev = section[0]
    #section안 숫자가 m보다 큰 경우 answer+1 하기
    for sec in section:
        if sec - prev >= m:
            prev = sec
            answer += 1

    return answer


print(solution(8,4,[2,4,6]))
print(solution(5,4,[1,3]))