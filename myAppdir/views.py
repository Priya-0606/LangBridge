from django.shortcuts import render
from deep_translator import GoogleTranslator

# Create your views here.
def index(request):
    if request.method == 'POST':
        textbox = request.POST.get('textbox')
        select = request.POST.get('select')  # Language code (e.g., 'hi' for Hindi)

        if textbox and select:
            trans = GoogleTranslator(source='auto', target=select).translate(textbox)
            context = {'text': textbox, 'translate': trans}
            return render(request, 'index.html', context)
        else:
            error_msg = "Please enter text and select a language."
            return render(request, 'index.html', {'error': error_msg})

    return render(request, 'index.html')
