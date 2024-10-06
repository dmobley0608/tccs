from django.shortcuts import render,redirect
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from .forms import ContactUsForm
from work_requests.models import WorkOrderRequest
def homepage(request):
    return render(request, 'homepage.html')

def contact_us(request):
    form = ContactUsForm()
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            work_order = WorkOrderRequest(
                customer_name=request.POST['name'],
                customer_email=request.POST['email'],
                customer_phone_number=request.POST['phone_number'],
                customer_request=request.POST['message']                
            )
            work_order.save()
            html_content = render_to_string("email/thank-you-for-contacting-us.html",context={"name":request.POST['name'], 'year':2024})
            
            msg = EmailMultiAlternatives(
                "Thank You",
                html_content,
                "no-reply@email.tccs.tech",
                [request.POST['email']],
                headers={"List-Unsubscribe": "<mailto:unsub@example.com>"},
            )
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            send_mail("New Request",request.POST['message'],'no-reply@email.tccs.tech', ['dmobley0608@gmail.com'])         
                  
            return redirect('homepage')
        print(request.POST)        
    return render(request, 'contact-us.html', {'form':form})