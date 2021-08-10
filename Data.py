import csv 
import math

with open('Data.csv',newline='')as f:
     reader=csv.reader(f)
     file_data=list(reader)

data=file_data[0]
#finding meme
def mean(data):
    n=len(data)
    total=0
    for x in data:
        total+=int(x)
    mean=total/n
    return mean

#squaring 
square_list=[]
for number in data:
    a=int(number)-mean(data)
    a=a**2
    square_list.append(a)

sum=0
for i in square_list:
    sum=sum+i

result=sum/(len(data)-1)
STD_devetion=math.sqrt(result)
print(STD_devetion)

