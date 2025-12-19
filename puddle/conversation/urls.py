from django.urls import path
from . import views

app_name = 'conversation'

urlpatterns = [
    path( 'new_conversation/<int:item_pk>/',
          views.new_conversation, name='new_conversation'),
    path('', views.inbox, name='inbox'),
    path('<int:primary_key>/',
         views.conversation_detail, name='conversation_detail'),
]
    