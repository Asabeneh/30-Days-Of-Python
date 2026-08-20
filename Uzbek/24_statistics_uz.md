<div align="center">
  <h1> 30 kunlik Python: 24-kun — Statistika va NumPy</h1>
</div>

[<< 23-kun](./23_virtual_environment_uz.md) | [25-kun >>](./25_pandas_uz.md)

- [📘 24-kun](#-24-kun)
  - [Statistika nima](#statistika-nima)
  - [statistics moduli](#statistics-moduli)
  - [NumPy](#numpy)
  - [NumPy massivini yaratish](#numpy-massivini-yaratish)
  - [Matematik amallar](#matematik-amallar)
  - [Ko'p o'lchamli massivlar](#ko-o-lchamli-massivlar)
  - [Kesish (Slicing)](#kesish-slicing)
  - [Foydali funksiyalar](#foydali-funksiyalar)
  - [Statistik funksiyalar](#statistik-funksiyalar)
  - [Chiziqli algebra](#chiziqli-algebra)
  - [💻 Mashqlar — 24-kun](#-mashqlar--24-kun)

# 📘 24-kun

## Statistika nima

**Statistika** — ma'lumotlarni yig'ish, tartibga solish, tahlil qilish va talqin qilish fani. Ma'lumotlar tahlili (data science) va sun'iy intellekt (machine learning) yo'nalishlarida statistika asosiy bilim hisoblanadi.

**Ma'lumot (data)** — biror maqsad uchun yig'ilgan va qayta ishlangan har qanday ma'lumot to'plami: raqamlar, matnlar, tasvirlar va hokazo.

## statistics moduli

Python'ning ichki `statistics` moduli oddiy statistik hisob-kitoblar uchun funksiyalar beradi:

```python
import statistics

yoshlar = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]

print(statistics.mean(yoshlar))    # o'rtacha — 30.04
print(statistics.median(yoshlar))  # mediana — 29
print(statistics.mode(yoshlar))    # moda (eng ko'p uchraydigan) — 26
print(statistics.stdev(yoshlar))   # standart og'ish — 4.2
```

> 🟡 Bu modul oddiy kalkulyator darajasida — professional hisob-kitoblar uchun **NumPy** ishlatiladi.

## NumPy

**NumPy** (Numerical Python) — Python'da ilmiy hisob-kitoblar uchun asosiy kutubxona. U **ko'p o'lchamli massivlar** (array) va ular ustida tezkor matematik amallarni taqdim etadi.

> 🟡 **JS bilan taqqoslash:** JS'dagi oddiy massiv (`[1,2,3]`) va NumPy massivi — bir narsa emas! JS massivida barcha elementga biror amal qilish uchun `.map()` kerak: `[1,2,3].map(x => x + 10)`. NumPy massivida esa shunchaki `arr + 10` yozasiz — barcha elementga avtomatik qo'shiladi. Bu **vektorizatsiya** deyiladi.

**O'rnatish:**

```sh
pip install numpy
```

**Import:**

```python
import numpy as np   # 'np' — odatiy qisqa nom, xuddi JS'da lodash'ni '_' deb import qilgandek
print(np.__version__)
```

## NumPy massivini yaratish

### Ro'yxat yoki kortejdan yaratish

```python
# Python ro'yxatidan
python_list = [1, 2, 3, 4, 5]
np_array = np.array(python_list)
print(type(np_array))   # <class 'numpy.ndarray'>
print(np_array)          # [1 2 3 4 5]  — vergulsiz chiqadi!

# Python kortejidan
python_tuple = (1, 2, 3, 4, 5)
np_from_tuple = np.array(python_tuple)
print(np_from_tuple)    # [1 2 3 4 5]
```

> 🟡 `ndarray` — "N-o'lchamli massiv" (N-dimensional array). JS'da bunday tuzilma yo'q.

### dtype (ma'lumot turi)

```python
# Butun sonlar
int_array = np.array([1, 2, 3, 4])
print(int_array.dtype)    # int64

# Float (kasr sonlar)
float_array = np.array([1, 2, 3, 4], dtype=float)
print(float_array)         # [1. 2. 3. 4.]
print(float_array.dtype)   # float64

# Boolean
bool_array = np.array([0, 1, -1, 0, 0], dtype=bool)
print(bool_array)          # [False  True  True False False]
```

### shape (shakl) va size (hajm)

```python
arr1d = np.array([1, 2, 3, 4, 5])
print(arr1d.shape)   # (5,)  — 5 ta elementli bir o'lchamli
print(arr1d.size)    # 5

arr2d = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
print(arr2d.shape)   # (3, 3)  — 3 qator, 3 ustun
print(arr2d.size)    # 9
```

> 🟡 JS'da `.length` faqat birinchi o'lchamni beradi. NumPy'da `.shape` barcha o'lchamlarni kortej (tuple) sifatida qaytaradi.

### Tur almashish (type conversion)

```python
int_arr = np.array([1, 2, 3], dtype=float)    # int -> float: [1. 2. 3.]
float_arr = np.array([1., 2., 3.], dtype=int)  # float -> int: [1 2 3]
```

## Matematik amallar

NumPy massivining **asosiy afzalligi** — barcha element ustida amal **bitta qadam**da bajariladi:

```python
arr = np.array([1, 2, 3, 4, 5])

# JS'da kerak bo'ladi: arr.map(x => x + 10)
# NumPy'da:
print(arr + 10)    # [11 12 13 14 15]
print(arr - 10)    # [-9 -8 -7 -6 -5]
print(arr * 10)    # [10 20 30 40 50]
print(arr / 10)    # [0.1 0.2 0.3 0.4 0.5]
print(arr % 3)     # [1 2 0 1 2]
print(arr // 10)   # [0 0 0 0 0]
print(arr ** 2)    # [ 1  4  9 16 25]
```

## Ko'p o'lchamli massivlar

```python
# 2D massiv — jadval kabi
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr2d)
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]

# Qatorlarni olish
print(arr2d[0])    # [1 2 3]  — birinchi qator
print(arr2d[1])    # [4 5 6]  — ikkinchi qator

# Ustunlarni olish  — [:, ustun_indeksi]
print(arr2d[:, 0]) # [1 4 7]  — birinchi ustun
print(arr2d[:, 1]) # [2 5 8]  — ikkinchi ustun

# Bitta elementni olish  — [qator, ustun]
print(arr2d[1, 2]) # 6  — 2-qator, 3-ustun
```

> 🟡 `arr2d[:, 0]` — "barcha qatorlarning 0-ustuni". JS'da bunday qulaylik yo'q, `for` bilan qo'lda yozishga to'g'ri keladi.

### zeros, ones — nol va birlardan massiv

```python
nollar = np.zeros((3, 3), dtype=int)
# [[0 0 0]
#  [0 0 0]
#  [0 0 0]]

birlar = np.ones((3, 3), dtype=int)
# [[1 1 1]
#  [1 1 1]
#  [1 1 1]]

ikkalar = birlar * 2   # barcha elementni 2 ga ko'paytirish
```

### reshape va flatten

```python
arr = np.array([[1, 2, 3], [4, 5, 6]])   # 2x3 shakl
qayta_shakl = arr.reshape(3, 2)            # 3x2 shakliga o'tkazish
# [[1 2]
#  [3 4]
#  [5 6]]

tekis = qayta_shakl.flatten()   # bitta qatorga aylantirish
# [1 2 3 4 5 6]
```

### hstack va vstack — birlashtirish

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(np.hstack((a, b)))   # gorizontal: [1 2 3 4 5 6]
print(np.vstack((a, b)))   # vertikal:
# [[1 2 3]
#  [4 5 6]]
```

## Kesish (Slicing)

```python
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# [boshlang'ich_qator:tugash_qator, boshlang'ich_ustun:tugash_ustun]
print(arr2d[0:2, 0:2])   # dastlabki 2 qator va 2 ustun
# [[1 2]
#  [4 5]]

# Teskari tartib
print(arr2d[::-1, ::-1])
# [[9 8 7]
#  [6 5 4]
#  [3 2 1]]
```

## Foydali funksiyalar

### arange — range()'ga o'xshash, lekin massiv qaytaradi

```python
# np.arange(boshlash, to'xtatish, qadam)
butun_sonlar = np.arange(0, 20, 1)
# [ 0  1  2  3 ... 19]

toq_sonlar = np.arange(1, 20, 2)
# [ 1  3  5  7 ... 19]

juft_sonlar = np.arange(2, 20, 2)
# [ 2  4  6  8 ... 18]
```

> 🟡 JS'da `range()` yo'q — klassik `for (let i=0; i<20; i++)` yoziladi. NumPy'da esa `np.arange()` massiv qaytaradi.

### linspace — teng oraliqli sonlar

```python
# 1 dan 5 gacha 10 ta teng oraliqli son
np.linspace(1.0, 5.0, num=10)
# [1.  1.44  1.88  2.33 ... 5.0]

# oxirgi qiymatni kiritmaslik
np.linspace(1.0, 5.0, num=5, endpoint=False)
# [1.  1.8  2.6  3.4  4.2]
```

### tile va repeat — takrorlash

```python
a = [1, 2, 3]
print(np.tile(a, 2))    # butun massivni 2 marta: [1 2 3 1 2 3]
print(np.repeat(a, 2))  # har elementni 2 marta: [1 1 2 2 3 3]
```

### Tasodifiy sonlar

```python
# [0, 1) orasida bir float
np.random.random()

# 5 ta tasodifiy float
np.random.random(5)

# [0, 10) orasida bir butun son
np.random.randint(0, 11)

# 4 ta tasodifiy butun son [2, 10) orasida
np.random.randint(2, 10, size=4)

# 3x3 o'lchamli tasodifiy butun sonlar massivi
np.random.randint(2, 10, size=(3, 3))

# Normal taqsimot: o'rtacha=79, standart og'ish=15, 80 ta son
normal_array = np.random.normal(79, 15, 80)
```

## Statistik funksiyalar

```python
arr = np.array([1, 2, 3, 4, 55, 44, 7, 8, 9])

print(np.min(arr))     # eng kichik: 1
print(np.max(arr))     # eng katta: 55
print(np.mean(arr))    # o'rtacha
print(np.median(arr))  # mediana
print(np.std(arr))     # standart og'ish
```

**2D massivda ustun/qator bo'yicha:**

```python
arr2d = np.array([[1, 2, 3], [4, 55, 44], [7, 8, 9]])

# axis=0 — ustun bo'yicha
print(np.amin(arr2d, axis=0))  # [1 2 3]
print(np.amax(arr2d, axis=0))  # [ 7 55 44]

# axis=1 — qator bo'yicha
print(np.amin(arr2d, axis=1))  # [1 4 7]
print(np.amax(arr2d, axis=1))  # [ 3 55  9]
```

## Chiziqli algebra

```python
# Dot product (nuqtaviy ko'paytma): f·g = 1*4 + 2*5 + 3*3 = 23
f = np.array([1, 2, 3])
g = np.array([4, 5, 3])
print(np.dot(f, g))   # 23

# Matritsa ko'paytmasi
h = [[1, 2], [3, 4]]
i = [[5, 6], [7, 8]]
print(np.matmul(h, i))
# [[19 22]
#  [43 50]]

# Determinant
print(np.linalg.det(i))   # -2.0
```

**Chiziqli munosabat — amaliy misol:**

```python
# Harorat va bosim o'rtasidagi bog'liqlik
temp = np.array([1, 2, 3, 4, 5])
pressure = temp * 2 + 5    # NumPy vektorizatsiyasi bilan formula
print(pressure)   # [ 7  9 11 13 15]
```

> 🟡 JS'da buning uchun: `temp.map(t => t * 2 + 5)` kerak. NumPy'da esa matematik formula to'g'ridan-to'g'ri yoziladi.

**NumPy massivi va Python ro'yxati asosiy farqlari:**

| Xususiyat | Python list | NumPy ndarray |
|-----------|-------------|---------------|
| Vektorizatsiya | Yo'q (`.map()` kerak) | Ha (`arr + 10` ishlaydi) |
| O'lcham o'zgartirish | Istalgan vaqt | Yaratilgandan keyin yo'q |
| Ma'lumot turi | Aralash bo'lishi mumkin | Faqat bitta turdagi |
| Xotira | Ko'proq | Kamroq |
| 2D indekslash | `lst[i][j]` | `arr[i, j]` |

🌕 Ajoyib! 24-kun'ni muvaffaqiyatli yakunladingiz. Endi mashqni bajaring.

## 💻 Mashqlar — 24-kun

1. Yuqoridagi barcha misollarni o'zingiz yozing va ishga tushiring.

🎉 TABRIKLAYMIZ! 🎉

[<< 23-kun](./23_virtual_environment_uz.md) | [25-kun >>](./25_pandas_uz.md)
