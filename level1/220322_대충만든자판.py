def solution(keymap, targets):
    answer = []
    keyword ={}
    for key in keymap:
        for i,k in enumerate(key):
            if keyword.get(k)!=None:
                keyword.update({k:min(keyword.get(k),i+1)})
            else:
                keyword.update({k:i+1})
    for tar in targets:
        result =0
        for t in tar:
            if keyword.get(t)!=None:
                result+=keyword.get(t)
            else:
                result=-1
                break
        answer.append(result)
    return answer

solution(["ABACD", "BCEFD"],["ABCD","AABB"])
solution(["AA"],["B"])
solution(["AGZ", "BSSS"],["ASA","BGZ"])