from distutils.core import setup
import py2exe

setup(
    console=['question_answer.py'],  # Spécifiez le nom de votre script principal ici
    options={
        'py2exe': {
            'bundle_files': 1,  # Créez un seul fichier exécutable
            'compressed': True,  # Comprimez les bibliothèques en un fichier zip
            'optimize': 2  # Optimisez le bytecode
        }
    },
    zipfile=None  # Créez un fichier exécutable sans fichier zip supplémentaire
)
