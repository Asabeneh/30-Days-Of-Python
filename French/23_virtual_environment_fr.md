<div align="center">
  <h1> 30 Jours de Python : Jour 23 - Environnement Virtuel </h1>
  <a class="header-badge" target="_blank" href="https://www.linkedin.com/in/asabeneh/">
  <img src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&logo=linkedin&style=social">
  </a>
  <a class="header-badge" target="_blank" href="https://twitter.com/Asabeneh">
  <img alt="Twitter Follow" src="https://img.shields.io/twitter/follow/asabeneh?style=social">
  </a>

<sub>Auteur :
<a href="https://www.linkedin.com/in/asabeneh/" target="_blank">Asabeneh Yetayeh</a><br>
<small>Deuxième édition : juillet 2021</small>
</sub>
</div>

[<< Jour 22](./22_web_scraping_fr.md) | [Jour 24 >>](./24_statistics_fr.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 Jour 23](#-jour-23)
  - [Configuration des environnements virtuels](#configuration-des-environnements-virtuels)
  - [💻 Exercices : Jour 23](#-exercices-jour-23)

# 📘 Jour 23

## Configuration des environnements virtuels

Pour commencer un projet, il est préférable d'avoir un environnement virtuel. Un environnement virtuel peut nous aider à créer un environnement isolé ou séparé. Cela nous aidera à éviter les conflits de dépendances entre projets. Si vous tapez pip freeze sur votre terminal, vous verrez tous les paquets installés sur votre ordinateur. Si nous utilisons virtualenv, nous n'accéderons qu'aux paquets spécifiques à ce projet. Ouvrez votre terminal et installez virtualenv.

```sh
asabeneh@Asabeneh:~$ pip install virtualenv
```

Dans le dossier 30DaysOfPython, créez un dossier flask_project.

Après avoir installé le paquet virtualenv, allez dans votre dossier de projet et créez un environnement virtuel en tapant :

Pour Mac/Linux :
```sh
asabeneh@Asabeneh:~/Desktop/30DaysOfPython/flask_project$ virtualenv venv

```

Pour Windows :
```sh
C:\Users\User\Documents\30DaysOfPython\flask_project>python -m venv venv
```

Je préfère appeler le nouveau projet venv, mais n'hésitez pas à le nommer différemment. Vérifions si le venv a été créé en utilisant la commande ls (ou dir pour l'invite de commande Windows).

```sh
asabeneh@Asabeneh:~/Desktop/30DaysOfPython/flask_project$ ls
venv/
```

Activons l'environnement virtuel en tapant la commande suivante dans notre dossier de projet.

Pour Mac/Linux :
```sh
asabeneh@Asabeneh:~/Desktop/30DaysOfPython/flask_project$ source venv/bin/activate
```
L'activation de l'environnement virtuel sous Windows peut varier entre Windows Power Shell et git bash.

Pour Windows Power Shell :
```sh
C:\Users\User\Documents\30DaysOfPython\flask_project> venv\Scripts\activate
```

Pour Windows Git bash :
```sh
C:\Users\User\Documents\30DaysOfPython\flask_project> venv\Scripts\. activate
```

Après avoir écrit la commande d'activation, votre dossier de projet commencera par venv. Voir l'exemple ci-dessous.

```sh
(venv) asabeneh@Asabeneh:~/Desktop/30DaysOfPython/flask_project$
```

Maintenant, vérifions les paquets disponibles dans ce projet en tapant pip freeze. Vous ne verrez aucun paquet.

Nous allons réaliser un petit projet flask, alors installons le paquet flask dans ce projet.

```sh
(venv) asabeneh@Asabeneh:~/Desktop/30DaysOfPython/flask_project$ pip install Flask
```

Maintenant, tapons pip freeze pour voir la liste des paquets installés dans le projet :

```sh
(venv) asabeneh@Asabeneh:~/Desktop/30DaysOfPython/flask_project$ pip freeze
Click==7.0
Flask==1.1.1
itsdangerous==1.1.0
Jinja2==2.10.3
MarkupSafe==1.1.1
Werkzeug==0.16.0
```

Quand vous avez terminé, vous devez désactiver l'environnement actif en utilisant _deactivate_.

```sh
(venv) asabeneh@Asabeneh:~/Desktop/30DaysOfPython$ deactivate
```

Les modules nécessaires pour travailler avec flask sont installés. Maintenant, votre dossier de projet est prêt pour un projet flask. Vous devez inclure le dossier venv dans votre fichier .gitignore pour ne pas le pousser sur GitHub.

## 💻 Exercices : Jour 23

1. Créez un dossier de projet avec un environnement virtuel basé sur l'exemple donné ci-dessus.

🎉 FÉLICITATIONS ! 🎉

[<< Jour 22](./22_web_scraping_fr.md) | [Jour 24 >>](./24_statistics_fr.md)
