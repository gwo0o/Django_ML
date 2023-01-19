# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Article(models.Model):
    field_id = models.CharField(db_column='_id', max_length=255, blank=True, null=True)  # Field renamed because it started with '_'.
    field_key = models.CharField(db_column='_key', max_length=255, blank=True, null=True)  # Field renamed because it started with '_'.
    category_ids = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.CharField(max_length=255, blank=True, null=True)
    is_breaking = models.CharField(max_length=255, blank=True, null=True)
    modified_at = models.CharField(max_length=255, blank=True, null=True)
    press_id = models.CharField(max_length=255, blank=True, null=True)
    published_at = models.CharField(max_length=255, blank=True, null=True)
    raw_id = models.CharField(max_length=255, blank=True, null=True)
    source_language = models.CharField(max_length=255, blank=True, null=True)
    source_parsed_at = models.CharField(max_length=255, blank=True, null=True)
    source_type = models.CharField(max_length=255, blank=True, null=True)
    styles = models.CharField(max_length=255, blank=True, null=True)
    tags = models.CharField(max_length=255, blank=True, null=True)
    thumbnail = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    updated_at = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'article'


class Comment(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    post_id = models.IntegerField()
    comment = models.CharField(max_length=255, blank=True, null=True)
    hidden = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comment'


class GeekNews(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    title = models.CharField(max_length=255, blank=True, null=True)
    content = models.CharField(max_length=255, blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'geek_news'


class NmArticles(models.Model):
    field_key = models.CharField(db_column='_key', primary_key=True, max_length=32)  # Field renamed because it started with '_'.
    category_ids = models.CharField(max_length=40)
    press_id = models.IntegerField()
    title = models.CharField(max_length=255)
    summary = models.CharField(max_length=500, blank=True, null=True)
    content = models.TextField()
    text = models.TextField()
    thumbnail = models.CharField(max_length=255, blank=True, null=True)
    link = models.CharField(max_length=255, blank=True, null=True)
    source_type = models.CharField(max_length=50, blank=True, null=True)
    source_date = models.CharField(max_length=10)
    source_key = models.CharField(unique=True, max_length=255)
    source_relation_key = models.CharField(max_length=32)
    source_language = models.CharField(max_length=10, blank=True, null=True)
    source_status = models.CharField(max_length=10, blank=True, null=True)
    source_parsed_logs = models.TextField(blank=True, null=True)
    source_parsed_at = models.DateTimeField(blank=True, null=True)
    published_at = models.DateTimeField(blank=True, null=True)
    modified_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    photos = models.TextField(blank=True, null=True)
    videos = models.TextField(blank=True, null=True)
    extras = models.TextField(blank=True, null=True)
    title_tokens = models.TextField()
    content_tokens = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'nm_articles'


class NmInterestPressArticle60DaysContent(models.Model):
    field_key = models.CharField(db_column='_key', max_length=32, blank=True, null=True)  # Field renamed because it started with '_'.
    tags = models.CharField(max_length=2000, blank=True, null=True)
    title = models.CharField(max_length=1000, blank=True, null=True)
    thumbnail = models.CharField(max_length=1000, blank=True, null=True)
    press_id = models.IntegerField(blank=True, null=True)
    published_at = models.DateTimeField(blank=True, null=True)
    category_ids = models.CharField(max_length=2000, blank=True, null=True)
    row_id = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nm_interest_press_article_60days_content'


class NmPage(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    admin_id = models.IntegerField()
    campaign_id = models.IntegerField()
    page_parent_id = models.IntegerField()
    page_type = models.CharField(max_length=20)
    page_group = models.CharField(max_length=30)
    page_code = models.CharField(max_length=50)
    page_slug = models.CharField(max_length=50)
    page_language = models.CharField(max_length=10, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    summary = models.TextField(blank=True, null=True)
    html = models.TextField(blank=True, null=True)
    extras = models.TextField(blank=True, null=True)
    thumbnail = models.CharField(max_length=255, blank=True, null=True)
    link = models.CharField(max_length=255, blank=True, null=True)
    display_start_at = models.DateTimeField(blank=True, null=True)
    display_end_at = models.DateTimeField(blank=True, null=True)
    published = models.IntegerField(blank=True, null=True)
    published_at = models.DateTimeField(blank=True, null=True)
    sort_order = models.IntegerField()
    resource_key = models.CharField(max_length=255)
    resources = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    archived = models.IntegerField(blank=True, null=True)
    archived_at = models.DateTimeField(blank=True, null=True)
    date_group = models.CharField(max_length=14, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nm_page'


class NmPost(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    post_type = models.CharField(max_length=20, blank=True, null=True)
    post_sub_type = models.CharField(max_length=20, blank=True, null=True)
    post_group = models.CharField(max_length=50, blank=True, null=True)
    post_parent_target = models.CharField(max_length=30, blank=True, null=True)
    post_parent_id = models.IntegerField(blank=True, null=True)
    post_depth = models.IntegerField(blank=True, null=True)
    post_order = models.IntegerField(blank=True, null=True)
    post_title = models.CharField(max_length=255, blank=True, null=True)
    post_content = models.TextField(blank=True, null=True)
    post_markdown_used = models.IntegerField(blank=True, null=True)
    post_markdown = models.TextField(blank=True, null=True)
    post_summary = models.CharField(max_length=500, blank=True, null=True)
    linked_target = models.CharField(max_length=50, blank=True, null=True)
    linked_target_id = models.CharField(max_length=32, blank=True, null=True)
    tags = models.CharField(max_length=255, blank=True, null=True)
    campaign_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    user_email = models.CharField(max_length=255, blank=True, null=True)
    user_password = models.CharField(max_length=50, blank=True, null=True)
    profile_image = models.CharField(max_length=255, blank=True, null=True)
    permission = models.IntegerField(blank=True, null=True)
    display_start_at = models.DateTimeField(blank=True, null=True)
    display_end_at = models.DateTimeField(blank=True, null=True)
    extras = models.TextField(blank=True, null=True)
    resource_key = models.CharField(max_length=255)
    resources = models.TextField(blank=True, null=True)
    hidden = models.IntegerField()
    hidden_at = models.DateTimeField(blank=True, null=True)
    blocked = models.IntegerField()
    blocked_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    archived = models.IntegerField(blank=True, null=True)
    archived_at = models.DateTimeField(blank=True, null=True)
    only_ming = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nm_post'


class NmPressArticle20210205(models.Model):
    field_key = models.CharField(db_column='_key', primary_key=True, max_length=32)  # Field renamed because it started with '_'.
    category_ids = models.CharField(max_length=40)
    press_id = models.IntegerField()
    title = models.CharField(max_length=255)
    summary = models.CharField(max_length=500, blank=True, null=True)
    content = models.TextField()
    text = models.TextField()
    thumbnail = models.CharField(max_length=255, blank=True, null=True)
    link = models.CharField(max_length=255, blank=True, null=True)
    source_type = models.CharField(max_length=50, blank=True, null=True)
    source_date = models.CharField(max_length=10)
    source_key = models.CharField(unique=True, max_length=255)
    source_relation_key = models.CharField(max_length=32)
    source_language = models.CharField(max_length=10, blank=True, null=True)
    source_status = models.CharField(max_length=10, blank=True, null=True)
    source_parsed_logs = models.TextField(blank=True, null=True)
    source_parsed_at = models.DateTimeField(blank=True, null=True)
    published_at = models.DateTimeField(blank=True, null=True)
    modified_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    photos = models.TextField(blank=True, null=True)
    videos = models.TextField(blank=True, null=True)
    extras = models.TextField(blank=True, null=True)
    title_tokens = models.TextField()
    content_tokens = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'nm_press_article_20210205'


class NmPressArticle20220622(models.Model):
    field_key = models.CharField(db_column='_key', primary_key=True, max_length=32)  # Field renamed because it started with '_'.
    category_ids = models.CharField(max_length=40)
    press_id = models.IntegerField()
    title = models.CharField(max_length=255)
    summary = models.CharField(max_length=500, blank=True, null=True)
    content = models.TextField()
    text = models.TextField()
    thumbnail = models.CharField(max_length=255, blank=True, null=True)
    link = models.CharField(max_length=255, blank=True, null=True)
    reporters = models.TextField(blank=True, null=True)
    source_type = models.CharField(max_length=50, blank=True, null=True)
    source_date = models.CharField(max_length=10)
    source_key = models.CharField(unique=True, max_length=255)
    source_relation_key = models.CharField(max_length=32)
    source_language = models.CharField(max_length=10, blank=True, null=True)
    source_status = models.CharField(max_length=10, blank=True, null=True)
    source_parsed_logs = models.TextField(blank=True, null=True)
    source_parsed_at = models.DateTimeField(blank=True, null=True)
    published_at = models.DateTimeField(blank=True, null=True)
    modified_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    photos = models.TextField(blank=True, null=True)
    videos = models.TextField(blank=True, null=True)
    extras = models.TextField(blank=True, null=True)
    title_tokens = models.TextField()
    content_tokens = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'nm_press_article_20220622'


class NmPressArticle20221227(models.Model):
    field_key = models.CharField(db_column='_key', primary_key=True, max_length=32)  # Field renamed because it started with '_'.
    category_ids = models.CharField(max_length=40)
    press_id = models.IntegerField()
    title = models.CharField(max_length=255)
    summary = models.CharField(max_length=500, blank=True, null=True)
    content = models.TextField()
    text = models.TextField()
    thumbnail = models.CharField(max_length=255, blank=True, null=True)
    link = models.CharField(max_length=255, blank=True, null=True)
    reporters = models.TextField(blank=True, null=True)
    source_type = models.CharField(max_length=50, blank=True, null=True)
    source_date = models.CharField(max_length=10)
    source_key = models.CharField(unique=True, max_length=255)
    source_relation_key = models.CharField(max_length=32)
    source_language = models.CharField(max_length=10, blank=True, null=True)
    source_status = models.CharField(max_length=10, blank=True, null=True)
    source_parsed_logs = models.TextField(blank=True, null=True)
    source_parsed_at = models.DateTimeField(blank=True, null=True)
    published_at = models.DateTimeField(blank=True, null=True)
    modified_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    photos = models.TextField(blank=True, null=True)
    videos = models.TextField(blank=True, null=True)
    extras = models.TextField(blank=True, null=True)
    title_tokens = models.TextField()
    content_tokens = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'nm_press_article_20221227'


class NmPressArticle20221228(models.Model):
    field_key = models.CharField(db_column='_key', primary_key=True, max_length=32)  # Field renamed because it started with '_'.
    category_ids = models.CharField(max_length=40)
    press_id = models.IntegerField()
    title = models.CharField(max_length=255)
    summary = models.CharField(max_length=500, blank=True, null=True)
    content = models.TextField()
    text = models.TextField()
    thumbnail = models.CharField(max_length=255, blank=True, null=True)
    link = models.CharField(max_length=255, blank=True, null=True)
    reporters = models.TextField(blank=True, null=True)
    source_type = models.CharField(max_length=50, blank=True, null=True)
    source_date = models.CharField(max_length=10)
    source_key = models.CharField(unique=True, max_length=255)
    source_relation_key = models.CharField(max_length=32)
    source_language = models.CharField(max_length=10, blank=True, null=True)
    source_status = models.CharField(max_length=10, blank=True, null=True)
    source_parsed_logs = models.TextField(blank=True, null=True)
    source_parsed_at = models.DateTimeField(blank=True, null=True)
    published_at = models.DateTimeField(blank=True, null=True)
    modified_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    photos = models.TextField(blank=True, null=True)
    videos = models.TextField(blank=True, null=True)
    extras = models.TextField(blank=True, null=True)
    title_tokens = models.TextField()
    content_tokens = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'nm_press_article_20221228'


class NmPressArticle20221229(models.Model):
    field_key = models.CharField(db_column='_key', primary_key=True, max_length=32)  # Field renamed because it started with '_'.
    category_ids = models.CharField(max_length=40)
    press_id = models.IntegerField()
    title = models.CharField(max_length=255)
    summary = models.CharField(max_length=500, blank=True, null=True)
    content = models.TextField()
    text = models.TextField()
    thumbnail = models.CharField(max_length=255, blank=True, null=True)
    link = models.CharField(max_length=255, blank=True, null=True)
    reporters = models.TextField(blank=True, null=True)
    source_type = models.CharField(max_length=50, blank=True, null=True)
    source_date = models.CharField(max_length=10)
    source_key = models.CharField(unique=True, max_length=255)
    source_relation_key = models.CharField(max_length=32)
    source_language = models.CharField(max_length=10, blank=True, null=True)
    source_status = models.CharField(max_length=10, blank=True, null=True)
    source_parsed_logs = models.TextField(blank=True, null=True)
    source_parsed_at = models.DateTimeField(blank=True, null=True)
    published_at = models.DateTimeField(blank=True, null=True)
    modified_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    photos = models.TextField(blank=True, null=True)
    videos = models.TextField(blank=True, null=True)
    extras = models.TextField(blank=True, null=True)
    title_tokens = models.TextField()
    content_tokens = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'nm_press_article_20221229'


class NmPressArticle20221230(models.Model):
    field_key = models.CharField(db_column='_key', primary_key=True, max_length=32)  # Field renamed because it started with '_'.
    category_ids = models.CharField(max_length=40)
    press_id = models.IntegerField()
    title = models.CharField(max_length=255)
    summary = models.CharField(max_length=500, blank=True, null=True)
    content = models.TextField()
    text = models.TextField()
    thumbnail = models.CharField(max_length=255, blank=True, null=True)
    link = models.CharField(max_length=255, blank=True, null=True)
    reporters = models.TextField(blank=True, null=True)
    source_type = models.CharField(max_length=50, blank=True, null=True)
    source_date = models.CharField(max_length=10)
    source_key = models.CharField(unique=True, max_length=255)
    source_relation_key = models.CharField(max_length=32)
    source_language = models.CharField(max_length=10, blank=True, null=True)
    source_status = models.CharField(max_length=10, blank=True, null=True)
    source_parsed_logs = models.TextField(blank=True, null=True)
    source_parsed_at = models.DateTimeField(blank=True, null=True)
    published_at = models.DateTimeField(blank=True, null=True)
    modified_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    photos = models.TextField(blank=True, null=True)
    videos = models.TextField(blank=True, null=True)
    extras = models.TextField(blank=True, null=True)
    title_tokens = models.TextField()
    content_tokens = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'nm_press_article_20221230'


class NmPressArticle20221231(models.Model):
    field_key = models.CharField(db_column='_key', primary_key=True, max_length=32)  # Field renamed because it started with '_'.
    category_ids = models.CharField(max_length=40)
    press_id = models.IntegerField()
    title = models.CharField(max_length=255)
    summary = models.CharField(max_length=500, blank=True, null=True)
    content = models.TextField()
    text = models.TextField()
    thumbnail = models.CharField(max_length=255, blank=True, null=True)
    link = models.CharField(max_length=255, blank=True, null=True)
    reporters = models.TextField(blank=True, null=True)
    source_type = models.CharField(max_length=50, blank=True, null=True)
    source_date = models.CharField(max_length=10)
    source_key = models.CharField(unique=True, max_length=255)
    source_relation_key = models.CharField(max_length=32)
    source_language = models.CharField(max_length=10, blank=True, null=True)
    source_status = models.CharField(max_length=10, blank=True, null=True)
    source_parsed_logs = models.TextField(blank=True, null=True)
    source_parsed_at = models.DateTimeField(blank=True, null=True)
    published_at = models.DateTimeField(blank=True, null=True)
    modified_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    photos = models.TextField(blank=True, null=True)
    videos = models.TextField(blank=True, null=True)
    extras = models.TextField(blank=True, null=True)
    title_tokens = models.TextField()
    content_tokens = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'nm_press_article_20221231'


class NmPressArticle20230101(models.Model):
    field_key = models.CharField(db_column='_key', primary_key=True, max_length=32)  # Field renamed because it started with '_'.
    category_ids = models.CharField(max_length=40)
    press_id = models.IntegerField()
    title = models.CharField(max_length=255)
    summary = models.CharField(max_length=500, blank=True, null=True)
    content = models.TextField()
    text = models.TextField()
    thumbnail = models.CharField(max_length=255, blank=True, null=True)
    link = models.CharField(max_length=255, blank=True, null=True)
    reporters = models.TextField(blank=True, null=True)
    source_type = models.CharField(max_length=50, blank=True, null=True)
    source_date = models.CharField(max_length=10)
    source_key = models.CharField(unique=True, max_length=255)
    source_relation_key = models.CharField(max_length=32)
    source_language = models.CharField(max_length=10, blank=True, null=True)
    source_status = models.CharField(max_length=10, blank=True, null=True)
    source_parsed_logs = models.TextField(blank=True, null=True)
    source_parsed_at = models.DateTimeField(blank=True, null=True)
    published_at = models.DateTimeField(blank=True, null=True)
    modified_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    photos = models.TextField(blank=True, null=True)
    videos = models.TextField(blank=True, null=True)
    extras = models.TextField(blank=True, null=True)
    title_tokens = models.TextField()
    content_tokens = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'nm_press_article_20230101'


class NmPressArticle20230102(models.Model):
    field_key = models.CharField(db_column='_key', primary_key=True, max_length=32)  # Field renamed because it started with '_'.
    category_ids = models.CharField(max_length=40)
    press_id = models.IntegerField()
    title = models.CharField(max_length=255)
    summary = models.CharField(max_length=500, blank=True, null=True)
    content = models.TextField()
    text = models.TextField()
    thumbnail = models.CharField(max_length=255, blank=True, null=True)
    link = models.CharField(max_length=255, blank=True, null=True)
    reporters = models.TextField(blank=True, null=True)
    source_type = models.CharField(max_length=50, blank=True, null=True)
    source_date = models.CharField(max_length=10)
    source_key = models.CharField(unique=True, max_length=255)
    source_relation_key = models.CharField(max_length=32)
    source_language = models.CharField(max_length=10, blank=True, null=True)
    source_status = models.CharField(max_length=10, blank=True, null=True)
    source_parsed_logs = models.TextField(blank=True, null=True)
    source_parsed_at = models.DateTimeField(blank=True, null=True)
    published_at = models.DateTimeField(blank=True, null=True)
    modified_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    photos = models.TextField(blank=True, null=True)
    videos = models.TextField(blank=True, null=True)
    extras = models.TextField(blank=True, null=True)
    title_tokens = models.TextField()
    content_tokens = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'nm_press_article_20230102'


class Post(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    post_group = models.CharField(max_length=11, blank=True, null=True)
    post_title = models.CharField(max_length=100, blank=True, null=True)
    post_content = models.CharField(max_length=500, blank=True, null=True)
    hidden = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'post'


class TestArticle(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    title = models.CharField(max_length=255, blank=True, null=True)
    content = models.CharField(max_length=1000, blank=True, null=True)
    class_field = models.CharField(db_column='class', max_length=255, blank=True, null=True)  # Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'test_article'


class User(models.Model):
    user_id = models.IntegerField(primary_key=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    user_image = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'
