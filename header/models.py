from django.db import models
from manageType.models import Type
from django.utils import timezone

# Create your models here.
class Header(models.Model):
    """課題ヘッダー"""
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
    content = models.CharField(verbose_name='内容', max_length=1000, blank=True, null=True)
    limit_date = models.DateField(verbose_name='期限', blank=True, null=True)
    status = models.IntegerField(verbose_name="ステータス", choices = STATUS_CHOICES, default = 1)

    class Meta:
        verbose_name_plural = 'Header'
        verbose_name = '課題ヘッダー'

    def __str__(self):
        return self.title


class Detail(models.Model):
    """課題明細"""
    header_id = models.ForeignKey(Header, on_delete=models.CASCADE, verbose_name='ヘッダーID')
    content = models.CharField(verbose_name='内容', max_length=1000, blank=True, null=True)
    create_at = models.DateField(verbose_name='作成日', default=timezone.now)

    class Meta:
        verbose_name_plural = 'Detail'
        verbose_name = '課題明細'

    def __str__(self):
        return str(self.header_id_id) + '　' + self.content[:20]