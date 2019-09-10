from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateField(auto_now=False)
 
    image = models.ImageField(upload_to='images/')
    body = models.TextField()

    def __str__(self):
        return self.title       # it will show title inplace of blog.object1

    def summary(self):
        return self.body[:200]

   # def date_prety(self):
     #   return self.date.strftime(' %b %e %Y ')
