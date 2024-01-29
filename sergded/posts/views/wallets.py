from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from posts.models import Wallets
from django.db.models import Count
from django.views import View
from django.template import loader
from django.shortcuts import get_object_or_404
import json

class WalletsView(View):

    def post(self,request,*args,**kwargs):
        name = request.POST.get('name','')
        currency = request.POST.get('currency','')
        
        if not name or not currency:
            return HttpResponseBadRequest('name or currency field is empty')
        wallet = Wallets(name=name,currency=currency)
        wallet.save()
        return(JsonResponse(data=wallet.serilize_from_db()))

    def get(self,request,*args,**kwargs):
        wallets = Wallets.objects.all()
        return JsonResponse({'data':[wallet.serilize_from_db() for wallet in wallets]})