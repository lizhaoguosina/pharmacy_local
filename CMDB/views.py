from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import models, forms
import hashlib
import time
# Create your views here.

def hashpass(username,password):
    md5 = hashlib.md5()
    sha256 = hashlib.sha256()
    md5.update(username.encode())
    salt = md5.hexdigest()
    password = password + salt
    sha256.update(password.encode())
    return sha256.hexdigest()

def get_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]#所以这里是真实的ip
    else:
        ip = request.META.get('REMOTE_ADDR')#这里获得代理ip
    return ip

def index(request):
    if not request.session.get('is_login',None):
        return redirect('/unlogindex/')
    assets = models.AsSet.objects.all()
    nowpage = '资产总表页'
    page = '资产总表页'
    return render(request,'CMDB/index.html',locals())

def unlogindex(request):
    if request.session.get('is_login',None):
        return redirect('/index/')
    return render(request,'CMDB/unlogindex.html')

def login(request):
    if request.session.get('is_login',None):
        return redirect('/index/')
    if request.method == 'POST':
        login_form = forms.UserForm(request.POST)
        message = "请检查填写内容"
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            try:
                user = models.User.objects.get(name=username)
            except:
                message = "用户不存在"
                return render(request, 'CMDB/login.html', locals())
            if user.password == hashpass(username,password):
                request.session['is_login'] = True
                request.session['user_id'] = user.id
                request.session['user_name'] = user.name
                return redirect('/index/')
            else:
                message = '密码错误'
                return render(request,'CMDB/login.html', locals())
    login_form = forms.UserForm()
    return render(request,'CMDB/login.html', locals())

def register(request):
    if request.session.get('is_login',None):
        return redirect('/index/')
    if request.method == 'POST':
        requester_form = forms.RegisterForm(request.POST)
        message = "请检查填写内容"
        if requester_form.is_valid():
            username = requester_form.cleaned_data.get('username')
            password1 = requester_form.cleaned_data.get('password1')
            password2 = requester_form.cleaned_data.get('password2')
            if password1 != password2:
                message = '两次密码不同'
                return render(request,'CMDB/register.html',locals())
            else:
                same_name_user = models.User.objects.filter(name=username)
                if same_name_user:
                    message = "用户已存在"
                    return render(request, "CMDB/register.html", locals())
                new_user = models.User()
                new_user.name = username
                new_user.password = hashpass(username,password2)
                new_user.save()
                
                return redirect('/login/')
        else:
            return render(request, 'CMDB/register.html',locals())
    requester_form = forms.RegisterForm()
    return render(request,'CMDB/register.html',locals())

def logout(request):
    if not request.session.get('is_login', None):
        return redirect("/login/")
    request.session.flush()
    return redirect("/login/")

def renew(request):
    if not request.session.get('is_login',None):
        return redirect('/unlogindex/')
    if request.method =='POST':
        requester_form = forms.RenewForm(request.POST)
    sn = request.session['sn']
    others = models.AsSet.objects.get(sn=sn)
    manufacturers = models.Manufacturer.objects.all()
    houses = models.House.objects.all()
    rooms = models.Room.objects.all()
    nowpage = '信息更新'
    page = '信息更新'
    return render(request,'CMDB/renew.html',locals())

def add(request):
    if not request.session.get('is_login',None):
        return redirect('/unlogindex/')
    if request.method =='POST':
        requester_form = forms.AddForm(request.POST)
        message = "检查填写内容"
        if requester_form.is_valid():
            sn = requester_form.cleaned_data.get('sn')
            called = requester_form.cleaned_data.get('called')
            manageIP = get_ip(request)
            indate = requester_form.cleaned_data.get('indate')
            expiredate = requester_form.cleaned_data.get('expiredate')
            status = requester_form.cleaned_data.get('status')
            memo = requester_form.cleaned_data.get('memo')
            manufacturer = requester_form.cleaned_data.get('manufacturer')
            house = requester_form.cleaned_data.get('house')
            room = requester_form.cleaned_data.get('room')
            if sn == "":
                message = '编码为必填项'
            else:
                same_sn = models.AsSet.objects.filter(sn=sn)
                if same_sn:
                    message = "更新请使用更新选项"
                    request.session['sn'] = sn
                    return redirect('/renew/')
                new_thing = models.AsSet()
                new_thing.sn = sn
                new_thing.called = called
                new_thing.manageIP = manageIP
                new_thing.indate = indate
                new_thing.expiredate = expiredate
                new_thing.memo = memo
                new_thing.status = status
                #new_thing.manufacturer = manufacturer
                #new_thing.house = house
                #new_thing.room = room
                new_thing.save()
                return redirect('/add/')
        else:
            return render(request,'/add/',locals())
    requester_form = forms.AddForm()
    manufacturers = models.Manufacturer.objects.all()
    houses = models.House.objects.all()
    rooms = models.Room.objects.all()
    nowpage = '新增页'
    page = '新增页'
    return render(request,'CMDB/add.html',locals())