from django.db import models

class Work(models.Model):
    image = models.ImageField(upload_to='images/')
    url = models.CharField(max_length=50)
    summary = models.CharField(max_length=200)
    
class Blog(models.Model):
# title
# pub_date
# body
# image
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')

