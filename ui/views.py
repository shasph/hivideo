from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from .models import Video
from .forms import VideoForm
from . import service
import os
import json
import re
import mimetypes
from wsgiref.util import FileWrapper
from django.http import StreamingHttpResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def home(request):
    videos = service.get_all_videos()
    return render(request, 'home.html', {'videos': videos})


def read(request):
    return render(request, 'read.html')


def detail(request, id):
    video = service.get_video(id)
    video_name = str(video.v_file).split('.')[0]
    path = r"D:\Desktop\project\Django-Project\videoUI\media\\" + video_name
    dirs = os.listdir(path)
    dirs.sort(key=lambda x: float(x[:-4]))
    # print(video.summerized)
    with open(path + '.json', 'r') as f:
        dict1 = json.load(fp=f)
    video.summerized = dict1
    video.slides = []
    for file in dirs:
        # print(file)
        video.slides.append("../../media/" + video_name + "/" + file)
    return render(request, "detail.html", {'video': video})


@csrf_exempt
def get_text(request):
    img_name = request.POST.get('find_text')
    prefix_name = r"D:\Desktop\project\Django-Project\videoUI\media\lecture_video\slide content\\"
    full_name = prefix_name + img_name.split(
        "/")[0] + "\\text\\" + img_name.split("/")[0] + ".json"
    with open(full_name, "r") as f:
        text_dict = json.load(fp=f)
    # print(text_dict)
    return HttpResponse(json.dumps(text_dict))


def vo(request):
    return render(request, "v-o.html")


def add(request):
    return HttpResponse("add page")


def edit(request, id):
    return HttpResponse("edit page of {}".format(id))


def test_filter(request):
    keyword = request.POST['keyword']
    videos = service.test_search(keyword)
    # print(videos.count() == 0)
    if videos.count() == 0:
        a = "NO RESULTS!"
        return render(request, "search-result.html", {'a': a})
    else:
        for video in videos:
            kw_position = video.audio_script.lower().find(keyword)
            video_name = str(video.v_file).split('.')[0]
            path = r"D:\Desktop\project\Django-Project\videoUI\media\\" + video_name
            dirs = os.listdir(path)
            dirs.sort(key=lambda x: float(x[:-4]))
            video.a = "{}/{}".format(video_name, dirs[1])
            video.b = "{}/{}".format(video_name, dirs[3])
            video.c = "{}/{}".format(video_name, dirs[4])
            print(kw_position)
            if kw_position == -1:
                video.audio_script_brief = video.audio_script[0:150] + "......"
            else:
                video.audio_script_brief = video.audio_script[
                    kw_position -
                    150:kw_position] + "<mark>" + video.audio_script[
                        kw_position:kw_position +
                        len(keyword)] + "</mark>" + video.audio_script[
                            kw_position + len(keyword):kw_position +
                            151] + "......"
                print(video.audio_script_brief)
        return render(request, "search-result.html", {'videos': videos})


def my_view(request):
    message = 'Upload files!'
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Video(v_file=request.FILES['v_file'])
            newdoc.save()

            # Redirect to the list after POST
            return redirect('video:my-view')
        else:
            message = 'The form is not valid. Fix the following error:'
    else:
        form = VideoForm()

    # Load for the list page
    videos = Video.objects.all()

    context = {'videos': videos, 'form': form, 'message': message}
    return render(request, 'list.html', context)


def file_iterator(file_name, chunk_size=8192, offset=0, length=None):
    with open(file_name, "rb") as f:
        f.seek(offset, os.SEEK_SET)
        remaining = length
        while True:
            bytes_length = chunk_size if remaining is None else min(
                remaining, chunk_size)
            data = f.read(bytes_length)
            if not data:
                break
            if remaining:
                remaining -= len(data)
            yield data


def stream_video(request):
    """将视频文件以流媒体的方式响应"""
    range_header = request.META.get('HTTP_RANGE', '').strip()
    range_re = re.compile(r'bytes\s*=\s*(\d+)\s*-\s*(\d*)', re.I)
    range_match = range_re.match(range_header)
    path = request.GET.get('path')
    # print("==============", path)
    size = os.path.getsize(path)
    content_type, encoding = mimetypes.guess_type(path)
    content_type = content_type or 'application/octet-stream'
    if range_match:
        first_byte, last_byte = range_match.groups()
        first_byte = int(first_byte) if first_byte else 0
        last_byte = first_byte + 1024 * 1024 * 10
        if last_byte >= size:
            last_byte = size - 1
        length = last_byte - first_byte + 1
        resp = StreamingHttpResponse(file_iterator(path,
                                                   offset=first_byte,
                                                   length=length),
                                     status=206,
                                     content_type=content_type)
        resp['Content-Length'] = str(length)
        resp['Content-Range'] = 'bytes %s-%s/%s' % (first_byte, last_byte,
                                                    size)
    else:
        resp = StreamingHttpResponse(FileWrapper(open(path, 'rb')),
                                     content_type=content_type)
        resp['Content-Length'] = str(size)
    resp['Accept-Ranges'] = 'bytes'
    return resp
