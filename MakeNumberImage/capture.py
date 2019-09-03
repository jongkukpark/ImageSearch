from PIL import ImageGrab
from PIL import Image
import pyautogui as pag

img = ImageGrab.grab()
#img_name = 'fournumbers.PNG'
#img.save(img_name)

x = 560
name = '8.PNG'

newImg = img.crop((x, 585, (x + 12), 606))
newImg.save(name)

#가로 12 세로 18

#첫번째 524
#두번째 542
#세번째 560
#네번째 578