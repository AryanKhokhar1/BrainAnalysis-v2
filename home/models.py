from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# To Store Questions in sqlite

class Question(models.Model):

    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    question_number = models.PositiveIntegerField(primary_key=True)
    question_id = models.CharField(max_length=100, null=False, default='GivemeId')
    question_text = models.TextField()
    keyed = models.CharField(max_length=10) # plus = 1  and minus = 0
    domain = models.CharField(max_length=10)
    facet = models.IntegerField()

    def aslist(self):
        return ([self.user, self.question_number, self.question_text, self.keyed, self.domain, self.facet])