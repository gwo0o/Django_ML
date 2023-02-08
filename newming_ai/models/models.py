from django.db import models

# Create your models here.

class Article(models.Model):
    id = models.CharField(db_column='_key', max_length=255, primary_key=True)
    title = models.TextField(db_column='title', blank=True, null=True)
    content = models.TextField(db_column='content', blank=True, null=True)
    tags = models.CharField(db_column='tags', max_length=255, blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = 'nm_interest_press_article_60days_content'