from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'mainApp/homepage.html')


def contact(request):
    return render(request,
        'mainApp/contact.html',{
            'cont':'Если у вас остались вопросы, то задавайте их мне по телефону',
            'tel':'+7(953)23-72-699',
            'Email':'kovalevskuy2017@outlook.com'}
            )
