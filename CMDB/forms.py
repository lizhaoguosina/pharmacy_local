from django import forms

class UserForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=64)
    password = forms.CharField(label='密码', max_length=254, widget=forms.PasswordInput)

class RegisterForm(forms.Form):
    username = forms.CharField(label='用户名',max_length=64, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label="密码", max_length=254, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="确认密码", max_length=254, widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class AddForm(forms.Form):
    sn = forms.CharField(label='资产编号',max_length=127, widget=forms.TextInput(attrs={'class': 'form-control'}))
    called = forms.CharField(label='名称',max_length=63)
    status = forms.IntegerField(label='状态')
    manufacturer = forms.CharField(label='制造商')
    memo = forms.CharField(label='备注',max_length=254)
    indate = forms.DateField(label='入库')
    expiredate = forms.DateField(label='出库')
    house = forms.CharField(label='实验楼')
    room = forms.CharField(label='房间')

class RenewForm(forms.Form):
    called = forms.CharField(label='名称')