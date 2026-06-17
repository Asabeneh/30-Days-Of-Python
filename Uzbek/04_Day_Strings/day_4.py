
# Bitta qatorli izoh
letter = 'P'                # satr bir belgidan ham, ko'p so'zdan ham iborat bo'lishi mumkin
print(letter)               # P
print(len(letter))          # 1
greeting = 'Hello, World!'  # bir yoki qo'sh tirnoq bilan yozilishi mumkin, "Hello, World!"
print(greeting)             # Hello, World!
print(len(greeting))        # 13
sentence = "Men 30 kunlik python challenge'idan zavqlanyapman"
print(sentence)

# Ko'p qatorli satr
multiline_string = '''Men o'qituvchiman va o'qitishni yaxshi ko'raman.
Odamlarga kuch berishdan ko'ra qoniqarli narsa topmadim.
Shu sababli 30 kunlik python'ni yaratdim.'''
print(multiline_string)
# Xuddi shu narsaning boshqa yozilishi
multiline_string = """Men o'qituvchiman va o'qitishni yaxshi ko'raman.
Odamlarga kuch berishdan ko'ra qoniqarli narsa topmadim.
Shu sababli 30 kunlik python'ni yaratdim."""
print(multiline_string)

# Satrlarni birlashtirish (Concatenation)
first_name = 'Asabeneh'
last_name = 'Yetayeh'
space = ' '
full_name = first_name + space + last_name
print(full_name)  # Asabeneh Yetayeh
# len() ichki funksiyasi orqali uzunlikni tekshirish
print(len(first_name))  # 8
print(len(last_name))   # 7
print(len(first_name) > len(last_name))  # True
print(len(full_name))  # 15

# Belgilarni o'zgaruvchilarga yoyish (unpacking)
language = 'Python'
a, b, c, d, e, f = language  # satr belgilarini alohida o'zgaruvchilarga yoyish
print(a)  # P
print(b)  # y
print(c)  # t
print(d)  # h
print(e)  # o
print(f)  # n

# Indeks orqali satr belgilariga murojaat
language = 'Python'
first_letter = language[0]
print(first_letter)  # P
second_letter = language[1]
print(second_letter)  # y
last_index = len(language) - 1
last_letter = language[last_index]
print(last_letter)  # n

# Agar o'ngdan boshlamoqchi bo'lsak, manfiy indeksdan foydalanamiz. -1 — oxirgi indeks
language = 'Python'
last_letter = language[-1]
print(last_letter)  # n
second_last = language[-2]
print(second_last)  # o

# Slicing (bo'lakka kesish)

language = 'Python'
# 0-indeksdan boshlanib, 3-gacha (3 kirmaydi)
first_three = language[0:3]
last_three = language[3:6]
print(last_three)  # hon
# Boshqa usul
last_three = language[-3:]
print(last_three)   # hon
last_three = language[3:]
print(last_three)   # hon

# Slicing paytida belgilarni o'tkazib yuborish
language = 'Python'
pto = language[0:6:2]
print(pto)  # Pto

# Maxsus belgilar (Escape sequence)
print('Hammaga python challenge yoqayotganiga ishonaman.\nSizgachi?')  # qator ko'chirish
print('Kunlar\tMavzular\tMashqlar')
print('1-kun\t3\t5')
print('2-kun\t3\t5')
print('3-kun\t3\t5')
print('4-kun\t3\t5')
print('Bu orqaga chiziq belgisi (\\)')  # orqaga chiziqni yozish
print('Har bir dasturlash tili \"Hello, World!\" bilan boshlanadi')

# Satr metodlari
# capitalize(): satrning birinchi harfini katta qiladi

challenge = 'thirty days of python'
print(challenge.capitalize())  # 'Thirty days of python'

# count(): qism-satr necha marta uchraganini qaytaradi, count(qism, start=.., end=..)

challenge = 'thirty days of python'
print(challenge.count('y'))  # 3
print(challenge.count('y', 7, 14))  # 1
print(challenge.count('th'))  # 2

# endswith(): satr berilgan qism bilan tugaydimi, tekshiradi

challenge = 'thirty days of python'
print(challenge.endswith('on'))   # True
print(challenge.endswith('tion'))  # False

# expandtabs(): tab belgisini bo'sh joyga almashtiradi, standart o'lcham 8

challenge = 'thirty\tdays\tof\tpython'
print(challenge.expandtabs())   # 'thirty  days    of      python'
print(challenge.expandtabs(10))  # 'thirty    days      of        python'

