from django.urls import path,re_path
from . import views

app_name='test'

urlpatterns = [
    path('',views.showArticles,name="Home"),
    path('CreateArticle/',views.ArticleCreate,name="NewArticle"),
    path('about/',views.about,name="About"),
    path('Contact/',views.contact,name="Contact"),
    # path(r'^(?P<slug>[\w_]+)/$',views.postDetail)
    # re_path(r'^(?P<slug>[\w-]+)/$', views.article_detail),
    path('<slug:Slg>/',views.article_detail,name="ArtiD")
]
