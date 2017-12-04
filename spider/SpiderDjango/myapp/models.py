from django.db import models

# Create your models here.
class Job(models.Model):
    # email = models.CharField(max_length=50)
    # state = models.IntegerField(default=1)
    # addtime = models.IntegerField()
    url = models.CharField(max_length=255)
    job_name = models.CharField(max_length=32)
    smoney = models.CharField(max_length=10)
    emoney = models.CharField(max_length=10)
    location = models.CharField(max_length=32)
    syear = models.IntegerField()
    eyear = models.IntegerField()
    degree = models.CharField(max_length=20)
    tags = models.CharField(max_length=255)
    date_pub = models.CharField(max_length=20)
    welfare = models.CharField(max_length=255)
    jobdesc = models.TextField()
    jobaddr = models.CharField(max_length=255)
    company_desc = models.TextField()
    company = models.CharField(max_length=30)
    source = models.CharField(max_length=255)
    crawl_time = models.DateTimeField()
    class Meta:
        db_table = "job"  # 更改表名
