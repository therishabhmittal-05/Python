# print('Hello, World!!')
# a = input("What's your name??\n").strip().title()
# print ("hello", a, sep= "", end=" ")

# x = int(input("X:"))
# y= int(input ("Y:"))
# print(x+y)




# def Adder(x, y):    
#     print(f"{round(x + y):,}")

# Adder(x, y)

# x = float(input("Enter a number: "))
# y= float(input("Enter another number: "))
# if x > y or x < y:
#     print(f"{x} and {y} not equal")
# else: 
#     print(f"{x} and {y} are equal")

name = input("What's your name??\n").strip().title()

match name:
    case "Harry"| "Ron"| "Hermione":
        print("Gryfindor")
    case "Draco"| "Crabbe"| "Goyle":
        print("Slytherin")
