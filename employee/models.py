from django.db import models
from django.db.models.deletion import CASCADE
import datetime
import uuid
import math

# Create your models here.
class PersonalData(models.Model):
    CHOICES_CIVIL_STATUS = [
        ('Single', 'Single'),
        ('Married', 'Married'), 
        ('Divorced', 'Divorced'),
        ('Widowed', 'Widowed'),
    ]
    CHOICES_GENDER = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]
    first_name = models.CharField(max_length=250)
    middle_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    affix = models.CharField(max_length=5, blank=True, null=True)
    birth_date = models.DateField()
    gender = models.CharField(max_length=7, choices=CHOICES_GENDER,)
    civil_status = models.CharField(max_length=8, choices=CHOICES_CIVIL_STATUS,)
    religion = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    phone_number = models.CharField(max_length=25)

    def __str__(self) -> str:
        return self.revrse_full_name()

    def full_name(self) -> str:
        return '{} {}'.format(self.first_name, self.last_name)
    full_name.short_description = 'Name'

    def revrse_full_name(self) -> str:
        return '{}, {}'.format(self.last_name, self.first_name)
    revrse_full_name.short_description = 'Name'

    def age(self):
        age = datetime.date.today() - self.birth_date
        return math.floor(age.days/365)

    class Meta:
        verbose_name_plural = 'Employees'


class Family(models.Model):
    CHOICES_RELATIONSHIP = [
        ('Mother', 'Mother'),
        ('Father', 'Father'),
        ('Sibling', 'Sibling'),
        ('Wife', 'Wife'),
        ('Child', 'Child'),
    ]
    first_name = models.CharField(max_length=250)
    middle_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    affix = models.CharField(max_length=5, blank=True, null=True)
    birth_date = models.DateField()
    relationship = models.CharField(max_length=7, choices=CHOICES_RELATIONSHIP,)
    address = models.CharField(max_length=250, blank=True, null=True)
    phone_number = models.CharField(max_length=25)
    employee = models.ForeignKey(PersonalData, on_delete=CASCADE)

    def __str__(self) -> str:
        return self.revrse_full_name()

    def full_name(self) -> str:
        return '{} {}'.format(self.first_name, self.last_name)
    full_name.short_description = 'Name'

    def revrse_full_name(self) -> str:
        return '{}, {}'.format(self.last_name, self.first_name)
    revrse_full_name.short_description = 'Name'

    def age(self):
        delta = datetime.date.today() - self.birth_date
        return math.floor(delta.days/365)

    class Meta:
        verbose_name_plural = 'Family Members'

class ContactInformation(models.Model):
    CHOICES_TYPE = [
        ('TR', 'Temporary Residence'),
        ('PR', 'Permanent Residence'),
        ('PA', 'Provincial Address'),
        ('OL', 'Office Location'),
        ('EC', 'Emergency Contact'),
    ]
    type= models.CharField(max_length=250, choices=CHOICES_TYPE)
    address = models.CharField(max_length=250)
    contact_person = models.CharField(max_length=25, blank=True, null=True)
    phone_number = models.CharField(max_length=25, blank=True, null=True)
    employee = models.ForeignKey(PersonalData, on_delete=CASCADE)

    class Meta:
        verbose_name_plural = 'Contact Information'
    

class GovernmentRelated(models.Model):
    tin = models.CharField(max_length=250)
    tax_exemption_status = models.CharField(max_length=250)
    hmdf = models.CharField(max_length=250, blank=True, null=True)
    philhealth = models.CharField(max_length=250, blank=True, null=True)
    sss = models.CharField(max_length=250, blank=True, null=True)
    gsis = models.CharField(max_length=250, blank=True, null=True)
    employee = models.ForeignKey(PersonalData, on_delete=CASCADE)

    class Meta:
        verbose_name_plural = 'Government Related'

class Education(models.Model):
    school = models.CharField(max_length=250)
    start = models.DateField()
    end = models.DateField()
    major = models.CharField(max_length=250, blank=True, null=True)
    minor = models.CharField(max_length=250, blank=True, null=True)
    degree = models.CharField(max_length=250, blank=True, null=True)
    award = models.CharField(max_length=250, blank=True, null=True)
    employee = models.ForeignKey(PersonalData, on_delete=CASCADE)

    class Meta:
        verbose_name_plural = 'Education'

