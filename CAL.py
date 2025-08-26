def calculator():
    print("options= add,sub,mul,div")
    num1=float(input("enter your first value:" ))
    num2=float(input("enter your second value: "))
    operation=input("Enter operations: ")

    if operation =="add":
       result=num1+num2
    elif operation == "sub":
       result=num1-num2
    elif operation == "mul":
       result=num1*num2
    elif operation =="div":
       if num2 !=0:
           result=num1/num2
       else :
           print ("Not valid or division with zero")
           return
    else:
        print("invalid operation entered")
        return

    print("Result is :",result)
calculator()
