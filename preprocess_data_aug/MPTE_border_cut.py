import cv2
import os
import tensorflow as tf

def eh_imagem(nome_arquivo):
    if nome_arquivo.endswith('jpg'):
        return True
    return False

def reduzir_tamanho_imagens(input_dir, output_dir, ext='.jpg'):
    lista_de_arquivos = [nome for nome in os.listdir(input_dir) if eh_imagem(nome)]
    i = 0
    s800x2688 = 0
    s800x2592 = 0
    other_shape = 0

    #img1 = Image.open(img)
    color = [0, 0, 0]

    for nome in lista_de_arquivos:
        img = cv2.imread(os.path.join(input_dir, nome))
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        
        if img.shape == (2688,800, 3):
            # border widths
            left, right = [944]*2
            s800x2688 += 1
            img = cv2.copyMakeBorder(img, 0, 0, left, right, cv2.BORDER_CONSTANT, value=color)
            #             img[start_row:end_row, start_col:end_col]
            img_cortada = img[560:1890, 670:2000]

            nome_sem_ext = os.path.splitext(nome)[0]
            tf.keras.preprocessing.image.save_img(os.path.join(output_dir, nome_sem_ext + ext), img_cortada)
        elif img.shape == (2592, 800, 3):
            # border widths
            left, right = [896]*2
            s800x2592 += 1
            img = cv2.imread(os.path.join(input_dir, nome))
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            img = cv2.copyMakeBorder(img, 0, 0, left, right, cv2.BORDER_CONSTANT, value=color)
            #             img[start_row:end_row, start_col:end_col]
            img_cortada = img[560:1890, 625:1955] # 390:1555, 390:1555

            nome_sem_ext = os.path.splitext(nome)[0]
            tf.keras.preprocessing.image.save_img(os.path.join(output_dir, nome_sem_ext + ext), img_cortada)
        else:
            other_shape += 1
        
        i+=1
        print(i)
    print(f"Quantidade 800x2688: {s800x2688} \nQuantidade 800x2592: {s800x2592}\nQuantidade shape desconhecido: {other_shape}")

if __name__ == "__main__":
    diretorio = '/home/guilherme/PIXFORCE/REDSOFT/MARFRIG/2022-10-31/class_8/'
    test_dir = '/home/guilherme/PIXFORCE/REDSOFT/MARFRIG/2022-10-31/class_8/'

    reduzir_tamanho_imagens(diretorio, test_dir)
