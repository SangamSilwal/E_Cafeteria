from django.db import models

class UUIDStudent(models.Model):
    UUID = models.CharField(unique=True,max_length=100,null=False)

class CanteenManager(models.Model):
    menu = models.CharField(max_length=200)
    perPrice = models.IntegerField()

class StudentData(models.Model):
    BEI = 'BEI'
    BCT = 'BCT'
    BEL = 'BEL'
    BME = 'BME'
    BARCH = 'BARCH'
    BCE = 'BCE'

    DEPARTMENT_CHOICES = [
        (BEI,'BEI'),
        (BCT,'BCT'),
        (BEL,'BEL'),
        (BME,'BME'),
        (BARCH,'BARCH'),
        (BCE,'BCE'),
    ]

    name = models.CharField(max_length=200)
    roll = models.CharField(max_length=200)
    phone = models.BigIntegerField()
    department = models.CharField(max_length=10,choices=DEPARTMENT_CHOICES,default=BEI)                        
    uuid = models.OneToOneField(UUIDStudent,on_delete=models.CASCADE,unique=True,null=False,related_name="uuidOFstudent")
    email = models.EmailField(default=None)
    points = models.IntegerField(default=0)
    profile_picture = models.ImageField(upload_to='profile_pics',null=True,blank=True)

    def __str__(self):
        return self.name

class TranscationHistory(models.Model):
    student = models.ForeignKey(StudentData,on_delete=models.CASCADE,null=True,blank=True,related_name="transaction_Ofstudent")
    foodOrderes = models.ForeignKey(CanteenManager,on_delete=models.CASCADE,null=True,blank=True)
    transcatedPoints = models.IntegerField()
    time = models.DateTimeField(auto_now_add=True)


class AnalysisTransaction(models.Model):
    amount = models.IntegerField()
    transaction_count = models.IntegerField()

