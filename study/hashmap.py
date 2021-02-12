#완주하지 못한 선수
def solution(participant, completion):
    hashM = dict()
    for i in participant:
        if not i in hashM.keys():
            hashM[i] = 1
        else:
            hashM[i] += 1
    for j in completion:
        hashM[j] -= 1

    for a in hashM.keys():
        if(hashM[a]==1):
            return a
       
