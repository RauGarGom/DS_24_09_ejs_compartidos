from pathlib import Path
from clase import Organizador

carpeta = Path.home() / 'Desktop' / 'carpeta_EJERCICIOS'
#carpeta = os.path.join(os.path.expanduser('~'), 'Desktop', 'carpeta_EJERCICIOS')   #C:\\Users\\TuUsuario\\Desktop\\carpeta_EJERCICIOS
                                                                                    # ~ --> C:\\Users\\TuUsuario

# Crear una instancia de la clase FileOrganizer y organizar los archivos
if __name__ == "__main__":
    organizar = Organizador(carpeta)
    organizar.organize()
