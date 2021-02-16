#배열 array의 i번째 숫자부터 j번째 숫자까지 자르고 정렬했을 때, k번째에 있는 수를 구하려 합니다.

#나의답

def solution(array, commands):
    result = []
    for i in commands:
        new_arr = sorted(array[i[0]-1:i[1]])
        result.append(new_arr[i[2]-1])
    return result
    
#파이썬의 장점을 살린 정답

def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))
    
#map을 사용해서 append역할을 하고 labmda 함수를 통해 for문을 사용하지 않아도 되는 효율성을 보임
