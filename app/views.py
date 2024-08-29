# from django.shortcuts import render,get_object_or_404,redirect
# from django.http import HttpResponse

# from .models import Departments,Doctors,Booking
# from .forms import BookingForm


# # Create your views here.
# def index(request):
#     return render(request,'index.html')

# def about(request):
#     return render(request,'about.html')

# def booking(request):
#     if request.method =="POST":
#         form = BookingForm(request.POST)

#         if form.is_valid():
#             form.save()
#             return render(request,'confirmation.html')

#     form = BookingForm()    
#     dict_form={
#         'form': form
#     }
#     return render(request,'booking.html',dict_form)

# def booking_confirmation(request,booking_id):
#     booking = get_object_or_404(Booking, id=booking_id)
#     print(booking.p_name, booking.p_phone, booking.p_email)

#     context ={
#         'booking':booking
#     }
#     return render(request,'booking_confirmation.html',context)

# def create_booking(request):
#     if request.method == 'POST':
#         form = BookingForm(request.POST)
#         if form.is_valid():
#             booking = form.save()
#             return redirect('booking_confirmation', booking_id=booking.id)
#     else:
#         form = BookingForm()

#     return render(request, 'booking_form.html', {'form': form})



# def doctors(request):
#     dict_docs = {
#         'doctors': Doctors.objects.all()
#     }

#     return render(request,'doctors.html',dict_docs)

# def contact(request):
#     return render(request,'contact.html')

# def department(request):
#     dict_dept={
#         'dept': Departments.objects.all()
#     }
#     return render(request,'department.html',dict_dept)
from django.shortcuts import render, get_object_or_404, redirect
from .models import Departments, Doctors, Booking
from .forms import BookingForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def searching(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save()  # Save the form and capture the instance
            return redirect('booking_confirmation', booking_id=booking.id)  # Redirect with the booking ID
    else:
        form = BookingForm()
    
    context = {
        'form': form
    }
    return render(request, 'booking.html', context)

def booking_confirmation(request, booking_id):
     booking = get_object_or_404(Booking, id=booking_id)
     print(booking.p_name, booking.p_phone, booking.p_email,booking.doc_name, booking.booking_date, booking.booked_on)  # For debugging
    
     context = {
         'booking': booking,
    }
     return render(request, 'confirmation.html', context)

def doctors(request):
    context = {
        'doctors': Doctors.objects.all()
    }
    return render(request, 'doctors.html', context)

def contact(request):
    return render(request, 'contact.html')

def department(request):
    context = {
        'dept': Departments.objects.all()
    }
    return render(request, 'department.html', context)
