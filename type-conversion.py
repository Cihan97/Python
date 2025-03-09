'''
x = input('1 sayi: ')
y = input('2 sayi: ')

print(type(x))
print(type(y))

toplam = int(x) + int(y)

print(toplam)
'''

x = 5           # int
y = 2.5      # float
name = 'Cinar'     # string
isOnline = True    # bool

# print(type(x))
# print(type(y))
# print(type(name))
# print(type(isOnline))

# Type Conversion

# int to float

x = float(x)
print(x)
print(type(x))


# float to int

# y = int(y)
# print(y)
# print(type(y))


# result = str(x) + str(y)
# print(result)
# # print(type(result))

isOnline = str(isOnline)
print(isOnline)
print(type(isOnline))



# bool to int

isOnline = False
isOnline = int(isOnline)
print(isOnline)
print(type(isOnline))   



pi = 3.14

yariCap = float(input("Yarıçap: "))  # Kullanıcı girdisini float'a çeviriyoruz

alan = pi * (yariCap ** 2)
cevre = 2 * pi * yariCap  # Hatalı olan diğer çevre hesaplamasını kaldırdık

print("Alan:", alan)
print("Çevre:", cevre)



