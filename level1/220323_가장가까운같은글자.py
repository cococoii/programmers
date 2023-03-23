def solution(s):
    answer = []
    word = {}
    for i,w in enumerate(s):
        if w not in word:
            answer.append(-1)
        else:
            answer.append(i-word[w])
        word[w] = i
    return answer

solution("banana")
solution("foobar")