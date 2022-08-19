from django.db import models
from authentication.models import CustomUser

# Create your models here.

your_choices_1 = (('1', u'Andhra Pradesh'),
('2',u'Arunachal Pradesh'),
('3',u'Assam'),
('4',u'Bihar'),
('5',u'Chattisgarh'),
('6',u'Goa'),
('7',u'Gujrat'),
('8',u'Haryana'),
('9',u'Himachal pradesh'),
('10',u'Jammu & Kashmir'),
('11',u'Jharkhand'),
('12',u'Karnataka'),
('13',u'Kerala'),
('14',u'Madhya Pradesh'),
('15',u'Maharastra'),
('16',u'Manipur'),
('17',u'Meghalaya'),
('18',u'Mizoram'),
('19',u'Nagaland'),
('20',u'Odisha'),
('21',u'Punjab'),
('22',u'Rajasthan'),
('23',u'Sikkim'),
('24',u'Tamil Nadu'),
('25',u'Telangana'),
('26',u'Tripura'),
('27',u'Uttar pradesh'),
('28',u'Uttarakhand'),
('29',u'West Bengal'),
('30',u'Delhi'),
)

your_choices_2 = (
('1',u'GSTServiceCenter'),
('2',U'Fintax epay'),
('3',u'Both'),
)

your_choices_4 = (
('1',u'CallBack'),
('2',u'No Answer'),
('3',u'Hang Up'),
('4',u'Wrong Number'),
('5',u'Language Barrier'),
('6',u'Not Available'),
('7',u'Busy'),
('8',u'Detail Share'),
('9',u'Not Interested'),
('10',u'Sale'),
('11',u'No Money'),
('12',u'Follow Up'),
('13',u'Document Required'),
)
class Sale(models.Model):
    
    created_by = models.ForeignKey(CustomUser,on_delete=models.CASCADE, blank=False)
    date= models.DateTimeField(auto_now_add=True)
    account_id = models.AutoField(primary_key=True )
    cx_name=models.CharField(max_length=50,editable=False)
    email=models.EmailField(unique=True,max_length=50,editable=False)
    phone=models.CharField(max_length=15,editable=False)
    alternate_phone=models.CharField(max_length=15,null=True)
    pincode=models.IntegerField(null=False,editable=False)
    state=models.CharField(max_length=40, choices=your_choices_1,blank=True,null=False,editable=False)
    plan_offered=models.CharField(max_length=32, choices=your_choices_2,blank=True,null=False,editable=False)
    price=models.CharField(max_length=8,blank=True,null=False,editable=False)
    disposition=models.CharField(max_length=200, choices=your_choices_4,null=False)
    remarks=models.TextField(max_length=20, null=True, blank=True)

  

    class Meta:
        verbose_name_plural = "Sale"
        db_table = 'newcustomer_newcustomer'
        managed = False


