import os
from PIL import Image
import tensorflow as tf

def eh_imagem(nome_arquivo):
    if nome_arquivo.endswith('jpg'):
        return True
    return False

def reduzir_tamanho_imagens(input_dir, output_dir, ext='.jpg'):
    lista_de_arquivos = [nome for nome in os.listdir(input_dir) if eh_imagem(nome)]
    i = 0
    for nome in lista_de_arquivos:
        imagem = Image.open(os.path.join(input_dir, nome))
        image = tf.image.rot90(imagem)
        image = tf.image.rot90(image)
        image = tf.image.rot90(image)
        hor_image = tf.image.flip_left_right(image)

        nome_sem_ext = os.path.splitext(nome)[0]
        tf.keras.preprocessing.image.save_img(os.path.join(output_dir, 'hor_rot_270_' + nome_sem_ext + ext), hor_image)
        i+=1
        print(i)


if __name__ == "__main__":
    diretorio = '/home/guilherme/PIXFORCE/REDSOFT/MARFRIG/IN_LOCO/output4/train/class_1/'
    test_dir = '/home/guilherme/PIXFORCE/REDSOFT/MARFRIG/IN_LOCO/output4/train/aug1/'

    reduzir_tamanho_imagens(diretorio, test_dir)