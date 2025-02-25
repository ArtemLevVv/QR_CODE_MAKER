from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .forms import Qrcode_Form

# Create your views here.
def render_ger(request: HttpRequest):
    form = Qrcode_Form()
    if request.method == "POST":
        form_post = Qrcode_Form(request.POST, request.FILES)
        if form_post.is_valid():
            link = form_post.cleaned_data.get('link')
            color = form_post.cleaned_data.get('color')
            size = form_post.cleaned_data.get('size')
            # Тут можна додати подальшу обробку отриманих даних, наприклад, згенерувати QR-код або зберегти їх у базі даних

            # Якщо хочеш після успішної обробки відправити повідомлення або перенаправити:
            return HttpResponse("QR код згенеровано успішно!")  # або redirect на іншу сторінку
        else:
            # Якщо форма не валідна, передаємо її з помилками назад на сторінку
            return render(
                request=request,
                template_name='ger/ger.html',
                context={'form': form_post},
            )

    # Якщо метод GET, просто відображаємо форму
    return render(
        request=request,
        template_name='ger/ger.html',
        context={'form': form},
    )


def render_my_qr(request):
    return render(
        request = request,
        template_name= 'my_qr/my_qr.html',
    )