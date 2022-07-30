while True:
    ree=open('pyttt')
    consol=ree.read()
    print(consol)
    ree.close()

    sum=int(input("enter your choice"))

    if sum == 1:
        one=int(input("enter first number"))
        two=int(input('enter second number'))
        print(one+two)
        quitt=int(input('3 for quit and any number to repeat operation again'))
        if quitt == 3:
            break
            
    elif sum == 2:
        one=int(input("enter first number"))
        two=int(input('enter second number'))
        print(one-two)
        quittt = int(input('3 for quit and any number to repeat operation again'))
        if quittt == 3:
            break
            
    elif sum == 3:
        one=int(input("enter first number"))
        two=int(input('enter second number'))
        print(one//two)
        quittt = int(input('3 for quit and any number to repeat operation again'))
        if quittt == 3:
            break
            
    elif sum == 4:
        
        one=int(input("enter first number"))
        two=int(input('enter second number'))
        print(one*two)
        quittt = int(input('3 for quit and any number to repeat operation again'))
        if quittt == 3:
            break
            
    else:
        print("wrong number")
        quittttt = int(input('3 for quit and any number to repeat operation again'))
        if quittttt == 3:
            break
