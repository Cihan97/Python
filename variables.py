maasAli = 5000
maasAhmet = 4000
vergi = 0.27

print(maasAli - (maasAli * vergi))
print(maasAhmet - (maasAhmet * vergi))

# Degisken Tanımlama Kuralları

# rakam ile baslyamaz

number1 = 10

number1 += 30
print(number1)

# Büyük küçük harf duyarlılığı vardır

age = 20
AGE = 30

print(age)
print(AGE)

# Türkçe karakter kullanmayın

yas = 20
_age =20    

x = 1             #int 
y = 2.3           #float
name = "Çınar"    #string
isStudent = True  #bool

x, y, name, isStudent = (1, 2.3, "Çınar", True)

a = '10'
b = '20'
print(a+b) #30 => 1020

firstName = 'Sadik'
lastName = 'turan'

print(firstName + lastName)  #Sadik turan


