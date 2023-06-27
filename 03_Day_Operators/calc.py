print("Selamat datang di program kalkulator sederhana")
print("================================================")

print("Step 1 : masukkan angka yang anda inginkan")
inputNumberUser = (int(input()))
print("================================================")

print("Step 2 : Pilih operasi perhitungan yang anda inginkan : ")
print("+")
print("/")
print("*")
print("-")
print("================================================")

operationChoiceInput = (str(input()))

if(operationChoiceInput== '+'):
    addNumberUser = (int(input()))
    print(inputNumberUser + addNumberUser)

elif(operationChoiceInput == "/"):
    dividerNumberUser = (int(input()))
    print(inputNumberUser/dividerNumberUser)

elif(operationChoiceInput == "*"):
    multiplicationNumberUser = (int(input()))
    print(inputNumberUser * multiplicationNumberUser)

elif(operationChoiceInput == "-"):
    substractionNumber = (int(input()))
    print(substractionNumber - substractionNumber)

else:
    print("You choose a wrong input!!!!")    