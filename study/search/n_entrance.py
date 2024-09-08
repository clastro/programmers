def solution(n, times):
    i = n-2
    answer = 0
    while(i>0):
        if (i%2 == 0):
            if(i == n-2):
                answer = times[0]
            else:
                answer += 2 * times[0] - times[1]
            
        else:
            answer += times[1] - times[0]
        i-=1
    return answer

# Failed
