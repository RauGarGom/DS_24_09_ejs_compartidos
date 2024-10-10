import os
import shutil
from pathlib import Path

class Organizador:

    def __init__(self, carpeta):
        self.carpeta = carpeta
        self.doc_types = ('.doc', '.docx', '.txt', '.pdf', '.xls', '.ppt', '.xlsx', '.pptx')
        self.img_types = ('.jpg', '.jpeg', '.png', '.svg', '.gif')
        self.software_types = ('.exe', '.py', '.ipynb')
        self.carpetas = ['Imagenes', 'Documentos', 'Software', 'Otros']
    

    def crear_carpeta(self):
        for carpeta in self.carpetas:
            carpeta_path = os.path.join(self.carpeta, carpeta)
            if not os.path.exists(carpeta_path):
                os.makedirs(carpeta_path)
    
    
    def mover_fichero(self, nombre_archivo):
        archivo_path = os.path.join(self.carpeta, nombre_archivo)
        
        if archivo_path.endswith(self.img_types):
            shutil.move(archivo_path, os.path.join(self.carpeta, 'Imagenes', nombre_archivo))

        elif nombre_archivo.endswith(self.doc_types):
            shutil.move(archivo_path, os.path.join(self.carpeta, 'Documentos', nombre_archivo))

        elif nombre_archivo.endswith(self.software_types):
            shutil.move(archivo_path, os.path.join(self.carpeta, 'Software', nombre_archivo))

        else:
            shutil.move(archivo_path, os.path.join(self.carpeta, 'Otros', nombre_archivo))

    
    def organizar(self):
        self.crear_carpetas()
        
        for nombre_archivo in os.listdir(self.carpeta):
            archivo_path = os.path.join(self.carpeta, nombre_archivo)

