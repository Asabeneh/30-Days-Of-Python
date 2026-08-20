<div align="center">
  <h1> 30 kunlik Python: 8-kun — Dictionary (Lug'at)</h1>
</div>

[<< 7-kun](./07_sets_uz.md) | [9-kun >>](./09_conditionals_uz.md)

- [📘 8-kun](#-8-kun)
  - [Dictionary yaratish](#dictionary-yaratish)
  - [Uzunligi](#uzunligi)
  - [Elementlarga murojaat](#elementlarga-murojaat)
  - [Element qo'shish va o'zgartirish](#element-qoshish-va-ozgartirish)
  - [Kalitni tekshirish](#kalitni-tekshirish)
  - [Elementni o'chirish](#elementni-ochirish)
  - [Kalit va qiymatlarni ro'yxat sifatida olish](#kalit-va-qiymatlarni-royxat-sifatida-olish)
  - [💻 Mashqlar — 8-kun](#-mashqlar--8-kun)

# 📘 8-kun

## Dictionary (Lug'at)

**Dictionary — JavaScriptdagi `Object` (obyekt)ning to'liq o'xshashi.** Tartiblanmagan, o'zgartirish mumkin, kalit-qiymat (`key: value`) juftliklaridan iborat.

## Dictionary yaratish

Jingalak qavs `{}` yoki `dict()` funksiyasi orqali yaratiladi:

```python
empty_dict = {}
dct = {'key1': 'value1', 'key2': 'value2'}
```

```javascript
// JavaScript — solishtirish uchun
const dct = { key1: 'value1', key2: 'value2' };
```

> 🟡 Farqi: Python'da kalitlar har doim tirnoq ichida yoziladi (`'key1':`), JS'da esa odatda tirnoqsiz yoziladi (`key1:`).

**To'liq misol:**

```python
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],   # qiymat list bo'lishi mumkin
    'address': {                                                       # qiymat dictionary ham bo'lishi mumkin
        'street': 'Space street',
        'zipcode': '02210'
    }
}
```

Qiymat — istalgan ma'lumot turi bo'lishi mumkin: string, son, boolean, list, tuple, set yoki yana boshqa dictionary (JS'dagi nested object kabi).

## Uzunligi

```python
print(len(person))   # 7 — kalit-qiymat juftliklari soni
```

## Elementlarga murojaat

```python
print(person['first_name'])         # Asabeneh
print(person['skills'][0])          # JavaScript — list ichidagi birinchi element
print(person['address']['street'])  # Space street — ichma-ich dictionary
print(person['city'])               # ❌ KeyError — bunday kalit yo'q
```

> 🟡 JS'da `obj.first_name` yoki `obj['first_name']` deb yozardingiz — Python'da esa **faqat** kvadrat qavs ichida tirnoq bilan: `person['first_name']`. Yana bir farq: JS'da mavjud bo'lmagan kalitga murojaat qilsangiz `undefined` qaytadi, **Python'da esa xatolik (`KeyError`) chiqadi!**

Xatolikdan qochish uchun **`.get()`** metodidan foydalaning — agar kalit topilmasa, xatolik o'rniga `None` qaytaradi:

```python
print(person.get('first_name'))   # Asabeneh
print(person.get('city'))         # None — xatolik emas!
```

> 🟡 Bu JS'dagi `obj.city ?? 'standart qiymat'` yoki optional chaining (`obj?.city`) mantig'iga yaqin — faqat Python'da bu tayyor metod sifatida keladi.

## Element qo'shish va o'zgartirish

```python
person['job_title'] = 'Instructor'    # yangi kalit qo'shiladi
person['age'] = 252                    # mavjud kalit qiymati o'zgartiriladi
person['skills'].append('HTML')        # ichidagi list'ga element qo'shish
```

> 🟡 JS'da bu xuddi `obj.job_title = 'Instructor'` bilan bir xil ishlaydi.

## Kalitni tekshirish

`in` operatori orqali — bu JavaScriptda ham mavjud (`'key2' in obj`), shuning uchun tanish bo'lishi kerak:

```python
print('country' in person)    # True
print('city' in person)       # False
```

## Elementni o'chirish

```python
person.pop('first_name')      # 'first_name' kalitini o'chiradi
person.popitem()              # oxirgi qo'shilgan elementni o'chiradi
del person['is_married']      # ko'rsatilgan kalitni o'chiradi
person.clear()                # barchasini tozalaydi, {} qaytaradi
del person                    # butun dictionary'ni xotiradan o'chiradi
```

> 🟡 JS'da elementni o'chirish uchun `delete obj.key` operatoridan foydalanardingiz — Python'da bunga `del dct['key']` mos keladi.

## Kalit va qiymatlarni ro'yxat sifatida olish

| Python | JavaScript'dagi o'xshashi |
|---|---|
| `dct.keys()` | `Object.keys(obj)` |
| `dct.values()` | `Object.values(obj)` |
| `dct.items()` | `Object.entries(obj)` |
| `dct.copy()` | `{...obj}` (spread) |

```python
dct = {'key1': 'value1', 'key2': 'value2'}
print(dct.keys())     # dict_keys(['key1', 'key2'])
print(dct.values())   # dict_values(['value1', 'value2'])
print(dct.items())    # dict_items([('key1', 'value1'), ('key2', 'value2')])
dct_copy = dct.copy()  # mustaqil nusxa
```

> ⚠️ List'dagi kabi: `dct2 = dct1` deb yozsangiz, `dct2` faqat `dct1`ning havolasi (reference) bo'ladi — mustaqil nusxa olish uchun `.copy()` dan foydalaning.

🌕 Siz ajoyibsiz! Endi dictionary kuchiga ega bo'ldingiz. 8-kun challenge'ini tugatdingiz. Mashqlarni bajaring.

## 💻 Mashqlar — 8-kun

1. `dog` nomli bo'sh dictionary yarating
2. `dog`ga `name`, `color`, `breed`, `legs`, `age` kalitlarini qo'shing
3. `student` nomli dictionary yaratib, `first_name`, `last_name`, `gender`, `age`, `marital_status`, `skills`, `country`, `city`, `address` kalitlarini qo'shing
4. `student` dictionary uzunligini toping
5. `skills` qiymatini olib, turini tekshiring — u list bo'lishi kerak
6. `skills` ro'yxatiga yana bir-ikki ko'nikma qo'shing
7. Dictionary kalitlarini ro'yxat sifatida olib chiqing (`.keys()`)
8. Dictionary qiymatlarini ro'yxat sifatida olib chiqing (`.values()`)
9. Dictionary'ni tuple'lardan iborat ro'yxatga aylantiring (`.items()`)
10. Dictionary'dagi elementlardan birini o'chiring
11. Dictionary'lardan birini butunlay o'chiring

🎉 TABRIKLAYMIZ! 🎉

[<< 7-kun](./07_sets_uz.md) | [9-kun >>](./09_conditionals_uz.md)
