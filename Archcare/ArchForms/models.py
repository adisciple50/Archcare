from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class StaffMember(models.Model):
    title = models.CharField("Title",choices=(("MR","Mr"),("MISS","Miss"),("MRS","Mrs"),("MS","Ms"),("DR","Dr"),("PROF","Prof."),("REVD","Revd"),),max_length=5)
    first_name = models.CharField("First Name",max_length=255)
    second_name = models.CharField("Surname",max_length=255)
    full_name = models.CharField("Full Name",max_length=518)
    contact_phone = PhoneNumberField()
    def __str__(self):
        return self.full_name

class ServiceUser(models.Model):
    title = models.CharField("Title",choices=(("MR","Mr"),("MISS","Miss"),("MRS","Mrs"),("MS","Ms"),("DR","Dr"),("PROF","Prof."),("REVD","Revd"),),max_length=5)
    first_name = models.CharField("First Name",max_length=255)
    second_name = models.CharField("Surname",max_length=255)
    full_name = models.CharField("Full Name",max_length=518)
    contact_phone = PhoneNumberField()
    def __str__(self):
        return self.full_name

class ProgressReport(models.Model):
    date = models.DateField("Date")
    content_of_one_to_one_support = models.TextField("Content of 1-1 Support")
    evaluation_and_comments = models.TextField("Evaluation & Comments")
    date_and_time_signed = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.content_of_one_to_one_support

class WeeklyReport(models.Model):
    def find_date_number(self):  # self only necessary to satisfy debugger.not actually referenced.
        import datetime
        date = datetime.date.today()
        week = date.isocalendar()[1]
        return week
    service_user = models.ForeignKey(ServiceUser)
    date = models.DateField("Date")
    morning = models.TextField("morning")
    evening = models.TextField("evening")
    week_number = models.IntegerField(default=find_date_number(None))
    daily_total_one_to_one_support_hours_provided = models.DecimalField(decimal_places=2,max_digits=5)
    def __str__(self):
        return '%s %s' % (self.service_user,self.date)



class House(models.Model):
    address = models.TextField()