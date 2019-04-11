import os
import time
from django.db import models

def candidate_image_path(instance, filename):
    ext = os.path.splitext(filename)[-1]
    now = str(time.time()).replace('.', '')
    f_name = '{}.{}'.format(now, ext)
    return os.path.join('candidates', f_name)

class Candidate(models.Model):
    name = models.CharField('姓名', max_length=50)
    politics = models.TextField('政見')
    age = models.PositiveIntegerField('年齡')
    image = models.ImageField('圖片', null=True, blank=True, upload_to=candidate_image_path)

    def __str__(self):
        return self.name