<div align="center">
  <h1> 30 kunlik Python: 13-kun — List Comprehension</h1>
</div>

[<< 12-kun](./12_modules_uz.md) | [14-kun >>](./14_higher_order_functions_uz.md)

- [📘 13-kun](#-13-kun)
  - [List Comprehension](#list-comprehension)
  - [Lambda funksiya](#lambda-funksiya)
  - [💻 Mashqlar — 13-kun](#-mashqlar--13-kun)

# 📘 13-kun

## List Comprehension

**List comprehension** — bitta qatorda yangi ro'yxat yaratishning qisqa va tez usuli. Bu — JavaScriptdagi **`array.map()`** va **`array.filter()`**ni bitta qatorga "siqib qo'yilgani" deb tasavvur qiling.

```python
# sintaksis
[ifoda for elem in iterable if shart]
```

```javascript
// JavaScript — solishtirish uchun
const squares = numbers.map(i => i * i);
const evens = numbers.filter(i => i % 2 === 0);
```

```python
# Python — list comprehension ikkisini ham bitta qatorga birlashtira oladi
squares = [i * i for i in numbers]              # .map() vazifasi
evens = [i for i in numbers if i % 2 == 0]       # .filter() vazifasi
both = [i * i for i in numbers if i % 2 == 0]    # ikkisi birga!
```

**Misol: satrni belgilar ro'yxatiga aylantirish**

```python
language = 'Python'
lst = [i for i in language]
print(lst)   # ['P', 'y', 't', 'h', 'o', 'n']
```

**Misol: sonlar generatsiyasi va matematik amal**

```python
numbers = [i for i in range(11)]           # [0, 1, 2, ..., 10]
squares = [i * i for i in range(11)]       # [0, 1, 4, 9, ..., 100]
pairs = [(i, i * i) for i in range(6)]      # [(0, 0), (1, 1), (2, 4), ...] — tuple'lardan iborat ro'yxat
```

**Misol: shart bilan filtrlash**

```python
even_numbers = [i for i in range(21) if i % 2 == 0]   # faqat juftlar
numbers = [-8, -7, -3, -1, 0, 1, 3, 4, 5, 7, 6, 8, 10]
positive_evens = [i for i in numbers if i % 2 == 0 and i > 0]   # ikki shart birga
```

**Misol: ichma-ich ro'yxatni tekislash (flatten)**

```python
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [number for row in list_of_lists for number in row]
print(flattened)   # [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

> 🟡 JS'da bunga eng yaqini: `list_of_lists.flat()` yoki `[].concat(...list_of_lists)`.

## Lambda funksiya

**Lambda — nomsiz (anonim) kichik funksiya.** Bu JavaScriptdagi **arrow function**ning to'g'ridan-to'g'ri o'xshashi!

```javascript
// JavaScript
const addTwoNums = (a, b) => a + b;
console.log(addTwoNums(2, 3));   // 5
```

```python
# Python — lambda kalit so'zi bilan
add_two_nums = lambda a, b: a + b
print(add_two_nums(2, 3))   # 5
```

> 🟡 Farqi: JS'da `=>` belgisi, Python'da **`lambda`** so'zi va keyin `:` ishlatiladi. Lambda funksiya faqat **bitta ifodaga** ega bo'lishi mumkin va natijani avtomatik qaytaradi (`return` yozish shart emas, JS arrow function'dagi yashirin return'ga o'xshaydi: `const f = (a, b) => a + b`).

```python
square = lambda x: x ** 2
print(square(3))    # 9

# O'z-o'zini chaqiruvchi lambda
print((lambda a, b: a + b)(2, 3))   # 5
```

**Lambda funksiyani boshqa funksiya ichida** — bu yuqori darajali funksiyalar (14-kunda chuqurroq ko'ramiz) uchun zamin bo'ladi:

```python
def power(x):
    return lambda n: x ** n

cube = power(2)(3)   # avval x=2 beriladi, keyin n=3
print(cube)           # 8
```

🌕 Davom etayotganingiz zo'r, osmon — chegaranigiz! 13-kun challenge'ini tugatdingiz. Endi mashqlarni bajaring.

## 💻 Mashqlar — 13-kun

1. List comprehension orqali faqat manfiy va nolga teng sonlarni filtrlang:
   ```py
   numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
   ```
2. Quyidagi ichma-ich ro'yxatni bir o'lchamli ro'yxatga tekislang:
   ```py
   list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
   # natija: [1, 2, 3, 4, 5, 6, 7, 8, 9]
   ```
3. List comprehension orqali quyidagi tuple'lar ro'yxatini yarating (ko'paytirish jadvali):
   ```py
   [(0, 1, 0, 0, 0, 0, 0),
    (1, 1, 1, 1, 1, 1, 1),
    (2, 1, 2, 4, 8, 16, 32),
    ...
    (10, 1, 10, 100, 1000, 10000, 100000)]
   ```
4. Quyidagi ro'yxatni tekislang va har bir qiymatni katta harfga o'tkazing:
   ```py
   countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
   # natija: [['FINLAND', 'FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]
   ```
5. Quyidagi ro'yxatni dictionary'lar ro'yxatiga aylantiring:
   ```py
   countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
   # natija: [{'country': 'FINLAND', 'city': 'HELSINKI'}, ...]
   ```
6. Quyidagi ichma-ich ro'yxatni birlashtirilgan ismlar ro'yxatiga aylantiring:
   ```py
   names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')]]
   # natija: ['Asabeneh Yetayeh', 'David Smith']
   ```
7. Chiziqli tenglamaning burchak koeffitsienti yoki y-kesishuvini hisoblovchi lambda funksiya yozing.

🎉 TABRIKLAYMIZ! 🎉

[<< 12-kun](./12_modules_uz.md) | [14-kun >>](./14_higher_order_functions_uz.md)
