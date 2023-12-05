from django.shortcuts import render, HttpResponse

def utworz_turniej(request):
    return render(request, 'turnieje/strona_glowna.html')

