<div align="center">
  <h1> 30 kunlik Python: 17-kun — Xatolarni boshqarish (Exception Handling)</h1>
</div>

[<< 16-kun](./16_python_datetime_uz.md) | [18-kun >>](./18_regular_expressions_uz.md)

- [📘 17-kun](#-17-kun)
  - [Try va Except](#try-va-except)
  - [Argumentlarni yoyish va yig'ish](#argumentlarni-yoyish-va-yigish)
  - [Spread (yoyish) operatori](#spread-yoyish-operatori)
  - [Enumerate](#enumerate)
  - [Zip](#zip)
  - [💻 Mashqlar — 17-kun](#-mashqlar--17-kun)

# 📘 17-kun

## Try va Except

JavaScriptda **`try...catch`** ishlatgansiz — xatolik yuz berganda dastur to'xtamasligi uchun. Python'da bu **`try...except`** deyiladi, mantiq xuddi bir xil:

```javascript
// JavaScript
try {
  // xato bo'lishi mumkin bo'lgan kod
} catch (error) {
  console.log('Nimadir xato ketdi');
}
```

```python
# Python
try:
    print(10 + '5')      # bu xatolik beradi — son va matnni qo'shib bo'lmaydi
except:
    print('Nimadir xato ketdi')
```

**Xatolik turini aniqlash** — har xil xatolik turi uchun alohida blok yozish mumkin (15-kunda ko'rgan xatolik turlarini eslang):

```python
try:
    name = input('Ismingizni kiriting: ')
    year_born = input('Tug\'ilgan yilingiz: ')
    age = 2024 - int(year_born)
    print(f'Siz {name}. Yoshingiz {age}.')
except TypeError:
    print('Turlar mos kelmadi (TypeError)')
except ValueError:
    print('Qiymat noto\'g\'ri (ValueError)')
except ZeroDivisionError:
    print('Nolga bo\'lish xatoligi')
```

> 🟡 JS'da bunday "xatolik turiga qarab alohida blok" yo'q — `catch (error)` ichida `if (error instanceof TypeError)` deb qo'lda tekshirish kerak bo'lardi. Python'da bu imkoniyat **tayyor holda** keladi.

**`else` va `finally`** — JS'da `finally` bor (har doim ishlaydi), lekin `else` yo'q (Python'ga xos: xatolik bo'lmasa ishlaydi):

```python
try:
    age = 2024 - int(input('Tug\'ilgan yilingiz: '))
except ValueError:
    print('Qiymat xato')
else:
    print('try bloki muvaffaqiyatli tugadi')   # xatolik bo'lmasa ishlaydi
finally:
    print('Bu har doim ishlaydi')                # JS'dagi finally bilan bir xil
```

**Qisqa yozilish** — barcha xatoliklarni bitta nom ostida ushlab, xabarini chiqarish:

```python
try:
    age = 2024 - int(input('Tug\'ilgan yilingiz: '))
except Exception as e:
    print(e)   # JS'dagi catch(error) { console.log(error.message) } ga o'xshaydi
```

## Argumentlarni yoyish va yig'ish

5-kunda ko'rgan **unpacking** tushunchasini funksiyalarga qo'llaymiz. Ikki belgi ishlatiladi: **`*`** (list/tuple uchun) va **`**`** (dictionary uchun).

**List'ni yoyib, funksiyaga argument qilib berish:**

```python
def sum_of_five_nums(a, b, c, d, e):
    return a + b + c + d + e

lst = [1, 2, 3, 4, 5]
print(sum_of_five_nums(*lst))   # 15 — har bir element alohida argument bo'lib boradi
```

> 🟢 Bu JS'dagi **spread operatori**ga to'g'ridan-to'g'ri mos keladi: `sumOfFiveNums(...lst)`.

**Dictionary'ni yoyib berish:**

```python
def unpacking_person_info(name, country, city, age):
    return f'{name} {country}, {city}da yashaydi. U {age} yoshda.'

dct = {'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'age': 250}
print(unpacking_person_info(**dct))
```

**Cheksiz argumentlarni "yig'ish" (packing)** — 11-kunda ko'rgan `*args` va `**kwargs`:

```python
def sum_all(*args):
    s = 0
    for i in args:
        s += i
    return s

print(sum_all(1, 2, 3, 4, 5, 6, 7))   # 28
```

## Spread (yoyish) operatori

Ro'yxatlarni birlashtirishda ham xuddi shu `*` belgisi ishlatiladi — bu **JavaScriptdagi spread operatori (`...`) bilan deyarli bir xil**:

```javascript
// JavaScript
const lstOne = [1, 2, 3];
const lstTwo = [4, 5, 6, 7];
const lst = [0, ...lstOne, ...lstTwo];
```

```python
# Python
lst_one = [1, 2, 3]
lst_two = [4, 5, 6, 7]
lst = [0, *lst_one, *lst_two]
print(lst)   # [0, 1, 2, 3, 4, 5, 6, 7]
```

## Enumerate

Sikl ichida elementning **indeksi** ham kerak bo'lsa, **`enumerate()`** ishlatiladi — bu JS'dagi `array.entries()` yoki `array.forEach((item, index) => ...)` ga to'g'ridan-to'g'ri mos keladi:

```javascript
// JavaScript
['Finland', 'Sweden', 'Norway'].forEach((country, index) => {
  console.log(index, country);
});
```

```python
# Python
countries = ['Finland', 'Sweden', 'Norway']
for index, country in enumerate(countries):
    print(index, country)
```

## Zip

Ikki (yoki undan ko'p) ro'yxatni **bir vaqtning o'zida** aylanib chiqish kerak bo'lsa, `zip()` ishlatiladi — JS'da bunga to'g'ridan-to'g'ri tayyor funksiya yo'q, qo'lda indeks orqali yozilardi:

```python
fruits = ['banana', 'orange', 'mango']
vegetables = ['Tomato', 'Potato', 'Cabbage']

for f, v in zip(fruits, vegetables):
    print(f, '-', v)
# banana - Tomato
# orange - Potato
# mango - Cabbage
```

🌕 Siz qat'iyatlisiz! 17-kun challenge'ini tugatdingiz. Endi mashqlarni bajaring.

## 💻 Mashqlar — 17-kun

1. `names = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland', 'Estonia', 'Russia']`. Birinchi besh davlatni `nordic_countries`ga, `Estonia`ni `es`ga, `Russia`ni `ru`ga ajratib oling (unpacking orqali).

🎉 TABRIKLAYMIZ! 🎉

[<< 16-kun](./16_python_datetime_uz.md) | [18-kun >>](./18_regular_expressions_uz.md)
