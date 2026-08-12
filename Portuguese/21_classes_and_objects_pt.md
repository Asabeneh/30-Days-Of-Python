<div align="center">
  <h1> 30 Dias de Python: Dia 21 - Classes e Objetos</h1>
  <a class="header-badge" target="_blank" href="https://www.linkedin.com/in/asabeneh/">
  <img src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&logo=linkedin&style=social">
  </a>
  <a class="header-badge" target="_blank" href="https://twitter.com/Asabeneh">
  <img alt="Twitter Follow" src="https://img.shields.io/twitter/follow/asabeneh?style=social">
  </a>

<sub>Autor:
<a href="https://www.linkedin.com/in/asabeneh/" target="_blank">Asabeneh Yetayeh</a><br>
<small>Segunda edição: Julho, 2021</small>
</sub>

</div>

[<< Dia 20](./20_python_package_manager_pt.md) | [Dia 22 >>](./22_web_scraping_pt.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 Dia 21](#-dia-21)
  - [Classes e Objetos](#classes-e-objetos)
    - [Criando uma Classe](#criando-uma-classe)
    - [Criando um Objeto](#criando-um-objeto)
    - [Construtor da Classe](#construtor-da-classe)
    - [Métodos do Objeto](#métodos-do-objeto)
    - [Métodos Padrão do Objeto](#métodos-padrão-do-objeto)
    - [Método para Modificar os Valores Padrão da Classe](#método-para-modificar-os-valores-padrão-da-classe)
    - [Herança](#herança)
    - [Sobrescrevendo o Método do Pai](#sobrescrevendo-o-método-do-pai)
  - [💻 Exercícios: Dia 21](#-exercícios-dia-21)
    - [Exercícios: Nível 1](#exercícios-nível-1)
    - [Exercícios: Nível 2](#exercícios-nível-2)
    - [Exercícios: Nível 3](#exercícios-nível-3)

# 📘 Dia 21

## Classes e Objetos

Python é uma linguagem de programação orientada a objetos. Tudo em Python é um objeto, com suas propriedades e métodos. Um número, uma string, uma lista, um dicionário, uma tupla, um set etc. usados em um programa são objetos de uma classe integrada correspondente. Criamos uma classe para criar um objeto. Uma classe é como um construtor de objetos, ou um "modelo" (blueprint) para criar objetos. Instanciamos uma classe para criar um objeto. A classe define os atributos e o comportamento do objeto, enquanto o objeto, por sua vez, representa a classe.

Já estamos trabalhando com classes e objetos desde o início deste desafio, sem saber. Todo elemento em um programa Python é um objeto de uma classe.
Vamos verificar se tudo em python é uma classe:

```py
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> num = 10
>>> type(num)
<class 'int'>
>>> string = 'string'
>>> type(string)
<class 'str'>
>>> boolean = True
>>> type(boolean)
<class 'bool'>
>>> lst = []
>>> type(lst)
<class 'list'>
>>> tpl = ()
>>> type(tpl)
<class 'tuple'>
>>> set1 = set()
>>> type(set1)
<class 'set'>
>>> dct = {}
>>> type(dct)
<class 'dict'>
```

### Criando uma Classe

Para criar uma classe precisamos da palavra-chave **class** seguida do nome e dois pontos. O nome da classe deve estar em **CamelCase**.

```sh
# sintaxe
class ClassName:
  código vai aqui
```

**Exemplo:**

```py
class Person:
  pass
print(Person)
```

```sh
<__main__.Person object at 0x10804e510>
```

### Criando um Objeto

Podemos criar um objeto chamando a classe.

```py
p = Person()
print(p)
```

### Construtor da Classe

Nos exemplos acima, criamos um objeto a partir da classe Person. No entanto, uma classe sem construtor não é muito útil em aplicações reais. Vamos usar uma função construtora para tornar nossa classe mais útil. Assim como a função construtora em Java ou JavaScript, Python também possui uma função construtora integrada **__init__**(). A função construtora **__init__** tem o parâmetro self, que é uma referência à instância atual da classe
**Exemplos:**

```py
class Person:
      def __init__ (self, name):
        # self permite associar um parâmetro à classe
          self.name =name

p = Person('Asabeneh')
print(p.name)
print(p)
```

```sh
# saída
Asabeneh
<__main__.Person object at 0x2abf46907e80>
```

Vamos adicionar mais parâmetros à função construtora.

```py
class Person:
      def __init__(self, firstname, lastname, age, country, city):
          self.firstname = firstname
          self.lastname = lastname
          self.age = age
          self.country = country
          self.city = city


p = Person('Asabeneh', 'Yetayeh', 250, 'Finland', 'Helsinki')
print(p.firstname)
print(p.lastname)
print(p.age)
print(p.country)
print(p.city)
```

```sh
# saída
Asabeneh
Yetayeh
250
Finland
Helsinki
```

### Métodos do Objeto

Objetos podem ter métodos. Os métodos são funções que pertencem ao objeto.

**Exemplo:**

```py
class Person:
      def __init__(self, firstname, lastname, age, country, city):
          self.firstname = firstname
          self.lastname = lastname
          self.age = age
          self.country = country
          self.city = city
      def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}'

p = Person('Asabeneh', 'Yetayeh', 250, 'Finland', 'Helsinki')
print(p.person_info())
```

```sh
# saída
Asabeneh Yetayeh is 250 years old. He lives in Helsinki, Finland
```

### Métodos Padrão do Objeto

Às vezes, você pode querer ter valores padrão para os métodos do seu objeto. Se dermos valores padrão para os parâmetros no construtor, podemos evitar erros ao chamar ou instanciar nossa classe sem parâmetros. Vamos ver como fica:

**Exemplo:**

```py
class Person:
      def __init__(self, firstname='Asabeneh', lastname='Yetayeh', age=250, country='Finland', city='Helsinki'):
          self.firstname = firstname
          self.lastname = lastname
          self.age = age
          self.country = country
          self.city = city

      def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}.'

p1 = Person()
print(p1.person_info())
p2 = Person('John', 'Doe', 30, 'Nomanland', 'Noman city')
print(p2.person_info())
```

```sh
# saída
Asabeneh Yetayeh is 250 years old. He lives in Helsinki, Finland.
John Doe is 30 years old. He lives in Noman city, Nomanland.
```

### Método para Modificar os Valores Padrão da Classe

No exemplo abaixo, a classe person, todos os parâmetros do construtor têm valores padrão. Além disso, temos o parâmetro skills, que podemos acessar usando um método. Vamos criar o método add_skill para adicionar habilidades à lista de habilidades.

```py
class Person:
      def __init__(self, firstname='Asabeneh', lastname='Yetayeh', age=250, country='Finland', city='Helsinki'):
          self.firstname = firstname
          self.lastname = lastname
          self.age = age
          self.country = country
          self.city = city
          self.skills = []

      def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}.'
      def add_skill(self, skill):
          self.skills.append(skill)

p1 = Person()
print(p1.person_info())
p1.add_skill('HTML')
p1.add_skill('CSS')
p1.add_skill('JavaScript')
p2 = Person('John', 'Doe', 30, 'Nomanland', 'Noman city')
print(p2.person_info())
print(p1.skills)
print(p2.skills)
```

```sh
# saída
Asabeneh Yetayeh is 250 years old. He lives in Helsinki, Finland.
John Doe is 30 years old. He lives in Noman city, Nomanland.
['HTML', 'CSS', 'JavaScript']
[]
```

### Herança

Usando herança podemos reaproveitar o código da classe pai. A herança nos permite definir uma classe que herda todos os métodos e propriedades da classe pai. A classe pai ou super ou base é a classe que fornece todos os métodos e propriedades. A classe filha é a classe que herda de outra classe, a classe pai.
Vamos criar uma classe student herdando da classe person.

```py
class Student(Person):
    pass


s1 = Student('Eyob', 'Yetayeh', 30, 'Finland', 'Helsinki')
s2 = Student('Lidiya', 'Teklemariam', 28, 'Finland', 'Espoo')
print(s1.person_info())
s1.add_skill('JavaScript')
s1.add_skill('React')
s1.add_skill('Python')
print(s1.skills)

print(s2.person_info())
s2.add_skill('Organizing')
s2.add_skill('Marketing')
s2.add_skill('Digital Marketing')
print(s2.skills)

```

```sh
saída
Eyob Yetayeh is 30 years old. He lives in Helsinki, Finland.
['JavaScript', 'React', 'Python']
Lidiya Teklemariam is 28 years old. He lives in Espoo, Finland.
['Organizing', 'Marketing', 'Digital Marketing']
```

Não chamamos o construtor **__init__**() na classe filha. Se não o chamamos, ainda podemos acessar todas as propriedades da classe pai. Mas se chamarmos o construtor, podemos acessar as propriedades do pai chamando _super_.  
Podemos adicionar um novo método à classe filha ou podemos sobrescrever os métodos da classe pai criando um método com o mesmo nome na classe filha. Quando adicionamos a função **__init__**(), a classe filha não vai mais herdar a função **__init__**() do pai.

### Sobrescrevendo o Método do Pai

```py
class Student(Person):
    def __init__ (self, firstname='Asabeneh', lastname='Yetayeh',age=250, country='Finland', city='Helsinki', gender='male'):
        self.gender = gender
        super().__init__(firstname, lastname,age, country, city)
    def person_info(self):
        gender = 'He' if self.gender =='male' else 'She'
        return f'{self.firstname} {self.lastname} is {self.age} years old. {gender} lives in {self.city}, {self.country}.'

s1 = Student('Eyob', 'Yetayeh', 30, 'Finland', 'Helsinki','male')
s2 = Student('Lidiya', 'Teklemariam', 28, 'Finland', 'Espoo', 'female')
print(s1.person_info())
s1.add_skill('JavaScript')
s1.add_skill('React')
s1.add_skill('Python')
print(s1.skills)

print(s2.person_info())
s2.add_skill('Organizing')
s2.add_skill('Marketing')
s2.add_skill('Digital Marketing')
print(s2.skills)
```

```sh
Eyob Yetayeh is 30 years old. He lives in Helsinki, Finland.
['JavaScript', 'React', 'Python']
Lidiya Teklemariam is 28 years old. She lives in Espoo, Finland.
['Organizing', 'Marketing', 'Digital Marketing']
```

Podemos usar a função integrada super() ou o nome da classe pai Person para herdar automaticamente os métodos e propriedades da sua classe pai. No exemplo acima, sobrescrevemos o método do pai. O método da classe filha tem uma característica diferente: ele consegue identificar se o gênero é masculino ou feminino e atribuir o pronome apropriado (He/She).

🌕 Agora você está totalmente carregado com o superpoder da programação. Agora faça alguns exercícios para o cérebro e os músculos.

## 💻 Exercícios: Dia 21

### Exercícios: Nível 1

1. Python tem o módulo chamado _statistics_ e podemos usar esse módulo para fazer todos os cálculos estatísticos. No entanto, para aprender a criar e reutilizar funções, vamos tentar desenvolver um programa que calcule as medidas de tendência central de uma amostra (média, mediana, moda) e as medidas de variabilidade (amplitude, variância, desvio padrão). Além dessas medidas, encontre o mínimo, o máximo, a contagem, o percentil e a distribuição de frequência da amostra. Você pode criar uma classe chamada Statistics e criar todas as funções que fazem os cálculos estatísticos como métodos da classe Statistics. Verifique a saída abaixo.

```py
ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]

print('Count:', data.count()) # 25
print('Sum: ', data.sum()) # 744
print('Min: ', data.min()) # 24
print('Max: ', data.max()) # 38
print('Range: ', data.range()) # 14
print('Mean: ', data.mean()) # 30
print('Median: ', data.median()) # 29
print('Mode: ', data.mode()) # {'mode': 26, 'count': 5}
print('Standard Deviation: ', data.std()) # 4.2
print('Variance: ', data.var()) # 17.5
print('Frequency Distribution: ', data.freq_dist()) # [(20.0, 26), (16.0, 27), (12.0, 32), (8.0, 37), (8.0, 34), (8.0, 33), (8.0, 31), (8.0, 24), (4.0, 38), (4.0, 29), (4.0, 25)]
```

```sh
# sua saída deve ser parecida com esta
print(data.describe())
Count: 25
Sum:  744
Min:  24
Max:  38
Range:  14
Mean:  30
Median:  29
Mode:  (26, 5)
Variance:  17.5
Standard Deviation:  4.2
Frequency Distribution: [(20.0, 26), (16.0, 27), (12.0, 32), (8.0, 37), (8.0, 34), (8.0, 33), (8.0, 31), (8.0, 24), (4.0, 38), (4.0, 29), (4.0, 25)]
```

### Exercícios: Nível 2

1. Crie uma classe chamada PersonAccount. Ela possui as propriedades firstname, lastname, incomes, expenses e os métodos total_income, total_expense, account_info, add_income, add_expense e account_balance. Incomes é um conjunto de receitas e suas descrições. O mesmo vale para expenses.

🎉 PARABÉNS ! 🎉

[<< Dia 20](./20_python_package_manager_pt.md) | [Dia 22 >>](./22_web_scraping_pt.md)
