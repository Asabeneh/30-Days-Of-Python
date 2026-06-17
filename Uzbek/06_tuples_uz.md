<div align="center">
  <h1> 30 kunlik Python: 6-kun — Tuple'lar</h1>
</div>

[<< 5-kun](./05_lists_uz.md) | [7-kun >>](./07_sets_uz.md)

- [📘 6-kun](#-6-kun)
  - [Tuple yaratish](#tuple-yaratish)
  - [Tuple uzunligi](#tuple-uzunligi)
  - [Elementlarga murojaat](#elementlarga-murojaat)
  - [Slicing](#slicing)
  - [Tuple'ni List'ga aylantirish](#tupleni-listga-aylantirish)
  - [Elementni tekshirish](#elementni-tekshirish)
  - [Tuple'larni birlashtirish](#tuplelarni-birlashtirish)
  - [Tuple'ni o'chirish](#tupleni-ochirish)
  - [💻 Mashqlar — 6-kun](#-mashqlar--6-kun)

# 📘 6-kun

## Tuple'lar

1-kunda eslatib o'tgan edik: **Tuple — list kabi tartiblangan to'plam, lekin yaratilgandan keyin o'zgartirib bo'lmaydi.** Yumaloq qavs `()` bilan yoziladi.

> 🟡 **Analogiya:** List — ochiq quti, istalgan vaqt narsa qo'shish, olib tashlash mumkin. **Tuple — bir marta narsa solib, muhrlab yopilgan quti.** Ichidagini ko'rish mumkin, lekin almashtirish, qo'shish yoki olib tashlash mumkin emas.

JavaScriptda bunga to'g'ridan-to'g'ri o'xshashi yo'q. Eng yaqin tasavvur — `Object.freeze()` qilingan massiv (`const frozen = Object.freeze([1, 2, 3])`), lekin Pythonda bu **alohida, tayyor ma'lumot turi** sifatida mavjud.

Tuple chunki o'zgartirib bo'lmaydi (immutable), uning metodlari juda kam:

- `tuple()` — bo'sh tuple yaratish
- `.count()` — elementning necha marta uchraganini sanash
- `.index()` — elementning indeksini topish
- `+` operatori — ikki tuple'ni birlashtirish

## Tuple yaratish

```python
empty_tuple = ()              # bo'sh tuple
empty_tuple = tuple()         # bo'sh tuple — funksiya orqali

fruits = ('banana', 'orange', 'mango', 'lemon')
```

## Tuple uzunligi

```python
fruits = ('banana', 'orange', 'mango', 'lemon')
print(len(fruits))    # 4
```

## Elementlarga murojaat

Listdagi kabi ishlaydi — musbat va manfiy indekslash:

```python
fruits = ('banana', 'orange', 'mango', 'lemon')
print(fruits[0])      # banana
print(fruits[-1])     # lemon — oxirgi element
```

## Slicing

```python
fruits = ('banana', 'orange', 'mango', 'lemon')
print(fruits[1:3])    # ('orange', 'mango')
print(fruits[-3:])    # ('orange', 'mango', 'lemon')
```

## Tuple'ni List'ga aylantirish

Tuple **immutable** — agar uni o'zgartirish kerak bo'lsa, avval **list**ga aylantirib, o'zgartirib, keyin yana tuple'ga qaytarish mumkin:

```python
fruits = ('banana', 'orange', 'mango', 'lemon')
fruits = list(fruits)        # endi o'zgartirish mumkin
fruits[0] = 'apple'
print(fruits)                # ['apple', 'orange', 'mango', 'lemon']
fruits = tuple(fruits)       # qayta "muhrlab yopamiz"
print(fruits)                # ('apple', 'orange', 'mango', 'lemon')
```

## Elementni tekshirish

`in` operatori — list'dagi bilan bir xil:

```python
fruits = ('banana', 'orange', 'mango', 'lemon')
print('orange' in fruits)    # True
print('apple' in fruits)     # False

fruits[0] = 'apple'   # ❌ TypeError: 'tuple' object does not support item assignment
```

> ⚠️ Yuqoridagi oxirgi qator xatolik beradi — bu **tuple'ning eng muhim xususiyati**: yaratilgandan keyin ichidagi elementni to'g'ridan-to'g'ri o'zgartirish mumkin emas.

## Tuple'larni birlashtirish

`+` operatori orqali — list'dagi kabi:

```python
fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot')
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables)
```

## Tuple'ni o'chirish

Tuple ichidan bitta elementni o'chirib bo'lmaydi (chunki immutable), lekin **butun tuple'ni** `del` orqali o'chirish mumkin:

```python
fruits = ('banana', 'orange', 'mango', 'lemon')
del fruits     # butun tuple xotiradan o'chadi
```

🌕 Siz juda jasursiz, shu yergacha yetib keldingiz! 6-kun challenge'ini tugatdingiz. Endi mashqlarni bajaring.

## 💻 Mashqlar — 6-kun

### 1-daraja

1. Bo'sh tuple yarating
2. Aka-ukalaringiz va opa-singillaringiz ismlaridan iborat tuple yarating (xayoliy bo'lsa ham bo'ladi)
3. Aka-ukalar va opa-singillar tuple'larini birlashtirib, `siblings` o'zgaruvchisiga yozing
4. Nechta aka-uka/opa-singilingiz bor?
5. `siblings`ga ota-onangiz ismini qo'shib, `family_members` o'zgaruvchisiga yozing (eslatma: tuple'ni o'zgartirish uchun avval list'ga aylantirishni unutmang)

### 2-daraja

1. `family_members`dan aka-ukalar/opa-singillar va ota-onani alohida ajratib oling (unpacking)
2. Mevalar, sabzavotlar va hayvon mahsulotlari tuple'larini yaratib, ularni birlashtirib `food_stuff_tp` ga yozing
3. `food_stuff_tp` tuple'ini `food_stuff_lt` list'iga aylantiring
4. `food_stuff_tp` yoki `food_stuff_lt`dan o'rtadagi element(lar)ni kesib (slice) oling
5. `food_stuff_lt`dan birinchi va oxirgi 3 elementni kesib oling
6. `food_stuff_tp` tuple'ini butunlay o'chiring (`del`)
7. Elementni tekshiring:
   - `'Estonia'` skandinaviya davlatimi?
   - `'Iceland'` skandinaviya davlatimi?

   ```py
   nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')
   ```

🎉 TABRIKLAYMIZ! 🎉

[<< 5-kun](./05_lists_uz.md) | [7-kun >>](./07_sets_uz.md)
