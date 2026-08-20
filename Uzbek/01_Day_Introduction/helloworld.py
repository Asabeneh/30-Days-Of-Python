# Kirish
# 1-kun - 30 kunlik Python Challenge
# (JavaScript bilimi asosida moslashtirilgan)

# print() — bu Python'dagi console.log()
print("Hello World!")   # ekranga "Hello World!" deb chiqaradi

# Matematik amallar — bular JavaScript'dagi bilan bir xil ishlaydi
print(2 + 3)   # qo'shish (+)        -> 5
print(3 - 1)   # ayirish (-)         -> 2
print(2 * 3)   # ko'paytirish (*)    -> 6
print(3 + 2)   # qo'shish (+)        -> 5
print(3 - 2)   # ayirish (-)         -> 1
print(3 * 2)   # ko'paytirish (*)    -> 6
print(3 / 2)   # bo'lish (/)         -> 1.5
print(3 ** 2)  # daraja (**)         -> 9  (JS'da Math.pow(3, 2) ga teng)
print(3 % 2)   # modul / qoldiq (%)  -> 1  (JS'dagi % bilan bir xil)
print(3 // 2)  # butun qismli bo'lish (//) -> 1 (JS'da Math.floor(3 / 2) ga teng)

# Ma'lumot turlarini tekshirish
# type() — JS'dagi typeof operatoriga o'xshaydi, lekin funksiya sifatida chaqiriladi

print(type(10))                    # Int — butun son (JS'da bu ham shunchaki "number")
print(type(3.14))                  # Float — kasr son (JS'da bu ham "number", Python'da alohida tur)
print(type(1 + 3j))                # Complex — kompleks son (JS'da bunday tur yo'q)
print(type('Asabeneh'))            # String — satr (JS'dagi string bilan bir xil)
print(type([1, 2, 3]))             # List — JS'dagi Array (massiv) ga teng
print(type({'name': 'Asabeneh'}))  # Dictionary — JS'dagi Object (obyekt)ga o'xshaydi
print(type({9.8, 3.14, 2.7}))      # Set — JS'da ham Set mavjud, tartiblanmagan, faqat noyob qiymatlar
print(type((9.8, 3.14, 2.7)))      # Tuple — list kabi, lekin o'zgartirib bo'lmaydi (JS'da to'g'ridan-to'g'ri o'xshashi yo'q)
