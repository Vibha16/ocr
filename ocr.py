try:
    from PIL import Image
except ImportError:
    import Image
import cv2
import pytesseract


def ocr_core(filename):
    #img = cv2.imread(filename)

    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

    tex = pytesseract.image_to_string(Image.open(filename))#, lang='tam')
    # cv2.imshow("Input image", img)
    return tex


# cv2.namedWindow("Input image")

# cv2.waitKey(0)
# cv2.destroyWindow("Test")
# cv2.destroyWindow("Main")
#print(ocr_core("tamilscript.png"))
