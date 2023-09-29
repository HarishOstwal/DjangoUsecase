from django.db import models

class Area(models.Model):
    region = models.CharField(max_length=255)
    subregion = models.CharField(max_length=255)    

    def __str__(self):
        return self.region+" "+self.subregion

class Encroachment(models.Model):
    encroachment_id = models.CharField(max_length=255)
    encroachment_type = models.CharField(max_length=255)
    encroachment_size_sq_ft = models.DecimalField(max_digits=10, decimal_places=2)
    criticality = models.CharField(max_length=255)
    encroachment_department = models.CharField(max_length=200)
    encroachment_status=models.CharField(max_length=200)
    distance_from_center_ft = models.IntegerField()
    area=models.ForeignKey(Area,on_delete=models.CASCADE,default=100)

    def __str__(self):
        return self.encroachment_id
