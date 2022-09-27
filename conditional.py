user_answer = int(input("Enter a number between 1 and 100: "))

if user_answer > 90 and user_answer < 100:
    print("A")
elif  user_answer >= 80:
    print("B")
elif  user_answer >= 70:
    print("C")
elif  user_answer >= 60:
    print("D")
elif  user_answer < 60:
    print("F")
