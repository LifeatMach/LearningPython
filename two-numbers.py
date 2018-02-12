num1 = int(input("Enter a random number: "))
num2 = int(input("Enter a random number: "))
print("---------------------------------------------------------------------------")
if num1 != num2 and num1 > num2:
        print("Because "+str(num1)+" is larger than "+str(num2)+", this will produce a valley design!")
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
        print("Because "+str(num2)+" is larger than "+str(num1)+", this will produce a mountain design!")
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
