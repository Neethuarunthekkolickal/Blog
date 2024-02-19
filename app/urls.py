from django.urls import path
from . import views
urlpatterns =[
    path("",views.index,name="index"),
    path("post",views.post,name="post"),
    path("singup",views.singup,name="singup"),
    path("show/<int:id>",views.show,name="show"),
    path("delete/<int:id>",views.delete,name="delete"),
    path("edit/<int:id>",views.edit,name="edit")
]