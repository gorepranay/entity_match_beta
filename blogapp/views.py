from .models import FileModel
from .forms import FileForm
from django.shortcuts import render, redirect


class FileCounter:
    cnt=0

def FileDetails(request):
    try:
        data = FileModel.objects.all()
    except FileModel.DoesNotExist:
        raise Http404('Data does not exist')

    if request.method == 'POST':
        form = FileForm(request.POST)
        if form.is_valid():
            files = FileModel(source_name=form.cleaned_data['source_name'],
                                   source_file=form.cleaned_data['source_file'])
            files.save()
            FileCounter.cnt += 1
            return redirect(f'/create')
    else:
        form = FileForm()

    context = {
        'form': form,
        'comments': data,
        'counter':FileCounter.cnt
    }

    print('CNT:',FileCounter.cnt)
    return render(request, 'blogapp/detailview.html', context)