# find(): qism-satrning birinchi uchragan indeksini qaytaradi

challenge = 'thirty days of python'
print(challenge.find('y'))  # 5
print(challenge.find('th'))  # 0

# format(): satrni chiroyli formatda chiqaradi
first_name = 'Asabeneh'
last_name = 'Yetayeh'
job = 'teacher'
country = 'Finland'
sentence = 'Mening ismim {} {}. Men {}man. {} da yashayman.'.format(
    first_name, last_name, job, country)
print(sentence)

radius = 10
pi = 3.14
area = pi * radius ** 2
result = 'Radiusi {} bo\'lgan doiraning yuzi {}'.format(str(radius), str(area))
print(result)  # Radiusi 10 bo'lgan doiraning yuzi 314.0

# index(): qism-satrning indeksini qaytaradi
challenge = 'thirty days of python'
print(challenge.find('y'))  # 5
print(challenge.find('th'))  # 0

# isalnum(): harf va raqamdan iboratligini tekshiradi

challenge = 'ThirtyDaysPython'
print(challenge.isalnum())  # True

challenge = '30DaysPython'
print(challenge.isalnum())  # True

challenge = 'thirty days of python'
print(challenge.isalnum())  # False, bo'sh joy harf-raqam emas

challenge = 'thirty days of python 2019'
print(challenge.isalnum())  # False

# isalpha(): barcha belgilar harfdan iboratligini tekshiradi

challenge = 'thirtydaysofpython'
print(challenge.isalpha())  # True
num = '123'
print(num.isalpha())      # False

# isdecimal(): o'nlik raqamlarni tekshiradi

challenge = 'thirty days of python'
print(challenge.find('y'))  # 5
print(challenge.find('th'))  # 0

# isdigit(): raqam belgilarini tekshiradi

challenge = 'Thirty'
print(challenge.isdigit())  # False
challenge = '30'
print(challenge.isdigit())   # True

# isdecimal(): o'nlik raqam belgilarini tekshiradi

num = '10'
print(num.isdecimal())  # True
num = '10.5'
print(num.isdecimal())  # False


# isidentifier(): satrning to'g'ri o'zgaruvchi nomi bo'la olishini tekshiradi

challenge = '30DaysOfPython'
print(challenge.isidentifier())  # False, raqamdan boshlanadi
challenge = 'thirty_days_of_python'
print(challenge.isidentifier())  # True


# islower(): barcha harflar kichikligini tekshiradi

challenge = 'thirty days of python'
print(challenge.islower())  # True
challenge = 'Thirty days of python'
print(challenge.islower())  # False

# isupper(): barcha harflar kattaligini tekshiradi

challenge = 'thirty days of python'
print(challenge.isupper())  # False
challenge = 'THIRTY DAYS OF PYTHON'
print(challenge.isupper())  # True


# isnumeric(): raqamga oid belgilarni tekshiradi

num = '10'
print(num.isnumeric())      # True
print('ten'.isnumeric())    # False

# join(): ro'yxat elementlarini birlashtirib bitta satr qaytaradi
# DIQQAT: JS'da array.join(sep), Python'da esa sep.join(array) — teskari!

web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = '#, '.join(web_tech)
print(result)  # 'HTML#, CSS#, JavaScript#, React'

# strip(): boshi va oxiridagi berilgan belgilarni olib tashlaydi

challenge = ' thirty days of python '
print(challenge.strip())  # boshi-oxiridagi bo'sh joylar olib tashlanadi

# replace(): qism-satrni boshqasiga almashtiradi

challenge = 'thirty days of python'
print(challenge.replace('python', 'coding'))  # 'thirty days of coding'

# split(): satrni ajratuvchi bo'yicha bo'lib, ro'yxat qaytaradi

challenge = 'thirty days of python'
print(challenge.split())  # ['thirty', 'days', 'of', 'python']

# title(): har bir so'zni katta harf bilan boshlaydi

challenge = 'thirty days of python'
print(challenge.title())  # Thirty Days Of Python

# swapcase(): katta-kichik harflarni bir-biriga almashtiradi

challenge = 'thirty days of python'
print(challenge.swapcase())   # THIRTY DAYS OF PYTHON
challenge = 'Thirty Days Of Python'
print(challenge.swapcase())  # tHIRTY dAYS oF pYTHON

# startswith(): satr berilgan qism bilan boshlanishini tekshiradi

challenge = 'thirty days of python'
print(challenge.startswith('thirty'))  # True
challenge = '30 days of python'
print(challenge.startswith('thirty'))  # False
