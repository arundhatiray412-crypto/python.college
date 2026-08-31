  #calculator
num1=int(input("enter the first number:"))
num2=int(input("enter the second number:"))
add=num1+num2
sub=num1-num2
mul=num1*num2
div=num1/num2
print("sum is:",add)
print("subtraction is:",sub)
print("multiplication is:",mul)
print("division is:",div)

#odd even
num1=int(input("enter the number:"))
if(num1%2==0):
    print("the number is even")
else:
    print("the number is odd")    

#leap year  
year=int(input("enter year:"))
if(year%4==0) or (year%400==0) and (year %100!=0):
    print("the year is a leap year")
else:
    print("the year is not a leap year")    


#factorial
def factorial(num):
    fact=1 
    
    for i in range(1,num+1):
        fact *=i
    return fact
num=int(input("enter a no:"))
print(factorial(num))   

#isPrime(num)
def isPrime(num):
    for i in range(2,num):
        if(num %i==0):
            return False
        else:
            return True
print(isPrime(5))

#doSum(num)
def doSum(num):
    total=0

    while num>0:
        digit=num % 10 #num=123 now 123 % 10 = 3(remainder)
        total=total+digit
        num=num //10 #123//1o=12(last digit removed)
    return total

num=int(input("enter a number:"))
print(doSum(num))

#armstrong no
def checkArmstrong(num):
    original =num
    total=0
    while num>0:
        digit=num%10
        total=total+digit**3
        num=num // 10
    if total==original:
        print("armstrong no")
    else:
        print("not armstrong no ")
num=int(input("enter a no:"))
(checkArmstrong(num))    

#list and tuples
#Q WAP to create a list of 10 std name create another list which is having the mark of 10 std
name=["papiya","juhi","pradeepta","ritwika","dibiya","ram","sam","jon","nura","isha"]
marks=[91,83,94,93,93,98,74,73,63,93]
name.sort()
print(name)
marks.sort()
print(marks)

#Q find out the name of the std scoring max,min marks
name=["papiya","juhi","pradeepta","ritwika","dibiya","ram","sam","jon","nura","isha"]
marks=[91,83,94,93,93,98,74,73,63,93]
max_marks=max(marks)
min_marks=min(marks)

print("maximum:",max_marks)
print("student:", name[marks.index(max_marks)])
print("minumum:",min_marks)
print("student:",name[marks.index(min_marks)])

#Q problem based questions
marks=[90,92,93,94,88,38,57,93,74,93,67,87,67,87,97,37,83,67,55,89]
avg_marks=sum(marks) / len(marks)
print(avg_marks)
count=0
for i in marks:
    if i > avg_marks:
        count=count+1
print(count)
highest=0
for i in marks:
    if marks.count(i)> highest:
        highest=marks.count(i)
        answer=i
print(answer)        


#Q
name=("riya","tiya","piya","isha","rita","rupa","ishan","shan","sree","papiya","era","mun","moon","sun","nisha","aruhi","ritwika","juhi","yum","jon")
for i in name:
    print(i,name.count(i))

distinct=set(name)
print(distinct)
highest=0
for i in name:
    if name.count(i)> highest:
        highest=name.count(i)
        answer=i
print(answer)  

sort_nm=sorted(name)
print(sort_nm)

nm=input("enter a name:")
if i in name:
    print("name exist")
else:
    print("doesnt exist")  


#Q set
fruits={"jackfruit","apple","banana","pineapple","guava","papaya","watermelon","mango","orange","grapes"}
summerFruits={"mango","jamun","watermelon","peach"}
winterFruits={"orange","pomegranate","apple","guava","strawberry"}
print( fruits | summerFruits | winterFruits)
print(fruits & winterFruits)
print(summerFruits - fruits)
print((summerFruits & winterFruits)- fruits)
print("orange" in fruits)
 
if "pineapple" in fruits:
    print("present in fruits")
if "pineapple" in summerFruits:
    print("present in summerFruits")
if "pineapple" in winterFruits:
    print("present in winterFruits")


#Qdictionary
employee={
    "emp1":{
        "empName":"riya",
        "designation":"manager",
        "department":"hr",
        "salary":90000
    },
    "emp2":{
        "empName":"priya",
        "designation":"developer",
        "department":"it",    
        "salary":40000
    },
    "emp3":{
        "empName":"isa",
        "designation":"analyst",
        "department":"finance",
        "salary":80000
        },
    "emp4":{
        "empName":"shan",
        "designation":"engineer",
        "department":"production",
        "salary":20000
        },
    "emp5":{
        "empName":"ishan",
        "designation":"tester",
        "department":"qa",
        "salary":50000
        }
}
print(employee["emp1"])
print(employee["emp4"]["department"])

max_salary=0
max_emp=""

for emp in employee:
    if employee[emp]["salary"]>max_salary:
        max_salary=employee[emp]["salary"]
        max_emp=emp
print(employee[max_emp])

employee["emp6"]={
        "empName":"isha",
        "designation":"tester",
        "department":"qa",
        "salary": 90000
        }
print(employee)

#lembda
student={
    101:{"name":"papiya","dept":"cse","marks":98},
    102:{"name":"priya","dept":"bba","marks":83},
    103:{"name":"riya","dept":"bca","marks":65},
    104:{"name":"juhi","dept":"cse","marks":68},
    105:{"name":"isha","dept":"bba","marks":48}
}
print("record highest to lowest")
for i in sorted(student.items(),key=lambda x:x[1]["marks"],reverse=True):
    print(i)

highest=max(student.items(),
            key=lambda x:x[1]["marks"])
print("\nhighest marks student:")
print(highest)

marks=list(map(lambda x: x["marks"],student.values()))
avg=sum(marks)/len(marks)
print("AVERAGE MARKS=",avg)


print("student scored above avg")

for roll in student:
    if student [roll]["marks"]>avg:
        print(student[roll])


#string
str="python programming"
print(str)

print(str.find("java"))

if "java" not in str:
    str += "java"
print(str)    

print(len(str))

print(len(str.split()))

print(str.title())

print(str.replace(" ",""))

print(str.count('a'))
print(str.count('p'))
print(str.count('r'))
print(str.count('m'))


#oops
class student:
    def __init__(self,name,dept,roll):
        self.name=name
        self.dept=dept
        self.roll=roll
    def show(self):
        print("name=",self.name) 
        print("dept=",self.dept)  
        print("roll=",self.roll)         
s1=student("ppii","cse",12)
s2=student("riya","cse",1)
s3=student("tiya","btbt",4)
s4=student("eraa","bca",8)
s5=student("isha","bba",23)

s1.show()
s2.show()
s3.show()
s4.show()
s5.show()



