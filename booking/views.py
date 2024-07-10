from django.shortcuts import get_object_or_404
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from .models import Consumer, Order, Invoice
import json
import logging
from django.shortcuts import render

logger = logging.getLogger(__name__)
def index(request):
    return render(request, 'booking/index.html')

@csrf_exempt
def book_cylinder(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            logger.info(f"Received data: {data}")
            consumer_number = data.get('consumer_number')
            if not consumer_number:
                return HttpResponseBadRequest('Consumer number is required.')
            
            consumer = get_object_or_404(Consumer, consumer_number=consumer_number)
            
            # Create Order
            order = Order.objects.create(consumer=consumer)
            
            # Generate Invoice
            invoice = Invoice.objects.create(order=order, amount=500.00)  # Assuming a fixed amount
            
            # Delivery Instructions (simplified)
            delivery_instructions = f"Deliver to {consumer.name}, {consumer.address}"
            
            return JsonResponse({
                'message': 'Booking successful! Invoice generated.',
                'invoice_id': invoice.id,
                
                'invoice_amount': invoice.amount,
                'order_id': order.id,
                'consumer_name': consumer.name,
                'delivery_address': consumer.address,
                'delivery_instructions': delivery_instructions
                
                
            })
        except json.JSONDecodeError:
            return HttpResponseBadRequest('Invalid JSON.')
    else:
        return HttpResponseBadRequest('Invalid request method.')
