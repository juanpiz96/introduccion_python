'''
int
float
str
list => array mutable list
tupl => array inmutable
dict => objetos
'''
numero1 = 10 # int 
numero2 = 15.5 # float
nombre = 'juan' # str 
# lsitas o arreglos => []
materias = ['base de datos II', 'lenguaje de 4 generacion']
lsitaNumeros = [0,1,2,3,4,5,6]
matrizEmpleo = [[1,2],[3,4]]
materias[0]= 'programacion avanzada'
print(materias[0])
print(matrizEmpleo [1][0])
print(materias[0], materias[1])
print(matrizEmpleo)
listasSinOrdenar = [10,15,2,-5,35]
print(listasSinOrdenar)
listasSinOrdenar.sort(reverse=True)
print(listasSinOrdenar)
# Tuplas => lista  inmutable => ()
dias = ('lunes','martes ', 'miercoles','lunes')
print(dias[2])
# dias[2]= 'jueves' esto no se puede realizar
# bolean
esCorrecto = True 
esCorrecto = False
print(len(materias))
print(len(dias))
print(dias.count('lunes'))
# dict => {}
persona = {
    'nombre': 'juan pablo',
    'apellido': 'garcia',
    'edad': 25,
    'materias':['basse de datos', 'lenguaje de cuarta'],
    'direccion': {
        'direcion': 'barrio centro',
        'ciudad': 'mocoa',
        'pais': 'colombia'
    }  
    

}
persona['apellido']='solarte'
print(persona['apellido'])
print(persona['materias'][1])
print(persona['direccion']['pais'])
persona['nombre_completo']=persona['nombre']+ ' '+persona['apellido']
print(persona)
# ciclos For
for materia in materias :
    print('este codigo pertenece al ciclo')
    print('este tambien pertenece al ciclo')
    print(materia)
print('este codigo no pertenece al ciclo')
'''
operadores aritmrticos
+
-
*
/
%
**
'''
'''
operadores logiocos
and
or
not
'''
'''
operadores relacionales
<
>
==
>=
<=
!=
'''
if 10 < 20 and 5 < 18:
    print('se cumple la condicion')
elif 5 <21:
    print('se cumple el elif')
elif 6>2:
    print('se cumple el segundo elif')
else:
    print('la condicion no se cumplio')
#Imput 
print('como te llamas?')
nombre= input()
print('bienvenido',nombre)