class DisciplinaryAction(models.Model):
    offense = models.CharField(max_length=250)
    penalty = models.CharField(max_length=250, blank=True, null=True)
    start = models.DateField(null=True, blank=True)
    end = models.DateField(null=True, blank=True)
    employee = models.ForeignKey(PersonalData, on_delete=CASCADE)

    class Meta:
        verbose_name_plural = 'Disciplinary Action'

class WorkProfile(models.Model):
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    hiring_date = models.DateField()
    current_position = models.CharField(max_length=250)
    division = models.CharField(max_length=250, blank=True, null=True)
    group = models.CharField(max_length=250, blank=True, null=True)
    department = models.CharField(max_length=250, blank=True, null=True)
    team = models.CharField(max_length=250, blank=True, null=True)
    subteam = models.CharField(max_length=250, blank=True, null=True)
    unit = models.CharField(max_length=250, blank=True, null=True)
    subunit = models.CharField(max_length=250, blank=True, null=True)
    section = models.CharField(max_length=250, blank=True, null=True)
    employee = models.ForeignKey(PersonalData, on_delete=CASCADE)

    def tenure(self) -> float:
        delta = datetime.date.today() - self.hiring_date
        return delta.days / 365
    
    def str_tenure(self) -> str:
        delta = datetime.date.today() - self.hiring_date
        years = math.floor(delta.days / 365)
        strYear = 'Years' if years > 1 else 'Year'
        month = round((delta.days % 365) / 30)
        strMonth = 'Months' if month > 1 else 'Month'
        return '{} {} & {} {}'.format(years, strYear, month, strMonth)
    str_tenure.short_description = 'Tenure'

    class Meta:
        verbose_name_plural = 'Work Profile'

class EmployeeMovement(models.Model):
    company = models.CharField(max_length=250)
    old_position = models.CharField(max_length=250)
    new_position = models.CharField(max_length=250)
    old_division = models.CharField(max_length=250, blank=True, null=True)
    new_division = models.CharField(max_length=250, blank=True, null=True)
    old_group = models.CharField(max_length=250, blank=True, null=True)
    new_group = models.CharField(max_length=250, blank=True, null=True)
    old_department = models.CharField(max_length=250, blank=True, null=True)
    new_department = models.CharField(max_length=250, blank=True, null=True)
    old_team = models.CharField(max_length=250, blank=True, null=True)
    new_team = models.CharField(max_length=250, blank=True, null=True)
    old_subteam = models.CharField(max_length=250, blank=True, null=True)
    new_subteam = models.CharField(max_length=250, blank=True, null=True)
    old_unit = models.CharField(max_length=250, blank=True, null=True)
    new_unit = models.CharField(max_length=250, blank=True, null=True)
    old_subunit = models.CharField(max_length=250, blank=True, null=True)
    new_subunit = models.CharField(max_length=250, blank=True, null=True)
    old_section = models.CharField(max_length=250, blank=True, null=True)
    new_section = models.CharField(max_length=250, blank=True, null=True)
    update_date = models.DateField(auto_now=True)
    employee = models.ForeignKey(PersonalData, on_delete=CASCADE)

class Employment(models.Model):
    company = models.CharField(max_length=250)
    position = models.CharField(max_length=250)
    start = models.DateField()
    end = models.DateField()

    def tenure(self) -> float:
        delta = self.end - self.start
        return delta.days / 365
    
    def str_tenure(self) -> str:
        delta = self.end - self.start
        years = math.floor(delta.days / 365)
        strYear = 'Years' if years > 1 else 'Year'
        month = round((delta.days % 365) / 30)
        strMonth = 'Months' if month > 1 else 'Month'
        return '{} {} & {} {}'.format(years, strYear, month, strMonth)
    str_tenure.short_description = 'Tenure'
    

class Organization(models.Model):
    employee = models.ForeignKey(PersonalData, on_delete=CASCADE)
    reports_to_id = models.PositiveIntegerField(blank=True, null=True)

    def get_direct_report(self):
        return self.objects.filter(reports_to=self.employee__id)

    def get_org_tree(self):
        #logic to be continued
        pass


