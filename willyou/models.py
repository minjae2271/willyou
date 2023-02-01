from django.db import models

class Couple(models.Model):
    groom = models.CharField(max_length=10, null=False) #최적이름 길이 뭘까...
    bride = models.CharField(max_length=10, null=False)
    date = models.DateTimeField(null=False) #날짜 + 시간? 시간 분리?
    
    groom_phone = models.CharField(max_length=11, null=False)
    bride_phone = models.CharField(max_length=11, null=False)

    groom_father_name = models.CharField(max_length=10, null=False)
    groom_mother_name = models.CharField(max_length=10, null=False)
    bride_father_name = models.CharField(max_length=10, null=False)
    bride_mother_name = models.CharField(max_length=10, null=False)

    groom_father_phone = models.CharField(max_length=11, null=False)
    groom_mother_phone = models.CharField(max_length=11, null=False)
    bride_father_phone = models.CharField(max_length=11, null=False)
    bride_mother_phone = models.CharField(max_length=11, null=False)

    groom_bank = models.CharField(max_length=10)
    groom_account = models.CharField(max_length=14)
    bride_bank = models.CharField(max_length=10)
    bride_account = models.CharField(max_length=14)

    #place_lat
    #place_lng