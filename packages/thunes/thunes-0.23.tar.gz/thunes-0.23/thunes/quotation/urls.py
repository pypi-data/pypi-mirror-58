from django.urls import path

from .views import QuotationCreateView, QuotationDetailView, ServerPing

app_name = 'quotation'

urlpatterns = [
    # sender api view
    path('ping', ServerPing.as_view(), name='Server-Ping'),
    path('create', QuotationCreateView.as_view(), name='quotation-create'),
    path('<int:id>', QuotationDetailView.as_view(), name='quotation-detail'),
]