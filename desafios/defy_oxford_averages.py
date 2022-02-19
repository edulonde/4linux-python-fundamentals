# Averages
# Make a program that asks the user for a series of numbers until they either want to output the average or quit the program.
# Extensions:
# 1. Expand the program to print the median and mode averages also
# 2. Include options so that if the user wants to, they can save their list of numbers to a text file and read them back out later on

import statistics

list = []

def menu():
    control = 1
    while control:
        n = input("enter a number or press 'q' to quit: ")
        if n == 'q':
            control = 0
        else:
            list.append(float(n))


menu()

list_sorted = sorted(list)


print(list_sorted)
average = statistics.mean(list_sorted)
median = statistics.median(list_sorted)
format_average = "{:.2f}".format(average)
mode = statistics.multimode(list_sorted)

print(f"the average is {format_average}, the median is {median} and the mode is {mode}")

save = input("Do you want to save the list in a file? (y/n)")
if save.lower() == 'y':
    f = open("list_average.txt", "w")
    f.write(f"The list: {list_sorted} \n"
            f"the average is {format_average}, the median is {median} and the mode is {mode}")
    f.close()
elif save.lower() == 'n':
    exit()
else:
    print("invalid choice")


