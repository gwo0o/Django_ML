from django.db import models

class Keyword(models.Model):
    _id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=30) # 제목
    content = models.CharField(max_length=255) # 내용

    def __str__(self):
        return self._id, self.title, self.content