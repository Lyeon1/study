def jud(a):
    while True:
        b=input("{}을 입력하시오. : ".format(a))
        b=b.strip()
        if bool(fun_3(b)) is True:
            return fun_3(b)
        else:
            print(f"{a}을/를 다시 입력하시오.")

def fun_3(a):
        try:
            if fun_4(a) >= 0:
                return float(a)
            else:
                print("0보다 큰 수를 입력하시오.", end=" ")
                return False
        except:
            return False

def fun_4(a):
    list_a=list(a)
    list_b=[]
    try:
        for i in list_a:
            if i=="." or i=="-":
                list_b.append(i)
            else:
                try:
                    list_b.append(int(i))
                except:
                    pass
        return float(("{}"*len(list_b)).format(*list_b))
    except:
        return False

a=jud("책값")
b=jud("할인율")
c=jud("배송료")

d=int(a-(a*(b/100))+c)

print("결제금액: {}원".format(d))
