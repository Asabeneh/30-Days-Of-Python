<div align="center">
  <h1> 30 kunlik Python: 14-kun — Yuqori darajali funksiyalar</h1>
</div>

[<< 13-kun](./13_list_comprehension_uz.md) | [15-kun >>](./15_python_type_errors_uz.md)

- [📘 14-kun](#-14-kun)
  - [Yuqori darajali funksiyalar nima](#yuqori-darajali-funksiyalar-nima)
  - [Python Closure (yopilish)](#python-closure-yopilish)
  - [Python Dekoratorlar](#python-dekoratorlar)
  - [Tayyor yuqori darajali funksiyalar: map, filter, reduce](#tayyor-yuqori-darajali-funksiyalar-map-filter-reduce)
  - [💻 Mashqlar — 14-kun](#-mashqlar--14-kun)

# 📘 14-kun

## Yuqori darajali funksiyalar nima

11-kunda ko'rgan edik: Python'da funksiyalar **"birinchi darajali fuqaro" (first-class citizen)** — JS'dagi kabi, ularni o'zgaruvchiga yozish, boshqa funksiyaga argument qilib berish va funksiyadan natija sifatida qaytarish mumkin. **Yuqori darajali funksiya** — boshqa funksiyani parametr sifatida qabul qiladigan yoki funksiyani natija sifatida qaytaradigan funksiya.

**Funksiyani parametr sifatida berish:**

```python
def sum_numbers(nums):
    return sum(nums)

def higher_order_function(f, lst):   # f — funksiya, parametr sifatida keladi
    return f(lst)

result = higher_order_function(sum_numbers, [1, 2, 3, 4, 5])
print(result)   # 15
```

> 🟢 Bu xuddi JS'da `setTimeout(callback, 1000)` yoki `array.forEach(callback)`ga funksiya berishga o'xshaydi — funksiyani "boshqa funksiyaga ovqat sifatida berish" tushunchasi.

**Funksiyani natija sifatida qaytarish:**

```python
def square(x):
    return x ** 2

def cube(x):
    return x ** 3

def higher_order_function(turi):
    if turi == 'square':
        return square          # funksiyaning o'zini qaytaramiz, chaqirmaymiz!
    elif turi == 'cube':
        return cube

result = higher_order_function('square')
print(result(3))   # 9
```

> 🟡 Diqqat: `return square` — qavssiz! Agar `return square()` deb yozsangiz, funksiya **chaqirilib**, natija qaytariladi. Qavssiz yozilganda esa funksiyaning **o'zi** (keyinroq chaqirish uchun) qaytariladi.

## Python Closure (yopilish)

**Closure — JavaScriptda allaqachon uchratgan tushuncha!** Ichki funksiya, uni o'rab turgan tashqi funksiyaning o'zgaruvchilariga "eslab qolgan holda" murojaat qila olishi.

```javascript
// JavaScript
function addTen() {
  const ten = 10;
  return function (num) {
    return num + ten;   // 'ten' tashqi funksiyadan "eslab qolingan"
  };
}
const closureResult = addTen();
console.log(closureResult(5));   // 15
```

```python
# Python — bir xil mantiq
def add_ten():
    ten = 10
    def add(num):
        return num + ten    # 'ten' tashqi funksiyadan "eslab qolingan"
    return add

closure_result = add_ten()
print(closure_result(5))    # 15
print(closure_result(10))   # 20
```

## Python Dekoratorlar

**Dekorator** — boshqa funksiyaning ichki tuzilishini o'zgartirmasdan, unga **yangi imkoniyat "qo'shib qo'yuvchi"** funksiya. JavaScriptda bunga to'g'ridan-to'g'ri o'xshashi yo'q — eng yaqin tasavvur: Express.js'dagi **middleware** yoki funksiyani boshqa funksiya bilan "o'rab olish" (wrapping).

> 🟡 **Analogiya:** Sovg'ani (funksiyani) o'zgartirmasdan, ustiga chiroyli qog'oz (qo'shimcha xatti-harakat) o'raб qo'yish — ichidagi sovg'a (asl funksiya) o'zgarmaydi, faqat tashqi ko'rinishi (xatti-harakati) boyiydi.

```python
def uppercase_decorator(function):
    def wrapper():
        func = function()
        return func.upper()    # asl funksiya natijasini katta harfga o'tkazadi
    return wrapper

@uppercase_decorator        # bu '@' belgisi dekoratorni ishlatish degani
def greeting():
    return 'Welcome to Python'

print(greeting())   # WELCOME TO PYTHON
```

`@uppercase_decorator` yozish — aslida `greeting = uppercase_decorator(greeting)` deyishning qisqa yo'li.

## Tayyor yuqori darajali funksiyalar: map, filter, reduce

Bu uchtasi — **JavaScriptdagi `array.map()`, `array.filter()`, `array.reduce()`ning Python'dagi versiyasi.** Faqat yozilish tartibi farq qiladi: JS'da metod massivga "ulanib" chaqiriladi, Python'da esa **funksiya birinchi, ro'yxat ikkinchi argument** sifatida beriladi.

| | JavaScript | Python |
|---|---|---|
| Har bir elementni o'zgartirish | `arr.map(x => x * x)` | `map(lambda x: x * x, arr)` |
| Shartga mos elementlarni saralash | `arr.filter(x => x % 2 === 0)` | `filter(lambda x: x % 2 == 0, arr)` |
| Hammasini bitta qiymatga "yig'ish" | `arr.reduce((a, b) => a + b)` | `reduce(lambda a, b: a + b, arr)` |

**`map()`** — har bir elementni o'zgartirib, yangi natija qaytaradi:

```python
numbers = [1, 2, 3, 4, 5]
numbers_squared = map(lambda x: x ** 2, numbers)
print(list(numbers_squared))   # [1, 4, 9, 16, 25] — list() ga o'rab olish kerak, chunki map() "lazy" obyekt qaytaradi
```

**`filter()`** — shartga mos keladigan elementlarni saralaydi:

```python
numbers = [1, 2, 3, 4, 5]
even_numbers = filter(lambda num: num % 2 == 0, numbers)
print(list(even_numbers))   # [2, 4]
```

**`reduce()`** — `functools` modulidan import qilinadi (JS'da `reduce()` array'ning o'z metodi, Python'da alohida modul kerak). Barcha elementlarni bitta natijaga "yig'ib qo'yadi":

```python
from functools import reduce

numbers = [1, 2, 3, 4, 5]
total = reduce(lambda x, y: x + y, numbers)
print(total)   # 15
```

> ⚠️ `map()` va `filter()` natijasi to'g'ridan-to'g'ri ro'yxat emas — ularni ko'rish uchun `list()` bilan o'rab olish kerak. Bu JS'dan farqli, chunki JS'da `.map()` va `.filter()` to'g'ridan-to'g'ri array qaytaradi.

🌕 Zo'r ishladingiz! 14-kun challenge'ini tugatdingiz. Endi mashqlarni bajaring.

## 💻 Mashqlar — 14-kun

```py
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

### 1-daraja

1. `map`, `filter`, `reduce` orasidagi farqni tushuntiring.
2. Yuqori darajali funksiya, closure va dekorator orasidagi farqni tushuntiring.
3. `map`, `filter` yoki `reduce`dan oldin ishlatiladigan funksiya yozish misolini ko'rsating.
4. `for` sikli orqali `countries` ro'yxatidagi har bir davlatni chiqaring.
5. `for` sikli orqali `names` ro'yxatidagi har bir ismni chiqaring.
6. `for` sikli orqali `numbers` ro'yxatidagi har bir sonni chiqaring.

### 2-daraja

1. `map` orqali `countries`dagi har bir davlatni katta harfga o'tkazib, yangi ro'yxat yarating.
2. `map` orqali `numbers`dagi har bir sonni kvadratga oshirib, yangi ro'yxat yarating.
3. `map` orqali `names`dagi har bir ismni katta harfga o'tkazing.
4. `filter` orqali nomida `'land'` so'zi bor davlatlarni saralang.
5. `filter` orqali aynan olti harfdan iborat davlatlarni saralang.
6. `filter` orqali olti yoki undan ko'p harfdan iborat davlatlarni saralang.
7. `filter` orqali `'E'` bilan boshlanadigan davlatlarni saralang.
8. Ikki yoki undan ko'p iteratorni zanjirlang (masalan, `map` natijasiga `filter`, keyin `reduce` qo'llang).
9. `get_string_lists` funksiyasini yozing — list oladi va faqat string elementlarni qaytaradi.
10. `reduce` orqali `numbers`dagi barcha sonlar yig'indisini toping.
11. `reduce` orqali barcha davlatlarni birlashtirib, quyidagi jumlani hosil qiling: *"Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries"*.
12. `categorize_countries` funksiyasini yozing — nomida umumiy qoliplar (`'land'`, `'ia'`, `'stan'` kabi) bo'lgan davlatlarni guruhlab qaytarsin ([countries.py](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries.py) fayli yordamida).
13. Davlat nomlarining boshlanish harfini kalit, shu harf bilan boshlanadigan davlatlar sonini qiymat qilib qaytaruvchi funksiya yozing.
14. `get_first_ten_countries` funksiyasini yozing — `countries` ro'yxatidan birinchi 10 ta davlatni qaytarsin.
15. `get_last_ten_countries` funksiyasini yozing — oxirgi 10 ta davlatni qaytarsin.

### 3-daraja

1. [countries-data.py](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries-data.py) faylidan foydalanib:
   - Davlatlarni nomi, poytaxti va aholisi bo'yicha saralang
   - Eng ko'p gaplashiladigan 10 tilni joylashuvi bo'yicha saralang
   - Eng aholisi ko'p 10 davlatni saralang

🎉 TABRIKLAYMIZ! 🎉

[<< 13-kun](./13_list_comprehension_uz.md) | [15-kun >>](./15_python_type_errors_uz.md)
