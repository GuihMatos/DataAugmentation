import cv2
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
    s800x1944 = 0
    s2560x1440 = 0
    s1280x720 = 0
    other_shape = 0

    #img1 = Image.open(img)
    color = [0, 0, 0]

    for nome in lista_de_arquivos:
        img = cv2.imread(os.path.join(input_dir, nome))
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        
        if img.shape == (1944,800, 3):
            # border widths
            left, right = [572]*2
            s800x1944 += 1
            img = cv2.copyMakeBorder(img, 0, 0, left, right, cv2.BORDER_CONSTANT, value=color)
            #             img[start_row:end_row, start_col:end_col]
            img_cortada = img[390:1555, 390:1555]

            nome_sem_ext = os.path.splitext(nome)[0]
            tf.keras.preprocessing.image.save_img(os.path.join(output_dir, nome_sem_ext + ext), img_cortada)
        elif img.shape == (1280,720, 3):
            # border widths
            s1280x720 += 1
            #             img[start_row:end_row, start_col:end_col]
            img_cortada = img[290:1010, 0:720]

            nome_sem_ext = os.path.splitext(nome)[0]
            tf.keras.preprocessing.image.save_img(os.path.join(output_dir, nome_sem_ext + ext), img_cortada)
        elif img.shape == (2560,1440, 3):
            # border widths
            s2560x1440 += 1
            #             img[start_row:end_row, start_col:end_col]
            img_cortada = img[590:2030, 0:1440]

            nome_sem_ext = os.path.splitext(nome)[0]
            tf.keras.preprocessing.image.save_img(os.path.join(output_dir, nome_sem_ext + ext), img_cortada)
        else:
            other_shape += 1
        
        i+=1
        print(i)
    print(f"Quantidade 800x1944: {s800x1944}\nQuantidade s1440x2560: {s2560x1440}\nQuantidade s720x1280: {s1280x720}\nQuantidade shape desconhecido: {other_shape}")

if __name__ == "__main__":
    diretorio = '/home/guilherme/reviewed/1/'
    test_dir = '/home/guilherme/reviewed/1/'

    reduzir_tamanho_imagens(diretorio, test_dir)
