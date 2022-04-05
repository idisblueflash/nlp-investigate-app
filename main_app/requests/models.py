from django.db import models


# Create your models here.
class Request(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()
    pub_date = models.DateTimeField('Date Published')

    def __str__(self):
        return f'{self.title}'


class Question(models.Model):
    request = models.ForeignKey(Request, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=256)

    def __str__(self):
        return f'{self.question_text}'
