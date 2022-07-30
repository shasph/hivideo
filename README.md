# HiVideo
HiVideo: Hierarchical Browsing Interface for Educational Videos

Jiahao Weng, Chao Zhang, Xi Yang, Haoran Xie. HiVideo: Hierarchical Browsing Interface for Educational Videos, SIGGRAPH 2022, Poster.

[[Project]](http://www.jaist.ac.jp/~xie/2022-hivideo)[[Video]](https://www.youtube.com/watch?v=OXTFH_WFQMw)[[ACM]](https://doi.org/10.1145/3532719.3543226)

![hivideo](https://user-images.githubusercontent.com/4180028/181871539-e4f46009-2073-4633-8d8b-f6b86994f15b.jpg)


# How to run the project
1. Install requirements
`pip install -r requirements.txt`
2. Run server
`python manage.py runserver`
3. Access website
`http://locoalhost:8080/home`

# How to preproccessing
### You can see the example in the jupyter notebook `layout_analyze.ipynb`
1. Slide extraction
Change your video path in the python file.
`python slide-extractor.py`
2. Title and figure extraction
Change the `yaml & pth` path in the python file.
`python layout_analyze.py`

Please contact xie@jaist.ac.jp for any comments or requests.

## Citation
If you use this code for your research, please cite our paper.
```
@inproceedings{hivideo-2022,
author = {Weng, Jiahao and Zhang, Chao and Yang, Xi and Xie, Haoran},
title = {HiVideo: Hierarchical Browsing Interface for Educational Videos},
year = {2022},
isbn = {9781450393614},
publisher = {Association for Computing Machinery},
address = {New York, NY, USA},
url = {https://doi.org/10.1145/3532719.3543226},
doi = {10.1145/3532719.3543226},
booktitle = {ACM SIGGRAPH 2022 Posters},
articleno = {2},
numpages = {2},
keywords = {user interface, slide-based video, information retrieval},
location = {Vancouver, BC, Canada},
series = {SIGGRAPH '22}
}
```
