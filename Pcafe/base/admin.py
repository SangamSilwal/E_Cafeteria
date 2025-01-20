from django.contrib import admin
from .models import *


admin.site.register(CanteenManager)
admin.site.register(StudentData)
admin.site.register(TranscationHistory)
admin.site.register(AnalysisTransaction)
admin.site.register(UUIDStudent)
