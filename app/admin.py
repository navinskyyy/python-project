from django.contrib import admin
from .models import Departments,Doctors,Booking
# Register your models here.

admin.site.register(Departments)

class DoctorAdmin(admin.ModelAdmin):
    list_display = ('doc_name', 'doc_spec', 'dep_name')
admin.site.register(Doctors,DoctorAdmin)

class BookingAdmin(admin.ModelAdmin):
    list_display = ('id','p_name','p_phone','p_email','doc_name','booking_date','booked_on')

admin.site.register(Booking,BookingAdmin)