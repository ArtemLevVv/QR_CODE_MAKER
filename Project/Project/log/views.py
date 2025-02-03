from django.shortcuts import render

# Create your views here.
def render_reg(request):
    return render(
        request = request,
        template_name= 'reg/reg.html',
    )

def render_log(request):
    return render(
        request = request,
        template_name= 'log/log.html',
    )