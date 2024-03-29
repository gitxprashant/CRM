# Generated by Django 4.0.5 on 2022-08-24 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DetailShared',
            fields=[
                ('date', models.DateTimeField(auto_now_add=True)),
                ('account_id', models.AutoField(primary_key=True, serialize=False)),
                ('cx_name', models.CharField(editable=False, max_length=50)),
                ('email', models.EmailField(editable=False, max_length=50, unique=True)),
                ('phone', models.CharField(editable=False, max_length=15)),
                ('alternate_phone', models.CharField(max_length=15, null=True)),
                ('pincode', models.IntegerField(editable=False)),
                ('state', models.CharField(blank=True, choices=[('1', 'Andhra Pradesh'), ('2', 'Arunachal Pradesh'), ('3', 'Assam'), ('4', 'Bihar'), ('5', 'Chattisgarh'), ('6', 'Goa'), ('7', 'Gujrat'), ('8', 'Haryana'), ('9', 'Himachal pradesh'), ('10', 'Jammu & Kashmir'), ('11', 'Jharkhand'), ('12', 'Karnataka'), ('13', 'Kerala'), ('14', 'Madhya Pradesh'), ('15', 'Maharastra'), ('16', 'Manipur'), ('17', 'Meghalaya'), ('18', 'Mizoram'), ('19', 'Nagaland'), ('20', 'Odisha'), ('21', 'Punjab'), ('22', 'Rajasthan'), ('23', 'Sikkim'), ('24', 'Tamil Nadu'), ('25', 'Telangana'), ('26', 'Tripura'), ('27', 'Uttar pradesh'), ('28', 'Uttarakhand'), ('29', 'West Bengal'), ('30', 'Delhi')], editable=False, max_length=40)),
                ('plan_offered', models.CharField(blank=True, choices=[('1', 'GSTServiceCenter'), ('2', 'Fintax epay'), ('3', 'Both')], editable=False, max_length=32)),
                ('price', models.CharField(blank=True, editable=False, max_length=8)),
                ('disposition', models.CharField(choices=[('1', 'CallBack'), ('2', 'No Answer'), ('3', 'Hang Up'), ('4', 'Wrong Number'), ('5', 'Language Barrier'), ('6', 'Not Available'), ('7', 'Busy'), ('8', 'Detail Share'), ('9', 'Not Interested'), ('10', 'Sale'), ('11', 'No Money'), ('12', 'Follow Up'), ('13', 'Document Required')], max_length=200)),
                ('remarks', models.TextField(blank=True, max_length=20, null=True)),
            ],
            options={
                'verbose_name_plural': 'Detail Shared',
                'db_table': 'newcustomer_newcustomer',
                'managed': False,
            },
        ),
    ]
