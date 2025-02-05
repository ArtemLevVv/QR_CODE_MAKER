from django.shortcuts import render

# Create your views here.
def render_pricing(request):
    return render(
        request = request,
        template_name = 'pricing/pricing.html',
    )
