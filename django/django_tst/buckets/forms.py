from django import forms
from .models import TravelBucketList


class TravelBucketListForm(forms.ModelForm):
    class Meta:
        model = TravelBucketList
        # exclude 사용방법을 모르겠어서 이렇게라도 적어봅니다...
        fields = ('destination_name', 'country', 'image', 'planned_visit_date', 'priority')
        widgets = {
            'destination_name': forms.TextInput(attrs={'class': 'form-control'}),
            'country': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'reason': forms.Textarea(attrs={'class': 'form-control'}),
            'planned_visit_date': forms.DateInput(attrs={'class': 'form-control'}),
            'priority': forms.Select(attrs={'class': 'form-control'}),
        }
