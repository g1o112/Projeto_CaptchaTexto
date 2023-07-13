import cv2
import os
import glob

arquivos = glob.glob('tratadas/*')

for arquivo in arquivos:
    imagem = cv2.imread(arquivo) # essa função sempre le o arquivo em rgb
    imagem = cv2.cvtColor(imagem, cv2.COLOR_RGB2GRAY)
    #em preto e branco
    _, nova_imagem = cv2.threshold(imagem, 0, 255, cv2.THRESH_BINARY_INV) #inv deixa preto em branco porem fundo preto e letra branca

    # ENCONTRA OS CONTORNOS DE CADA LETRA
    contornos, _ = cv2.findContours(nova_imagem, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) #procura o contorno a imagem olhando de fora para dentro

    regiao_letras = []

    # filtrar os contornos que são das letras e não dos arranhados
    for retangulo in contornos:
        (x, y, l, a) = cv2.boundingRect(retangulo) # boundingrect te da a posição y, x, altura e largura do retangulo, sendo ele a identificação coladinha na letra
        area = cv2.contourArea(retangulo)
        if area > 115:
            regiao_letras.append((x,y,l, a))
    if len(regiao_letras) != 5:
        continue #pula para a próxima img se ele não identifica 5 letras

    # desenhar contornos e separa em letras arquivos individuais

    imagem_final = cv2.merge([imagem] * 3)

    i=0
    for retangulo in regiao_letras:
        x, y, l, a = retangulo
        imagem_letra = imagem[y-2:y+a+2, x-2:x+l+2]
        i+=1
        nome_arquivo = os.path.basename(arquivo).replace(".png", f"letras{i}.png")
        cv2.imwrite(f'letras/{nome_arquivo}', imagem_letra)
        cv2.rectangle(imagem_final, (x-2, y-2),(x+l+2, y+a+2), (0,255,0), 1)
    nome_arquivo= os.path.basename(arquivo)
    cv2.imwrite(f'identificadas/{nome_arquivo}',imagem_final)
