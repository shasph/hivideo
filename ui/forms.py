from django import forms


class VideoForm(forms.Form):
    v_file = forms.FileField(label='Select a file')
    # title = forms.CharField(label="Title")
