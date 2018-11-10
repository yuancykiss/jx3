from django.db import models


class Experience(models.Model):
    class Meta:
        db_table = 'zili'

    rank = models.IntegerField(primary_key=True, null=False)
    name = models.CharField(max_length=50, null=True)
    war = models.CharField(max_length=50, null=True)
    menpai = models.CharField(max_length=50, null=True)
    daqu = models.CharField(max_length=50, null=True)
    server = models.CharField(max_length=50, null=True)
    score = models.CharField(max_length=50, null=True)