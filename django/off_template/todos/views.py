from django.shortcuts import render

todo_list = []
# Create your views here.
# 함수는 input 에 대한 어떤 처리후 output 내는게 목적
# views.py에 만드는 모든 함수들의 목적은
# 사용자의 요청에 따라 반환해야할 적절한 html을 내는게 목적
def main(request):
    # main view 함수가 할 일이 늘어남.
    # 사용자가 요청을 보냈는데 그냥 todos/main으로 요청이 온게 아니라
    # todos/main?work=어떤 값을 같이 담아 보냄 
    # 요청할 때 데이터도 보냈다. 그걸 내 html에 표현 해줘야함
    # 사용자의 모든 요청 정보는 request 인자에 들어있음
    # print(dir(request))
    # print(request.GET.get('work'))
    
    todo_list.append(request.GET.get('work'))
    work = request.GET.get('work')
    if work:  # work에 값이 있을 때만 
        todo_list.append(work)
    
    context ={
        'work' : todo_list }
    # app_name/templates 까지는 내가 안적어도 알아서 찾아간다.
    # app_name/templates/*/*.html
    return render(request, 'todos/main.html', context)

def create(request):
    return render(request, 'todos/create.html')