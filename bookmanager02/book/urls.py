from django.urls import path
from book import views
urlpatterns = [
    path('<cat_id>/<goods_id>', views.index),
]
