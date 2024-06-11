from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import User
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
def login(request):
    # 检查请求是否为POST
    if request.method == 'POST':
        # 从POST请求中获取用户名和密码
        username = request.POST.get('username')
        password = request.POST.get('password')
        # 在数据库中查找用户
        try:
            user = User.objects.get(username=username, password=password)
            # 用户存在且密码匹配，将用户ID保存在session中
            request.session['user_id'] =user.id
            # 登录成功，重定向到某个页面
            return HttpResponseRedirect('/lesson/')
        except User.DoesNotExist:
            # 用户不存在或密码不匹配
            error_message = "用户不存在或密码不匹配."
            return render(request, 'login.html', {'error_message': error_message})
            # 如果是GET请求，则显示登录表单
    return render(request, 'login.html')

def index(request):
    return render(request, 'lesson_list.html')
def indexa(request):
    return render(request, 'indexa.html')
def logout(request):
    del request.session['User_id']
    return HttpResponseRedirect('/User/login/')
@csrf_exempt
def xiugai(request):
    mima =  request.POST.get('mima')
    print(1)
    User_id = request.session.get('User_id')
    User = User.objects.get(id=User_id)
    User.密码=mima
    User.save()
    response_data = {
        'msg': '修改成功',
    }
    return JsonResponse(response_data)
@csrf_exempt

@csrf_exempt

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password != password2:
            messages.error(request, '两次输入的密码不一致，请重新输入。')
            return render(request, 'register.html')
            # 检查用户名是否已存在
        if User.objects.filter(username=username).exists():
            messages.error(request, '用户名已存在，请换一个用户名。')
            return render(request, 'register.html')
            # 创建用户
        user = User.objects.create(username=username, password=password)
        request.session['user_id'] = user.id
        return redirect('/lesson/')
    return render(request, 'register.html')