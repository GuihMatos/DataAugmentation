
import os
from glob import glob


def eh_imagem(path):
    c = 0
    for i in glob(path + '*.png'):
        os.remove(i)
        c += 1
        print(c)

if __name__ == "__main__":
    diretorio = '/home/guilherme/PIXFORCE/REDSOFT/FRIGOBOM/5C/3/'

    eh_imagem(diretorio)
