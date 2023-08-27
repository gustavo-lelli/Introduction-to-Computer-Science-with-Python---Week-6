col=int(input("digite a largura: "))
rows=int(input("digite a altura: "))

i=1
j=1

while(i<=rows):
    j=1
    if(i==1 or i==rows):
        while(j<=col):
            print("#", end="")
            j+=1
    else:
        j=2
        print("#", end="")
        while(j<col):
            print(" ", end="")
            j+=1
        print("#", end="")
    i+=1
    print()
