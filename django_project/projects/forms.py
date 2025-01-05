from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from .models import Project


class ProjectUrlsForm(forms.ModelForm):
    web_page = forms.URLField(required=False, label="Web Page")
    git_hub = forms.URLField(required=False, label="GitHub")
    git_lab = forms.URLField(required=False, label="GitLab")
    play_store = forms.URLField(required=False, label="Play Store")
    app_store = forms.URLField(required=False, label="App Store")
    image = forms.URLField(required=False, label="Image")
    video = forms.URLField(required=False, label="Video")
    other = forms.URLField(required=False, label="Other")

    class Meta:
        model = Project
        fields = "__all__"

        widgets = {
            "runs_on": FilteredSelectMultiple("Run On", is_stacked=False),
            "categories": FilteredSelectMultiple("Categories", is_stacked=False),
            "goals": FilteredSelectMultiple("Goals", is_stacked=False),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        urls = self.instance.urls if self.instance and self.instance.urls else {}
        self.fields["web_page"].initial = urls.get("web_page", "")
        self.fields["git_hub"].initial = urls.get("git_hub", "")
        self.fields["git_lab"].initial = urls.get("git_lab", "")
        self.fields["play_store"].initial = urls.get("play_store", "")
        self.fields["app_store"].initial = urls.get("app_store", "")
        self.fields["image"].initial = urls.get("image", "")
        self.fields["video"].initial = urls.get("video", "")
        self.fields["other"].initial = urls.get("other", "")

    def clean(self):
        cleaned_data = super().clean()
        cleaned_data["urls"] = {
            "web_page": cleaned_data.pop("web_page", None),
            "git_hub": cleaned_data.pop("git_hub", None),
            "git_lab": cleaned_data.pop("git_lab", None),
            "play_store": cleaned_data.pop("play_store", None),
            "app_store": cleaned_data.pop("app_store", None),
            "image": cleaned_data.pop("image", None),
            "video": cleaned_data.pop("video", None),
            "other": cleaned_data.pop("other", None),
        }
        runs_on = cleaned_data.get("runs_on", [])
        if not any(platform in runs_on for platform in ["android", "ios"]):
            cleaned_data["mobile_stack"] = []
        return cleaned_data
