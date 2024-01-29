from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from posts.models import Wallets
from django.db.models import Count
from django.views import View
from django.template import loader
from django.shortcuts import get_object_or_404
import json

class WalletsTemp(View):
    
    def get(self,request,*args,**kwargs):
        wallets = Wallets.objects.all()
        template = loader.get_template('wallets/wallets_list.html')
        context = {
            'wallets':wallets,
        }
        return HttpResponse(template.render(context,request))