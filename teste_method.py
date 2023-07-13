import cv2
from PIL import Image

# metodos da biblioteca para renderizar a imagem
metodos = [
    cv2.THRESH_BINARY,
    cv2.THRESH_BINARY_INV,
    cv2.THRESH_TRUNC,
    cv2.THRESH_TOZERO,
    cv2.THRESH_TOZERO_INV,
]

imagem = cv2.imread("bdcaptcha/telanova9.png")

# transformar a imagem em degradê de cinza

imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_RGB2GRAY)

#usando os metodos de metodos
i = 0
for metodo in metodos:
    i += 1
    _, imagem_tratada = cv2.threshold(imagem_cinza, 127, 255, metodo or cv2.THRESH_OTSU) #descobre o numero de pixel e "pinta" de acordo
    cv2.imwrite(f'testedosmethods/imagem_tratada_{i}.png', imagem_tratada)

# metodo trunc ganhou

# 2 pintar imagem
imagem = Image.open("testedosmethods/imagem_tratada_3.png")
 #usar metodos do pil para pintar de preto e branco
imagem = imagem.convert("P")
imagem2 = Image.new("P", imagem.size, 255) #255 mais claro ent o fundo vai ser branco

for x in range(imagem.size[1]): #percorre as colunas
    for y in range(imagem.size[0]): #percorre as linhas
        cor_pixel = imagem.getpixel((y, x))
        if cor_pixel < 115:
            imagem2.putpixel((y, x), (0,0,0)) #pinta as letras de preto
        elif cor_pixel >115:
            imagem2.putpixel((y, x), (255,255,255)) #pinta as letras de preto

imagem2.save('testedosmethods/imagem1final.png')
