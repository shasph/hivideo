import os
import layoutparser as lp
import cv2
from PIL import Image
import imagehash
from decord import VideoReader, cpu

DIFF_THRESHOLD = 2


def extractSlides(videoPath):
    vr = VideoReader(videoPath, ctx=cpu(0))
    slides = []
    prevImageHash = None
    imageChanged = False

    for i in len(vr):
        slide_time = vr.get_frame_timestamp(i)[0]
        frame = vr[i].asnumpy()
        pilImage = Image.fromarray(frame)
        prevImageHash = imagehash.average_hash(
            pilImage) if not prevImageHash else currentImageHash
        currentImageHash = imagehash.average_hash(pilImage)
        imageDiff = currentImageHash - prevImageHash

        if imageChanged and imageDiff < DIFF_THRESHOLD:
            slides.append(pilImage)
            has_floder = os.path.exists(videoPath.stem)
            if not has_floder:
                os.makedirs(videoPath.stem)
            pilImage.save("F:\\Desktop\\slide-extractor\\{}\\{}.jpg".format(
                videoPath.stem, slide_time))
            imageChanged = False

        if imageDiff > DIFF_THRESHOLD:
            imageChanged = True

    return slides


extractSlides(
    "F:\\Desktop\\Django-Project\\videoUI\\media\\lecture_video\\Skeleton2Stroke__Interactive_Stroke_Correspondence_Editing.mp4"
)
