# Qu'est-ce que c'est ?
Ceci est un jeu de Pong pour patate-app-launcher, un système d'éxploitation qui fonctionne sur raspberry pi Sense Hat.

# Installation :
Pour installer ce pong sur [patate-app-launcher](https://github.com/AstralArchitect/patate-app-launcher/), copiez l'archive install.tar.xz dans une clé USB, en suite démarrez votre ordinateur fonctionnant sous patate-app-launcher et attendez jusqu'a ce que "Bonjour" ai finit de défiler. Ensuite branchez votre clé sur n'importe quel port USB et "install..." devrait apparaître. ensuite une barre de chargement rouge va avançer et quand elle a disparue enlevez la clé USB et poussez le joystick vers le haut pour pouvoir jouer à pong sur patat-app-launcher  !

# Règles du jeu : 
Le jeu constiste à utiliser le joystick pour bouger la raquette jaune à gauche et essayer de renvoyer la balle verte sur l'énnemi vous devrez la renvoyer le plus de fois et ne pas la ratter pour gagner.


![image](https://github.com/AstralArchitect/pong-patate-app-launcher/assets/154975712/490df7b8-8bb8-4ab1-b08a-24ce0222e168)

# Créer d'autres programmes sur patate-app-launcher :
Si vous voulez créer votre propre programme sur patate-app-launcher, il faudra procéder comme suit:
  1. Créer un fichier s'appelant "name" (sans les guillemets et il ne faut aucune éxtension au fichier) et y mettre à l'interieur le nom de votre application (pas d'éspaces ni de caractères spéciaux dans le nom)
  2. créer un fichier python, vous pourrez lui donner le nom que vous voulez et y entrer le script python de votre application. J'ai donné un éxemple de script avec les librairies sense hat dans [exemple](https://github.com/AstralArchitect/pong-patateOS/blob/main/exemple/exemple.py)
  3. créer un dossier config
  4. créer un fichier qui portera le nom de votre application (ex: dans le jeu pong le dossier config contiendra "pong"(sans les guillmets et aucune éxtensions)) à l'interieur de ce fichier, entrez y le contenu suivant:" /root/python-packages/nom-de-votre-application " (sans les guillmets et remplacez nom-de-votre-appllication par le nom réel de votre application que vous avez entré dans name.
  6. enfin créez un archive compressé tar.xz (pas gz) qui contient :
       - votre fichier python
       - le dossier config
       - et le fichier name
## installer votre programme : 
Pour installer votre programme, copiez votre archive à la racine de la première partition d'une clé USB et insérez la clé dans un port USB de votre ordinateur tournant sur patate-app-launcher, ensuite l'installation se fera automatiquement.
