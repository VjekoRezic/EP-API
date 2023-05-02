from django.contrib import admin
from .models import WO_Category, WO_Status, WorkOrder

admin.site.register(WO_Category)
admin.site.register(WO_Status)
admin.site.register(WorkOrder)

