import random
import os
def rolldice():
    dice = []
    for i in range(2):
        dice.append(random.randrange(1,6))
    return dice
def totalvalues(x):
    count = 0
    print(x)
    for i in x:
        count += i
    return count

def writetofile(x,values):
    try:
        if x == "----------------- new game begins here --------------":
            fw = open('ans.txt', 'a')
            fw.write("----------------- new game begins here --------------\n\n")
            fw.close()
        else:
            if not os.path.exists("ans.txt"):
                fw = open("ans.txt", 'w')
            fw = open('ans.txt', 'a')
            fw.write("Dice values\n")
            fw.write(" ".join(str(i) for i in values) + "\n")
            fw.write("Result " + x + "\n")
            fw.close()
    except:
        print("File Cant be created")


def newroll(firstroll):
    try:
        print("You will have to roll again")
        l="You lose the game"
        w="You won the game"
        roll = int(input("Do you wish to roll dice: \n 1.Yes \n 2.No \n"))
        if roll==1:
            new_values = rolldice()
            new_sum_values = totalvalues(new_values)
            if new_sum_values == 7:
                print(l)
                writetofile(l, new_values)
            elif new_sum_values == firstroll:
                print(w)
                writetofile(w, new_values)

            else:
                newroll(firstroll)
                writetofile(a, new_values)
    except:
        print("Please provide valid option")




roll = int(input("Do you wish to roll dice: \n 1.Yes \n 2.No \n"))
try:
    writetofile("----------------- new game begins here --------------",[])
    if roll == 1:
        l = "You lose the game"
        w = "You won the game"
        a = "You will have to roll again"
        values = rolldice()
        sum_values = totalvalues(values)
        if sum_values == 7 or sum_values == 11:
            print(w)
            writetofile(w, values)
        elif sum_values == 2 or sum_values == 3 or sum_values == 12:
            print(l)
            writetofile(l, values)
        else:
            newroll(sum_values)
            writetofile(a, values)
except:
    print("Error")
