<div align="center">
  <h1> 30 kunlik Python: 5-kun — Ro'yxatlar (Lists)</h1>
</div>

[<< 4-kun](./04_strings_uz.md) | [6-kun >>](./06_tuples_uz.md)

- [📘 5-kun](#-5-kun)
  - [Ro'yxat qanday yaratiladi](#royxat-qanday-yaratiladi)
  - [Indeks orqali murojaat](#indeks-orqali-murojaat)
  - [Ro'yxatni yoyish (Unpacking)](#royxatni-yoyish-unpacking)
  - [Slicing](#slicing)
  - [Ro'yxatni o'zgartirish](#royxatni-ozgartirish)
  - [Ro'yxat metodlari](#royxat-metodlari)
  - [💻 Mashqlar — 5-kun](#-mashqlar--5-kun)

# 📘 5-kun

## Ro'yxatlar (Lists)

Pythonda to'rt xil **to'plam (collection)** turi bor:

- **List** — tartiblangan, **o'zgartirish mumkin**, takrorlanuvchi elementlarga ruxsat beradi.
- **Tuple** — tartiblangan, **o'zgartirib bo'lmaydi**, takrorlanuvchi elementlarga ruxsat beradi.
- **Set** — tartiblanmagan, indekssiz, takrorlanuvchi elementlarga ruxsat bermaydi.
- **Dictionary** — tartiblanmagan (Python 3.7+da kiritilgan tartib saqlanadi), kalit-qiymat juftliklari, takrorlanuvchi kalitga ruxsat bermaydi.

**List — JavaScriptdagi `Array`ning to'liq o'xshashi.** Tartiblangan, o'zgartirish mumkin, turli ma'lumot turlarini bir vaqtda saqlay oladi.

## Ro'yxat qanday yaratiladi

Ikki usul bor — JavaScriptda faqat `[]` bor edi, Pythonda ikkinchi usul ham mavjud (`list()` funksiyasi):

```python
empty_list = list()    # bo'sh ro'yxat
empty_list = []         # bo'sh ro'yxat — bu usul ko'proq ishlatiladi
print(len(empty_list))  # 0
```

```python
fruits = ['banana', 'orange', 'mango', 'lemon']                      # mevalar
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']       # sabzavotlar

print('Mevalar:', fruits)
print('Mevalar soni:', len(fruits))
```

Ro'yxat turli ma'lumot turlarini bir vaqtda saqlay oladi — JS'dagi array kabi:

```python
lst = ['Asabeneh', 250, True, {'country': 'Finland', 'city': 'Helsinki'}]
```

## Indeks orqali murojaat

JavaScriptdagi `array[0]` bilan bir xil. Sanash noldan boshlanadi:

```python
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits[0])    # banana — birinchi element
print(fruits[1])    # orange
last_index = len(fruits) - 1
print(fruits[last_index])   # lemon
```

**Manfiy indekslash** — Python'ning qulay xususiyati, JS'da yo'q (JS'da `array[array.length - 1]` deb yozish kerak edi):

```python
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits[-1])   # lemon — oxirgi element
print(fruits[-2])   # mango — oxiridan ikkinchi
```

## Ro'yxatni yoyish (Unpacking)

JS'dagi destructuring'ga o'xshaydi (`const [a, b, ...rest] = arr`), faqat Python'da `*` belgisi "qolganlarini olib ket" degani:

```python
fruits = ['banana', 'orange', 'mango', 'lemon', 'lime', 'apple']
first_fruit, second_fruit, third_fruit, *rest = fruits
print(first_fruit)    # banana
print(rest)           # ['lemon', 'lime', 'apple']
```

## Slicing

JS'dagi `array.slice(start, end)` bilan bir xil mantiq, faqat Python'da kvadrat qavs ichida `:` orqali yoziladi:

```python
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits[1:3])    # ['orange', 'mango'] — oxirgi indeks kirmaydi
print(fruits[::2])     # ['banana', 'mango'] — har 2-elementni oladi
print(fruits[::-1])    # ['lemon', 'mango', 'orange', 'banana'] — teskari tartib
```

## Ro'yxatni o'zgartirish

List **mutable (o'zgartirish mumkin)** — JS'dagi array kabi, indeks orqali qiymatni almashtirish mumkin:

```python
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits[0] = 'avocado'
print(fruits)   # ['avocado', 'orange', 'mango', 'lemon']
```

**Elementni tekshirish** — `in` operatori (JS'dagi `array.includes()` ga o'xshaydi):

```python
fruits = ['banana', 'orange', 'mango', 'lemon']
print('banana' in fruits)   # True
print('lime' in fruits)     # False
```

## Ro'yxat metodlari

Quyida JavaScript bilan taqqoslagan holda eng muhim ro'yxat metodlari:

| Python metodi | JS'dagi o'xshashi | Vazifasi |
|---|---|---|
| `.append(x)` | `.push(x)` | oxiriga element qo'shadi |
| `.insert(i, x)` | `.splice(i, 0, x)` | ko'rsatilgan indeksga element qo'shadi |
| `.remove(x)` | — (to'g'ridan-to'g'ri yo'q) | qiymati `x` bo'lgan birinchi elementni o'chiradi |
| `.pop()` / `.pop(i)` | `.pop()` / `.splice(i,1)` | elementni o'chirib, uni qaytaradi |
| `.clear()` | `array.length = 0` | barcha elementlarni o'chiradi |
| `.copy()` | `[...array]` (spread) | ro'yxatning nusxasini yaratadi |
| `list1 + list2` | `[...arr1, ...arr2]` | ikki ro'yxatni birlashtiradi |
| `.extend(lst2)` | `arr1.push(...arr2)` | ro'yxatga boshqa ro'yxat elementlarini qo'shadi |
| `.count(x)` | — (`.filter().length` kerak) | `x` necha marta uchraganini sanaydi |
| `.index(x)` | `.indexOf(x)` | `x` ning birinchi indeksini topadi |
| `.reverse()` | `.reverse()` | tartibni teskari aylantiradi (bir xil!) |
| `.sort()` | `.sort()` | o'sish tartibida saralaydi (asl ro'yxatni o'zgartiradi) |
| `sorted(lst)` | — | saralangan **yangi** ro'yxat qaytaradi, aslini o'zgartirmaydi |

```python
fruits = ['banana', 'orange', 'mango', 'lemon']

fruits.append('apple')        # ['banana', 'orange', 'mango', 'lemon', 'apple']
fruits.insert(2, 'kiwi')      # 'mango'dan oldin 'kiwi' qo'shiladi
fruits.remove('banana')       # 'banana' o'chadi
last = fruits.pop()           # oxirgi elementni o'chirib, qiymatini qaytaradi
fruits_copy = fruits.copy()   # mustaqil nusxa — asl ro'yxatga ta'sir qilmaydi

ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.count(24))         # 3 — necha marta uchraydi
print(ages.index(24))         # 2 — birinchi marta qaysi indeksda

ages.sort()                   # asl ro'yxatni o'zgartiradi: [19, 22, 24, 24, 24, 25, 25, 26]
print(sorted(ages, reverse=True))  # yangi ro'yxat qaytaradi, kamayish tartibida
```

> ⚠️ **Muhim eslatma (ko'chirma muammosi):** JavaScriptda bo'lgani kabi, Python'da ham `list2 = list1` deb yozsangiz, `list2` — `list1`ning **havolasi (reference)** bo'ladi, mustaqil nusxa emas! `list2`ni o'zgartirsangiz, `list1` ham o'zgaradi. Mustaqil nusxa olish uchun `.copy()` yoki `list(list1)` ishlating — bu JS'dagi `[...array]` spread sintaksisi vazifasini bajaradi.

🌕 Siz tirishqoqsiz va ko'p narsaga erishdingiz! 5-kun challenge'ini tugatdingiz. Endi mashqlarni bajaring.

## 💻 Mashqlar — 5-kun

### 1-daraja

1. Bo'sh ro'yxat e'lon qiling
2. 5 tadan ortiq elementli ro'yxat e'lon qiling
3. Ro'yxatingiz uzunligini toping
4. Ro'yxatning birinchi, o'rtadagi va oxirgi elementini olib chiqing
5. `mixed_data_types` nomli ro'yxat e'lon qiling: ism, yosh, bo'y, turmush holati, manzilingizni joylashtiring
6. `it_companies` nomli ro'yxat e'lon qilib, qiymat bering: Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon
7. Ro'yxatni `print()` orqali chiqaring
8. Ro'yxatdagi kompaniyalar sonini chiqaring
9. Birinchi, o'rtadagi va oxirgi kompaniyani chiqaring
10. Kompaniyalardan birini o'zgartirib, ro'yxatni qayta chiqaring
11. `it_companies`ga yana bitta IT kompaniya qo'shing
12. Ro'yxat o'rtasiga yangi IT kompaniya qo'shing (`.insert()`)
13. `it_companies`dagi kompaniyalardan birining nomini katta harfga o'tkazing (IBM bundan mustasno!)
14. `it_companies`ni `'#; '` satri bilan birlashtiring (`.join()`)
15. Ro'yxatda ma'lum kompaniya bor-yo'qligini tekshiring (`in`)
16. Ro'yxatni `.sort()` orqali saralang
17. Ro'yxatni `.reverse()` orqali kamayish tartibiga o'tkazing
18. Ro'yxatdan birinchi 3 kompaniyani kesib oling (slice)
19. Ro'yxatdan oxirgi 3 kompaniyani kesib oling
20. Ro'yxat o'rtasidagi kompaniya(lar)ni kesib oling
21. Birinchi IT kompaniyani o'chiring
22. O'rtadagi IT kompaniya(lar)ni o'chiring
23. Oxirgi IT kompaniyani o'chiring
24. Barcha IT kompaniyalarni o'chiring
25. `it_companies` ro'yxatini butunlay yo'q qiling (`del`)
26. Quyidagi ro'yxatlarni birlashtiring:

    ```py
    front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
    back_end = ['Node', 'Express', 'MongoDB']
    ```

27. 26-savoldagi birlashtirilgan ro'yxatni nusxalab, `full_stack` o'zgaruvchisiga yozing, so'ng `'Redux'`dan keyin `'Python'` va `'SQL'`ni qo'shing.

### 2-daraja

1. Quyidagi 10 talabaning yoshi berilgan:

```sh
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
```

   - Ro'yxatni saralab, eng kichik va eng katta yoshni toping
   - Eng kichik va eng katta yoshni ro'yxatga qayta qo'shing
   - O'rtacha qiymatni (median — o'rtadagi element yoki ikkitasining yarmi) toping
   - O'rtacha arifmetikni (barcha elementlar yig'indisi / soni) toping
   - Yoshlar oralig'ini (max - min) toping
   - `abs()` funksiyasi orqali `(min - o'rtacha)` va `(max - o'rtacha)` qiymatlarini taqqoslang

2. [Davlatlar ro'yxati](https://github.com/Asabeneh/30-Days-Of-Python/tree/master/data/countries.py)dagi o'rtadagi davlat(lar)ni toping
3. Davlatlar ro'yxatini ikkiga teng bo'ling (toq bo'lsa, birinchi yarmiga bitta ko'proq qo'shing)
4. `['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']` — birinchi 3 davlatni va qolganlarini (skandinaviya davlatlari) alohida yoying.

🎉 TABRIKLAYMIZ! 🎉

[<< 4-kun](./04_strings_uz.md) | [6-kun >>](./06_tuples_uz.md)
