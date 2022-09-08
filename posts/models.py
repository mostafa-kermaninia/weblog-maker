from django.db import models

# مدل ها يسري كلاس هستن


class Post(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField(blank=True)
    is_enable = models.BooleanField(default=False)
    publish_date = models.DateField(null=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    # اين تابع براي اينه كه وقتي ميخواي كامنت بنويسي و ميخواي   پتي كه قراره بر اش كامنت بذاري رو انتخاب كني
    # بياد و اين چيزيكه ريترن كردي رو نشون بده بعنوان اسم پست ها
    def __str__(self):
        # است اما بهتره اينو بنويسيidهمون pk منظور از
        return (f'{self.pk}.{self.title}')


class Comment(models.Model):
    # title = models.CharField(max_length=50,default='pp')

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()
    # text2 = models.TextField()
    # is_enable = models.BooleanField(default=False)

    # text2 = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
