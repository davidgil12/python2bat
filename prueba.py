# lA FUNCION PRINT() IMPRIME POR PANTALLA
print("Hola Marina")
#  LA FUNCION INPUT PERMITE INTRODUCIR INFORMACION POR TECLADO
input()
#  

def(t,n,r,p):
    A=p*(1+r/n)**(n*t)
    return A
p= float(input("Capital Inicial"))
r= float(input("Interes anual en %"))
t= float(input("numero de años"))
n= float(input("numero de periodo por años"))

print(f("La cantidad final es el resultado de {t} y {n}"))
