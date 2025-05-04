from django.db import models

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    date = models.DateField()
    image = models.URLField(blank=True)
    author = models.CharField(max_length=255)

    def __str__(self):
        return self.title
    
    class Meta:
        # ! By default, Django shows "Newss" on the admin page 🤦‍♂️
        # ! This sets the correct name: "News"
        # ! ✅ Try this: comment out this Meta block and reload /admin
        # ! You'll see "Newss" appear — that's why we need it!
        # - Christian V
        verbose_name = "News"
        verbose_name_plural = "News"
