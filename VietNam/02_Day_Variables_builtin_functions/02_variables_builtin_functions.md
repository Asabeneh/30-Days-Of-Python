<div align="center">
  <h1> 30 Ngày Thử Thách Với Python: Ngày 2 - Biến, Các Hàm Dựng Sẵn</h1>
  <a class="header-badge" target="_blank" href="https://www.linkedin.com/in/asabeneh/">
  <img src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&logo=linkedin&style=social">
  </a>
  <a class="header-badge" target="_blank" href="https://twitter.com/Asabeneh">
  <img alt="Twitter Follow" src="https://img.shields.io/twitter/follow/asabeneh?style=social">
  </a>

<sub>Tác giả:
<a href="https://www.linkedin.com/in/asabeneh/" target="_blank">Asabeneh Yetayeh</a><br>
<small> Bản in lần 2: Tháng 7, 2021</small>
</sub>

</div>

[<< Day 1](../readme.md) | [Day 3 >>](../03_Day_Operators/03_operators.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 Ngày 2](#-ngày-2)
  - [Hàm dựng sẵn](#hàm-dựng-sẵn)
  - [Biến](#biến)
    - [Khai báo nhiều biến trên một dòng](#khai-báo-nhiều-biến-trên-một-dòng)
  - [Kiểu dữ liệu](#kiểu dữ liệu)
  - [Kiểm tra kiểu dữ liệu và ép kiểu](#kiểm-tra-kiểu-dữ-liệu-và-ép-kiểu)
  - [Số](#số)
  - [💻 Bài tập - Ngày 2](#-bài tập---ngày-2)
    - [Bài tập: cấp độ 1](#bài tập-cấp độ-1)
    - [Bài tập: cấp độ 2](#bài tập-cấp độ-2)

# 📘 Ngày 2

## Hàm dựng sẵn

Trong Python, chúng ta có rất nhiều hàm dựng sẵn (built-in functions). Đây là những hàm luôn có sẵn để bạn sử dụng, nghĩa là bạn có thể dùng chúng mà không cần import hay cấu hình gì thêm. Một số hàm dựng sẵn được dùng phổ biến nhất trong Python là: _print()_, _len()_, _type()_, _int()_, _float()_, _str()_, _input()_, _list()_, _dict()_, _min()_, _max()_, _sum()_, _sorted()_, _open()_, _file()_, _help()_, và _dir()_. Bảng dưới đây liệt kê đầy đủ các hàm dựng sẵn của Python, lấy từ [tài liệu chính thức của Python](https://docs.python.org/3/library/functions.html).

![Built-in Functions](../images/builtin-functions.png)

Hãy cùng mở Python shell và bắt đầu sử dụng một số hàm dựng sẵn phổ biến.

![Built-in functions](../images/builtin-functions_practice.png)

Hãy thực hành thêm với các hàm dựng sẵn khác nhau

![Help and Dir Built in Functions](../images/help_and_dir_builtin.png)

Như bạn thấy trong terminal ở trên, Python có các từ khóa dành riêng (reserved words). Chúng ta không được dùng các từ khóa này để đặt tên biến hay hàm. Chúng ta sẽ tìm hiểu về biến ở phần tiếp theo.

Mình tin rằng đến giờ bạn đã quen thuộc với các hàm dựng sẵn. Hãy thực hành thêm một lần nữa trước khi chuyển sang phần kế tiếp.

![Min Max Sum](../images/builtin-functional-final.png)

## Variables

Biến (variables) dùng để lưu trữ dữ liệu trong bộ nhớ máy tính. Ở nhiều ngôn ngữ lập trình, người ta khuyến khích đặt tên biến theo kiểu "biến gợi nhớ" (mnemonic variable). Biến gợi nhớ là tên biến dễ nhớ và dễ liên tưởng đến ý nghĩa của nó. Một biến tham chiếu đến một địa chỉ bộ nhớ, nơi dữ liệu được lưu trữ.
Tên biến không được bắt đầu bằng số, ký tự đặc biệt hay dấu gạch nối. Biến có thể có tên ngắn (như x, y, z), nhưng nên đặt tên có ý nghĩa mô tả rõ ràng hơn (firstname, lastname, age, country) thì tốt hơn nhiều.

Quy tắc đặt tên biến trong Python

- Tên biến phải bắt đầu bằng một chữ cái hoặc dấu gạch dưới
- Tên biến không được bắt đầu bằng một con số
- Tên biến chỉ được chứa các ký tự chữ và số cùng dấu gạch dưới (A-z, 0-9, và \_)
- Tên biến phân biệt chữ hoa chữ thường (firstname, Firstname, FirstName và FIRSTNAME là các biến khác nhau)

Dưới đây là một số ví dụ về tên biến hợp lệ:

```shell
firstname
lastname
age
country
city
first_name
last_name
capital_city
_if # nếu muốn dùng từ khóa dành riêng để đặt tên biến
year_2021
year2021
current_year_2021
birth_year
num1
num2
```

Tên biến không hợp lệ

```shell
first-name
first@name
first$name
num-1
1num
```

Chúng ta sẽ sử dụng phong cách đặt tên biến chuẩn của Python, được rất nhiều lập trình viên Python áp dụng. Các lập trình viên Python dùng quy ước đặt tên kiểu snake case (snake_case). Chúng ta dùng dấu gạch dưới sau mỗi từ đối với biến có nhiều hơn một từ (ví dụ: first_name, last_name, engine_rotation_speed). Ví dụ dưới đây là cách đặt tên biến chuẩn; dấu gạch dưới là bắt buộc khi tên biến gồm nhiều hơn một từ.

Khi ta gán một kiểu dữ liệu nào đó cho một biến, việc này gọi là khai báo biến (variable declaration). Ví dụ ở dưới đây, tên của mình được gán cho biến first_name. Dấu bằng là toán tử gán (assignment operator). Gán nghĩa là lưu trữ dữ liệu vào biến. Dấu bằng trong Python không phải là dấu bằng thể hiện sự bằng nhau như trong Toán học.

_Ví dụ:_

```py
# Variables in Python
first_name = 'Asabeneh'
last_name = 'Yetayeh'
country = 'Finland'
city = 'Helsinki'
age = 250
is_married = True
skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
person_info = {
   'firstname':'Asabeneh',
   'lastname':'Yetayeh',
   'country':'Finland',
   'city':'Helsinki'
   }
```

Hãy sử dụng hai hàm dựng sẵn _print()_ và _len()_. Hàm print có thể nhận số lượng đối số không giới hạn. Đối số (argument) là giá trị mà chúng ta có thể truyền hoặc đặt vào bên trong dấu ngoặc đơn của hàm, xem ví dụ dưới đây.

**Ví dụ:**

```py
print('Hello, World!') # Chuỗi Hello, World! là một đối số
print('Hello',',', 'World','!') # hàm có thể nhận nhiều đối số, ở đây có bốn đối số được truyền vào
print(len('Hello, World!')) # hàm này chỉ nhận một đối số
```

Hãy in ra và tìm độ dài của các biến đã khai báo ở trên:

**Ví dụ:**

```py
# Printing the values stored in the variables

print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)
```

### Khai báo nhiều biến trên một dòng

Chúng ta cũng có thể khai báo nhiều biến chỉ trong một dòng:

**Ví dụ:**

```py
first_name, last_name, country, age, is_married = 'Asabeneh', 'Yetayeh', 'Helsink', 250, True

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)
```

Lấy dữ liệu nhập từ người dùng bằng hàm dựng sẵn _input()_. Hãy gán dữ liệu nhận được từ người dùng vào các biến first_name và age.
**Ví dụ:**

```py
first_name = input('What is your name: ')
age = input('How old are you? ')

print(first_name)
print(age)
```

## Kiểu dữ liệu

Python có nhiều kiểu dữ liệu khác nhau. Để xác định kiểu dữ liệu, chúng ta dùng hàm dựng sẵn _type_. Mình muốn bạn tập trung tìm hiểu thật kỹ các kiểu dữ liệu khác nhau. Trong lập trình, mọi thứ đều xoay quanh kiểu dữ liệu. Mình đã giới thiệu về kiểu dữ liệu ngay từ đầu, và nó sẽ còn xuất hiện lại nhiều lần, vì hầu như chủ đề nào cũng liên quan đến kiểu dữ liệu. Chúng ta sẽ tìm hiểu kỹ hơn về kiểu dữ liệu ở các phần tương ứng sau này.

## Kiểm tra kiểu dữ liệu và ép kiểu

- Kiểm tra kiểu dữ liệu: Để kiểm tra kiểu dữ liệu của một dữ liệu/biến nào đó, chúng ta dùng _type_
  **Ví dụ:**

```py
# Different python data types
# Let's declare variables with various data types

first_name = 'Asabeneh'     # str
last_name = 'Yetayeh'       # str
country = 'Finland'         # str
city= 'Helsinki'            # str
age = 250                   # int, it is not my real age, don't worry about it

# Printing out types
print(type('Asabeneh'))          # str
print(type(first_name))          # str
print(type(10))                  # int
print(type(3.14))                # float
print(type(1 + 1j))              # complex
print(type(True))                # bool
print(type([1, 2, 3, 4]))        # list
print(type({'name':'Asabeneh'})) # dict
print(type((1,2)))               # tuple
print(type(zip([1,2],[3,4])))    # zip
```

- Ép kiểu (Casting): Chuyển đổi từ kiểu dữ liệu này sang kiểu dữ liệu khác. Chúng ta dùng _int()_, _float()_, _str()_, _list_, _set_
  Khi thực hiện các phép toán số học, chuỗi số phải được chuyển sang int hoặc float trước, nếu không sẽ báo lỗi. Nếu nối (concatenate) một số với một chuỗi, số đó phải được chuyển thành chuỗi trước. Chúng ta sẽ nói về phép nối chuỗi ở phần String.

  **Ví dụ:**

```py
# int to float
num_int = 10
print('num_int',num_int)         # 10
num_float = float(num_int)
print('num_float:', num_float)   # 10.0

# float to int
gravity = 9.81
print(int(gravity))             # 9

# int to str
num_int = 10
print(num_int)                  # 10
num_str = str(num_int)
print(num_str)                  # '10'

# str to int or float
num_str = '10.6'
num_float = float(num_str)  # Convert the string to a float first
num_int = int(num_float)    # Then convert the float to an integer
print('num_int', int(num_str))      # 10
print('num_float', float(num_str))  # 10.6
num_int = int(num_float)
print('num_int', int(num_int))      # 10

# str to list
first_name = 'Asabeneh'
print(first_name)               # 'Asabeneh'
first_name_to_list = list(first_name)
print(first_name_to_list)            # ['A', 's', 'a', 'b', 'e', 'n', 'e', 'h']
```

## Số

Number data types in Python:

Các kiểu dữ liệu số trong Python:

1. Số nguyên (Integers): Các số nguyên (âm, không và dương)
   Ví dụ:
   ... -3, -2, -1, 0, 1, 2, 3 ...

2. Số thực dấu phẩy động (Floating Point Numbers) - số thập phân
   Ví dụ:
   ... -3.5, -2.25, -1.0, 0.0, 1.1, 2.2, 3.5 ...

3. Số phức (Complex Numbers)
   Ví dụ:
   1 + j, 2 + 4j, 1 - 1j

🌕 Bạn thật tuyệt vời! Bạn vừa hoàn thành thử thách ngày 2 và đã tiến thêm hai bước gần hơn đến thành công. Giờ hãy làm vài bài tập để rèn luyện cho cả não lẫn tay nhé.

## 💻 Bài tập - Ngày 2

### Bài tập: Cấp độ 1

1. Bên trong thư mục 30DaysOfPython, tạo một thư mục tên là day_2. Bên trong thư mục này, tạo một file tên là variables.py
2. Viết một comment Python với nội dung 'Day 2: 30 Days of python programming'
3. Khai báo biến first name và gán giá trị cho nó
4. Khai báo biến last name và gán giá trị cho nó
5. Khai báo biến full name và gán giá trị cho nó
6. Khai báo biến country và gán giá trị cho nó
7. Khai báo biến city và gán giá trị cho nó
8. Khai báo biến age và gán giá trị cho nó
9. Khai báo biến year và gán giá trị cho nó
10. Khai báo biến is_married và gán giá trị cho nó
11. Khai báo biến is_true và gán giá trị cho nó
12. Khai báo biến is_light_on và gán giá trị cho nó
13. Khai báo nhiều biến trên cùng một dòng

### Bài tập: Cấp độ 2

1. Kiểm tra kiểu dữ liệu của tất cả các biến bạn đã khai báo bằng hàm dựng sẵn type()
2. Dùng hàm dựng sẵn _len()_ để tìm độ dài của first name của bạn
3. So sánh độ dài của first name và last name của bạn
4. Khai báo 5 là num_one và 4 là num_two
5. Cộng num_one và num_two rồi gán giá trị cho biến total
6. Lấy num_one trừ num_two rồi gán giá trị cho biến diff
7. Nhân num_two và num_one rồi gán giá trị cho biến product
8. Chia num_one cho num_two rồi gán giá trị cho biến division
9. Dùng phép chia lấy dư (modulus) để tính num_two chia cho num_one rồi gán giá trị cho biến remainder
10. Tính num_one lũy thừa num_two rồi gán giá trị cho biến exp
11. Tìm phép chia lấy phần nguyên (floor division) của num_one cho num_two rồi gán giá trị cho biến floor_division
12. Bán kính của một hình tròn là 30 mét.
    1. Tính diện tích hình tròn và gán giá trị cho biến tên là _area_of_circle_
    2. Tính chu vi hình tròn và gán giá trị cho biến tên là _circum_of_circle_
    3. Lấy bán kính từ người dùng nhập vào và tính diện tích.
13. Dùng hàm dựng sẵn input để lấy first name, last name, country và age từ người dùng, rồi lưu giá trị vào các biến tương ứng
14. Chạy help('keywords') trong Python shell hoặc trong file của bạn để xem các từ khóa dành riêng (reserved words/keywords) của Python

🎉 CHÚC MỪNG BẠN! 🎉

[<< Ngày 1](../readme.md) | [Ngày 3 >>](../03_Day_Operators/03_operators.md)
