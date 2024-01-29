from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from posts.models import Wallets
from django.db.models import Count
from django.views import View
from django.template import loader
from django.shortcuts import get_object_or_404
import json
    
class DetailWallet(View):
    def get(self,request,_id,*args,**kwargs):
        wallet = get_object_or_404(Wallets, id=_id)
        template = loader.get_template('wallets/wallet_details.html')
        context = {
            'wallet':wallet,
            'url_path':'/posts/wallets/'
        }
        return HttpResponse(template.render(context,request))