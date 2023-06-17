import numpy as np
import pandas as pd
from pathlib import Path
import cv2
import numpy as np

def get_mask_image_overlay(image_id):    
    annots = polygons_df.loc[polygons_df["id"] == image_id, 'annotations'].iloc[0]
    img = cv2.imread(str(ROOT / "train/image" / f"{image_id}.tif"))
    cv2.imshow("img" , img)
    
    RED= (0,0,255)
    GREEN= (0,255,0)
    BLUE= (255,0,0)
    color_map = {'blood_vessel':RED, 'glomerulus':BLUE, 'unsure':GREEN}
    instance_count = {'blood_vessel':0, 'glomerulus':0, 'unsure':0}
    
    for annot in annots:
        color = color_map[annot['type']]
        instance_count[annot['type']]+=1
        coords = np.array(annot['coordinates'])
        cv2.polylines(img, coords, True, color, 3)
    
    return img, instance_count

if __name__ == '__main__':

    ROOT = Path("./data/hubmap-hacking-the-human-vasculature")
    polygons_df = pd.read_json(ROOT / "polygons.jsonl", lines=True)
    training_examples = polygons_df['id'].to_numpy() 

    for pic in training_examples:

        img, instance_count = get_mask_image_overlay(pic)
        print(f"image id = {pic}")
        print(f"Blood Vessels (Red) Count: {instance_count['blood_vessel']}")
        print(f"Glomerulus (Blue) Count: {instance_count['glomerulus']}")
        print(f"Unsure (Green) Count: {instance_count['unsure']}")

        cv2.imshow("img" , img)
        cv2.waitKey(0)
