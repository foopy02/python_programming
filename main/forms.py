from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.conf import settings 
from . models import Lesson
NUMBER_OF_LESSONS = 26
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

class AuthUserForm(AuthenticationForm, forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']


class RegisterUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-class'

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])

        if commit:
            user.save()

        for i in range(1, NUMBER_OF_LESSONS + 1):
            try:
                lesson = Lesson(user=user,number=i,topic=topics[i])
                lesson.save()
            except:
                break
        return user