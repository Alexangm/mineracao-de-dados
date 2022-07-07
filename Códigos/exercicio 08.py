import numpy

x = numpy.array([1, 2, 3, 4, 5])
y = numpy.array([6, 7, 8, 9, 10])
print(x + y)
print(x - y)
print(y - x)
print(x * y)
print(x / y)
print(y / x)

print('\n\n')

print(numpy.sum(x))
print(numpy.max(x))
print(numpy.min(x))
print(numpy.sum(y))
print(numpy.max(y))
print(numpy.min(y))

z = numpy.random.randint(low=0, high=1001, size=200)

print(f"Média = {numpy.mean(z)}")
print(f"Mediana = {numpy.median(z)}")
print(f"Maior = {numpy.max(z)}")
print(f"Menor = {numpy.min(z)}")