import layoutparser as lp
import cv2
import os
from PIL import Image,ImageDraw
import json


def layout_analyze(img, video_name, index):
    # Get title of the slide
    layout,image=apply_laoutparser(img, video_name, index)
    ocr_agent = lp.TesseractAgent(languages='eng')
    title_blocks=lp.Layout([b for b in layout if b.type=='Title'])
    block=title_blocks[0]
    segment_image= block.pad(left=5, right=5, top=5, bottom=5).crop_image(image)
    text = ocr_agent.detect(segment_image)
    block.set(text=text, inplace=True)
    # Get img of the slide
    img_blocks=lp.Layout([b for b in layout if b.type=='Figure'])
    for block in img_blocks:
        segment_image= block.pad(left=5, right=5, top=5, bottom=5).crop_image(image)
        im = Image.fromarray(segment_image)
        im.save("img.jpg")
        

def apply_laoutparser(img, video_name, index):
    model = lp.Detectron2LayoutModel(
        config_path=
        'F:\Code\Python\layoutparser\LP\layout-model-training\config.yaml',
        model_path=
        'F:\Code\Python\layoutparser\LP\layout-model-training\model_final.pth',
        extra_config=["MODEL.ROI_HEADS.SCORE_THRESH_TEST", 0.8],
        label_map={
            0: "Figure",
            1: "Text",
            2: "Title"
        })
    image = cv2.imread(img)
    image = image[..., ::-1]
    return model.detect(image),img