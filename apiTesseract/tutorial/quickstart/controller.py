from PIL import Image
import pytesseract as ocr
from pdf2image import convert_from_path
import numpy as np
import cv2

ocr.pytesseract.tesseract_cmd = r'C:\Users\andre.lt\AppData\Local\Tesseract-OCR\tesseract.exe'


def verificaArquivo(arquivo, numero):

    img = convert_from_path("./quickstart/media/" + arquivo, dpi=200,
                            poppler_path=r'C:\poppler\bin', single_file=True)
    for imgs in img:
        imgs.save("./quickstart/media/" +
                  arquivo.replace(".pdf", ".jpeg"), 'JPEG')

    imagem = Image.open(
        "./quickstart/media/" + arquivo.replace(".pdf", ".jpeg")).convert('RGB')

    npimagem = np.asarray(imagem).astype(np.uint8)
    npimagem[:, :, 0] = 0
    npimagem[:, :, 2] = 0

    im = cv2.cvtColor(npimagem, cv2.COLOR_RGB2GRAY)
    ret, thresh = cv2.threshold(
        im, 127, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    binimagem = Image.fromarray(thresh)

    phrase = ocr.image_to_string(binimagem, lang='por')
    if(phrase.find(numero)):
        return True
    return False
