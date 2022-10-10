#리스트 내포 List comprehension
#An=2n+1 (0<=n<10)
# #A={1,3,5,7,9,...,19}
A=[]
for i in range(0,10):
    A.append(2*i+1)
print(A) #[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# 위처럼 전형적인 코드를 간단하게 입력할 수 있게 해주는게 리스트 내포
# 기본적인 형태는 [표현식 for 반복자 in 반복할 수 있는것 if 조건문]
# 순서는 위처럼 표현식 반복자 조건문 형태로 와야함.

A=[2*i+1 for i in range(0,10)]
print(A) #[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

A=[2*i+1
for i in range(0,10)
if i%2==0]
print(A) # i가 짝수일때만 리스트에 추가해라

array=["사과","자두","초콜릿","바나나","체리"]
output=[fruit for fruit in array if fruit !='초콜릿']
# for fruit in array    에서 array라는 리스트에서 반복시킬 반복자 fruit를 생성하고
# if fruit != '초콜릿'   에서 조건을 만들고
# 맨앞의 fruit라는 형태로 output이라는 리스트에 추가하겠다.
print(output) #['사과', '자두', '바나나', '체리']
# 위 아래 코드는 서로 같은걸 나타낸다
output=[]
for fruit in array:
    if fruit !="초콜릿":
        output.append(fruit)
print(output) #['사과', '자두', '바나나', '체리']

#-------------------------------
 
output=[a for a in range(1,100+1) if "{:b}".format(a).count("0") == 1]

# output=[]
# for a in range(1,101):
#     if ("{:b}".format(a)).count("0") == 1:
#         output.append(a)

for i in output:
    print("{} : {}".format(i,"{:b}".format(i)))
print("합계:", sum(output))