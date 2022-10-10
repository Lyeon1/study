a=[0,1] # a=피보나치수열 첫 시작숫자 두개			
b=0 # b=추가할 인덱스 위치			
input_a=input("몇번쨰 피보나치 수까지 나타낼까요? 정수로 입력하세요.: ")			
input_a=int(input_a)			
if input_a <=2:			
    print("2보다 큰 정수를 입력하시오.")			
    exit()			
			
for c in a:			
    b+=1			
    d=(a[b-1]+a[b]) # 피보나치 수열 식			
    a.insert(b+1,d)			
    if b==input_a-2:			
        break			
print(a)			

# append나 insert함수를 이용해서 list를 추가하는 것은 파이썬의 구조상 느림. 그래서 리스트 반복연산자 사용시 빨라짐.

N=input("피보나치 수열의 몇번째 까지 나타낼지 양의 정수로 입력하시오. : ")
N=int(N)
a=[None]*(N+1)
if N<=0:
    print("0보다 큰 양의 정수를 입력하시오")
else:
    for n in range(1, N+1):
        if n==1:
            a[n]=0
        elif n==2:
            a[n]=1
        else:
            a[n]=a[n-2]+a[n-1]
    print(a[1:])

# 피보나치 수열의 위치값을 변환해주는 함수
# 5를 입력하면 5번째 피보나치 수열의 값이 나오도록
# 피보나치 수열: 0,1,1,2,3,5,8,13,21,.......
# fibo(5) -> 3 이 나와야 함.
# 재귀함수 사용
num=input("몇번째 피보나치 수를 나타낼지 입력: ")
num=int(num)
def fibo1(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibo1(n-1)+fibo1(n-2)
print(fibo1(num))

def fibo2(n):
    a=0
    b=1
    count=0
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        for i in range(1,n+1):
            if i < n:
                c=a+b
                a=b
                b=c
                i+=1
    return a
print(fibo2(num))
