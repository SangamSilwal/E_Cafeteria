
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

from . import views
urlpatterns = [
    path('',views.homePage,name="homePage"),
    path('StudentCreate/',views.createStudent,name="Create-Student"),
    path('ScanR',views.registerRFID,name="re_Rf"),
    path('afterscan/<int:uuid>',views.after_scan_page,name="afterscan"),
    path('transactionPage/<int:uuid>',views.view_transaction_history,name='transactionpage'),
    path("inspect/profile",views.inspect_profile,name="inspect-profile"),
    path("inspect-sales-today",views.inspect_sales,name="inspect-sales"),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)