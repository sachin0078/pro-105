import csv
import math

with open("sd.csv",newline="")as f:
    reader=csv.reader(f)
    file_data=list(reader)

data=file_data[0]
n=len(data)

def mean(data):
    sum=0
    for i in data:
        sum=sum+int(i)
    mean=sum/n
    return mean

sqList=[]
for i in data:
    num=int(i)-mean(data)
    num=num**2
    sqList.append(num)

total=0
for i in sqList:
    total=total+i

result=total/n

sd=math.sqrt(result)

print(sd)



