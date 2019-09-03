import pyautogui as pag
from PIL import Image
from PIL import ImageGrab
from PIL import ImageChops
from PIL import ImageStat
from time import sleep, time

print(pag.size())
# 클릭 후 대기 시간
pag.PAUSE = 0

# 신청버튼 좌표 입력
a = input('신청버튼에 대고 a입력 후 엔터: ')
X_request_button, Y_request_button = pag.position()
XY_request_button = X_request_button, Y_request_button
print('신청버튼 좌표: ', XY_request_button)

# 저장버튼 좌표 입력
a = input('저장버튼에 대고 a입력 후 엔터: ')
X_save_button, Y_save_button = pag.position()
XY_save_button = X_save_button, Y_save_button
print('저장버튼 좌표: ', XY_save_button)

# 입력숫자박스 좌표 입력
a = input('입력숫자박스의 안에 대고 a입력 후 엔터: ')
X_input_box, Y_input_box = pag.position()
XY_input_box = X_input_box, Y_input_box
print('숫자박스 좌표: ', XY_input_box)

# 제시 숫자 왼쪽 위 좌표
a = input('제시된 첫번째 숫자 왼쪽 위에 대고 a입력 후 엔터: ')
X_number_box_left_top, Y_number_box_left_top = pag.position()
XY_number_box_left_top = X_number_box_left_top, Y_number_box_left_top
print('좌표: ', XY_number_box_left_top)

# 제시 숫자 오른쪽 아래 좌표
a = input('제시된 마지막 숫자 오른쪽 아래에 대고 a입력 후 엔터: ')
X_number_box_right_bottom, Y_number_box_right_bottom = pag.position()
XY_number_box_right_bottom = X_number_box_right_bottom, Y_number_box_right_bottom
print('좌표: ', XY_number_box_right_bottom)

# 초과확인버튼 좌표 입력
a = input('초과확인버튼에 대고 a입력 후 엔터: ')
X_ok_button, Y_ok_button = pag.position()
XY_ok_button = X_ok_button, Y_ok_button
print('숫자박스 좌표: ', XY_ok_button)

# 저장된 숫자 이미지 불러오기
target = [Image.open("number/0.PNG"), Image.open("number/1.PNG"), Image.open("number/2.PNG"), \
Image.open("number/3.PNG"), Image.open("number/4.PNG"), Image.open("number/5.PNG"), \
Image.open("number/6.PNG"), Image.open("number/7.PNG"), Image.open("number/8.PNG"), \
Image.open("number/9.PNG")]

# 시작하려면 입력
delay = float(input("딜레이 입력 후 시작(second): "))

def Search(cx, cy, compare, tag):
    tx, ty = tag.size
    cut = compare.crop((cx, cy, cx + tx, cy + ty))

    diff = ImageChops.difference(cut, tag)
    stat = ImageStat.Stat(diff)

    if stat.sum == [0, 0, 0]:
        return True
    else:
        return False

def Crop(multiple, cood):
    return img.crop((X_number_box_left_top + ((multiple - 1) * cood), Y_number_box_left_top, \
    X_number_box_left_top + (multiple * cood), Y_number_box_right_bottom))

while True:
    # 전체 화면 캡쳐
    img = ImageGrab.grab()
    '''
    # 네자리 숫자 화면 추출
    img_cut = img.crop((X_number_box_left_top, Y_number_box_left_top, X_number_box_right_bottom, Y_number_box_right_bottom))
    '''
    # 숫자 추출을 위한 좌표 계산
    x = (X_number_box_right_bottom - X_number_box_left_top) / 4

    # 첫번째 숫자 화면 추출
    img_first = Crop(1, x)

    # 두번째 숫자 화면 추출
    img_second = Crop(2, x)

    # 세번째 숫자 화면 추출
    img_third = Crop(3, x)

    # 네번째 숫자 화면 추출
    img_fourth = Crop(4, x)

    img_list = [img_first, img_second, img_third, img_fourth]

    # 입력하는 숫자박스 안 클릭
    pag.click(X_input_box, Y_input_box)
    sleep(delay)

    for j in range(4):
        sx, sy = img_list[j].size
        for i in range(10):
            tag = target[i]
            tx, ty = tag.size
            for cy in range(sy - ty):
                for cx in range(sx - tx):
                    if Search(cx, cy, img_list[j], tag) == True:
                        pag.typewrite(str(i))
                        sleep(0)
    
    # 저장 버튼 클릭
    pag.press('enter')
    sleep(delay)
    # 초과 확인 버튼 클릭
    pag.press('enter')
    sleep(delay)
    # 신청 버튼 클릭
    pag.click(X_request_button, Y_request_button)
    sleep(delay)