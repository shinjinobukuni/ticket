from django.db import models

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
    type_cls = models.IntegerField(verbose_name="種別", choices =TYPE_CLS_CHOICES, default=1)
    title = models.CharField(verbose_name='タイトル', max_length=40)
    limit_date = models.DateField(verbose_name='期限')
    status = models.IntegerField(verbose_name="ステータス", choices = STATUS_CHOICES, default = 1)

    class Meta:
        verbose_name_plural = 'Header'

    def __str__(self):
        return self.title

