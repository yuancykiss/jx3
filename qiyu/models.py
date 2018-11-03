from django.db import models

# Create your models here.

class P_Server(models.Model):
    class Meta():
        db_table = 'p_server'

    server_id = models.IntegerField(null=False, unique=True, primary_key=True, )
    area_name = models.CharField(max_length=50, null=True, default='')
    server_name = models.CharField(max_length=50, null=True, default='')


class P_user(models.Model):
    class Meta():
        db_table = 'p_user'

    user_id = models.IntegerField(null=False, unique=True, primary_key=True)
    user_name = models.CharField(null=True, default='', max_length=128)
    user_server = models.ForeignKey(P_Server, related_name='server')