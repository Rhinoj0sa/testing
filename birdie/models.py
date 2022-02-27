from django.db import models


class Post(models.Model):
    body = models.TextField()
    message = models.TextField()
    date_posted = models.DateField(auto_now=True)

    def get_excerpt(self, chars_to_show):
        return self.body[:chars_to_show]
