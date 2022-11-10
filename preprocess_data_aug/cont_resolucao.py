import cv2
from glob import glob

folder = '/home/guilherme/PIXFORCE/REDSOFT/MARFRIG/resultados/class_8/'

imagens = glob(folder + '/*.jpg')

s800x2688 = 0
s800x2592 = 0
other_shape = 0
for i in range(len(imagens)):
    img = cv2.cvtColor(cv2.imread(imagens[i]), cv2.COLOR_BGR2RGB)
    print(f'{img.shape}\n')
    if img.shape == (2688,800, 3):
        s800x2688 += 1
    elif img.shape == (2592, 800, 3):
        s800x2592 += 1
    else:
        other_shape += 1
    print(i)

print(f'Quantidade 800x2688: {s800x2688} \nQuantidade 800x2592: {s800x2592}\nQuantidade outros shapes: {other_shape}')