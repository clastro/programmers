def solution(wallet, bill):
    bill = sorted(bill)
    wallet = sorted(wallet)
    answer = 0
    while((wallet[0]<bill[0]) | (wallet[1]<bill[1])):
        print(answer)
        bill[1] = int(bill[1]/2)
        bill = sorted(bill)
        answer += 1
    return answer
