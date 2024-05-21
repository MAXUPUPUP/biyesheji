from django.db import models


class User(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    # 添加其他学生特有的字段...
    # email = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    # name = models.CharField(max_length=100)
    TYPE_CHOICES = [
        (0, '可用'),
        (1, '禁用'),
    ]

    status = models.IntegerField(choices=TYPE_CHOICES, default=0)
    class Meta:
        verbose_name = '用户'  # 单数形式的显示名称
        verbose_name_plural = '用户'  # 复数形式的显示名称，如果你希望复数和单数形式一样，就设置为相同的值。

    def __str__(self):
        return self.username  # 这将定义在后台管理界面中显示的对象名称
