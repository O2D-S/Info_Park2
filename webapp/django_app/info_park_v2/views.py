from re import A
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required

from django.views.generic import UpdateView,DeleteView
from django.urls import reverse_lazy
import sys
from tkinter import messagebox

# ログイン・ログアウト処理に利用
from django.contrib.auth import get_user_model,authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

# Create your views here.

from .models import Content,Follower,Goods,account
from .forms import ContentsForm, ContentsResearchForm,PostForm,AccountForm#AddAccountForm
from django.core.paginator import Paginator

#@login_required(login_url='/admin/login/')
def index(request,num=1):
    if(request.method == 'POST'):
        form = ContentsResearchForm(request.POST)
        find = request.POST['keyword']
        data = Content.objects.filter(content__contains=find)
        #msg = '検索件数：'+str(data.sum())

    else:
        #msg = '検索したいキーワードを入力してください'
        form = ContentsResearchForm()
        data = Content.objects.all()
    
    paginator = Paginator(data,5)
    params = {
        'title':"トップ",
        #'message':msg,
        'form':form,
        'contents':paginator.get_page(num),
        'login_user':request.user,
    }

    return render(request, 'info_park_v2/index.html',params)

#@login_required(login_url='/admin/login/')
def post(request):
    log_judge = request.user.is_authenticated
    if log_judge == True:
        if request.method == 'POST':
            content = request.POST['content']
            msg = Content()
            msg.owner = request.user
            msg.content = content
            msg.save()

            messages.success(request, '投稿しました！')
            return redirect(to='/info_park_v2')
        else:
            form = PostForm()
            #ログイン機能を入れたら、form = PostForm(request.user)にすると思う
        params = {
            'title':'投稿する',
            'login_user':request.user,
            'form':form,
        }
    
    else:
        return Login(request)#render(request, 'info_park_v2/login.html')

    return render(request, 'info_park_v2/post.html',params)

#@login_required(login_url='/admin/login/')
#def signup(request):
#    if request.method=='GET':
#        form = AddAccountForm()
#    elif request.method == "POST":
#        form = AddAccountForm(request.POST)
        #if form.is_valid():
        #    get_user_model().objects.create_user(
        #        name=form.cleaned_data['name'],
        #        email=form.cleaned_data['email'],
        #        password=form.cleaned_data['password']
        #    )
        #    return HttpResponse('アカウント登録完了しました。')
#    params = {
#        'title':'Info-Park',
#        'form': form
#    }
#    return render(request, 'info_park_v2/signup.html', params)

def register(request):
    params = {
    "title":"新規登録/登録内容確認・変更",
    "AccountCreate":False,
    "account_form": AccountForm(),
    }

    if request.method=='POST':
        params["account_form"] = AccountForm(data=request.POST)
        # フォーム入力の有効検証
        if params["account_form"].is_valid():
            # アカウント情報をDB保存
            account = params["account_form"].save()
            # パスワードをハッシュ化
            account.set_password(account.password)
            # ハッシュ化パスワード更新
            account.save()

            # 下記追加情報
            # 下記操作のため、コミットなし
            #add_account = params["add_account_form"].save(commit=False)
            #add_account.user = account

            # アカウント作成情報更新
            params["AccountCreate"] = True

            #accountobj = account()
            #UserAccount = AccountForm(request.POST,instance=accountobj)
            #UserAccount.save()
        else:
            print(params["account_form"].errors)

    else:
        params["account_form"] = AccountForm()
        params["AccountCreate"] = False

    return render(request,"info_park_v2/register.html",params)


