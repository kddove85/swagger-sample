from rest_framework.decorators import api_view

from datetime import date
from django.http import JsonResponse


@api_view(['GET'])
def get_current_time(request):
    today = date.today()
    return JsonResponse({"response": f"Today's Date is {today}"})
