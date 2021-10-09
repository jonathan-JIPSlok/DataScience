import shutil
import os

"""
    O modulo shutil (shell utilities, ou utilitarios do shell) contem funções que permitem copiar, mover, renomear e apagar arquivos em seus programas python.
"""

#shutil.copy(os.path.join(os.getcwd(), "File", "newfile.py"), os.getcwd()) #Copiara o arquivo no path File para a pasta atual 

#shutil.copytree(os.path.join(os.getcwd(), "File"), os.path.join(os.getcwd(), "File_Copia"))
"""Copiara uma pasta completa, com todas as pastas e os arquivoscontidos.
    ou seja faz um Backup, no destino deve passar a pasta que criara
"""

#shutil.move(os.path.join(os.getcwd(), 'File', 'newfile.py'), os.path.join(os.getcwd(), "File_Move")) #movera o arquivo ou a pasta

#os.unlink(os.path.join(os.getcwd(), "File_Copia", "newfile.py")) # apagara o arquivo
#os.rmdir(os.path.join(os.getcwd(), "File_Copia")) #apagara a pasta, mas ela deve estar vazia
#shutil.rmtree(os.path.join(os.getcwd(), "File_Move")) #apagara a pasta e todos os arquivos dentro dela

print(list(os.walk(os.path.join(os.getcwd())))) #Percorre todas as pastas do diretorio e mostra tudo oque a dentro delas