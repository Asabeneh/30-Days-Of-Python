<div align="center">
  <h1> 30 kunlik Python: 7-kun — Set'lar (To'plamlar)</h1>
</div>

[<< 6-kun](./06_tuples_uz.md) | [8-kun >>](./08_dictionaries_uz.md)

- [📘 7-kun](#-7-kun)
  - [Set yaratish](#set-yaratish)
  - [Elementni tekshirish va qo'shish](#elementni-tekshirish-va-qoshish)
  - [Elementni o'chirish](#elementni-ochirish)
  - [List'ni Set'ga aylantirish](#listni-setga-aylantirish)
  - [Set'larni birlashtirish va matematik amallar](#setlarni-birlashtirish-va-matematik-amallar)
  - [💻 Mashqlar — 7-kun](#-mashqlar--7-kun)

# 📘 7-kun

## Set'lar (To'plamlar)

Maktabdagi matematika darslarini eslaysizmi — **to'plam (set)** tushunchasi? Pythondagi set ham xuddi shu — **tartiblanmagan, indekssiz, faqat noyob (takrorlanmaydigan) elementlardan** iborat to'plam. Set orqali matematikadagi **union (birlashma)**, **intersection (kesishma)**, **difference (ayirma)** kabi amallarni bajarish mumkin.

> 🟢 **Yaxshi xabar:** JavaScriptda ham `Set` mavjud (ES6'dan beri) — `new Set([1, 2, 3])`. Demak, bu tushuncha sizga unchalik begona emas! Faqat Python'dagi set yanada ko'p matematik amallarga ega (union, intersection va h.k.), JS'dagi Set'da bularni qo'lda yozish kerak bo'ladi.

## Set yaratish

Bo'sh set yaratish uchun **albatta `set()` funksiyasidan foydalaning** — bo'sh jingalak qavs `{}` esa **dictionary** yaratadi (bu keyingi kunda ko'ramiz), set emas!

```python
st = set()                                    # bo'sh set
fruits = {'banana', 'orange', 'mango', 'lemon'}   # boshlang'ich qiymatlar bilan
print(len(fruits))     # 4 — len() bu yerda ham ishlaydi
```

> 🟡 JS'da: `const fruits = new Set(['banana', 'orange', 'mango', 'lemon']); fruits.size` — Python'da `len()` funksiyasi, JS'da `.size` xususiyati ishlatiladi.

## Elementni tekshirish va qo'shish

`in` operatori orqali tekshiriladi (list/tuple'dagi kabi):

```python
fruits = {'banana', 'orange', 'mango', 'lemon'}
print('mango' in fruits)   # True
```

Element qo'shish — `.add()` (bitta element) yoki `.update()` (bir nechta element):

```python
fruits.add('lime')                              # bitta element qo'shish
fruits.update(['kiwi', 'plum'])                 # bir nechta element qo'shish
```

> 🟡 JS'dagi `set.add(item)` bilan bir xil — bu nom ham bir xil! Lekin JS'da bir nechtasini birdan qo'shadigan tayyor metod yo'q, har birini alohida `.add()` qilish kerak bo'lardi.

## Elementni o'chirish

```python
fruits.remove('lime')     # agar topilmasa, xatolik beradi
fruits.discard('lime')    # agar topilmasa ham, xatolik bermaydi — xavfsizroq
fruits.pop()               # tasodifiy elementni o'chiradi (set tartiblanmagan!)
fruits.clear()              # barchasini tozalaydi
del fruits                  # butun set'ni xotiradan o'chiradi
```

> 🟡 JS'da `set.delete(item)` — bitta metod, xatolik bermaydi (Python'dagi `.discard()` ga o'xshaydi). Python'da esa ikkita variant bor: qattiqroq (`remove`) va yumshoqroq (`discard`).

## List'ni Set'ga aylantirish

Bu — **takrorlanuvchi elementlarni tozalashning** eng tez usuli:

```python
fruits = ['banana', 'orange', 'mango', 'lemon', 'orange', 'banana']
fruits = set(fruits)
print(fruits)   # {'mango', 'lemon', 'banana', 'orange'} — takrorlanganlar yo'qoladi, tartib tasodifiy
```

> 🟡 JS'da xuddi shu maqsadda: `[...new Set(array)]` — massivdan takrorlanganlarni olib tashlashning eng mashhur "hiyla"si aynan shu!

## Set'larni birlashtirish va matematik amallar

Bu qism Python set'ining eng kuchli tomoni — JS Set'da bu metodlar **yo'q**, qo'lda yozishingiz kerak bo'lardi:

| Python metodi | Belgi | Vazifasi | JS'da qanday qilinardi |
|---|---|---|---|
| `.union()` | `\|` | ikkisini birlashtiradi | `new Set([...a, ...b])` |
| `.intersection()` | `&` | ikkisida ham bor elementlar | `[...a].filter(x => b.has(x))` |
| `.difference()` | `-` | faqat birinchisida bor elementlar | `[...a].filter(x => !b.has(x))` |
| `.symmetric_difference()` | `^` | ikkisida ham **bo'lmagan** elementlar | qo'lda yozish kerak |
| `.issubset()` | — | barcha elementlari boshqasida bormi | qo'lda tekshirish kerak |
| `.issuperset()` | — | barcha elementlarni o'z ichiga oladimi | qo'lda tekshirish kerak |
| `.isdisjoint()` | — | umumiy elementi yo'qmi | qo'lda tekshirish kerak |

```python
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}

print(whole_numbers.union(even_numbers))          # birlashma
print(whole_numbers.intersection(even_numbers))    # {0, 2, 4, 6, 8, 10} — kesishma
print(whole_numbers.difference(even_numbers))       # {1, 3, 5, 7, 9} — faqat juft bo'lmaganlar
print(even_numbers.issubset(whole_numbers))          # True — even_numbers, whole_numbers ichida
print(whole_numbers.issuperset(even_numbers))        # True

odd_numbers = {1, 3, 5, 7, 9}
print(even_numbers.isdisjoint(odd_numbers))          # True — umumiy elementi yo'q
```

🌕 Siz porlayotgan yulduzsiz! 7-kun challenge'ini tugatdingiz. Endi mashqlarni bajaring.

## 💻 Mashqlar — 7-kun

```py
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
```

### 1-daraja

1. `it_companies` setining uzunligini toping
2. `it_companies`ga `'Twitter'`ni qo'shing
3. `it_companies`ga bir nechta IT kompaniyani birdaniga qo'shing (`.update()`)
4. `it_companies`dan bitta kompaniyani o'chiring
5. `.remove()` va `.discard()` orasidagi farq nima?

### 2-daraja

1. `A` va `B`ni birlashtiring
2. `A` va `B`ning kesishmasini toping
3. `A`, `B`ning qism to'plami (subset)mi?
4. `A` va `B` — "disjoint" (umumiy elementi yo'q) to'plamlarmi?
5. `A`ni `B`ga va `B`ni `A`ga birlashtiring (natija farqlanadimi?)
6. `A` va `B` orasidagi symmetric difference nima?
7. Setlarni butunlay o'chiring

### 3-daraja

1. `age` ro'yxatini set'ga aylantirib, ro'yxat va set uzunligini taqqoslang — qaysi biri kattaroq?
2. String, list, tuple va set ma'lumot turlari orasidagi farqni tushuntiring
3. *"Men o'qituvchiman va odamlarni ilhomlantirish, o'qitishni yaxshi ko'raman"* — bu jumlada nechta noyob (takrorlanmagan) so'z ishlatilgan? `.split()` va `set()` orqali toping.

🎉 TABRIKLAYMIZ! 🎉

[<< 6-kun](./06_tuples_uz.md) | [8-kun >>](./08_dictionaries_uz.md)
