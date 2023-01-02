# Marienbad

A simple toolsuite for help you to win at [Marienbad](https://fr.wikipedia.org/wiki/Jeu_de_Marienbad) game, a [Nim](https://en.wikipedia.org/wiki/Nim) game.

It is recommended to use the [PyPy](https://www.pypy.org/) interpreter instead of the CPython standart.

## Generator

Pour utiliser cet outil, entrez la commande :
```bash
marienbad-generator
```

Pour voir toutes les options disponibles :
```bash
marienbad-generator --help
```

Vous pouvez aussi le démarrer depuis un script python :
```python
import marienbad
marienbad.generator.main()
```

Bien sûr, vous pourvez ré-utiliser certaines fonctions :
```python
from marienbad.generator import checkCombination
checkCombination([1,3,5,7]) # True
checkCombination([1,3,6,7]) # False
```

La fonction `generateTable` imprime le résultat sur la sortie standart. Pour récupérer cette sortie, utilisez le script suivant :
```python
import sys
from io import StringIO

# rediriger stdout dans un buffer :
sys.stdout = StringIO()

# appel de la fonction qui remplira stdout (donc le buffer)
generateTable(10,10)

# récupérer le contenu du buffer :
s = sys.stdout.getvalue()

# fermer le buffer :
sys.stdout.close()

# rediriger stdout vers la sortie standart :
sys.stdout = sys.__stdout__

# le résultat est maintenant dans la variable s
```
