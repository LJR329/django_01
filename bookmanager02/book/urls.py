from django.urls import path
from book import views
urlpatterns = [
    # path('<cat_id>/<goods_id>', views.index),
    path('string/', views.string),
    path('register/', views.register),
    path('json/', views.json1)
]
