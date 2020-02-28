from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.sectorlist),
    path('/generate', views.generatesector),
    path('/sectordetail/<int:sectorid>', views.sectordetail),
    path('/editsector/<int:sectorid>', views.editsector),
    path('/updatesector/<int:sectorid>', views.updatesector),
    path('/worlddetail/<int:worldid>', views.worlddetail),
    path('/editworld/<int:worldid>', views.editworld),
    path('/updateworld/<int:worldid>', views.updateworld),
    path('/exportsector/<int:sectorid>', views.exportxlsx),
    path('/confirmsectordelete/<int:sectorid>', views.confirmsectordelete),
    path('/confirmworlddelete/<int:worldid>', views.confirmworlddelete),
    path('/sectordelete/<int:sectorid>', views.deletesector),
    path('/worlddelete/<int:worldid>', views.deleteworld),
]