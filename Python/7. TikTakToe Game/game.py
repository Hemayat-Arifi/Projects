# TODO: _______________________________ Empty Cells


USER1 = "X"
USER2 = "O"


a = " "   # a 0
b = " "   # b 0
c = " "   # c 0
a1 = " "  # a 1
a2 = " "  # a 2
b1 = " "  # b 1
b2 = " "  # b 2
c1 = " "  # c 1
c2 = " "  # c 2


# TODO: _____________________________ The TIC TAK TOE Map

print("")

_map = f"""
  a    b    c
   {a} | {b} | {c}     0
---------------
   {a1} | {b1} | {c1}     1  
---------------
   {a2} | {b2} | {c2}     2

"""

print(_map)
print("")

# TODO: ____________________________ Functions


# TODO: ____________________________ The Game Loop

is_on = True

while is_on:

    user1 = input("Player 1:- Which Column & Row you want to go for?\nColumns --> (a, b, c) rows --> (0, 1, 2) eg:- b 0"
                  " \n")

    # logical conditions --> (a 0)(a 1)(a 2)(b 0)(b 1)(b 2)(c 0)(c 1)(c 2)
    if user1.lower() == "a 0":
        a = USER1
    elif user1.lower() == "a 1":
        a1 = USER1
    elif user1.lower() == "a 2":
        a2 = USER1
    elif user1.lower() == "b 0":
        b = USER1
    elif user1.lower() == "b 1":
        b1 = USER1
    elif user1.lower() == "b 2":
        b2 = USER1
    elif user1.lower() == "c 0":
        c = USER1
    elif user1.lower() == "c 1":
        c1 = USER1
    elif user1.lower() == "c 2":
        c2 = USER1
    else:
        print("Wrong Input (a 2)")

    _map = f"""
           {a} | {b} | {c}
        ---------------
           {a1} | {b1} | {c1}  
        ---------------
           {a2} | {b2} | {c2}
        """

    print(_map)

    user2 = input("Player 2 :- Which Column & Row you wanna insert\nColumns --> (a, b, c) rows --> (0, 1, 2) eg:- b 0 "
                  "\n")

    # logical conditions --> (a 0)(a 1)(a 2)(b 0)(b 1)(b 2)(c 0)(c 1)(c 2)
    if user2.lower() == "a 0":
        a = USER2
    elif user2.lower() == "a 1":
        a1 = USER2
    elif user2.lower() == "a 2":
        a2 = USER2
    elif user2.lower() == "b 0":
        b = USER2
    elif user2.lower() == "b 1":
        b1 = USER2
    elif user2.lower() == "b 2":
        b2 = USER2
    elif user2.lower() == "c 0":
        c = USER2
    elif user2.lower() == "c 1":
        c1 = USER2
    elif user2.lower() == "c 2":
        c2 = USER2
    else:
        print("Wrong Input (a 2)")

    _map = f"""
           {a} | {b} | {c}
        ---------------
           {a1} | {b1} | {c1}  
        ---------------
           {a2} | {b2} | {c2}
        """

    print(_map)

