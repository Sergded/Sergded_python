from django.http import HttpResponse, JsonResponse
from posts.models import Posts
from django.db.models import Count
from django.views import View

class New_views(View):
    @staticmethod
    def parse_new(new:Posts):
        return{'id':new.id, 'title':new.title, 'text':new.text, 'description':new.description, 'counter':new.counter, 'category':new.category}

    def post(self,request,*args,**kwargs):
        instance = Posts(title='New2',text='Ozzy Osborne',counter='1',category='singers')
        instance.save()
        return JsonResponse(self.parse_new(instance))
    
    def get(self,request):
        result = {
            'data':[],
            'filter_by_counter':[],
            'exclude_by_counter':[]
        }
        news=Posts.objects.all()
        for item in news:
            result['data'].append({'id':item.id,'title':item.title,'text':item.text,'description':item.description,'counter':item.counter})
        result['count'] = news.count()
    
        for item in news.filter(counter=3):
            result['filter_by_counter'].append({'id':item.id,'title':item.title,'text':item.text,'description':item.description,'counter':item.counter})

        for item in news.exclude(counter=6):
            result['exclude_by_counter'].append({'id':item.id,'title':item.title,'text':item.text,'description':item.description,'counter':item.counter})    
        return JsonResponse(result)
    
    def delete(self,request,_id):
        delete_post = Posts.objects.filter(id = _id).delete()
        return JsonResponse({'delete post': _id})
    
    def put(self,request):
        new = Posts.objects.update_or_create(title='Who are you?',counter='3',defaults={'counter':6})
        return JsonResponse({})