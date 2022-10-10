# 로또는 1부터 45까지 중복되지 않는 숫자 중 6개 뽑음
# 순서가 상관없음

a=1

for i in range(0,6):
        a*=(45-i)
print(a)

# 5864443200
# 하지만 이 경우에는 숫자가 같아도 순서가 다르면 다른걸로 침
# ---------------------------------------------------------------------------
a=0
for n1 in range(1,46):
    for n2 in range(n1+1,46):
        for n3 in range(n2+1,46):
            for n4 in range(n3+1,46):
                for n5 in range(n4+1,46):
                    for n6 in range(n5+1,46):
                        a+=1
print(a)
# 재귀함수 사용
# 8145060
#----------------------------------------------------------------------------------
from itertools import *
a=list(range(1,45+1))
b=list(combinations(a,6))
print(len(b))