import time
import os
from colorama import Fore

"""
1.El problema del caballo consiste en averiguar el camino que un caballo de ajedrez debe seguir para recorrer todo el tablero empezando desde una casilla cualquiera y 
sin volver a tocar la misma casilla 2 veces
"""
while True:
    x=int(input("Ingrese la posición inicial del caballo en X "))+1
    y=int(input("Ingrese la posición inicial del caballo en Y "))+1

    if x<2 or x>9 or y<2 or y>9:
        print("Ingrese una posicion valida del tablero de ajedrez 8x8\n")
    else:
        break

tab =  [[99,99,99,99,99,99,99,99,99,99,99,99],
        [99,99,99,99,99,99,99,99,99,99,99,99],
        [99,99,2,3,4,4,4,4,3,2,99,99],
        [99,99,3,4,6,6,6,6,4,3,99,99],
        [99,99,4,6,8,8,8,8,6,4,99,99],
        [99,99,4,6,8,8,8,8,6,4,99,99],
        [99,99,4,6,8,8,8,8,6,4,99,99],
        [99,99,4,6,8,8,8,8,6,4,99,99],
        [99,99,3,4,6,6,6,6,4,3,99,99],
        [99,99,2,3,4,4,4,4,3,2,99,99],
        [99,99,99,99,99,99,99,99,99,99,99,99],
        [99,99,99,99,99,99,99,99,99,99,99,99]
        ]

for i in range(64):

    tab[x][y]="C"
    lista=[]
    try:
        tab[x+2][y-1]-=1
        lista.append(tab[x+2][y-1])
    except:
        pass
    try:
        tab[x+2][y+1]-=1
        lista.append(tab[x+2][y+1])
    except:
        pass
    try:
        tab[x-2][y+1]-=1
        lista.append(tab[x-2][y+1])
    except:
        pass
    try:
        tab[x-2][y-1]-=1
        lista.append(tab[x-2][y-1])
    except:
        pass
    try:
        tab[x+1][y-2]-=1
        lista.append(tab[x+1][y-2])
    except:
        pass
    try:
        tab[x-1][y-2]-=1
        lista.append(tab[x-1][y-2])
    except:
        pass
    try:
        tab[x+1][y+2]-=1
        lista.append(tab[x+1][y+2])
    except:
        pass
    try:
        tab[x-1][y+2]-=1
        lista.append(tab[x-1][y+2])
    except:
        pass
    
    for m in range(2,10):
        for n in range(2,10):
            if tab[m][n] == "C":
                print(Fore.RED,tab[m][n]," ",end="")
            else:
                print(Fore.WHITE,tab[m][n]," ",end="")
        print("")
    print("")
    try:
        menor=min(lista)
    except:
        pass
    del lista
    time.sleep(1)
    tab[x][y]=str(i+1)
    os.system('cls')
    if tab[x+2][y-1] == menor:
        x+=2
        y-=1
    elif tab[x+2][y+1] == menor:
        x+=2
        y+=1
    elif tab[x-2][y+1] == menor:
        x-=2
        y+=1
    elif tab[x-2][y-1] == menor:
        x-=2
        y-=1
    elif tab[x+1][y-2] == menor:
        x+=1
        y-=2
    elif tab[x-1][y-2] == menor:
        x-=1
        y-=2
    elif tab[x+1][y+2] == menor:
        x+=1
        y+=2
    elif tab[x-1][y+2] == menor:
        x-=1
        y+=2
for m in range(2,10):
    for n in range(2,10):
        print(tab[m][n]," ",end="")
    print("")