def generate_fibonacci(num):
    lst=[0]
    num1=0
    num2=1
    for i in range(num-1):
        lst.append(num2)
        num1,num2=num2,num1+num2
    return lst
