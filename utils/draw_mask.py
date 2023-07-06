import numpy as np
import pandas as pd
from pathlib import Path
import cv2
import numpy as np

def draw_black_mask(path, width, hight):

    color = (0, 0, 0) 
    arr = np.zeros((width, hight, 3), dtype=np.uint8) 
    pic = color - arr
    cv2.imwrite(path, pic)


def get_mask_image_overlay(image_id):    
    annots = polygons_df.loc[polygons_df["id"] == image_id, 'annotations'].iloc[0]

    ori = cv2.imread(str(ROOT / "train/ori_image" / f"{image_id}.png"))
    path = str(ROOT / "train/mask" / f"{image_id}.png")
    draw_black_mask(path, ori.shape[0], ori.shape[1])
    img = cv2.imread(path)
    
    cnt = 0
    for annot in annots:
        if annot['type'] == 'blood_vessel':
            cnt += 1
            coords = np.array(annot['coordinates'])
            # cv2.polylines(img, coords, True, WHITE, 3)
            cv2.fillPoly(img, coords, (255-10*cnt, 255-5*cnt, 255-cnt))
         
    
    if cnt > 0:
        cv2.imwrite(path, img)
    else:
        pathfile = Path(path)
        pathfile.unlink()
        print(path)

    return img

if __name__ == '__main__':

    ROOT = Path("./data/hubmap-hacking-the-human-vasculature")
    polygons_df = pd.read_json(ROOT / "polygons.jsonl", lines=True)
    training_examples = polygons_df['id'].to_numpy() 

    for pic in training_examples:

        img = get_mask_image_overlay(pic)
        # print(f"image id = {pic}")

        # cv2.imshow("img" , img)
        # cv2.waitKey(0)
