import os
import math
import random 
from PIL import Image
import tensorflow as tf
import tensorflow_addons as tfa

def eh_imagem(nome_arquivo):
    if nome_arquivo.endswith('jpg'):
        return True
    return False

def reduzir_tamanho_imagens(input_dir, output_dir, ext='.jpg'):
    lista_de_arquivos = [nome for nome in os.listdir(input_dir) if eh_imagem(nome)]
    i = 0
    upper = 0 * (math.pi/180.0) # degrees -> radian
    lower = 360 * (math.pi/180.0)
    up_low = random.uniform(lower, upper)
    for nome in lista_de_arquivos:
        imagem = Image.open(os.path.join(input_dir, nome))
        image = tfa.image.rotate(imagem, up_low)

        nome_sem_ext = os.path.splitext(nome)[0]
        tf.keras.preprocessing.image.save_img(os.path.join(output_dir, 'rand_rot_12' + nome_sem_ext + ext), image)
        i+=1
        print(i)


if __name__ == "__main__":
    diretorio = '/home/guilherme/PIXFORCE/REDSOFT/FRIGOBOM/5C/output3/val/5/'
    test_dir = '/home/guilherme/PIXFORCE/REDSOFT/FRIGOBOM/5C/output3/val/aug5/'

    reduzir_tamanho_imagens(diretorio, test_dir)