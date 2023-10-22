from django import forms

from .models import TierItem


class DropZoneFileInput(forms.FileInput):
    template_name = "dropzone.html"


class TierItemForm(forms.ModelForm):
    image = forms.ImageField(
        widget=DropZoneFileInput(
            attrs={
                "hx-post": "/upload-image",
                "hx-encoding": "multipart/form-data",
                "hx-target": "#tier-items-base",
                "hx-swap": "beforeend",
                "id": "dropzone-file",
            }
        )
    )

    class Meta:
        model = TierItem
        fields = ["image"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, field in self.fields.items():
            field.label = ""  # To remove the widget labels
