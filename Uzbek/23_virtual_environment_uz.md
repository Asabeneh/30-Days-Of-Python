<div align="center">
  <h1> 30 kunlik Python: 23-kun — Virtual muhit (Virtual Environment)</h1>
</div>

[<< 22-kun](./22_web_scraping_uz.md) | [24-kun >>](./24_statistics_uz.md)

- [📘 23-kun](#-23-kun)
  - [Virtual muhit nima uchun kerak](#virtual-muhit-nima-uchun-kerak)
  - [💻 Mashqlar — 23-kun](#-mashqlar--23-kun)

# 📘 23-kun

## Virtual muhit nima uchun kerak

JavaScriptda `npm install` qilganingizda, paket avtomatik ravishda **shu loyihaning** `node_modules` papkasiga o'rnatiladi — har bir loyiha o'z paketlariga ega bo'ladi, loyihalar bir-biriga aralashmaydi.

**Python'da esa bu avtomatik emas!** Agar siz `pip install paket_nomi` desangiz, paket **butun kompyuteringizga global** o'rnatiladi. Agar ikkita loyihangizda bir xil paketning **turli versiyalari** kerak bo'lsa — muammo chiqadi.

> 🟡 **Analogiya:** `node_modules` — har bir loyiha o'zining shaxsiy "asboblar qutisi"ga ega, boshqa loyihaning asboblariga tegmaydi. Python'da standart holatda esa **hamma loyiha bitta umumiy asboblar omborida** ishlaydi — bu yerda har xil loyiha turli vintlar (versiyalar) talab qilsa, chalkashlik yuzaga keladi.

Bu muammoni hal qilish uchun **virtual muhit (virtual environment)** ishlatiladi — bu JS'dagi `node_modules`ga o'xshash, **har bir loyiha uchun alohida, izolyatsiya qilingan** paket muhiti yaratadi.

**1-qadam: `virtualenv` paketini o'rnatish**

```sh
pip install virtualenv
```

**2-qadam: Loyiha papkasi ichida virtual muhit yaratish**

```sh
# Mac/Linux
cd flask_project
virtualenv venv

# Windows
python -m venv venv
```

**3-qadam: Virtual muhitni faollashtirish**

```sh
# Mac/Linux
source venv/bin/activate

# Windows PowerShell
venv\Scripts\activate
```

Faollashtirilgandan keyin terminal qatori boshida `(venv)` paydo bo'ladi:

```sh
(venv) ~/Desktop/30DaysOfPython/flask_project$
```

> 🟢 Bu — JS loyihasida `node_modules` papkasi avtomatik faol bo'lishiga o'xshaydi, faqat Python'da buni **qo'lda "yoqish"** kerak.

**4-qadam: Shu loyiha uchun paketlarni o'rnatish**

Endi `pip install` qilganingiz **faqat shu virtual muhitga** o'rnatiladi, butun kompyuterga emas:

```sh
(venv) $ pip install Flask
(venv) $ pip freeze
Flask==1.1.1
Jinja2==2.10.3
Werkzeug==0.16.0
```

**5-qadam: Tugagandan keyin o'chirish**

```sh
(venv) $ deactivate
```

> ⚠️ `venv` papkasini **`.gitignore`** fayliga qo'shing — uni GitHub'ga yuklash shart emas (xuddi `node_modules`ni `.gitignore`ga qo'shganingizdek!). Boshqa odam loyihani olganda, `requirements.txt` orqali (19-20-kunlarda ko'rgan edik) o'zi virtual muhit yaratib, paketlarni qayta o'rnatadi — bu xuddi `package.json` orqali `npm install` qilishga o'xshaydi.

🌕 Maqsadga yetishga endi 7 kun qoldi, davom eting! 23-kun challenge'ini tugatdingiz. Endi mashqni bajaring.

## 💻 Mashqlar — 23-kun

1. Yuqoridagi misol asosida virtual muhitli loyiha papkasi yarating.

🎉 TABRIKLAYMIZ! 🎉

[<< 22-kun](./22_web_scraping_uz.md) | [24-kun >>](./24_statistics_uz.md)
