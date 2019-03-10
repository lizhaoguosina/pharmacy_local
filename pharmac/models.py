from django.db import models

# Create your models here.
class pharmacy(models.Model):
    '''药品管理'''
    ph_id = models.CharField("药品编码",max_length=1024) # 药品部分主键
    ph_name = models.CharField("药品名称",max_length=512) # 药品名称
    ph_class = models.CharField("药品类别",max_length=256) # 药品类别
    ph_status = models.CharField("药品状况",max_length=128) # 药品状况
    ph_indata = models.DateField("入库时间") # 药品入库时间
    ph_outdata = models.DateField("过期时间") # 药品过期时间
    ph_enddata = models.DateField("使用结束时间") # 药品使用结束时间

    def __str__(self):
        return self.ph_id
