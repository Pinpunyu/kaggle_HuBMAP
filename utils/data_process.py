from pathlib import Path
import shutil
import cv2
import torch
import numpy as np
from PIL import Image

def tiftopng():
    images = Path("./data/hubmap-hacking-the-human-vasculature/train/image").glob("*.tif")

    for img in images:

        # print(f"image id = {img}")
        ori = cv2.imread(str(img))
        png = str(img).split('.')[0]+'.png'
        cv2.imwrite(png, ori)

def move():

    file_source_path = Path('./data/hubmap-hacking-the-human-vasculature/train/ori_image')
    file_destination ='./data/hubmap-hacking-the-human-vasculature/train/image'
    images = Path("./data/hubmap-hacking-the-human-vasculature/train/mask").glob("*.png")

    for img in images:
        # print(img)
        name = str(img).split("mask\\")[1]
        file_source = file_source_path / name
        # print(file_source)
        shutil.copy(file_source,file_destination)
        # exit(0)

def img_showmask(img, mask):

    # img = cv2.imread(imgpath)
    # mask = cv2.imread(maskpath)

    black = np.array([0, 0, 0])
    for i in range(0,mask.shape[0]):
        for j in range(0,mask.shape[1]):
            if np.all(np.equal(mask[i][j], black)) == False:
                img[i][j] = mask[i][j]
                # print(f"{i} {j} {mask[i][j]}")

    # cv2.imshow("img", img)
    # cv2.waitKey()
    return img

def remove_no_mask(path):

    for img in path.iterdir():
        hands_mask = Image.open(str(img))
        r, g, b = hands_mask.getextrema()
        if r[1] == 0 and g[1] == 0 and b[1] == 0:
            img.unlink()
            img = Path(str(img).replace("mask", "image"))
            img.unlink()

if __name__ == '__main__':

    # move
    # move()

    # img_showmask
    # imgpath = './data/hubmap-hacking-the-human-vasculature/train/ori_image/0a1d277fb473.png'
    # maskpath = './data/hubmap-hacking-the-human-vasculature/train/mask/0a1d277fb473.png'
    # img = cv2.imread(imgpath)
    # mask = cv2.imread(maskpath)
    # img_showmask(img, mask)

    # remove_no_mask
    path = Path("./data/hubmap-hacking-the-human-vasculature/train/mask")
    remove_no_mask(path)
       
