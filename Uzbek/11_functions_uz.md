<div align="center">
  <h1> 30 kunlik Python: 11-kun — Funksiyalar</h1>
</div>

[<< 10-kun](./10_loops_uz.md) | [12-kun >>](./12_modules_uz.md)

- [📘 11-kun](#-11-kun)
  - [Funksiya nima](#funksiya-nima)
  - [Parametrsiz funksiya](#parametrsiz-funksiya)
  - [Qiymat qaytaruvchi funksiya](#qiymat-qaytaruvchi-funksiya)
  - [Parametrli funksiya](#parametrli-funksiya)
  - [Kalit-qiymat orqali argument berish](#kalit-qiymat-orqali-argument-berish)
  - [Standart (default) parametrlar](#standart-default-parametrlar)
  - [Cheksiz miqdordagi argumentlar (*args)](#cheksiz-miqdordagi-argumentlar-args)
  - [Dictionary'ni yoyish (**kwargs)](#dictionaryni-yoyish-kwargs)
  - [Funksiyani boshqa funksiyaga parametr qilish](#funksiyani-boshqa-funksiyaga-parametr-qilish)
  - [💻 Mashqlar — 11-kun](#-mashqlar--11-kun)

# 📘 11-kun

## Funksiya nima

JavaScriptda funksiyalarni yaxshi bilasiz — qayta-qayta ishlatish mumkin bo'lgan kod bo'lagi. Python'da funksiyalar **xuddi shu maqsadda**, faqat boshqacha kalit so'z bilan yoziladi:

```javascript
// JavaScript
function generateFullName() {
  const firstName = 'Asabeneh';
  const lastName = 'Yetayeh';
  return firstName + ' ' + lastName;
}
console.log(generateFullName());
```

```python
# Python — function o'rniga "def" kalit so'zi ishlatiladi
def generate_full_name():
    first_name = 'Asabeneh'
    last_name = 'Yetayeh'
    return first_name + ' ' + last_name

print(generate_full_name())
```

**Asosiy farqlar:**

| | JavaScript | Python |
|---|---|---|
| Funksiya e'lon qilish | `function name() { }` | `def name():` |
| Kod blokini belgilash | `{ }` | `:` va indentatsiya |
| Funksiya nomi | camelCase | snake_case |
| Qiymat qaytarmasa | `undefined` | `None` |

## Parametrsiz funksiya

```python
def add_two_numbers():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    print(total)

add_two_numbers()    # funksiyani chaqirish
```

## Qiymat qaytaruvchi funksiya

JS'dagi `return` bilan bir xil ishlaydi:

```python
def add_two_numbers():
    num_one = 2
    num_two = 3
    return num_one + num_two

print(add_two_numbers())   # 5
```

> 🟡 Agar funksiyada `return` bo'lmasa, Python avtomatik **`None`** qaytaradi — bu JS'dagi `undefined`ga mos keladi.

## Parametrli funksiya

JS'dagi kabi, funksiya bitta yoki bir nechta parametr qabul qila oladi:

```python
def greetings(name):
    return name + ', Python olamiga xush kelibsiz!'

print(greetings('Asabeneh'))

def sum_two_numbers(num_one, num_two):
    return num_one + num_two

print(sum_two_numbers(1, 9))
```

## Kalit-qiymat orqali argument berish

Python'ning qulay xususiyati — argumentlarni **kalit nomi bilan** berish mumkin, shunda **tartib muhim emas**:

```python
def print_full_name(firstname, lastname):
    print(firstname + ' ' + lastname)

print_full_name(lastname='Yetayeh', firstname='Asabeneh')   # tartib teskari, lekin to'g'ri ishlaydi!
```

> 🟡 JS'da bunga eng yaqin narsa — funksiyaga **obyekt** sifatida argument berish va uni destructuring qilish: `function f({firstname, lastname}) {...}`. Python'da bu imkoniyat **tayyor holda**, qo'shimcha sintaksissiz mavjud.

## Standart (default) parametrlar

JS'dagi default parametrlar bilan bir xil sintaksis (`function f(name = 'Peter')`):

```python
def greetings(name='Peter'):
    return name + ', Python olamiga xush kelibsiz!'

print(greetings())            # 'Peter' ishlatiladi
print(greetings('Asabeneh'))  # 'Asabeneh' beriladi
```

## Cheksiz miqdordagi argumentlar (`*args`)

JavaScriptdagi **rest parameter** (`...args`) bilan bir xil mantiq, faqat Python'da `*` belgisi bir yulduzcha:

```javascript
// JavaScript
function sumAllNums(...nums) {
  return nums.reduce((total, n) => total + n, 0);
}
```

```python
# Python
def sum_all_nums(*nums):
    total = 0
    for num in nums:
        total += num
    return total

print(sum_all_nums(2, 3, 5))   # 10
```

## Dictionary'ni yoyish (`**kwargs`)

Funksiya nomlangan (keyword) argumentlarni cheksiz miqdorda qabul qilishi mumkin — `**` (ikki yulduzcha) bilan:

```python
def arbitrary_named_args(**args):
    print('Jami argumentlar soni:', len(args))
    for k, v in args.items():
        print(' * kalit:', k, 'qiymat:', v)
```

Dictionary'ni to'g'ridan-to'g'ri funksiyaga "yoyib" yuborish ham mumkin:

```python
def greet(name, location):
    print('Salom', name, ',', location, 'da ob-havo qanday?')

my_dict = {'name': 'Alice', 'location': 'New York'}
greet(**my_dict)   # dictionary kalitlari mos parametrlarga avtomatik tarqaladi
```

> 🟡 Bu JS'dagi spread operatori (`...obj`) ga g'oyaviy jihatdan o'xshaydi, lekin JS'da funksiya chaqirishda obyektni shunchaki "yoyib yuborish" yo'q — odatda obyektni o'zini parametr sifatida uzatib, ichida destructuring qilinardi.

> ⚠️ Odatda `**kwargs`ni shart bo'lmasa ishlatmang — funksiya nimani qabul qilishini tushunish qiyinlashadi.

## Funksiyani boshqa funksiyaga parametr qilish

JavaScriptda funksiyalarni "first-class citizen" deb atashgan bo'lardingiz — ularni o'zgaruvchiga yozish, boshqa funksiyaga argument sifatida berish mumkin (callback'lar!). Python'da ham xuddi shunday:

```python
def square_number(n):
    return n * n

def do_something(f, x):
    return f(x)

print(do_something(square_number, 3))   # 9
```

> 🟢 Bu xuddi JS'dagi `array.map(callback)`, `setTimeout(callback, 1000)` kabi joylarda funksiyani argument qilib berishga o'xshaydi — tushuncha sizga begona emas!

🌕 Siz ancha narsaga erishdingiz, davom eting! 11-kun challenge'ini tugatdingiz. Endi mashqlarni bajaring.

## 💻 Mashqlar — 11-kun

### 1-daraja

1. `add_two_numbers` funksiyasini yozing — ikki parametr oladi va yig'indisini qaytaradi.
2. Doira yuzi: `yuza = π x r x r`. `area_of_circle` funksiyasini yozing.
3. `add_all_nums` funksiyasini yozing — cheksiz miqdordagi argument oladi va yig'indisini qaytaradi. Barcha elementlar son ekanligini tekshiring, aks holda mos xabar bering.
4. Selsiydan Farengeytga aylantirish formulasi: `°F = (°C x 9/5) + 32`. `convert_celsius_to_fahrenheit` funksiyasini yozing.
5. `check_season` funksiyasini yozing — oy nomini oladi va fasl (Kuz, Qish, Bahor, Yoz) qaytaradi.
6. `calculate_slope` funksiyasini yozing — chiziqli tenglamaning burchak koeffitsientini qaytaradi.
7. Kvadrat tenglama: `ax² + bx + c = 0`. `solve_quadratic_eqn` funksiyasini yozing.
8. `print_list` funksiyasini yozing — list oladi va har bir elementini chiqaradi.
9. `reverse_list` funksiyasini yozing — list oladi va uni teskari tartibda qaytaradi (sikl orqali):

```py
print(reverse_list([1, 2, 3, 4, 5]))    # [5, 4, 3, 2, 1]
print(reverse_list(["A", "B", "C"]))    # ["C", "B", "A"]
```

10. `capitalize_list_items` funksiyasini yozing — list oladi va har bir elementini katta harf bilan boshlanadigan qilib qaytaradi.
11. `add_item` funksiyasini yozing — list va element oladi, elementni oxiriga qo'shib qaytaradi:

```py
food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(add_item(food_stuff, 'Meat'))   # ['Potato', 'Tomato', 'Mango', 'Milk', 'Meat']
```

12. `remove_item` funksiyasini yozing — list va element oladi, elementni o'chirib qaytaradi.
13. `sum_of_numbers` funksiyasini yozing — son oladi va shu sonigacha barcha sonlar yig'indisini qaytaradi:

```py
print(sum_of_numbers(5))    # 15
print(sum_of_numbers(10))   # 55
```

14. `sum_of_odds` funksiyasini yozing — son oladi va shu oraliqdagi toq sonlar yig'indisini qaytaradi.
15. `sum_of_even` funksiyasini yozing — son oladi va shu oraliqdagi juft sonlar yig'indisini qaytaradi.

### 2-daraja

1. `evens_and_odds` funksiyasini yozing — musbat butun son oladi va undagi juft va toq sonlar sonini sanaydi:

```py
print(evens_and_odds(100))
# Toq sonlar: 50
# Juft sonlar: 51
```

2. `factorial` funksiyasini yozing — butun son oladi va uning faktorialini qaytaradi.
3. `is_empty` funksiyasini yozing — biror narsa oladi va u bo'sh yoki yo'qligini tekshiradi.
4. List oladigan funksiyalar yozing: `calculate_mean`, `calculate_median`, `calculate_mode`, `calculate_range`, `calculate_variance`, `calculate_std` (standart og'ish).
5. `greet` funksiyasini yozing — standart parametr `name` bilan. Argument berilmasa "Hello, Guest!" deb, aks holda ism bilan salomlashsin:

```py
greet()          # "Hello, Guest!"
greet("Alice")   # "Hello, Alice!"
```

6. `show_args` funksiyasini yozing — cheksiz miqdordagi nomlangan argument oladi va ularning nomi-qiymatini chiqaradi:

```py
show_args(name="Alice", age=30, city="New York")
# Received: name: Alice, age: 30, city: New York
```

### 3-daraja

1. `is_prime` funksiyasini yozing — son tub (prime) ekanligini tekshiradi.
2. List elementlari noyob (unique) ekanligini tekshiruvchi funksiya yozing.
3. List elementlari bir xil ma'lumot turida ekanligini tekshiruvchi funksiya yozing.
4. Berilgan satr to'g'ri Python o'zgaruvchi nomi bo'la olishini tekshiruvchi funksiya yozing.
5. [countries-data.py](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries-data.py) faylidan foydalanib:
   - `most_spoken_languages` funksiyasini yozing — dunyoda eng ko'p gaplashiladigan 10-20 tilni kamayish tartibida qaytarsin
   - `most_populated_countries` funksiyasini yozing — eng aholisi ko'p 10-20 davlatni kamayish tartibida qaytarsin

🎉 TABRIKLAYMIZ! 🎉

[<< 10-kun](./10_loops_uz.md) | [12-kun >>](./12_modules_uz.md)
