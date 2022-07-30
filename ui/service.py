from .models import Video
from django.db.models import Q


def get_all_videos():
    return Video.objects.all().order_by('-id')


def get_video(id):
    return Video.objects.get(pk=id)


def test_search(keyword):
    return Video.objects.filter(
        Q(audio_script__icontains=keyword) | Q(title__icontains=keyword))
