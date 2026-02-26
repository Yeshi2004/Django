# Create your views here.
from django.shortcuts import redirect, render
from .models import SmartNote
from django.contrib.auth.decorators import login_required
    

@login_required
def smart_notes(request):
    notes=SmartNote.objects.filter(user=request.user).order_by('-id')
    return render(request, 'notes/index.html', {'notes': notes})

@login_required
@login_required
def create_note(request):
    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        content = request.POST.get('content', '').strip()

        # ✅ define notes FIRST
        notes = SmartNote.objects.filter(user=request.user)

        if not content:
            return render(
                request,
                'notes/index.html',
                {
                    'error': 'Content is required.',
                    'title': title,
                    'notes': notes
                }
            )

        SmartNote.objects.create(
            user=request.user,
            title=title,
            content=content
        )

        # reload notes after adding
        notes = SmartNote.objects.filter(user=request.user)
        return render(request, 'notes/index.html', {'notes': notes})

    return redirect('notes:index')

@login_required
def delete_note(request, note_id):
    note = SmartNote.objects.get(id=note_id, user=request.user)
    note.delete()
    return redirect('notes:index')