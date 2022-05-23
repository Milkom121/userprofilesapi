#CON I ROUTERS
from django.urls import path , include
from rest_framework.routers import DefaultRouter
from profiles.api.views import (ProfileViewSet,
                                ProfileStatusViewSet ,
                                AvatarUpdateView)

#i routers slavorano con le viewset e generano automaticamente gli endpoint
router = DefaultRouter()
router.register(r'profiles', ProfileViewSet)
router.register(r'status', ProfileStatusViewSet)


urlpatterns = [
    path('' , include (router.urls)),
    path('avatar/', AvatarUpdateView.as_view(), name='avatar-update'),

]










#SENZA I ROUTERS
# from django.urls import path
# from profiles.api.views import ProfileViewSet
#
# #questo è un binding esplicito - 03:50 https://www.udemy.com/course/guida-per-sviluppatori-a-django-rest-framework-e-vue-js/learn/lecture/12960220#notes
# profile_list = ProfileViewSet.as_view({'get' : 'list' })
# profile_detail = ProfileViewSet.as_view({'get' : 'retrieve' })
#
# urlpatterns = [
#     path('profiles/' , profile_list, name='profile-list'),
#     path('profiles/<int:pk>/' , profile_detail, name='profile-detail')
# ]
