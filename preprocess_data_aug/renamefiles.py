
import os
from PIL import Image
import tensorflow as tf

def eh_imagem(nome_arquivo):
    if nome_arquivo.endswith('.png'):
        return True
    return False

def rename_images(input_dir, output_dir, ext='.jpg'):
    lista_de_arquivos = [nome for nome in os.listdir(input_dir) if eh_imagem(nome)]
    i = 0
    for nome in lista_de_arquivos:
        image = Image.open(os.path.join(input_dir, nome))

        nome_sem_ext = os.path.splitext(nome)[0]
        tf.keras.preprocessing.image.save_img(os.path.join(output_dir, nome_sem_ext + ext), image)
        i+=1
        print(i)

if __name__ == "__main__":
    diretorio = '/home/guilherme/PIXFORCE/REDSOFT/FRIGOBOM/5C/1/'
    test_dir = '/home/guilherme/PIXFORCE/REDSOFT/FRIGOBOM/5C/1/'

    rename_images(diretorio, test_dir)
