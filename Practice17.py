'''
Date: 2021-04-18 18:42:55
LastEditors: GC
LastEditTime: 2021-04-22 10:36:22
FilePath: \Python Work\.vscode\Python Practice100\Practice17.py
'''
# Practice 17:
    # --> Write a program that computes the net amount of a bank account based a transaction log from console input. 
    #     The transaction log format is shown as following:

    #     D 100
    #     W 200
        
    #     D means deposit(存款) while W means withdrawal(提款).
    #     Suppose the following input is supplied to the program:

    #     D 300
    #     D 300
    #     W 200
    #     D 100
    #     Then, the output should be:

    #     500


# Solution 1:
# total = 0
# while True:
#     s = input().split()
#     if not s:   
#         break
#     cm, num = map(str, s)

#     if cm == "D":
#         total += int(num)
#     if cm == "W":
#         total -= int(num)
# print(total)


# Solution 2:
# lst = []
# while True:
#     s = input()
#     if len(s) == 0:
#         break
#     lst.append(s)

# balance = 0
# for i in lst:
#     if "D" in i:
#         balance += int(i.strip("D "))
#     if "W" in i:
#         balance -= int(i.strip("W "))
# print(balance)


# Solution 3:
# account = 0
# while True:
#     action = input("Deposit/Whitdrow/Balance/Quit? D/W/B/Q: ").lower()
#     if action == "d":
#         deposit = input("How much would you like to deposit? ")
#         account = account + int(deposit)
#     elif action == "w":
#         withdrow = input("How much would you like to withdrow? ")
#         account = account - int(withdrow)
#     elif account == "b":
#         print(account)
#     else:
#         quit()


# Solution 4:
# lines = []
# while True:
#     loopInput = input()
#     if loopInput == "done":
#         break
#     else:
#         lines.append(loopInput)

# lst = list(int(i[2:]) if i[0] == "D" else -int(i[2:]) for i in lines)
# print(sum(lst))


# Solution 5:
# transactions = []

# while True:
#     text = input("< ")
#     if text:
#         text = text.strip("D ")
#         text = text.replace("W", "-")
#         transactions.append(text)
#     else:
#         break

# transactions = (int(i) for i in transactions)
# balance = sum(transactions)
# print(f"Balance is {balance}")


# Solution 6:
money = 0
while True:
    trans = input()
    if trans[0] == "D":
        money = money + int(trans[1])
    elif trans[0] == "W":
        money = money - int(trans[1])
    elif trans[0] == "":
        break
    print(f"Your current balance is {money}")

    