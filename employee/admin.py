from django.contrib import admin
from employee.models import PersonalData as Employee, Family, DisciplinaryAction, WorkProfile
# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    @admin.display(description='Age')
    def age(self, obj):
        return obj.age()
    list_display = ('reverse_full_name', 'middle_name', 'birth_date', 'age', 'gender')
    search_fields = ['last_name', 'first_name', 'middle_name', 'gender']
admin.site.register(Employee, EmployeeAdmin)

#------------------

class FamilyAdmin(admin.ModelAdmin):
    @admin.display(description='Employee Name')
    def employee_name(self, obj):
        return obj.employee.reverse_full_name()
    
    @admin.display(description='Age')
    def age(self, obj):
        return obj.age()
    list_display = ('reverse_full_name', 'age', 'relationship', 'employee_name')
    search_fields = ['last_name', 'first_name', 'middle_name', 'employee__last_name']
admin.site.register(Family, FamilyAdmin)

#------------------

# class ContactInformationAdmin(admin.ModelAdmin):
#     @admin.display(description='Employee Name')
#     def employee_name(self, obj):
#         return obj.employee.reverse_full_name()
#     list_display = ('employee_name', 'type', 'address', 'contact_person', 'phone_number')
#     search_fields = ['employee__last_name', 'type']
# admin.site.register(ContactInformation, ContactInformationAdmin)

#------------------

class DisciplinaryActionAdmin(admin.ModelAdmin):
    @admin.display(description='Employee Name')
    def employee_name(self, obj):
        return obj.employee.reverse_full_name()
    list_display = ('employee_name', 'offense', 'penalty', 'start', 'end')
    search_fields = ['employee__last_name']
admin.site.register(DisciplinaryAction, DisciplinaryActionAdmin)

#------------------

class WorkProfileAdmin(admin.ModelAdmin):
    @admin.display(description='Employee Name')
    def employee_name(self, obj):
        return obj.employee.reverse_full_name()

    @admin.display(description='Tenure')
    def tenure(self, obj):
        return obj.str_tenure()
    
    list_display = ('employee_name', 'unique_id', 'tenure', 'hiring_date', 'current_position', \
        'division', 'group', 'department')
    search_fields = ['employee__last_name', 'current_position', 'division', 'group', 'department']
admin.site.register(WorkProfile, WorkProfileAdmin)

