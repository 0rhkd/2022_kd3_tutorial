from django.db import models


class Armyshop(models.Model):
    year = models.IntegerField()
    month = models.IntegerField()
    type = models.TextField()
    name = models.TextField()

    class Meta:
        db_table = 'army_shop'
        # 이미 생성되어 있는 테이블이므로
        managed = False

class Course(models.Model):
 name = models.CharField(max_length=30)
 cnt = models.IntegerField()

