from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from users.models import Profile, Employee, Review

# Register your models here.
#class UserInline(admin.StackedInline):
    #model = Employee
    #can_delete = False
    #verbose_name_plural = 'User'
    
#class UserAdmin(BaseUserAdmin):
   # inlines = (UserInline, )

#admin.site.unregister(User)
#admin.site.register(User, UserAdmin)

admin.site.register(Profile)
admin.site.register(Employee)
admin.site.register(Review)