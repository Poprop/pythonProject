# # #def happy_birthday() -> None:
# #
# #
# #     print("What's your name?:")
# #     name = (input())
# #     print (f'Happy birthday , {name}!')
# # #happy_birthday()
#
# def happy_birthday() -> None:
#  name = input("What's your name?:")
#  print(f'Happy birthday , {name}!')
#
#

# while True:
#   print("What number do you want to check?:")
#   user_manual_input = int(input())
#   user_input = user_manual_input % 2
#
#   if user_input == 0 or user_manual_input == 0:
#
#     print("odd")
#   else:
#       print("even")

# def parity_checker() -> None:
#     print("What number do you want to check?:")
#
#
# user_manual_input = int(input())
# user_input = user_manual_input % 2
#
# if user_input == 0 or user_manual_input == 0:
#
#     print("Odd")
# else:
#     print("Even")


def parity_checker() -> None:
    user_manual_input = int(input("What number do you want to check?:"))
    user_input = user_manual_input % 2
    if user_input == 0 or user_manual_input == 0:

        print("Odd")
    else:
        print("Even")




