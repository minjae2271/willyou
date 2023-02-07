from django.db import models

class Couple(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.IntegerField(default=1)
    groom = models.CharField(max_length=10) #최적이름 길이 뭘까...
    bride = models.CharField(max_length=10)
    date = models.DateTimeField(null=False) #날짜 + 시간? 시간 분리?
    
    bride_phone = models.CharField(max_length=11)
    groom_phone = models.CharField(max_length=11)

    groom_mother_name = models.CharField(max_length=10)
    groom_father_name = models.CharField(max_length=10)
    bride_father_name = models.CharField(max_length=10)
    bride_mother_name = models.CharField(max_length=10)

    groom_father_phone = models.CharField(max_length=11)
    groom_mother_phone = models.CharField(max_length=11)
    bride_father_phone = models.CharField(max_length=11)
    bride_mother_phone = models.CharField(max_length=11)

    groom_bank = models.CharField(max_length=10)
    groom_account = models.CharField(max_length=14)
    bride_bank = models.CharField(max_length=10)
    bride_account = models.CharField(max_length=14)

    #place_lat
    #place_lng


def image_upload_path(instance, filename):
    return f'willyou/{instance.couple.id}_{filename}'

class WeddingImage(models.Model):
    id = models.AutoField(primary_key=True)
    couple = models.ForeignKey(Couple, on_delete=models.CASCADE, related_name='image')
    image = models.ImageField(upload_to=image_upload_path)
