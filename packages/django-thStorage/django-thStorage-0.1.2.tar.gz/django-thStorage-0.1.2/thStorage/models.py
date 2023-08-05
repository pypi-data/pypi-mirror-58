from django.db import models

# Create your models here.

class NetDiskUser(models.Model):
    id = models.AutoField(primary_key=True)
    platform = models.CharField(u'所属平台', max_length=256,default="default")
    username = models.CharField(u'用户名', max_length=256)
    systemUsername = models.CharField(u'系统用户名', max_length=256)
    cluster = models.CharField(u'集群',max_length=256)
    token = models.CharField(u'令牌', max_length=128, blank=True, null=True)
    tokenGererateTime = models.IntegerField(u'令牌生成时间戳', blank=True, null=True)
    tokenValidityPeriod = models.IntegerField(u'令牌有效期', default=3600)

    class Meta:
        db_table = u'netDiskUser'
        verbose_name = u'网盘用户'
        verbose_name_plural = u"网盘用户"
        unique_together = ("cluster","systemUsername")