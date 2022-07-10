#NaengEnamul

import matplotlib.pyplot as plt
# import time
x=[]
count=[]
i = 0

def collatz(number):   #콜라츠 함수 만드는거 
    if number % 2 == 0:
        return number // 2
    elif number % 2 == 1:
        return number * 3 + 1
    else:
        print("없다")
        return None

number = 0
l_i = 0
mi=0
repeat_count=int(input("x에 대입할 숫자들(1~x까지) : "))

while mi != repeat_count:
    mi += 1
    number = mi
    while number != 1:
        i+=1
        number = collatz(number)
        x.append(number)
        count.append(i)
    plt.plot(count, x, "k-.")
    i = 0
    print(x)
    print(count)
    x.clear()
    count.clear()
    print("그래프 갯수 : ", mi)

plt.title("-Collatz conjecture-") #제목
plt.legend(["Number of Graphs : {}".format(mi)])    #그래프 갯수 나타내기
plt.xlabel("Count")
plt.ylabel("result")
plt.show()