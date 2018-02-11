from operator import index
#This is my first python script. It will be a living script for a while, meaning I will add to it as I learn more and more things.
#John Adcock - Started on 1/30/2018 - age 26

print("---------------------------------------------------------------------------")
print("..................Start.................")
print("---------------------------------------------------------------------------")

fn = input("Enter your first name: ")
ln = input("Enter your last name: ")
num1 = int(input("Enter your favroite number: "))
num2 = int(input("Enter a random number: "))

print("---------------------------------------------------------------------------")
#LEARNING list
list1=[fn,ln,num1,num2]
print("These are all of your entries: " + str(list1))
print("Here is the second letter of your firstname: " + str(list1[0][1]))
print("These are all of your entries, again:")
print(list1[0])
print(list1[1])
print(list1[2])
print(list1[3])
print(list1*4)
list1[2]=list1[3]-list1[2]
num4=num1+num2
num5=num1-num2
list1.append(num4)
print("number of items in your list1: " + str(len(list1)))
Lst_Length = len(list1)
list1.insert(Lst_Length-2,num5)
##maxy = max(list1) (Will not work on list1s that are both STR and INT)
##print(str(max))
list1.reverse()
if fn=="John":
        print("list1 index of your first name: " + str(list1.index("John")))
print(list1)
list1.remove(num5)
print(list1)

print("---------------------------------------------------------------------------")
#LEARNING RANGE
interval=int(1)
if num1>num2:
    interval*=-1
    print(list(range(num1, num2, interval)))
elif num1<num2:
    print(list(range(num1, num2, interval)))
print("---------------------------------------------------------------------------")
#Learning more Loops

i = int(0)
count = len(list1)-1
while i <= count:
    print("List Item #" + str(i) + ": " + str(list1[i]))
    i += 1
print("-----")
for x in list1:  ## as you can tell.. The While loop above and the for loop here do the exact same thing. However the for loop si a million times easier/simple/shorter!
    print("List Item #" + str(list1.index(x)) + ": " + str(x))
print("-----")
for x in range(3):
    print(num1)

 
print("---------------------------------------------------------------------------")
print("This is your name: \"" + fn + " " + ln + "\"")
print("Your Name is so epic we are going to repeat it 10 times!")
print((fn + " " + ln + " ") * 10)

print("---------------------------------------------------------------------------")
#Showing the elif
if num1 > num2:
        print("Your favorite number (of "+str(num1)+") is larger than the random number you entered!")
elif num1 == num2:
        print("your numbers match!")
else:
        print("Your favorite number (of "+str(num1)+") is smaller than the random number you entered!")

print("---------------------------------------------------------------------------")
#showing the if else if
if fn != ln:
        print("Your names do not match!")
else:
        if fn == ln:
                print("Your names match!")

print("---------------------------------------------------------------------------")
#Learning if statments and while loops and boolean logic
if num1 != num2 and num1 > num2:
        print(str(num1)+" and "+str(num2)+" are not equal and "+str(num1)+" is larger than "+str(num2)+"!")
        num3=num1
        while num3:
                print("." * num3 + " " + str(num3))
                num3-=1
                if num3==num2:
                        print("." * num3 + " " + str(num2))
                        num3+=1
                        while num3<=num1:
                                print("." * num3 + " " + str(num3))
                                num3+=1
                        break
elif num1 != num2 and num1 < num2:
        print(str(num1)+" and "+str(num2)+" are not equal and "+str(num2)+" is larger than " +str(num1)+"!")
        num3=num1
        while num3:
                print("." * num3 + " " + str(num3))
                num3+=1
                if num3==num2:
                        print("." * num3 + " " + str(num2))
                        num3-=1
                        while num3>=num1:
                                print("." * num3 + " " + str(num3))
                                num3-=1
                        break
                                   
print("---------------------------------------------------------------------------")
if num1 != num2 and (num1 + 2 == 4 or num2 + 2 == 4):
        print("You've unlocked a easter egg!")
        print("---------------------------------------------------------------------------")
if num1 != num2:
        num3=num1
        while True:
                if num3 <= num2:
                        print(num3)
                        num3 += 1
                        continue
                break
        print("---------------------------------------------------------------------------")



        

print("---------------------------------------------------------------------------")             
print("...................End..................")
print("---------------------------------------------------------------------------")

      
