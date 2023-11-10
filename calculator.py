import sys

print ('Number of arguments: ', len(sys.argv), 'arguments.')
print ('Argument List:', str(sys.argv))

argnums = [int(x) for x in sys.argv[1:]]

def multiplyAllNumbers(argnums):
    sum = 1

    for x in argnums:
        sum = sum * x

    return sum

print(multiplyAllNumbers(argnums))