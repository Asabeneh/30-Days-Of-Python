<div align="center">
  <h1> 30 kunlik Python: 15-kun — Python xatolik turlari</h1>
</div>

[<< 14-kun](./14_higher_order_functions_uz.md) | [16-kun >>](./16_python_datetime_uz.md)

- [📘 15-kun](#-15-kun)
  - [Python xatolik turlari](#python-xatolik-turlari)
  - [💻 Mashqlar — 15-kun](#-mashqlar--15-kun)

# 📘 15-kun

## Python xatolik turlari

Kod yozganda xato qilish — odatiy hol (JavaScriptda ham shunday). Agar kod ishlamasa, Python sizga xatolik haqida xabar beradi — qayerda muammo borligini va xatolik turini ko'rsatadi. Xatolik turlarini tushunish — kodni tezroq "debug" qilishga yordam beradi.

Quyida eng ko'p uchraydigan xatolik turlari, JavaScriptdagi o'xshashlari bilan birga:

| Python xatoligi | JS'dagi o'xshashi | Qachon yuzaga keladi |
|---|---|---|
| `SyntaxError` | `SyntaxError` | kod yozilishida qoida buzilganda |
| `NameError` | `ReferenceError` | e'lon qilinmagan o'zgaruvchiga murojaat qilinganda |
| `IndexError` | (yo'q — `undefined` qaytadi) | ro'yxatda mavjud bo'lmagan indeksga murojaat qilinganda |
| `KeyError` | (yo'q — `undefined` qaytadi) | dictionary'da mavjud bo'lmagan kalitga murojaat qilinganda |
| `TypeError` | `TypeError` | mos kelmaydigan ma'lumot turlari bilan amal bajarilganda |
| `ValueError` | — | qiymat to'g'ri turda, lekin mos emas (masalan, `int('12a')`) |
| `ZeroDivisionError` | (yo'q — `Infinity` qaytadi) | songa nolga bo'linganda |
| `ModuleNotFoundError` / `ImportError` | (modul topilmasa import xatoligi) | mavjud bo'lmagan modul/funksiyani import qilganda |
| `AttributeError` | `TypeError` (`undefined is not a function`) | obyekt/modulda mavjud bo'lmagan xususiyatga murojaat qilinganda |

> 🟡 **Muhim farq:** JavaScriptda ro'yxatdan tashqari indeksga yoki mavjud bo'lmagan obyekt xususiyatiga murojaat qilsangiz, jim-jit `undefined` qaytadi — kod davom etadi. **Python'da esa bunday holatlar darhol xatolik (`IndexError`, `KeyError`) chiqaradi va dastur to'xtaydi!** Bu, aslida, xatoni erta payqashga yordam beradi.

### SyntaxError

```python
>>> print 'hello world'
SyntaxError: Missing parentheses in call to 'print'. Did you mean print('hello world')?
```

To'g'rilash:

```python
>>> print('hello world')
hello world
```

### NameError

```python
>>> print(age)
NameError: name 'age' is not defined
```

To'g'rilash — o'zgaruvchini avval e'lon qiling:

```python
>>> age = 25
>>> print(age)
25
```

### IndexError

```python
>>> numbers = [1, 2, 3, 4, 5]
>>> numbers[5]
IndexError: list index out of range
```

> 🟡 List'da indekslar 0 dan 4 gacha (5 element), shuning uchun `[5]` mavjud emas.

### ModuleNotFoundError

```python
>>> import maths
ModuleNotFoundError: No module named 'maths'
```

To'g'rilash — modul nomida xato bor edi:

```python
>>> import math
```

### AttributeError

```python
>>> import math
>>> math.PI
AttributeError: module 'math' has no attribute 'PI'
```

To'g'rilash — to'g'ri nom kichik harf bilan:

```python
>>> math.pi
3.141592653589793
```

### KeyError

```python
>>> user = {'name': 'Asab', 'age': 250, 'country': 'Finland'}
>>> user['county']
KeyError: 'county'
```

To'g'rilash — kalit nomidagi xatoni tuzating:

```python
>>> user['country']
'Finland'
```

### TypeError

```python
>>> 4 + '3'
TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

> 🟡 2-kunda eslatib o'tgan edik: JS'da `4 + '3'` natija `'43'` (avtomatik birlashtiradi), Python'da esa xatolik beradi. To'g'rilash uchun turlarni mos qiling:

```python
>>> 4 + int('3')
7
```

### ImportError

```python
>>> from math import power
ImportError: cannot import name 'power' from 'math'
```

To'g'rilash — funksiya nomi boshqacha (`pow`):

```python
>>> from math import pow
>>> pow(2, 3)
8.0
```

### ValueError

```python
>>> int('12a')
ValueError: invalid literal for int() with base 10: '12a'
```

> 🟡 `'12a'` ichida harf bor, shuning uchun sonlarga aylantirib bo'lmaydi.

### ZeroDivisionError

```python
>>> 1 / 0
ZeroDivisionError: division by zero
```

> 🟡 JavaScriptda `1 / 0` natijasi `Infinity` bo'ladi — kod davom etadi. **Python'da bu xatolik hisoblanadi va dastur to'xtaydi.**

Xatolik turlarini yaxshi o'qiy bilsangiz, xatolarni tezroq tuzatasiz va yaxshi dasturchiga aylanasiz.

🌕 Siz a'lo darajada ketyapsiz. Challenge'ning yarmiga yetdingiz! 15-kun challenge'ini tugatdingiz.

## 💻 Mashqlar — 15-kun

1. Python interaktiv shell'ni ochib, shu bo'limdagi barcha misollarni o'zingiz sinab ko'ring.

🎉 TABRIKLAYMIZ! 🎉

[<< 14-kun](./14_higher_order_functions_uz.md) | [16-kun >>](./16_python_datetime_uz.md)
