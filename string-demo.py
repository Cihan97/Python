website = "http://www.python.org"
course  = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40+ Saat)"

# 1- 'course' karakter dizisinde kaç karakter bulunmaktadır?
print(len(course))

# 2- 'website' içinden www karakterlerini alın.
result = website[7:10]
print(result)

# 3- 'website' içinden com karakterlerini alın.
result = website[-3:]
print(result)


# 4- 'course' içinden ilk 15 ve son 15 karakterlerini alın.
result = course[0:15]
result = course[:15]

# 5- 'course' ifadesindeki karakterleri tersten yazdirin.
result = course[::-1]

name, surname, age, job = "Bora", "Yılmaz", 32, "Mühendis"

# 6 - Yukarıda verilen değişkenler ile ekrana aşağıdaki ifadeyi yazdirin.
#   'Benim adım Bora Yılmaz, Yaşım 32 ve mesleğim Mühendis.'

result = "Benim adim" + name+ " " + surname + ", Yasim " + str(age) + " ve meslegim " + job + "."

print(result)

# 7 'Hello world' ifadesindeki w harfini 'W' ile degisitirin.
s = "Hello world"
s = s[0:6] + "W" + s[-4:]
print(s)


# 8- 'abc' ifadesini yan yana 3 defa yazdirin.

result = 'abc' * 3
print(result)
