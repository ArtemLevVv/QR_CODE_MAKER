from django.shortcuts import render

# Create your views here.
def render_ger(request):
    return render(
        request = request,
        template_name= 'ger/ger.html',
    )

def render_my_qr(request):
    return render(
        request = request,
        template_name= 'my_qr/my_qr.html',
    )