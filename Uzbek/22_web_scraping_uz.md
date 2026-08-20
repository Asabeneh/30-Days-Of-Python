<div align="center">
  <h1> 30 kunlik Python: 22-kun — Veb-skreyping (Web Scraping)</h1>
</div>

[<< 21-kun](./21_classes_and_objects_uz.md) | [23-kun >>](./23_virtual_environment_uz.md)

- [📘 22-kun](#-22-kun)
  - [Veb-skreyping nima](#veb-skreyping-nima)
  - [💻 Mashqlar — 22-kun](#-mashqlar--22-kun)

# 📘 22-kun

## Veb-skreyping nima

Internet — turli maqsadlar uchun foydali ulkan ma'lumotlar manbai. Bu ma'lumotlarni yig'ish jarayoni **veb-skreyping (web scraping)** deyiladi — veb-saytdan ma'lumotni "qirib olib", o'z kompyuteringizga yoki bazaga saqlash.

> 🟡 Agar siz brauzer konsolida `document.querySelector()` orqali HTML elementlarni "ushlagan" bo'lsangiz — bu tushuncha sizga tanish. Farqi: u yerda siz brauzerdagi sahifa bilan ishlagansiz, bu yerda esa Python orqali **istalgan veb-saytning HTML kodini serverdan o'qib**, undan kerakli qismni ajratib olamiz (Node.js dunyosida bunga `cheerio` kutubxonasi mos keladi).

Veb-skreyping uchun ikkita paket kerak (PIP orqali, 20-kunda ko'rgan edik):

```sh
pip install requests
pip install beautifulsoup4
```

- **`requests`** — saytdan HTML kodini olib keladi (JS'dagi `fetch()` vazifasini bajaradi)
- **`BeautifulSoup`** — olingan HTML ichidan kerakli elementlarni topib beradi (JS'dagi `document.querySelector()` vazifasiga o'xshaydi, faqat brauzersiz)

```python
import requests
from bs4 import BeautifulSoup

url = 'https://archive.ics.uci.edu/ml/datasets.php'

response = requests.get(url)        # saytdan HTML'ni olib kelish
print(response.status_code)          # 200 — muvaffaqiyatli

content = response.content
soup = BeautifulSoup(content, 'html.parser')   # HTML'ni "tahlil qilish" uchun tayyorlash

print(soup.title)              # <title>...</title> — butun teg bilan
print(soup.title.get_text())   # faqat teg ichidagi matn
```

**Elementlarni topish** — HTML teg, klass yoki id orqali (CSS selektor mantig'iga o'xshaydi):

```python
tables = soup.find_all('table', {'cellpadding': '3'})   # cellpadding="3" atributiga ega barcha <table>larni topadi
table = tables[0]    # natija ro'yxat, birinchisini olamiz

for td in table.find('tr').find_all('td'):    # birinchi <tr> ichidagi barcha <td>lar
    print(td.text)
```

> 🟡 JS'da bunga eng yaqini: `document.querySelectorAll('table[cellpadding="3"]')`. `find()` — birinchi moslikni, `find_all()` — barcha mosliklarni qaytaradi (JS'dagi `querySelector()` va `querySelectorAll()` ga mos).

⚠️ **Muhim eslatma:** Veb-skreyping qilishdan oldin saytning `robots.txt` faylini va foydalanish shartlarini tekshiring — har bir saytni skreyping qilish ruxsat etilgan emas.

🌕 Siz alohida insonsiz, har kuni rivojlanmoqdasiz! Maqsadga yetishga atigi 8 kun qoldi. 22-kun challenge'ini tugatdingiz. Endi mashqlarni bajaring.

## 💻 Mashqlar — 22-kun

1. `http://www.bu.edu/president/boston-university-facts-stats/` saytini skreyping qilib, ma'lumotni JSON fayl sifatida saqlang.
2. `https://archive.ics.uci.edu/ml/datasets.php` saytidagi jadvalni ajratib olib, JSON faylga aylantiring.
3. [AQSh prezidentlari ro'yxati](https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States) jadvalini skreyping qilib, JSON sifatida saqlang (jadval murakkab tuzilgan, vaqt ko'p ketishi mumkin).

🎉 TABRIKLAYMIZ! 🎉

[<< 21-kun](./21_classes_and_objects_uz.md) | [23-kun >>](./23_virtual_environment_uz.md)
