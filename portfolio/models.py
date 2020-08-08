from django.db import models

class Coca(models.Model):
    title = models.CharField(max_length=100)
    discription = models.TextField(max_length=9000)
    image = models.ImageField(upload_to='cocacola/media/portfolio/images/')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title
