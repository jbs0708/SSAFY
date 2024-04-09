from django.shortcuts import render

# Create your views here.
# 메인 페이지를 만드는 index라는 이름의 함수를 작성
def index(request):
    # Why?
    # render 함수가 그렇게 만들어져 있음
    return render(request, 'index.html')
  # return render(request, 템플릿'경로')
    # 경로에 'templates 이후'의 경로를 기입
    # 그러므로 articles 폴더 하위에 'templates' 폴더를 만들어야함

def r(request):
    return render(request, '.html')