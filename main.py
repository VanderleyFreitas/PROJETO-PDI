# -*- coding: utf-8 -*-
"""ObjectIndentification.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NDE_oVaGEeE7b0if20QnMYQPmHbLVziB

## Código Final
"""

import cv2
import numpy as np
from preprocess import PrePro
from skimage import img_as_ubyte
from google.colab.patches import cv2_imshow

pre = PrePro()

from google.colab import drive
drive.mount('/content/drive')

def achar_bolos(imagem_preprocessada):
  contornos, _ = cv2.findContours(imagem_preprocessada[0:720, 300:1280], cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE, offset= (300, 0))

  coord_retangulos = [None]*len(contornos)
  for i, c in enumerate(contornos):
      retangulo = cv2.boundingRect(c)

      if retangulo[2] > 80 and retangulo[3] > 80 and retangulo[2] < 150 and retangulo[3] < 150:
        coord_retangulos[i] = cv2.boundingRect(c)
  
  coord_retangulos = list(filter(None, coord_retangulos))
  
  return coord_retangulos

def classifica(subimagem):
  subimagem = cv2.medianBlur(subimagem,3)
  _, subimagem_limiarizada = cv2.threshold(subimagem, 70, 255, cv2.THRESH_BINARY)
  miolo_subimagem_limiarizada = subimagem_limiarizada[subimagem_limiarizada.shape[1]//2-20:subimagem_limiarizada.shape[1]//2+20, \
                                          subimagem_limiarizada.shape[1]//2-20:subimagem_limiarizada.shape[1]//2+20]
  media_miolo = miolo_subimagem_limiarizada.mean()
  if media_miolo < 100:
    return 'Coberto'
  elif media_miolo < 200:
    return 'Semicoberto'
  else:
    return 'Descoberto'

def processamento(imagem_original, coord_retangulos):
  classificacoes = []
  for retangulo in coord_retangulos:
    subimagem = imagem_original[retangulo[1]:retangulo[1]+retangulo[3], \
                                retangulo[0]:retangulo[0]+retangulo[2]]
    classificacoes.append(classifica(subimagem))
  return classificacoes

def frame_processado(imagem_original, coord_retangulos, classificacoes):
  for i in range(len(coord_retangulos)):
    if classificacoes[i] == 'Coberto':
      color = (0, 255, 0)
    elif classificacoes[i] == 'Semicoberto':
      color = (255, 0, 0)
    else:
      color = (0, 0, 255)
    cv2.rectangle(imagem_original, (int(coord_retangulos[i][0]), int(coord_retangulos[i][1])), \
      (int(coord_retangulos[i][0]+coord_retangulos[i][2]), int(coord_retangulos[i][1]+coord_retangulos[i][3])), color, 2)

vidcap = cv2.VideoCapture('/content/drive/MyDrive/PDI/Cópia de Video30(1%).mp4')
success,image = vidcap.read()
count = 0
success = True
while success:
  success, imagem_original = vidcap.read()
  ## main
  imagem_cinza = cv2.cvtColor(imagem_original, cv2.COLOR_BGR2GRAY)
  imagem_preprocessada = pre.ApplyCanny(imagem_cinza,5,0.1,0.15)

  # pre processamento
  imagem_preprocessada = img_as_ubyte(imagem_preprocessada)
  kernel = np.ones((4,4),np.uint8)
  gradient = cv2.morphologyEx(imagem_preprocessada, cv2.MORPH_GRADIENT, kernel)
  closing = cv2.morphologyEx(gradient, cv2.MORPH_CLOSE, kernel)
  _, imagem_preprocessada = cv2.threshold(closing, 127, 255, cv2.THRESH_BINARY)

  coord_retangulos = achar_bolos(imagem_preprocessada)

  classificacoes = processamento(imagem_cinza, coord_retangulos)

  frame_processado(imagem_original, coord_retangulos, classificacoes)
  
  cv2.imwrite("/content/frames_novos/frame%d.jpg" % count, imagem_original)
  count += 1

import numpy as np
import glob
import cv2
import re

def by_number(filename):
  numbers = re.findall(r'\d', filename)
  return int(''.join(numbers))
  
img_array = []
files = sorted(glob.glob('./frames_novos/*.jpg'), key = by_number)
for filename in files:
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width,height)
    img_array.append(img)


out = cv2.VideoWriter('./project.avi',cv2.VideoWriter_fourcc(*'DIVX'), 30, size)

for i in range(len(img_array)):
    out.write(img_array[i])
out.release()

from shutil import copyfile
copyfile('/content/project.avi', '/content/drive/MyDrive/PDI/project.avi')