def solution(N):
    
    binary_rep = bin(N)[2:]

    gaps = binary_rep.strip('0').split('1')

    return max(len(gap) for gap in gaps)

print(solution(55))
