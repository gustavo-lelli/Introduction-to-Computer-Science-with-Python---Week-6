import math

def eh_Hipotenusa(hip):
    i=1
    j=1
    
    while(i<=hip):
        j=1
        while(j<=hip):
            if((j*j)+(i*i)==(hip*hip)):
                return hip
            j+=1
        i+=1
    
    return 0

def soma_hipotenusas(n):
    soma=0
    hip=2
    
    while(hip<=n):
        soma+=eh_Hipotenusa(hip)
        hip+=1

    return soma
