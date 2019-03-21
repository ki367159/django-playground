from django.db import models


class Candidate(models.Model):
    name = models.CharField('姓名', max_length=50)
    politics = models.TextField('政見')
    age = models.PositiveIntegerField('年齡')

    def __str__(self):
        return self.name