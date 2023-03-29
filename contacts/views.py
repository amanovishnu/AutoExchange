from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact
from django.core.mail import send_mail
from django.contrib.auth.models import User

# Create your views here.
def enquiry(request):
    if request.method == 'POST':
        car_id = request.POST.get('car_id')
        user_id = request.POST.get('user_id')
        car_title = request.POST.get('car_title')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        customer_query = request.POST.get('customer_query')
        city = request.POST.get('city')
        state = request.POST.get('state')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        comments = request.POST.get('comments')

        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.filter(car_id=car_id, user_id=user_id)
            if has_contacted:
                messages.error(request,'You have already made an enquiry about this car, Please wait until we get back to you')
                return redirect('/cars/'+car_id)

        contact = Contact(
            car_id=car_id,
            user_id=user_id,
            first_name=first_name,
            last_name=last_name,
            car_title=car_title,
            customer_query=customer_query,
            city=city,
            state=state,
            email=email,
            phone_number=phone_number,
            comments=comments
        )

        admin_info = User.objects.get(is_superuser=True)
        admin_email_id = admin_info.email

        send_mail(
            'Enquiry : New Car',
            f'You have a new Enquiry for the car {car_title}, Please login to your admin console for more info',
            'dev.geekymano@gmail.com',
            [email],
            fail_silently=False
        )
        contact.save()
        messages.success(request, 'Thankyou, your Request has been submitted, we will get back to you shortly.')
    return redirect('/cars/'+car_id)
