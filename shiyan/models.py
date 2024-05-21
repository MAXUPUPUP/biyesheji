from django.db import models


class Shiyan(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    # 添加其他学生特有的字段...
    # email = models.CharField(max_length=100)
    lid = models.CharField(max_length=100)
    uid = models.CharField(max_length=10)
    pingyu=models.CharField(max_length=100)
    score =models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    file = models.FileField(upload_to='shiyan')
    chong=models.CharField(max_length=100)
    text=models.TextField(max_length=10000)
    datetime=models.DateTimeField(auto_now_add=True)
    # TYPE_CHOICES = [
    #     (0, '可用'),
    #     (1, '禁用'),
    # ]


    class Meta:
        verbose_name = '实验'  # 单数形式的显示名称
        verbose_name_plural = '实验'  # 复数形式的显示名称，如果你希望复数和单数形式一样，就设置为相同的值。

    def __str__(self):
        return self.uid  # 这将定义在后台管理界面中显示的对象名称
