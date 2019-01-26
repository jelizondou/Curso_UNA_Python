#Escribir un código en Python que imprima en pantalla lo siguiente: 
#* 3.1415926 ** 3.141592 *** 3.14159 **** 3.1415 ***** 3.141 ****** 3.14 
#usando el operador % para definir la cantidad de digitos decimales de PI y la cantidad de asteriscos. 

b = '*'
pi = 3.1415926
print ( '%s %.7f %s %.6f %s %.5f %s %.4f %s %.3f %s %.2f' %(b, pi,2*b,pi,3*b,pi,4*b,pi,5*b,pi,6*b,pi))