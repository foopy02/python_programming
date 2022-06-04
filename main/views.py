from django.shortcuts import redirect, render
from .forms import AuthUserForm, RegisterUserForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.views.generic import ListView, CreateView, DetailView
from django.contrib.auth.decorators import login_required
from .models import Lesson
from django.utils import timezone
import random
# Create your views here.
topics = {
    1:"Жаңадан бастаушыларға арналған Python",
    2:'Даму ортасын орнату',
    3:'Python тіліндегі негізгі операциялар',
    4:'Python тіліндегі айнымалылар мен деректер түрлері',
    5:'Шартты операторлар',
    6:'Олардағы циклдар мен операторлар (for, while)',
    7:'Тізімдер (list). Функциялар және олардың әдістері',
    8:'Жолдық функциялар. Индекстер мен кесінділер',
    9:'Кортеждер (tuple)',
    10:'Сөздіктер (dict) және олармен жұмыс',
    11:'Жиындар (set и frozenset)',
    12:'Функциялар (def, lambda)',
    13:'Python көмегімен файлдармен жұмыс істеу',
    14:'Ерекшелік өңдеушісі. «try - except» конструкциясы',
    15:'Файлдармен жұмыс істеуге арналған «with...  as» менеджері',
    16:'Python тіліндегі модульдер. Модульдерді құру және олармен жұмыс істеу',
    17:'OOP негіздері. Класс пен объект құру',
    18:'Конструкторлар, қайта анықтау әдістері',
    19:'Мұрагерлік, инкапсуляция, полиморфизм',
    20:'Функция декораторлары',
    21:'Python бағдарламасының соңғы бөлігі',
}
def index(request):
    users = User.objects.all()
    lessons = list(Lesson.objects.all())
    random.shuffle(lessons)

    context = {
        'count':users.count,
        # 'lessons':set(random.sample(lessons, 8))  
        'topics': topics

    }
    return render(request, 'main/index.html', context )


@login_required(login_url='/login/')
def lesson(request, number):
    lesson = Lesson.objects.get(user=request.user, number=number)
    context = {
        'lesson': lesson,
        'topics': topics
    }
    return render(request, f'main/lessons/lesson{number}.html', context )


@login_required(login_url="/login/")
def all_lessons(request):
    lessons = Lesson.objects.filter(user=request.user)
    context = {
        'lessons':lessons
    }
    return render(request, 'main/lessons.html', context )

@login_required(login_url="/login/")
def passed_lesson(request, number):
    lesson = Lesson.objects.get(user=request.user, number=number)
    lesson.isPassed = True
    lesson.dataPassed = timezone.now()+ timezone.timedelta(hours=6)
    lesson.save()
    return redirect("lessons")
    

class MyLoginView(LoginView):
    template_name = "main/login.html"
    form_class = AuthUserForm
    success_url = reverse_lazy('index')


class MyLogoutView(LogoutView):
    next_page = reverse_lazy('index')

class RegisterUserView(CreateView):
    model = User
    template_name = "main/signup.html"
    form_class = RegisterUserForm
    success_url = reverse_lazy('login')
    success_msg = "Пользователь успешно создан"
