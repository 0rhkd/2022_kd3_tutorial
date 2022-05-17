from django.http import HttpResponse
from django.shortcuts import render

from .models import Armyshop, Course

from django.shortcuts import redirect
from .forms import CourseForm
def course_save(request):
    if request.method == 'POST':

        form = CourseForm(request.POST)
        if form.is_valid():
            # commit False 사용 시 Curriculum 모델클래스로 반환
            c = form.save(commit=False)
            c.save()
            return redirect('/second/course/save/')
    else:
        form = CourseForm()

    return render(
    request, 'secondapp/course_save.html',
        { 'form': form }
    )



def course(request):
  return render(
    request, 'secondapp/course.html', {}
    )

def insert(request):
    Course(name='데이터 분석', cnt=30).save()
    Course(name='데이터 수집', cnt=20).save()
    Course(name='웹개발', cnt=25).save()
    Course(name='인공지능', cnt=20).save()

    return HttpResponse('완료')

def main(request):
    return HttpResponse(
        '<h1><u>Main</u></h1>'
    )


def show(request):
    course = Course.objects.all()
#     result = ''
#     for c in course:
#      result += c.name + '<br>'
#     return HttpResponse(result)
    return render(
       request, 'secondapp/show.html',
        {'data': course }
    )


def army_shop2(request, year, month):
    shops = Armyshop.objects.filter(year=year, month=month)
    
    return render(
     request, 'secondapp/army_shop.html',
     { 'data' : shops }
)

def army_shop(request):
    # shops = Armyshop.objects.all()
    # GET['prd'] 도 사용가능은 함
    
    prd = request.GET.get('prd')
    if not prd: # prd에 값이 없을 경우
        prd = ''

    shops = Armyshop.objects.filter(name__contains=prd)

    return render(
     request, 'secondapp/army_shop.html',
     { 'data' : shops }
)


