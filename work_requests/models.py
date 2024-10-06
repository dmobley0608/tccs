from django.db import models
from django.urls import reverse
from enum import Enum



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
    
   