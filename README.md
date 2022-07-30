# HiVideo
HiVideo: Hierarchical Browsing Interface for Educational Videos

Jiahao Weng, Chao Zhang, Xi Yang, Haoran Xie. HiVideo: Hierarchical Browsing Interface for Educational Videos, SIGGRAPH 2022, Poster.

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
