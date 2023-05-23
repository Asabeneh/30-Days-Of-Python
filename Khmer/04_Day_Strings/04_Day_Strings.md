<div align="center">
  <h1> 30 Days Of Python: Day 4 - Strings</h1>
  <a class="header-badge" target="_blank" href="https://www.linkedin.com/in/asabeneh/">
  <img src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&logo=linkedin&style=social">
  </a>
  <a class="header-badge" target="_blank" href="https://twitter.com/Asabeneh">
  <img alt="Twitter Follow" src="https://img.shields.io/twitter/follow/asabeneh?style=social">
  </a>

<sub>Author:
<a href="https://www.linkedin.com/in/asabeneh/" target="_blank">Asabeneh Yetayeh</a><br>
<small> Second Edition: July, 2021</small>
</sub>

</div>

[<< Day 3](../03_Day_Operators/03_Day_Operators.md) | [Day 5 >>](../05_Day_Lists/05_lists.md)

![30DaysOfPython](../../images/30DaysOfPython_banner3@2x.png)

- [Day 4](#day-4)
  - [សំណុំអក្សរ](#strings)
    - [ការបង្កេីតសំណុំអក្សរមួយ](#creating-a-string)
    - [ការផ្កុំសំណុំអក្សរ](#string-concatenation)
    - [ការដកឃ្លា រឺ ចុះបន្ទាត់ក្នុងសំណុំអក្សរ](#escape-sequences-in-strings)
    - [ការរៀបចំទ្រង់ទ្រាយសំណុំអក្សរ](#string-formatting)
      - [ការរៀបចំទ្រង់ទ្រាយសំណុំអក្សរតាមរបៀបចាស់(% Operator)](#old-style-string-formatting--operator)
      - [ការរៀបចំទ្រង់ទ្រាយសំណុំអក្សរតាមរបៀបថ្មី (str.format)](#new-style-string-formatting-strformat)
      - [ការដាក់បញ្ចូលសំណុំអក្សរ / f-Strings (Python 3.6+)](#string-interpolation--f-strings-python-36)
    - [Python សំណុំអក្សរជាលំដាប់នៃតួអក្សរ](#python-strings-as-sequences-of-characters)
      - [ការពង្រាយតួអក្សរ](#unpacking-characters)
      - [ការចូលដំណើរការ តួអក្សរ ក្នុង សំណុំអក្សរ ដោយ កម្រិតនៃតួអក្សរ](#accessing-characters-in-strings-by-index)
      - [ការកាត់សំណុំអក្សរក្នុងPython](#slicing-python-strings)
      - [ការត្រលប់សំណុំអក្សរ](#reversing-a-string)
      - [ការរំលងតួរអក្សរ កំឡុងពេលកាត់](#skipping-characters-while-slicing)
    - [វិធីសាស្ត្រ ប្រេីប្រាស់សំណុំអក្សរ](#string-methods)
  - [💻 លំហាត់ - Day 4](#-exercises---day-4)
