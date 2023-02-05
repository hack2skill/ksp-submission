from django.db import models
import numpy as np

class Person(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('others','Others')
    ]

    districts = [
        ( 'Bagalkot' , 'Bagalkot' ),
        ( 'Ballari' , 'Ballari' ),
        ( 'Belagavi' , 'Belagavi' ),
        ( 'Bengaluru Rural' , 'Bengaluru Rural' ),
        ( 'Bengaluru Urban' , 'Bengaluru Urban' ),
        ( 'Bidar' , 'Bidar' ),
        ( 'Chamarajanagar' , 'Chamarajanagar' ),
        ( 'Chikkaballapura' , 'Chikkaballapura' ),
        ( 'Chikkamagaluru' , 'Chikkamagaluru' ),
        ( 'Chitradurga' , 'Chitradurga' ),
        ( 'Dakshina Kannada' , 'Dakshina Kannada' ),
        ( 'Davangere' , 'Davangere' ),
        ( 'Dharwad' , 'Dharwad' ),
        ( 'Gadag' , 'Gadag' ),
        ( 'Gulbarga' , 'Gulbarga' ),
        ( 'Hassan' , 'Hassan' ),
        ( 'Haveri' , 'Haveri' ),
        ( 'Kalaburagi' , 'Kalaburagi' ),
        ( 'Kodagu' , 'Kodagu' ),
        ( 'Kolar' , 'Kolar' ),
        ( 'Koppal' , 'Koppal' ),
        ( 'Mandya' , 'Mandya' ),
        ( 'Mysuru' , 'Mysuru' ),
        ( 'Raichur' , 'Raichur' ),
        ( 'Ramanagara' , 'Ramanagara' ),
        ( 'Shivamogga' , 'Shivamogga' ),
        ( 'Tumakuru' , 'Tumakuru' ),
        ( 'Udupi' , 'Udupi' ),
        ( 'Uttara Kannada' , 'Uttara Kannada' ),
        ( 'Vijayapura' , 'Vijayapura' ),
        ( 'Yadgir' , 'Yadgir' ),
    ]


    id = models.AutoField(primary_key=True)
    District_Name = models.CharField(max_length=50,choices=districts)
    UnitName=models.CharField(max_length=100)
    FIRNo=models.CharField(max_length=15)
    FIR_Date=models.DateTimeField(auto_now_add=True)
    FIR_Stage=models.BooleanField(default=False)
    Photo_Full_front=models.CharField(max_length=500)
    Gender=models.CharField(max_length=10, choices=GENDER_CHOICES)
    Person_Name=models.CharField(max_length=200)
    age=models.PositiveSmallIntegerField()
    image=models.ImageField(upload_to='images')
    encodings = models.TextField(blank=True, null=True)
    #
    # = models.ImageField(upload_to='images')
    # # image_url = models.URLField()
    # # encodings=models.TextField(blank=True,null=True)
    # encodings = models.TextField(blank=True,null=True)
    # # gender = models.CharField(max_length=10)
    # gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    # age = models.PositiveSmallIntegerField()
    #
    # guardian_name=models.CharField(max_length=255)
    # guardian_phone_no=models.CharField(max_length=15)
    #
    # station_id=models.CharField(max_length=30)
    # station_district=models.CharField(max_length=50,choices=districts)
    #
    # last_seen_address=models.TextField()
    #
    # resolved=models.BooleanField(default=False)
    #
    # missing_reported_date = models.DateTimeField(auto_now_add=True)
    # resolved_date = models.DateTimeField(auto_now=True)
    #



    # def save_encodings(self, face_encodings):
    #     f_encodings = ", ".join(map(str, face_encodings))
    #     print(f_encodings)
    #     print(type(f_encodings))
    #     self.face_encodings = f_encodings
    #     print(type(self.face_encodings))
    #     print(self.face_encodings)
    #     self.save()


    def __str__(self):
        return self.Person_Name


