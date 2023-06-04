import colorama, random
from colorama import Fore
colorama.init(autoreset = True)
num_rows = 30
colors = [Fore.RED,Fore.YELLOW,Fore.GREEN,Fore.BLUE,Fore.MAGENTA]
for i in range(0, num_rows):
    for j in range(0, num_rows-i-1):
        print(end=" ")
    for j in range(0,i+1):
        print(random.choice(colors) +"#", end=" ")
    print()
print(Fore.BLACK+"                         ",random.choice(colors)+"# "+random.choice(colors)+"# "+random.choice(colors)+"# "+random.choice(colors)+"# "+random.choice(colors)+"#")
print(Fore.BLACK+"                         ",random.choice(colors)+"# "+random.choice(colors)+"# "+random.choice(colors)+"# "+random.choice(colors)+"# "+random.choice(colors)+"#")
print(Fore.BLACK+"                         ",random.choice(colors)+"# "+random.choice(colors)+"# "+random.choice(colors)+"# "+random.choice(colors)+"# "+random.choice(colors)+"#")