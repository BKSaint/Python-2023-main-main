# dolist = open('to.txt', 'w+')

# todos = []
# counter = 0
# prompt = input("Do you want to make a to-do list? Yes or No: ")
# while prompt != "end":
#     if prompt == "No":
#         break
#     elif prompt == "Yes":
#         amount = int(input("How many thingssss do you want to add: "))
#         while amount < 0:
#             amount = int(input("How many things do you want to add: "))
#             if amount < 0: #User Error
#                 print("Invalid Answer")
#                 amount = int(input("How many things do you want to add: "))
#             else: 
#                 break
#     while amount > 0:
#         counter += 1
#         dolist.writelines(input(str(counter) + ": ") + "\n")
#         amount -= 1
#         prompt = "end"
# else:
#     print("This is your to-do list")
#     dolist = open('to.txt')
#     content = dolist.readlines()
#     for lines in content:
#         print(lines, end="")


   