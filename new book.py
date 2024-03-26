print("welcome to abbey bank")
p = int(input("please enter your 4 digit pin: "))
m = 20000
if p == 2000:
    print("1- Withdraw")
    print("2- Deposit")
    print("3- Transfer")
    print("4- check balance")
else:
    print("Sorry incorrect pin\nPlease try again")
    exit()

c = int(input("please choose transaction: "))
if c == 1:
    w = int(input("enter withdraw amount: "))
    diff = m - w
    if w < m:
        print("take your cash,\nNew balance is now", diff)
    else:
        print("invalid amount")
        exit()
elif c == 2:
    d = int(input("enter deposit amount: "))
    add = d + m
    print("deposit successfully\nYour balance is now", add)
elif c == 3:
    t = int(input("please enter recipient account number: "))
    if t == 10:
        b = input("bank name: ")
    else:
        print("invalid account number")
        exit()
    tm = int(input("please enter amount: "))
    dt = m - tm
    if tm < m:
        print("Transfer successfully\nBalance is now", dt)
    else:
        print("invalid amount")
if c == 4:
    print("Your account balance is", m)
