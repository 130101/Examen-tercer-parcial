import math

left = None
right = None
x = None
arr = None
list2 = None
resultado = None
mid1 = None
mid2 = None

# Describe this function...
def ternarySearch(left, right, x, arr):
  global list2, resultado, mid1, mid2
  if left >= right:
    mid1 = left + math.floor((right - left) / 3)
    mid2 = right - math.floor((right - left) / 3)
    if arr[int((mid1 + 1) - 1)] == x:
      return mid1
    if arr[int((mid2 + 1) - 1)] == x:
      return mid2
    if x < arr[int((mid1 + 1) - 1)]:
      resultado = ternarySearch(left, mid1 - 1, x, arr)
    elif x < arr[int((mid2 + 1) - 1)]:
      resultado = ternarySearch(mid2 + 1, right, x, arr)
    else:
      resultado = ternarySearch(mid1 + 1, mid2 - 1, x, arr)
  else:
    resultado = -1
  return resultado

def text_prompt(msg):
  try:
    return raw_input(msg)
  except NameError:
    return input(msg)


list2 = '1,2,3,4,5,6,7,8,9,10'.split(',')
x = float(text_prompt('"Numero que deseas encontrar: "'))
resultado = ternarySearch(0, len(list2) - 1, x, list2)
if resultado >= 0:
  print(''.join([str(x2) for x2 in ['Numero: ', x, 'Posicion: ', resultado]]))
else:
  print('No se ha encontrado el numero')