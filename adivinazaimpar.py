#encoding:UTF-8
'''
Created on 03/03/2013

@author: Usuario
'''

def mostrar(jue):
    a=[]
    b=[]
    c=[]  
    for nom in range(len(jue)):
        
        if (nom+3)%3==0:
            a.append(jue[nom])
        if (nom+2)%3==0:
            b.append(jue[nom])
        if (nom+1)%3==0:
            c.append(jue[nom])
          
    for x in range(7):
        print a[x],'\t',b[x],'\t',c[x]
    print '=============='

    return a,b,c
    
def unir(j,k,l):
    union=j+k+l
    return union

def obtenerrespuesta(desto):
    decuantoes=len(desto)
    if decuantoes%2==0:
        print ''
        
#======Inicia=====   

juego=['z','h','j','t','p','ñ','q','s','c','w','r','l','d','f','v','e','i','b','u','o','k']
for op in range(3):
    b,n,m=mostrar(juego)
    opcion=input('En que gupo esta\n--->')
    if opcion ==1:
        juego=unir(n, b, m)
    if opcion==2:
        juego=unir(m,n,b)
    if opcion==3:
        juego=unir(n,m,b)
      
#obtenerrespuesta(juego)
print juego[10]

