from django.db import models

# Create your models here.
# 게시글  (post)엔 제목(postname), 내용(contents)이 존재

class Post(models.Model):
    postname = models.CharField(max_length=50)
    mainphoto = models.ImageField(blank=True, null=True)
    contents = models.TextField()
    

    def __srt__(self):
        return self.postname