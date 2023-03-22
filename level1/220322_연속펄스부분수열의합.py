def solution(sequence):
    arr1 =[sequence[0]*(-1)]
    arr2 =[sequence[0]]
    seq1 = [-1,1]*len(sequence)
    seq2 = [1,-1]*len(sequence)
    for i in range(1,len(sequence)):
        arr1.append(max(arr1[i-1]+sequence[i]*seq1[i],sequence[i]*seq1[i]))
        arr2.append(max(arr2[i - 1] + sequence[i] * seq2[i], sequence[i] * seq2[i]))

    return max(max(arr1),max(arr2))

solution([2, 3, -6, 1, 3, -1, 2, 4])