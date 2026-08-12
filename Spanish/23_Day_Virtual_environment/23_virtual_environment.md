<div align="center">
  <h1> 30 días de Python: Día 23 - Entornos virtuales </h1>
  <a class="header-badge" target="_blank" href="https://www.linkedin.com/in/asabeneh/">
  <img src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&logo=linkedin&style=social">
  </a>
  <a class="header-badge" target="_blank" href="https://twitter.com/Asabeneh">
  <img alt="Twitter Follow" src="https://img.shields.io/twitter/follow/asabeneh?style=social">
  </a>

<sub>Autor:
<a href="https://www.linkedin.com/in/asabeneh/" target="_blank">Asabeneh Yetayeh</a><br>
<small> Segunda edición: julio de 2021</small>
</sub>
</div>

[<< Día 22](../22_Day_Web_scraping/22_web_scraping.md) | [Día 24 >>](../24_Day_Statistics/24_statistics.md)

![30DaysOfPython](../../images/30DaysOfPython_banner3@2x.png)

- [📘 Día 23](#-día-23)
  - [Configurar un entorno virtual](#configurar-un-entorno-virtual)
  - [💻 Ejercicios: Día 23](#-ejercicios-día-23)

# 📘 Día 23

## Configurar un entorno virtual

Al comenzar un proyecto es recomendable usar un entorno virtual. Un entorno virtual nos permite crear un entorno aislado o independiente, evitando conflictos de dependencias entre proyectos. Si ejecutas pip freeze en la terminal verás todos los paquetes instalados en la máquina. Con virtualenv solo tendrás acceso a los paquetes instalados en ese entorno específico. Abre tu terminal e instala virtualenv:

```sh
pip install virtualenv
```

Dentro de la carpeta 30DaysOfPython crea un directorio llamado flask_project.

Una vez instalado virtualenv, entra en la carpeta del proyecto y crea el entorno virtual:

Para Mac/Linux:
```sh
virtualenv venv
```

Para Windows:
```sh
python -m venv venv
```

A mí me gusta nombrar el entorno como venv, pero puedes elegir otro nombre. Usa ls (o dir en Windows) para comprobar que venv se creó:

```sh
ls
# venv/
```

Activa el entorno virtual desde la carpeta del proyecto:

Para Mac/Linux:
```sh
source venv/bin/activate
```

En Windows la activación puede variar según PowerShell o Git Bash.

Para Windows PowerShell:
```sh
venv\Scripts\activate
```

Para Windows Git Bash:
```sh
venv\Scripts\. activate
```

Tras ejecutar el comando de activación,el prompt mostrará el nombre del entorno (venv) al inicio.Ejemplo:

```sh
(venv) user@host:~/Desktop/30DaysOfPython/flask_project$
```

Ahora,si ejecutas pip freeze no verás los paquetes globales;solo los del entorno.Instalemos Flask para este proyecto:

```sh
pip install Flask
```

Después,comprobemos los paquetes instalados:

```sh
pip freeze
# ejemplo de salida:
# Click==7.0
# Flask==1.1.1
# itsdangerous==1.1.0
# Jinja2==2.10.3
# MarkupSafe==1.1.1
# Werkzeug==0.16.0
```

Cuando termines,ejecuta deactivate para salir del entorno activo:

```sh
deactivate
```

Los módulos necesarios para trabajar con Flask ya están instalados en el entorno del proyecto.Es buena práctica añadir venv al archivo .gitignore para no subir el entorno a GitHub.

## 💻 Ejercicios: Día 23

1. Crea un directorio de proyecto con un entorno virtual siguiendo el ejemplo anterior.

🎉 ¡Felicidades! 🎉

[<< Día 22](../22_Day_Web_scraping/22_web_scraping.md) | [Día 24 >>](../24_Day_Statistics/24_statistics.md)