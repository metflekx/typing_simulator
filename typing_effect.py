import sys
from time import sleep
from termcolor import colored, cprint

cprint("================", "red")
cprint("typing simulator", "red")
cprint("================", "red")

path = input("enter the absolute path or drag and drop the document here : ").strip()
speed = 0;

while speed < 1 or speed > 10 :
    speed = int(input("enter the speed on the scale of 1 to 10 (smaller is faster) : "))


f = open(path, "r")
color = "light_blue"
is_long_comment = 0;

for x in f:
    cprint("-",end="    ")

    for i in range(len(x)):
        if x[i] == '/' and x[i+1] == '/':
            color = "light_red"
        elif x[i] == '/' and x[i+1] == '*':
            color = "light_red"
            is_long_comment = 1;
        elif x[i] == '*' and x[i+1] == '/':
            is_long_comment = 0;

        sleep(speed/100)
        sys.stdout.write(colored(x[i], color))
        sys.stdout.flush()

    sleep((speed/100) * 5)
    if not is_long_comment: 
        color = "light_blue"

sleep(2)

print(":wq")

sleep(4)

f.close()
