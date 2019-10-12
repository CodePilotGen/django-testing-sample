from django.db import models

class NewsArticle(models.Model):

    name = models.CharField(("Arcticle Name"), max_length=50)
    content = models.TextField(("Article Content"))
    created_at = models.DateTimeField(("Created at"), auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(("Updated at"), auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"
