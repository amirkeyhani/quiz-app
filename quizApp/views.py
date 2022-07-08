from django.shortcuts import redirect, render

from .models import Quiz
from .forms import addQuestionForm
# Create your views here.

def home(request):
    if request.method == 'POST':
        questions = Quiz.objects.all()
        score = 0
        correct = 0
        wrong = 0
        total = 0
        for q in questions:
            total += 1
            if q.answer == request.POST.get(q.question):
                score += 1
                correct += 1
            else:
                wrong += 1
            
        context = {
            'score': f'{score}/{total}', 
            'correct': correct, 
            'wrong': wrong, 
            'total': total, 
        }
        return render(request, 'result.html', context)
    
    questions = Quiz.objects.all()
    return render(request, 'home.html', {'questions': questions})
    
def addQuestion(request):
    if request.method == 'POST':
        form = addQuestionForm(request.POST)
        if form.is_valid():
            form.save()
            
        return redirect('addQuestion')
    
    form = addQuestionForm()
    return render(request, 'AddQuestion.html', {'form': form})