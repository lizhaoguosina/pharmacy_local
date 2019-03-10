from django.db import models

# Create your models here.
class location(models.Model):
    '''定位'''
    te_id = models.CharField("固定资产编码",max_length=256) # 固定资产主键，数据库唯一
    te_class = models.CharField("资产类别",max_length=32) # 资产类别
    te_local = models.CharField("校区位置",max_length=16) # 校区位置
    te_build = models.CharField("实验楼",max_length=16) # 实验楼
    te_floor = models.CharField("楼层",max_length=4) # 楼层
    te_room = models.CharField("房间",max_length=5) # 房间
    te_Xdata = models.DecimalField("X轴数据",max_digits=6, decimal_places=3)# X轴数据，六位有效数字三位小数
    te_Ydata = models.DecimalField("Y轴数据",max_digits=6, decimal_places=3)# Y轴数据，同上
    te_Zdata = models.DecimalField("Z轴数据",max_digits=6, decimal_places=3)# Z洲数据，同上
    te_ladata = models.DateField("上次清查日期") # 上次清查日期
    te_nedata = models.DateField("下次清查日期") # 下次清查日期
    te_buydate = models.DateField("购买日期") # 购买日期
    te_make = models.CharField("设备生产商",max_length=256) # 设备生产商
    te_persion = models.CharField("设备负责人",max_length=32) # 设备负责人
    te_status = models.BooleanField("设备能否正常使用(留空为否)") # 设备使用状况
    te_back = models.TextField("备注") # 备注

    def __str__(self):
        return self.te_id