import cv2
import os
import glob
from PIL import Image

def tratar_imagens(pasta_origem, pasta_destino='tratadas'):
    arquivos = glob.glob(f"{pasta_origem}/*") #glob le todos os arquivos da pasta
    for arquivo in arquivos:
        imagem = cv2.imread(arquivo)

        # transformar a imagem em degradê de cinza
        imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_RGB2GRAY)

        _, imagem_tratada = cv2.threshold(imagem_cinza, 127, 255, cv2.THRESH_TRUNC or cv2.THRESH_OTSU)  # descobre o numero de pixel e "pinta" de acordo

        nome_arquivo = os.path.basename(arquivo) #só pega o nome do arquivo e copia para na pasta de destino ele ter o mesmo nome depois de tratadp
        cv2.imwrite(f'{pasta_destino}/{nome_arquivo}', imagem_tratada)

        #segunda etapada do teste>>>>>>>
    arquivos = glob.glob(f"{pasta_destino}/*")
    for arquivo in arquivos:
        imagem = Image.open(arquivo)

        # usar metodos do pil para pintar de preto e branco
        imagem = imagem.convert("P")
        imagem2 = Image.new("P", imagem.size, 255)  # 255 mais claro ent o fundo vai ser branco

        for x in range(imagem.size[1]):  # percorre as colunas
            for y in range(imagem.size[0]):  # percorre as linhas
                cor_pixel = imagem.getpixel((y, x))
                if cor_pixel < 115 :
                    imagem2.putpixel((y, x), (0, 0, 0))  # pinta as letras de preto
                elif cor_pixel > 115:
                    imagem2.putpixel((y, x), (255, 255, 255))  # pinta as letras de preto

        nome_arquivo = os.path.basename(arquivo)
        imagem2.save(f'{pasta_destino}/{nome_arquivo}')

if __name__ == "__main__":
    tratar_imagens('bdcaptcha')

