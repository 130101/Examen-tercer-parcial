import math

list2 = None
low = None
high = None
arr = None
x = None
resultado = None
mid = None
midc = None

# Describe this function...
def binarySearch(low, high, arr, x):
  global list2, resultado, mid, midc
  if high >= low:
    mid = round(low + (high - low) / 2)
    midc = arr[int((mid + 1) - 1)]
    if midc == x:
      resultado = mid
    elif midc > x:
      resultado = binarySearch(low, mid - 1, arr, x)
    else:
      resultado = binarySearch(mid + 1, high, arr, x)
  else:
    resultado = -1
  return resultado

def text_prompt(msg):
  try:
    return raw_input(msg)
  except NameError:
    return input(msg)


list2 = '1,3,5,7,9,11,13,15,17,19,21,23'.split(',')
x = float(text_prompt('Numero que deseas encontrar: '))
resultado = binarySearch(0, len(list2) - 1, list2, x)
if resultado >= 0:
  print(''.join([str(x2) for x2 in ['El numero: ', x, ' Posicion: ', resultado]]))
else:
  print(''.join([str(x3) for x3 in ['El numero: ', x, ' No fue encontrado,', 'Tamaño del arreglo: ', len(list2)]]))