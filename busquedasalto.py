import math
from numbers import Number

arr = None
x = None
n = None
list2 = None
index = None
salto = None
resultado = None
saltos = None

# Describe this function...
def do_something(arr, x, n):
  global list2, index, salto, resultado, saltos
  index = 0
  salto = 1
  saltos = math.floor(math.sqrt(n))
  if arr[0] == x:
    return [0, 0]
  while list2[int((min([saltos, n]) + 1) - 1)] < x:
    index = saltos
    saltos = (saltos if isinstance(saltos, Number) else 0) + round(math.sqrt(n))
    salto = (salto if isinstance(salto, Number) else 0) + 1
    if index >= n:
      return [-1, salto]
  while arr[int((index + 1) - 1)] < x:
    index = (index if isinstance(index, Number) else 0) + 1
    if index == min([saltos, n]):
      return [-1, salto]
  if arr[int((index + 1) - 1)] == x:
    return [index, salto]
  return [-1, salto]

def text_prompt(msg):
  try:
    return raw_input(msg)
  except NameError:
    return input(msg)


list2 = '0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610'.split(',')
x = float(text_prompt('El numero que deseas encontrar: '))
resultado = do_something(list2, x, len(list2))
if resultado[0] >= 0:
  print(''.join([str(x2) for x2 in ['El numero: ', x, ' Se ha encontrado en la posición: ', resultado[0], ' Saltos: ', resultado[1]]]))
else:
  print(''.join([str(x3) for x3 in ['El numero: ', x, 'No se ha encontrado', ' Saltos: ', resultado[1], ' Tamaño del arreglo: ', len(list2)]]))