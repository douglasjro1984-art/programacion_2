
#TUPLAS
tupla=(1,2,3)
print(tupla)#(1,2,3)

tupla = 1, 2, 3 # Los parentesis son opcionales 
print(type(tupla)) # class 'tuple'
print(tupla) #(1,2,3)

lista_tupla=[(1,2),(3,4),(5,6)]

t=(1) # esto no es una tupla
print(type(t))
print(t)

tupla_b=(1,) #hay que añadir , al final para indicar que es tupla de 1 elemento 
print(type(tupla_b))
print(tupla_b)

tupla=(1,2,3)#tupla[0]=5 # Error ! typeError

tupla = 1,2,('a','b'),3
print(tupla)
print(tupla[2][0])#(1,2,('a','b'),3)
print(tupla[2][0])#a

lista = [1,2,3]
tupla=tuple(lista)
print(type(tupla))#<class 'tuple'>
print(tupla) #(1,2,3)

tupla=[1,2,3]
for t in tupla:
    print(t)#1,2,3
    
tupla_c =(1,2,3)
x,y,z=tupla_c
print(x,y,z)#1,2,3

#MÉTODOS TUPLAS
#count(<obj>)
tupla_d = [1,1,1,3,5]
print(tupla_d.count(1))#3

#index(<obj>[,index])

tupla_e = [7,6,7,3,5]
print(tupla_e.index(6))

#Diccionario 

d1 = {
    "Nombre": "Sara",
    "Edad": 27,
    "Documento":1003882
}
print(d1)

d2 = dict([
    ("Nombre", "Sara"),
    ("Edad", 27),
    ("Documento", 1003882),
])
print(d2)

d3 = dict(Nombre= 'Sara',
    Edad= 27,
    Documento= 1003882,)
print(d3)

diccionario_auto = {
    "marca": "Ford",
    "electrico": False,
    "año": 1964,
    "color": ["red","white","blue"]
}

print(diccionario_auto)

#Acceder

d1 ={
   "Nombre": "Sara",
   "Edad": 27,
   "Documento":1003882
}
print(d1['Nombre']) # sara
print(d1.get('Nombre'))#sara

#modificar
d1 ={
   "Nombre": "Sara",
   "Edad": 27,
   "Documento":1003882
}
d1['Nombre']= "Laura"
print(d1)

#agregar

d1 ={
   "Nombre": "Sara",
   "Edad": 27,
   "Documento":1003882
}
d1['Dirección']= "calle 123" 
print(d1)

#iterar diccionario 

