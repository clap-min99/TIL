from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=12)
    # password는 문자열인데 비밀번호를 입력받을 공간이다.
        # HTML에서 만들어질 input 태그가 어떤 모양이 될건지 추가 옵션 정의
    password = forms.CharField(widget=forms.PasswordInput())