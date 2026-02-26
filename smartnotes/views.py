from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Note

@login_required
def smart_notes(request):
    if request.method == "POST":
        content = request.POST.get("content")
        title = request.POST.get("title", "")

        if content:
            Note.objects.create(
                user=request.user,
                title=title,
                content=content
            )

        return redirect("smartnotes:home")

    notes = Note.objects.filter(user=request.user)
    return render(request, "smartnotes/index.html", {"notes": notes})

@login_required
def delete_note(request, note_id):
    if request.method == "POST":
        note = Note.objects.get(id=note_id, user=request.user)
        note.delete()
    return redirect('smartnotes:home')