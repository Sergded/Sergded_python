from .posts import New_views
from .wallets import WalletsView
from .detail_wallets import DetailWallet
from .wallets_temp import WalletsTemp
from .posts_drf_views import Posts_get
from .posts_drf_views import Posts_APIList
from .posts_drf_views import Posts_APIUpdate
from .posts_drf_views import Posts_APIDetailView
from .detail_posts_drf_views import Posts_APIfilter

all = (
    'New_views',
    'WalletsView',
    'DetailWallet',
    'WalletsTemp',
    'Posts_get',
    'Posts_APIList',
    'Posts_APIUpdate',
    'Posts_APIDetailView',
    'Posts_APIfilter'
)
