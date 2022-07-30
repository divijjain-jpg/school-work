while True:
    print('1 for addition','2 for sub','3 for div','4 for multiplication')
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
