from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet
from .models import Expense
from .serializers import *
from django.utils import timezone
from datetime import timedelta


class ExpenseViewSet(ModelViewSet):
    serializer_class = ExpenseSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        queryset = Expense.objects.filter(owner=self.request.user)


        current_time = timezone.now().date()
        filter_type = self.request.query_params.get("filter", None)
        start_date = self.request.query_params.get("start_date", None)
        end_date = self.request.query_params.get("end_date", None)

        # also implement for future dates and test all filter ranges
        match filter_type:
            case "past_week":
                queryset = queryset.filter(purchase_date__gte=(current_time - timedelta(days=7)))

            case "last_month":
                queryset = queryset.filter(purchase_date__gte=(current_time - timedelta(days=30)))

            case "last_3_months":
                queryset = queryset.filter(purchase_date__gte=(current_time - timedelta(days=30)))


            case "custom":
                if start_date and not end_date:
                    queryset = queryset.filter(purchase_date__range=[start_date, current_time])
                
                elif start_date and end_date:
                    queryset = queryset.filter(purchase_date__range=[start_date, end_date])

        return queryset



