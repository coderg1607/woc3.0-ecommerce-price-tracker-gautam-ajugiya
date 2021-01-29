from django.db import models

# Create your models here.
class data(models.Model):
    cust_email=models.EmailField(max_length=100)
    cust_pro_link=models.URLField(blank=True)
    cust_pro_price=models.CharField(max_length=100)
    company=models.CharField(max_length=10,null=True)
    def __str__(self):
        return self.company+"-----"+self.cust_email+'-----'+self.cust_pro_link+'-----'+self.cust_pro_price
    