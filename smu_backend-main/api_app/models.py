from django.db import models

#from board.models import Post  #보드 앱 추가 필요

class Address(models.Model):
    full_address = models.CharField(max_length=255,default="입력되지 않음")

    def __str__(self):
        return self.full_address
    
    


class Document(models.Model):
    #게시자 아이디
    #post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='documents')
    id = models.AutoField(primary_key=True)
    #게시자 메일
    email = models.EmailField(verbose_name='email address', max_length = 255, unique = True)
    #주소
    #addr=models.CharField(max_length=100)
    #json 원본파일 위치
    json_original_file_location = models.CharField(max_length=255, verbose_name='JSON 원본 파일 위치')
    #근저당 관련 정보 //요약내용
    mager_info=models.CharField(max_length=500)

    #안전한지 최종결과
    mager_info=models.CharField(max_length=50)



class JsonDb(models.Model):
    json_data = models.JSONField()  # JSON 데이터를 저장할 필드
    #created_at = models.DateTimeField(auto_now_add=True)  # 데이터 생성 시간
    

#등기부등본 pdf 원본파일
class PDFFile(models.Model):
    file_name = models.CharField(max_length=255)
    file_data = models.BinaryField()
    uploaded_at = models.DateTimeField(auto_now_add=True)
    summary = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.file_name