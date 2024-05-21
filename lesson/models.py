from django.db import models


class Lesson(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    # 添加其他学生特有的字段...
    # email = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    jianjie = models.CharField(max_length=100)
    # # TYPE_CHOICES = [
    # #     (0, '可用'),
    # #     (1, '禁用'),
    # # ]
    #
    # status = models.IntegerField(choices=TYPE_CHOICES, default=0)
    class Meta:
        verbose_name = '实验课程'  # 单数形式的显示名称
        verbose_name_plural = '实验课程'  # 复数形式的显示名称，如果你希望复数和单数形式一样，就设置为相同的值。

    def __str__(self):
        return self.lname  # 这将定义在后台管理界面中显示的对象名称
