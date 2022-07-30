import pysubs2
import os
import json
from pysubs2.time import make_time


def read_subt(floder):
    path_f = "F:\\Desktop\\Django-Project\\videoUI\\media\\lecture_video\\"
    path_f = path_f + floder
    path_sub = "F:\\Desktop\\1\\"
    path_sub = path_sub + floder + ".srt"
    subs = pysubs2.load(path_sub)
    """ for line in subs:
        print(line.text) """
    """ print(type(subs[1].end))
    print(pysubs2.time.times_to_ms(subs[1].end)) """

    dirs = os.listdir(path_f)
    dirs.sort(key=lambda x: float(x[:-4]))
    sub_json = {}
    pre_time = 0
    for files in dirs:
        # print(files.split(".jpg")[0])
        t = files.split(".jpg")[0]
        sub_json["{}".format(t)] = ""
        for line in subs:
            if line.end <= make_time(s=float(t)) and line.start >= pre_time:
                sub_json["{}".format(t)] = sub_json["{}".format(t)] + line.text
                pre_time = line.end
    print(sub_json)
    with open(
            "F:\\Desktop\\Django-Project\\videoUI\\media\\lecture_video\\slide content\\"
            + floder + "\\text\\" + "{}.json".format(floder), 'w') as f:
        json.dump(sub_json, f)


read_subt("Skeleton2Stroke__Interactive_Stroke_Correspondence_Editing")
