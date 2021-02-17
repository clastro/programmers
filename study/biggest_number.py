#배열에 숫자가 주어져 있고 숫자를 조합해서 가장 큰 수를 만드는 함수

#예제만 통과하고 시간이 초과된 잘못된 코드
from itertools import permutations
import re
def solution(array):
    perm = list(permutations(array,len(array)))
    num_list = [''.join(re.findall('\d+', str(i))) for i in perm ]
    num_list = list(map(int, num_list))
    result = str(max(num_list))
    return result
