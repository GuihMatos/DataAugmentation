import os
from PIL import Image


def eh_imagem(nome_arquivo):
    if nome_arquivo.endswith('jpg'):
        return True
    return False

def resize_images(input_dir, output_dir, ext='.jpg'):
    lista_de_arquivos = [nome for nome in os.listdir(input_dir) if eh_imagem(nome)]
    i = 0
    for nome in lista_de_arquivos:
        imagem = Image.open(os.path.join(input_dir, nome))
        redimensionada = imagem.resize((512, 512))
        nome_sem_ext = os.path.splitext(nome)[0]
        redimensionada.save(os.path.join(output_dir, nome_sem_ext + ext))
        i+=1
        print(i)

if __name__ == "__main__":
    diretorio = '/home/guilherme/PIXFORCE/REDSOFT/MARFRIG/2022-10-31/class_8/'
    input_folder2 = '/home/guilherme/PIXFORCE/REDSOFT/MARFRIG/2022-10-31/class_8/'

    resize_images(diretorio, input_folder2)