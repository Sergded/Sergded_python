from django.http import HttpResponse, JsonResponse
from .models import Posts, Comment, Wallet
from django.db.models import Count
from django.db import transaction
from django.views import View

# Create your views here.

POSTS = [{
    'Title':'First post',
    'Text':'Hi! I am postwriter'
},
{
    'Title':'Second post',
    'Text':'And my posts are very good'
},
{
    'Title':'Third post',
    'Text':'I am tired, i am gone'
}
]


def get_posts(request):
    all_posts=[]
    for post in POSTS:
        all_posts.append(post)
    return JsonResponse(all_posts,safe=False)

# Django Postgres Homework

def create_post(request):
    new = Posts(title='New2',text='Ozzy Osborne',counter='1',category='singers')
    new.save()
    return JsonResponse({})

def get_news(request):
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

def get_newpost(request,_id):
    newpost=Posts.objects.get(id=_id)
    return JsonResponse({'id':newpost.id,'title':newpost.title,'text':newpost.text,'description':newpost.description})

def get_with_union(request):
    result = {
        '3':[],
        '6':[],
        'all':[]
    }
    news_1=Posts.objects.filter(counter=3)
    for item in news_1:
        result['3'].append({'id':item.id,'title':item.title,'description':item.description,'counter':item.counter})
    
    news_2=Posts.objects.filter(counter=6)
    for item in news_2:
        result['6'].append({'id':item.id,'title':item.title,'description':item.description,'counter':item.counter})

    news_3=news_1.union(news_2)
    for item in news_3:
        result['all'].append({'id':item.id,'title':item.title,'description':item.description,'counter':item.counter})    
    return JsonResponse(result)

def exist_object(request,counter):
    news = Posts.objects.filter(counter=counter).exists()
    result = {'is_exists':news}
    return JsonResponse(result)

def parse_object(request,counter):
    new = Posts.objects.update_or_create(title='Bad story',counter='1',defaults={'counter':5})
    return JsonResponse({})


def delete_post(request,_id):
    delete_post = Posts.objects.filter(id = _id).delete()
    return JsonResponse({'delete post': _id})

# Django Foreign keys homework

def create_comment (request):
    new_id=23
    text='Comment'
    new = Posts.objects.get(id=23)
    comment = Comment(text=text,new=new)
    comment.save()
    return JsonResponse({'id':comment.id,'text':comment.text,'new_id':comment.new_id})

def get_comments(request,post_id):
    post = Posts.objects.get(id=post_id)
    comments = post.comments.all()
    result = []
    for comment in comments:
        result.append({'id': comment.id, 'text' : comment.text})
    return JsonResponse(result, safe= False)

def change_status(request,post_id,status):
    comment = Comment.objects.filter(new_id = post_id).update(status = status)
    return JsonResponse(comment, safe=False)

# Django Transactions homework

class Transaction(View):
    @transaction.atomic
    def post(self, request,*args,**kwargs):
        p_wallet = request.POST.get('p_wallet')
        b_wallet = request.POST.get('b_wallet')
        wallets_1 = Wallet(private_wallet = int(p_wallet) + 100)
        wallets_2 = Wallet(business_wallet = int(b_wallet) - 100)
        wallets_1.save()
        wallets_2.save()
        return JsonResponse({'transaction' : 'successful' ,'p_wallet' : wallets_1.private_wallet ,'b_wallet': wallets_2.business_wallet })
