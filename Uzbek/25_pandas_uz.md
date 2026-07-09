<div align="center">
  <h1> 30 kunlik Python: 25-kun — Pandas</h1>
</div>

[<< 24-kun](./24_statistics_uz.md) | [26-kun >>](./26_python_web_uz.md)

- [📘 25-kun](#-25-kun)
  - [Pandas nima](#pandas-nima)
  - [Series](#series)
  - [DataFrame](#dataframe)
  - [CSV fayl o'qish](#csv-fayl-o-qish)
  - [Ma'lumotlarni o'rganish](#ma-lumotlarni-o-rganish)
  - [DataFrame'ni o'zgartirish](#dataframeni-o-zgartirish)
  - [Boolean indekslash](#boolean-indekslash)
  - [💻 Mashqlar — 25-kun](#-mashqlar--25-kun)

# 📘 25-kun

## Pandas nima

**Pandas** — Python'da jadval ko'rinishidagi ma'lumotlar bilan ishlash uchun eng mashhur kutubxona. Pandas ikki asosiy tuzilmani taqdim etadi: **Series** (bir ustunli ma'lumot) va **DataFrame** (ko'p ustunli jadval).

> 🟡 **JS bilan taqqoslash:** Pandas DataFrame — JS'dagi "massiv ichida obyektlar" (`[{name:'Ali', age:25}, ...]`) ga o'xshaydi, lekin ancha kuchliroq: filter, sort, group, merge kabi amallar bir qator kod bilan bajariladi.

**O'rnatish:**

```sh
pip install pandas
```

**Import:**

```python
import pandas as pd
import numpy as np
```

## Series

`Series` — indeksli bir ustunli ma'lumot. Xuddi lug'atning bir ustuni kabi.

### Default indeks bilan

```python
nums = [1, 2, 3, 4, 5]
s = pd.Series(nums)
print(s)
# 0    1
# 1    2
# 2    3
# 3    4
# 4    5
# dtype: int64
```

### O'z indeksi bilan

```python
nums = [1, 2, 3, 4, 5]
s = pd.Series(nums, index=[1, 2, 3, 4, 5])
print(s)

mevalar = ['Apelsin', 'Banan', 'Mango']
s = pd.Series(mevalar, index=[1, 2, 3])
print(s)
# 1    Apelsin
# 2      Banan
# 3      Mango
# dtype: object
```

### Lug'atdan Series

```python
dct = {'ism': 'Ali', 'mamlakat': 'Uzbekistan', 'shahar': 'Toshkent'}
s = pd.Series(dct)
print(s)
# ism         Ali
# mamlakat    Uzbekistan
# shahar      Toshkent
# dtype: object
```

### Doimiy qiymat va linspace bilan

```python
# Barcha elementlar 10 bo'ladi
s = pd.Series(10, index=[1, 2, 3])

# NumPy linspace dan
s = pd.Series(np.linspace(5, 20, 10))
```

## DataFrame

`DataFrame` — ko'p ustunli jadval. Har bir ustun — bitta `Series`.

### Ro'yxatlar ro'yxatidan

```python
data = [
    ['Ali', 'Uzbekistan', 'Toshkent'],
    ['David', 'UK', 'London'],
    ['John', 'Sweden', 'Stokgolm']
]
df = pd.DataFrame(data, columns=['Ism', 'Mamlakat', 'Shahar'])
print(df)
```

### Lug'atdan

```python
data = {
    'Ism': ['Ali', 'David', 'John'],
    'Mamlakat': ['Uzbekistan', 'UK', 'Sweden'],
    'Shahar': ['Toshkent', 'London', 'Stokgolm']
}
df = pd.DataFrame(data)
print(df)
```

> 🟡 Lug'atdan yaratish — JS'da `const data = {name: [...], country: [...]}` ga o'xshaydi.

### Lug'atlar ro'yxatidan

```python
data = [
    {'Ism': 'Ali', 'Mamlakat': 'Uzbekistan', 'Shahar': 'Toshkent'},
    {'Ism': 'David', 'Mamlakat': 'UK', 'Shahar': 'London'},
    {'Ism': 'John', 'Mamlakat': 'Sweden', 'Shahar': 'Stokgolm'}
]
df = pd.DataFrame(data)
print(df)
```

> 🟡 Bu usul JS'da eng keng tarqalgan: `[{name:'Ali',...}, ...]` formatiga aynan mos.

## CSV fayl o'qish

```python
import pandas as pd

df = pd.read_csv('weight-height.csv')
print(df)
```

> 🟡 JSON o'qish uchun: `pd.read_json('fayl.json')` — 19-kunda ko'rgan `json.load()` ga nisbatan ancha qulayroq.

## Ma'lumotlarni o'rganish

```python
# Birinchi 5 qator
print(df.head())      # JS'da bunday usul yo'q, qo'lda slice ishlatiladi

# Oxirgi 5 qator
print(df.tail())

# Shakl (qatorlar, ustunlar)
print(df.shape)       # (10000, 3)

# Ustun nomlari
print(df.columns)     # Index(['Gender', 'Height', 'Weight'], dtype='object')

# Bir ustunni olish — lug'at kabi
heights = df['Height']   # Series qaytaradi
print(heights)

# Statistik ma'lumot
print(heights.describe())
# count    10000.0
# mean        66.37
# std          3.85
# min         54.26
# 25%         63.51
# 50%         66.32
# 75%         69.17
# max         78.99

# Butun DataFrame uchun
print(df.describe())

# Tur va bo'sh qiymatlar haqida
print(df.info())
```

## DataFrame'ni o'zgartirish

### Yangi ustun qo'shish

```python
data = {
    'Ism': ['Ali', 'David', 'John'],
    'Mamlakat': ['Uzbekistan', 'UK', 'Sweden'],
    'Shahar': ['Toshkent', 'London', 'Stokgolm']
}
df = pd.DataFrame(data)

# Yangi ustun qo'shish — lug'atga kalit qo'shgandek
ogʻirlik = [74, 78, 69]
df['Ogʻirlik'] = ogʻirlik

balandlik = [173, 175, 169]
df['Balandlik'] = balandlik

print(df)
```

> 🟡 JS'da: `data.forEach(obj => obj.weight = ...)` — har bir elementga qo'lda qo'shishga to'g'ri keladi. Pandas'da esa bir qatorda ustun qo'shiladi.

### Ustun qiymatlarini o'zgartirish

```python
# Foiz hisoblash
df['BMI'] = df['Ogʻirlik'] / (df['Balandlik'] / 100) ** 2
```

### Ma'lumot turini o'zgartirish

```python
# Float -> int
df['Ogʻirlik'] = df['Ogʻirlik'].astype(int)

# Ustun turini tekshirish
print(df.dtypes)
```

## Boolean indekslash

Ma'lumotlarni shart asosida filterlash — JS'dagi `.filter()` ga o'xshaydi:

```python
# Yoshi 30 dan katta bo'lganlarni filterlash
# JS'da: data.filter(s => s.age > 30)
# Pandas'da:
kattalar = df[df['yosh'] > 30]

# Ikkita shart
# JS'da: data.filter(s => s.age > 30 && s.country === 'Finland')
finlar_katta = df[(df['yosh'] > 30) & (df['mamlakat'] == 'Finland')]
```

> 🟡 **Muhim:** Pandas'da bir necha shart qo'shganda `&` (va) va `|` (yoki) ishlatiladi — Python'ning `and`/`or` kalit so'zlari Pandas'da ishlamaydi. Har bir shartni `()` ichiga olish kerak.

🌕 Siz datalarga ega bo'ldingiz! Maqsadga yetishga 5 kun qoldi. 25-kun challenge'ini tugatdingiz. Endi mashqlarni bajaring.

## 💻 Mashqlar — 25-kun

1. `pd.read_csv()` bilan istalgan CSV faylni o'qing va `head()`, `describe()`, `shape` metodlarini qo'llang.
2. Yangi ustun yarating (masalan, vazn kg'dan lbs'ga aylantirish: `df['weight_lbs'] = df['Weight'] * 2.205`).
3. Boolean filterlash bilan faqat biror shartga mos qatorlarni ajrating.

🎉 TABRIKLAYMIZ! 🎉

[<< 24-kun](./24_statistics_uz.md) | [26-kun >>](./26_python_web_uz.md)
