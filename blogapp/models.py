from django.db import models


class BlogModel(models.Model):
    id = models.IntegerField(primary_key=True)
    blog_title = models.CharField(max_length=20)
    blog = models.TextField()

    def __str__(self):
        return f"Blog: {self.blog_title}"


class FileModel(models.Model):
    source_name = models.CharField(max_length=20)
    source_file = models.CharField(max_length=20)
    # blog = models.ForeignKey('BlogModel', on_delete=models.CASCADE)

    def __str__(self):
        return f"Comment by Name: {self.source_name}"
