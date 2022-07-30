from django.db import models


# Create your models here.
class Video(models.Model):
    title = models.CharField(max_length=255)
    v_file = models.FileField(upload_to="lecture_video")
    v_info = models.TextField(blank=True, null=True)
    # v_cover = models.FileField(upload_to="cover_image")
    # sild_image = models.CharField(max_length=255)
    audio_script = models.TextField(blank=True, null=True)
    video_time = models.CharField(blank=True, null=True, max_length=255)

    def __str__(self):
        return self.title

    def content_validity(self):
        if len(str(self.audio_script)) > 20:
            return '{}……'.format(str(self.audio_script)[0:20])
        else:
            return str(self.audio_script)
