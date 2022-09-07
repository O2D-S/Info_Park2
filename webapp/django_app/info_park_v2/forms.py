from asyncio import format_helpers
from django import forms
from .models import Content,Follower,Goods,account
from django.contrib.auth.models import User

from django.core.exceptions import ValidationError

#Contentのフォーム（未使用）
class ContentsForm(forms.ModelForm):
    class Meta:
        model = Content
        fields = ['owner','content']
    #owner = forms.CharField(label='Name',widget=forms.TextInput(attrs={'class':'form-control'}))
    #keyword = forms.CharField(label='Email',widget=forms.EmailInput(attrs={'class':'form-control'}))
    #content = forms.CharField(label='Content',widget=forms.TextInput(attrs={'class':'form-control'}))

#Followerのフォーム（未使用）
class Follower(forms.ModelForm):
    class Meta:
        model = Follower
        fields = ['following','follower']

#Goodsのフォーム（未使用）
class GoodsForm(forms.ModelForm):
    class Meta:
        model = Goods
        fields = ['owner','content']

#accountのフォーム（未使用）
#class accountForm(forms.ModelForm):
#    class Meta:
#        model = account
#        fields = ['name','mail','content','password']

#コンテンツ検索フォーム
class ContentsResearchForm(forms.Form):
    keyword = forms.CharField(label="",max_length=10,required=False,widget=forms.TextInput(attrs={'class':'form-control'}))

#投稿フォーム
class PostForm(forms.Form):
    content = forms.CharField(label="",max_length=1000,widget=forms.Textarea(attrs={'class':'form-control','rows':2}))
    
    #def __init__(self,user,*args,**kwargs):
    #    super(PostForm,self).__init__(*args,**kwargs)
        #public = User.objects.filter(username='public').first()

#アカウント情報フォーム
#class AddAccountForm(forms.Form):
#    name = forms.CharField(label="名前",required=True,max_length=20,widget=forms.TextInput(attrs={'class':'form-control'}))
#    mail = forms.EmailField(label="E-mail",required=True,max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
#    password = forms.CharField(label="パスワード",required=True,max_length=255,min_length=6,widget=forms.PasswordInput(attrs={'placeholder': '******',}))
#    confirm_password = forms.CharField(label="パスワード（確認用）",required=True,max_length=255,min_length=6,widget=forms.PasswordInput(attrs={'placeholder': '******',}))

    #def clean_username(self):
    #    username = self.cleaned_data['name']
    #    return username

    #def clean_email(self):
    #    email = self.cleaned_data['email']
    #    if User.objects.filter(email=email):
    #        raise ValidationError('既に登録されているメールアドレスです。')
    #    return email

    #def clean_password(self):
    #    password = self.cleaned_data['password']
    #    return password

    #def clean_confirm_password(self):
    #    confirm_password = self.cleaned_data['confirm_password']
    #    return confirm_password

    #def clean(self):
    #    cleaned_data = super().clean()
    #    password = self.cleaned_data.get('password')
    #    confirm_password = self.cleaned_data.get('confirm_password')
    #    if password != confirm_password:
    #        self.add_error(field='confirm_password',error=ValidationError('パスワードが一致しません。'))
    #    return cleaned_data

# フォームクラス作成
class AccountForm(forms.ModelForm):
    # パスワード入力：非表示対応
    password = forms.CharField(widget=forms.PasswordInput(),label="パスワード")

    class Meta():
        # ユーザー認証
        model = User
        # フィールド指定
        fields = ['username','email','password']
        # フィールド名指定
        labels = {'username':"ユーザーID",'email':"メール"}