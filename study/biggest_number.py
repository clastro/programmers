#배열에 숫자가 주어져 있고 숫자를 조합해서 가장 큰 수를 만드는 함수

#예제만 통과하고 시간이 초과된 잘못된 코드
#Permutation을 사용하면 시간이 너무 오래 걸림

from itertools import permutations
import re
def solution(array):
    perm = list(permutations(array,len(array)))
    num_list = [''.join(re.findall('\d+', str(i))) for i in perm ]
    num_list = list(map(int, num_list))
    result = str(max(num_list))
    return result

# 100점 중 27.3점 코드
# [40,403] 의 경우 40403이 되어야 하는데 40340이 되므로 수정이 필요하다

def solution(array):
    new_list = [i/10 if len(str(i)) == 2 else i/100 if len(str(i)) == 3 else i/1000 if len(str(i)) == 4 else i for i in array ]
    sorted_list = sorted(new_list,reverse=True)
    result = ''.join([str(elem) for elem in sorted_list]).replace('.','')
    return result


