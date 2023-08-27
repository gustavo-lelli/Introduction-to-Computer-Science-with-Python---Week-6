col=int(input("digite a largura: "))
rows=int(input("digite a altura: "))

i=0
j=0

while(i<rows):
    j=0
    while(j<col):
        print("#", end="")
        j+=1
    i+=1
    print()
