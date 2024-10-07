from django.db import models
from django.urls import reverse
from enum import Enum
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


class WorkOrderRequest(models.Model):
    STATUS = (
        ('NEW', 'new'),
        ('ACCEPTED', 'accepted'),
        ('COMPLETED', 'completed'),
        ('CANCELLED', 'cancelled')
    )
    customer_name = models.CharField(max_length=75)
    customer_email = models.CharField(max_length=75)
    customer_phone_number = models.CharField(max_length=75, blank=True, null=True)
    customer_request = models.TextField()
    notes = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=30, choices=STATUS, default='NEW')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = ("WorkOrderRequest")
        verbose_name_plural = ("WorkOrderRequests")

    def __str__(self):
        return self.customer_name

    def get_absolute_url(self):
        return reverse("WorkOrderRequest_detail", kwargs={"pk": self.pk})
    

class WorkRequestResponse(models.Model):
    work_request = models.ForeignKey(WorkOrderRequest, on_delete=models.CASCADE)
    subject = models.CharField(max_length=75)
    message = models.TextField(blank=True, null=True)   
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def save(self, **kwargs):
        html_content = render_to_string("email/request-response.html",context={"message":self.message, 'year':2024})            
        msg = EmailMultiAlternatives(
            self.subject,
            html_content,
            "tim@email.tccs.tech",
            [self.work_request.customer_email],
            headers={"List-Unsubscribe": "<mailto:unsub@example.com>"},
            )
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        super().save(**kwargs)  
       