from PIL import Image
import random
from pathlib import Path

path = Path("./data/hubmap-hacking-the-human-vasculature/train/ori_image")

for img in path.iterdir():

    img = str(img)
    mask = img.replace('image', 'mask')

    oriimg = Image.open(img)
    orimask  = Image.open(mask)
    
    degree = random.randint(1,360)
    rotated_img = oriimg.rotate(degree)
    # oriimg.show()
    # rotated_img.show()

    rotated_mask = orimask.rotate(degree)
    # orimask.show()
    # rotated_mask.show()

    img_path = img.replace("ori_", "")
    mask_path = mask.replace("ori_", "")
    img_path = img_path.split(".")[0] + f"_{degree}.png"
    mask_path = mask_path.split(".")[0] + f"_{degree}.png"
    rotated_img.save(img_path)
    rotated_mask.save(mask_path)

    # print(img)
    # print(img_path)
    # print(mask)
    # print(mask_path)
    # exit(0)