import os
import codecs

total_lines = 0

# Diretório que contém os arquivos .py
# pegar o diretorio atual
directory = os.getcwd()

# Loop através de todos os arquivos no diretório
for filename in os.listdir(directory):
    if filename.endswith(".py"):
        # Abre o arquivo em modo de leitura de texto
        with codecs.open(os.path.join(directory, filename), "r", "utf-8") as file:
            # Conta o número de linhas no arquivo e adiciona ao total
            file_lines = len(file.readlines())
            total_lines += file_lines
        continue
    else:
        continue

print("O numero total de linhas de codigo em arquivos .py eh:", total_lines)