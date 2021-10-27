# Projet-FranceInter

Création d'une solution technologique assurant la distanciation sociale dans leurs studios d’enregistrement.

France Inter utilise une caméra IP dans chacun des studios d’enregistrement et nous met à disposition une image issue de la caméra toutes les X secondes.

Nous devions écrire un programme prenant en entrée l’image pour y détecter le respect des règles de distanciation. Si la distanciation n’est pas respectée, un message audio en français et en anglais doit être diffusé.

Le cahier des charges indique :

les studios étant de taille réduite, seul X personnes en simultané sont admises pour considérer que la distanciation est respectée. Ce nombre doit être paramétrable depuis le backoffice.
le message audio doit être diffusé en français et en anglais
le message audio diffusé doit être entré sur un backoffice sous forme d’une chaîne de caractères. L’application doit automatiquement générer le message audio à partir du texte.
Attention : l’équipe RF qui administrera l’application étant francophone, le message doit être inscrit dans le backoffice uniquement en français.
L’application se chargera automatiquement de le traduire en anglais avant la diffusion.

Le projet a été réalisé en deux étapes : 

La première étant la réalisation d'une interface WEB permettant à l’opérateur d’entrer le message qui sera diffusé sous forme d’une chaîne de caractère. Une fois le message entré et traité par l'application, les messages audio en français et anglais sont sauvegardés dans des fichiers.

La seconde étant de réaliser un script prenant en entrée les fichiers suivants :

l’image d’une des caméras
le fichier de configuration contenant le nombre de personnes admises (en bonus, vous pouvez ajouter des options supplémentaires)
le fichier audio en français
le fichier audio en anglais
Si le script détecte que la distanciation sociale est respectée, il s'arrête.

Si le script détecte que la distanciation sociale n’est pas respectée, il diffuse les messages audio puis s'arrête.
