from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#Contentクラス
class Content(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE,related_name='content_owner')
    keyword = models.TextField(max_length=10)
    content = models.TextField(max_length=1000)
    good_count = models.IntegerField(default=0)
    #pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        #return str(self)
        return str(self.content)+'('+str(self.owner)+')'
    
    #class Meta:
    #    ordering = ('-pub_date',)

#Followerクラス
class Follower(models.Model):
    following = models.ForeignKey(User,on_delete=models.CASCADE,related_name='follower_owner')
    follower = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.follower)+'(Followed by:'+str(self.follower)+'")'

#Goodsクラス
class Goods(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE,related_name='goods_owner')
    content = models.ForeignKey(Content,on_delete=models.CASCADE)

    def __str__(self):
        return 'good for"'+str(self.content)+'"(by '+str(self.owner)+')'

#accountクラス
class account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    #name = models.ForeignKey(User,on_delete=models.CASCADE,related_name='account_owner')
    #mail = models.EmailField(max_length=100)
    #content = models.ForeignKey(Content,on_delete=models.CASCADE)
    #password = models.ForeignKey(User,max_length=15,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
