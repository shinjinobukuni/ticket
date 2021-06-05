from django.db import models
from manageType.models import Type

# Create your models here.
class Header(models.Model):
    """チケットヘッダー"""
    TYPE_CLS_CHOICES = [
        (1, "周知"),
        (2, "検討"),
        (3, "作業"),
    ]
    STATUS_CHOICES = [
        (1, "未着手"),
        (2, "着手中"),
        (3, "完了"),
    ]
    type_cls = models.ForeignKey(Type, models.SET_NULL, null=True)
    title = models.CharField(verbose_name='タイトル', max_length=40)
    limit_date = models.DateField(verbose_name='期限', blank=True, null=True)
    status = models.IntegerField(verbose_name="ステータス", choices = STATUS_CHOICES, default = 1)

    class Meta:
        verbose_name_plural = 'Header'
        verbose_name = '課題ヘッダー'

    def __str__(self):
        return self.title

