from django.urls import path
from . import views

app_name = 'bbsnote'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:board_id>/', views.detail, name='detail'), 
    path('comment/create/<int:board_id>/',views.comment_create, name='comment_create'),
    path('board/create', views.board_create, name='board_create'),
    path('board/modify/<int:board_id>', views.board_modify, name='board_modify'),
    path('board/delete/<int:board_id>', views.board_delete, name='board_delete'),
    path('comment/modify/<int:comment_id>/', views.comment_modify, name='comment_modify'),
    path('comment/delete/<int:comment_id>/', views.comment_delete, name='comment_delete'),
]



# path('', views.index, name='index'),
    # 위에 먼저  app_name이라는 변수에 bbsnote 라고 설정해주고, 
    # 그 다음 url  path 설정할 때 name='index' 라고 해주면,
    # 프로젝트 내에 어디에서도 url 을 사용해야하는 순간에 bbsnote:index 라고 하면
    # 장고가 찰떡같이 urls.py에 정의해놓은 appname=bbsnote, path의 name은 index라고 
    # 지정해놓은 path('', views.index, name='index') 을 찾아서 url 처리해주는거라 생각하시면 어떨까요~~