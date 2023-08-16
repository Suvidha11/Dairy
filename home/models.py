from django.db import models
from  django.contrib.auth.models import User
# Create your models here.
class memo(models.Model):
    post_id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=20)
    desc= models.TextField()
    image=models.ImageField(upload_to="images")
    user =models.ForeignKey(User,on_delete=models.CASCADE)
    Privcy=models.CharField(max_length=10, default="Public")
   
    def __str__(self):
       return f'{self.title} - {self.Privcy}'     
    
class comments(models.Model):
    post=models.ForeignKey(memo,on_delete=models.CASCADE)
    comment=models.TextField()
    comment_by = models.ForeignKey(User, on_delete=models.CASCADE)
     
    def __str__(self):
       return self.comment
      