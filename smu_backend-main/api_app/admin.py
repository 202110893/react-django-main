from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import PDFFile

@admin.register(PDFFile)
class PDFFileAdmin(admin.ModelAdmin):
    list_display = ('file_name', 'uploaded_at')  # 필요한 필드를 설정
