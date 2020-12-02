from django.db import models
#from django.contrib.auth.models import  User
# Create your models here.

class AsSet(models.Model):
    #共用部分
        
    asset_status = (
        (0,'正常未使用'),
        (1,'故障'),
        (2,'备用'),
        (3,'未知'),
        (4,'使用中'),
    )# 状态

    sn = models.CharField(
        max_length = 128,
        unique = True,
        verbose_name = '编号'
    )#唯一

    called = models.CharField(
        max_length= 64,
        verbose_name = '名称',
        null = True,
        blank = True,
    ) 

    status = models.SmallIntegerField(
        choices = asset_status,
        default = 0,
        verbose_name = '状态'
    )#选项

    indate = models.DateField(
        null = True,
        blank = True,
        verbose_name = '入库日期'
    )

    expiredate = models.DateField(
        null = True,
        blank = True,
        verbose_name = '过期时间'
    )
    
    manufacturer = models.ForeignKey(
        'Manufacturer',
        null = True,
        blank = True,
        verbose_name = '制造商',
        on_delete = models.SET_NULL
    )

    manager = models.ForeignKey(
        'User',
        null = True,
        blank = True,
        verbose_name = '管理者',
        related_name = 'aadmin',
        on_delete = models.SET_NULL
    )

    manageIP = models.GenericIPAddressField(
        null = True,
        blank = True,
        verbose_name = '管理IP'
    )

    house = models.ForeignKey(
        'House',
        null = True,
        blank = True,
        verbose_name = '实验楼',
        on_delete = models.SET_NULL
    )

    room = models.ForeignKey(
        'Room',
        null = True,
        blank = True,
        verbose_name = '房间号',
        on_delete = models.SET_NULL
    )

    x_locations = models.CharField(
        max_length=254,
        null=True,
        blank=True,
        verbose_name='定位信息X'
    )

    y_locations = models.CharField(
        max_length=254,
        null=True,
        blank=True,
        verbose_name='定位信息Y'
    )

    z_locations = models.CharField(
        max_length=254,
        null=True,
        blank=True,
        verbose_name='定位信息Z'
    )

    memo = models.TextField(
        null = True,
        blank = True,
        verbose_name = '备注'
    )

    def __str__(self):
        return self.sn
    
    class Meta:
        verbose_name = '资产总表'
        verbose_name_plural = '总表'
        ordering = ['-sn']

class Manufacturer(models.Model):
      
    name = models.CharField(
        verbose_name = '厂商名称',
        max_length = 254,
        unique = True
    )
        
    phone =  models.CharField(
        verbose_name = '电话',
        max_length = 30,
        null = True,
        blank = True
    )

    def __str__(self):
        return self.name
       
    class Meta:
        verbose_name = '厂商'
        verbose_name_plural = '厂商'

class Room(models.Model):

    RoomNum = models.IntegerField(
        null = True,
        blank = True
    )

    def __str__(self):
        temp = str(self.RoomNum)
        return temp
        
    class Meta:
        verbose_name = '房间号'
        verbose_name_plural = '房间号'

class House(models.Model):
    detials = ""

    stand = (
        (0,'奉贤校区'),
        (1,'徐汇校区'),
        (2,'金山校区'),
    )

    WhereStand = models.SmallIntegerField(
        choices = stand,
        default = 0,
        verbose_name = '校区'
    )#选项

    HouseNumber = models.IntegerField(
        default = 1,
        verbose_name = '实验楼号'
    )
     
    def __str__(self):
        temps = self.stand[int(self.WhereStand)]
        temp = temps[-1]
        self.detials = str(temp)+str(self.HouseNumber)+"号楼"
        return self.detials
        
    class Meta:
        verbose_name = '校区+实验楼'
        verbose_name_plural = '校区'

class User(models.Model):
    name = models.CharField(max_length=64, unique=True)
    password = models.CharField(max_length=254)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = '用户基本信息'
        verbose_name_plural = '用户基本信息'
