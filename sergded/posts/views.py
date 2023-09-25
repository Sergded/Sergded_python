from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
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


def get_posts(reqest):
    all_posts=[]
    for post in POSTS:
        all_posts.append(post)
    return JsonResponse(all_posts,safe=False)
