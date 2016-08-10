from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class LibraryUser(models.Model):

    library_user_belongs_to_user = models.ForeignKey(User)
    is_user_librarian = models.BooleanField(default=False)

    def __unicode__(self):
        return self.library_user_belongs_to_user.username


class Books(models.Model):

    book_title = models.CharField(max_length=200)
    book_author = models.CharField(max_length=13)
    book_price = models.PositiveIntegerField()
    book_author_contact = models.CharField(max_length=13, null=True, blank=True)

    def __unicode__(self):
        return self.book_title
