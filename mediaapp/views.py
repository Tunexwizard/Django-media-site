from django.shortcuts import render, redirect
from .models import MediaFile
from .forms import MediaFileForm

def upload_file(request):
    if request.method == 'POST':
        form = MediaFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload')
    else:
        form = MediaFileForm()

    files = MediaFile.objects.all()
    return render(request, 'upload.html', {'form': form, 'files': files})