#ログイン
def Login(request):
    params = {
        'title':'ログイン'
    }
    # POST
    if request.method == 'POST':
        # フォーム入力のユーザーID・パスワード取得
        ID = request.POST.get('userid')
        Pass = request.POST.get('password')

        # Djangoの認証機能
        user = authenticate(username=ID, password=Pass)

        # ユーザー認証
        if user:
            #ユーザーアクティベート判定
            if user.is_active:
                # ログイン
                login(request,user)
                # ホームページ遷移
                return HttpResponseRedirect(reverse('index'))
            else:
                # アカウント利用不可
                return HttpResponse("アカウントが有効ではありません")
        # ユーザー認証失敗
        else:
            return HttpResponse("ログインIDまたはパスワードが間違っています")
    # GET
    else:
        return render(request, 'info_park_v2/login.html',params)


#ログアウト
@login_required
def Logout(request):
    logout(request)
    # ログイン画面遷移
    return HttpResponseRedirect(reverse('Login'))


#普通の関数
#def get_message(owner,page):
#   page_num=10


def profile(request,num=1):
    log_judge = request.user.is_authenticated
    if log_judge == True:
        owner = request.user
        data = Content.objects.filter(owner=owner)
        paginator = Paginator(data,5)
        
        params = {
            'title':'プロフィール',
            'name':owner.username,
            'contents':paginator.get_page(num),
            'login_user':request.user,
        }

    else:
        return Login(request)
    
    return render(request,'info_park_v2/profile.html',params)

def other_pro(request,user_id,num=1):
    log_judge = request.user.is_authenticated
    if log_judge == True:
        #owner = request.user
        #owner = account(id=user_id)
        owner = User.objects.get(id= user_id)
        #user = User.objects.all().values()
        data = Content.objects.filter(owner=owner)
        paginator = Paginator(data,5)
        
        params = {
            'title':'プロフィール',
            #'name':owner.name,
            #'email':owner.mail,
            'name':owner.username,
            'ID':user_id,
            'contents':paginator.get_page(num),
            'login_user':request.user,
        }

    else:
        return Login(request)
    
    return render(request,'info_park_v2/other_pro.html',params)

class EditContentView(UpdateView):
    model = Content
    form_class = ContentsForm
    success_url = reverse_lazy('profile')
    def edit(request):
        if (request.method == "POST"):
            form_class = ContentsForm(request.POST)
            form_class.save()

        params = {
            'title':"編集する",
            'form':form_class,
        }
        return render(request,'info_park_v2/edit.html',params)
    

class DeleteContentView(DeleteView):
    model = Content
    success_url = reverse_lazy('profile')

#def delete(request,num,pk):
#    content = Content.content.get(id=pk)
#    if request.method == "POST":
#        messages.info(request, "削除しますか")
#    return render(request,'info_park_v2/profile.html',params)

def good(request,good_id):
    log_judge = request.user.is_authenticated
    if log_judge == True:
        good_content = Content.objects.get(id = good_id)
        is_good = Goods.objects.filter(owner=request.user).filter(content=good_content).count()
        #is_good = 0
        if is_good > 0:
            messages.success(request, 'Good済')
            return redirect(to='/info_park_v2')

        good_content.good_count += 1
        good_content.save()

        good = Goods()
        good.owner = request.user
        good.content = good_content
        good.save()

        messages.success(request, 'Goodしました！')
    else:
        return Login(request)
    
    #is_good = 0
    return redirect(to='/info_park_v2')

def follow(request):
    log_judge = request.user.is_authenticated
    if log_judge == True:
        follow_name = request.GET['name']
        follow_user = User.objects.filter(username=follow_name).first()

        if follow_user == request.user:
            messages.info(request, "自分自身をFollowerに追加することはできません")
            return redirect(to='/info_park_v2')
        
        flw_num = Follower.objects.filter(following=request.user).filter(follower=follow_user).count()

        if flw_num > 0:
            messages.info(request, follow_user.username+'はすでに追加されています。')
            return redirect(to = '/info_park_v2')
        
        flw = Follower()
        flw.following = request.user
        flw.follower = follow_user
        flw.save()

        messages.success(request, follow_user.username + 'を追加しました！')

    else:
        return Login(request)

    return redirect(to='/info_park_v2')