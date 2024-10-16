from django import forms 
from .models import Todo

class TodoForm(forms.ModelForm):
    # Todo가 가지고 있는 모든 필드에 사용자가 값을 입력함녀 
    # 그 데이터로 todo 데이터를 생성
    # 그걸 위한 form tag를 만들어줌 
    class Meta:
        model = Todo
        fields = '__all__'