# while condition:
#     answer = input("Do you want to stop?: y/n")
#     if answer == 'y':
#         condition = False
#     elif answer == 'n':
#         print("Okay!")
#     else:
#         print("I don't understand")
for index in range(1000, 1100):
    if index % 2 == 0:
        print(str(index)+" is even!")
