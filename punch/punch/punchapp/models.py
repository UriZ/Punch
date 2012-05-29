from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=200)
    password = models.CharField(max_length=200,null=True,blank=True,)
    
    following = models.ManyToManyField('self',related_name = 'users_i_follow',
        symmetrical=False,null=True, blank=True,)
    followers = models.ManyToManyField('self',related_name = 'users_following_me',
        symmetrical=False,null=True, blank=True,)
    def __unicode__(self):
            return self.name

class Punchcollection(models.Model):
    title = models.CharField(max_length=200)
    user = models.ForeignKey(User)

    def __unicode__(self):
            return self.title
#user

class Punch(models.Model):
    href = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
   # description = models.CharField(max_length=200)
    #user
    funny_count = models.IntegerField()
    boo_count = models.IntegerField()
    #set
    punchcollection = models.ForeignKey(Punchcollection)

    def __unicode__(self):
            return self.title