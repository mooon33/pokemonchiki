
# imports
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# User Model
# This class defines a model for user registration with various fields such as phone number, account
# number, email, gender, account type, balance, address, image, PAN, Aadhaar, and date of birth.
from django.db import models
from django.contrib.auth.models import User

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class User_reg(models.Model):
    ACCOUNT_TYPES = [
        ('savings', 'Savings'),
        ('checking', 'Checking'),
        ('business', 'Business'),
    ]

    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    account_number = models.CharField(max_length=20, unique=True)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    account_type = models.CharField(max_length=10, choices=ACCOUNT_TYPES)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    address = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='user_photos/', null=True, blank=True)
    pan = models.CharField(
        max_length=20,
        default='NOT_PROVIDED',  # Временное значение для существующих записей
        verbose_name='PAN Number'
    )
    aadhaar = models.CharField(max_length=20)
    ob = models.DateField(
        verbose_name='Date of Birth',
        default=timezone.now,  # Используем текущую дату как временное значение
        blank=True  # Если поле необязательное
    )
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username} - {self.account_number}"
class Transactions(models.Model):
    TRANSACTION_TYPES = [
        ('DEPOSIT', 'Deposit'),
        ('WITHDRAW', 'Withdraw'),
        ('TRANSFER', 'Transfer'),
        ('LOAN', 'Loan'),
        ('BILL', 'Bill Payment'),
    ]

    user = models.ForeignKey(User_reg,on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=20,choices=TRANSACTION_TYPES)
    timestamp = models.DateTimeField(default=timezone.now())
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    about = models.CharField(max_length=100)
    receiptent = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    receiptent_no = models.CharField(max_length=30, default="",null=True)

    def __str__(self):
        return self.user.user.username

    
class Loan(models.Model):
    LOAN_TYPES = [
        ('HOME_LOAN', 'Home Loan'),
        ('PERSONAL_LOAN', 'Personal Loan'),
        ('EDUCATION_LOAN', 'Education Loan'),
        ('CAR_LOAN', 'Car Loan'),
        ('GOLD_LOAN', 'Gold loan'),
        ('OTHERS', 'Others')
    ]
    loan_status = [
        ('PENDING', 'Pending'),
        ('APPROVED', 'Approved'),
        ('REJECTED', 'Rejected')
    ]
    user = models.ForeignKey(User_reg,on_delete=models.CASCADE)
    loan_type = models.CharField(max_length=50,choices=LOAN_TYPES)
    loan_tenure = models.IntegerField(default=1)
    loan_amount = models.DecimalField(max_digits=10, decimal_places=2)
    loan_status = models.CharField(max_length=20,choices=loan_status,default='PENDING')
    employment_type = models.CharField(max_length=90,default="")
    timestamp = models.DateTimeField(default=timezone.now())
    def __str__(self):
        return self.user.account_number + '-' + self.loan_type
    
    def Loan_count(self):
        laon = int(Loan.objects.filter(loan_status="PENDING").count())
        return laon

class BillPayment(models.Model):
    BILL_TYPES = (
        ('Electricity', 'Electricity'),
        ('Water', 'Water'),
        ('Internet', 'Internet'),
        ('Rent', 'Rent'),
        ('Other', 'Other'),
    )

    BILL_STATUS = (
        ('PENDING', 'Pending'),
        ('PAID', 'Paid'),
    )
    
    user = models.ForeignKey(User_reg, on_delete=models.CASCADE)
    bill_type = models.CharField(max_length=20, choices=BILL_TYPES)
    bill_status = models.CharField(max_length=20, choices=BILL_STATUS, default='PENDING')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.user.username + '-' + self.bill_type

# Support Model    
# This Python class defines a model called Supports with fields for name, email, and issue.
class Supports(models.Model):

    name = models.CharField(max_length=20,default="")
    email = models.EmailField(max_length=40)
    issue = models.CharField(max_length=300,default="")

    def __str__(self):
        return self.name