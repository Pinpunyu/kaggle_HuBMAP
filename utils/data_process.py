from pathlib import Path
import shutil
import cv2
import torch

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





if __name__ == '__main__':

    move()
    # boxes = torch.as_tensor([[183.,   0., 511., 511.]])
    # print(boxes)
    # area = (boxes[:, 3] - boxes[:, 1]) * (boxes[:, 2] - boxes[:, 0])
    # print(boxes[:, 3])
       
