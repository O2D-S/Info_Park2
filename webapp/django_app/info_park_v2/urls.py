from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:num>',views.index,name='index'),
    path('post',views.post,name='post'),
    path('register',views.register,name='register'),
    path('login',views.Login,name='Login'),
    path('logout',views.Logout,name='Logout'),
    path('profile',views.profile,name='profile'),
    path('profile/<int:num>',views.profile,name='profile'),
    path('other_pro',views.other_pro,name="other_pro"),
    path('other_pro/<int:user_id>',views.other_pro,name="other_pro"),
    path('other_pro/<int:user_id>/<int:num>',views.other_pro,name="other_pro"),
    #path('edit',views.edit,name='edit'),
    #path('profile/edit',views.edit,name='edit'),
    #path('edit/<msg>',views.edit,name='edit'),
    path('edit/<int:pk>',views.EditContentView.as_view(),name='edit'),
    path('delete/<int:pk>', views.DeleteContentView.as_view(), name='delete'),
    #path('delete/<int:pk>', views.delete, name='delete'),
    #path('delete/<int:num>/<int:pk>', views.delete, name='delete'),
    #path('edit/', views.EditContentView.as_view(), name='edit'),
    #path('edit/<int:pk>', views.EditContentView.as_view(), name='edit'),
    path('good/<int:good_id>',views.good,name='good'),
    #path('profile/edit/?msg=<msg>',views.edit,name='edit')
    path('follow/',views.follow,name='follow'),
    #path('signup',views.signup,name='signup'),
    #path('create', views.create, name='create'),
    #path('delete/<int:num>', views.delete, name='delete'),
    #path('list', FriendList.as_view()), 
]