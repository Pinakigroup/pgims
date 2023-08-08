from django.shortcuts import render, get_object_or_404, redirect
from .forms import FileForm
from .models import File
from django.contrib import messages
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import FileSerializer
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from accounts.decorators import allowed_users

# Create your views here.


# Create
@login_required
@allowed_users(allowed_roles=['admin', 'merchandiser', 'store'])
def create(request):
    form = FileForm()
    if request.method == 'POST':
        form = FileForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'File Created successfully')
            return redirect('file_read')
    context= {
        'form': form
    }
    return render(request, 'file/create.html', context)

# Create
@login_required
@allowed_users(allowed_roles=['admin', 'merchandiser', 'store'])
def file_read(request):
    file_data = File.objects.all().order_by('-id')
    context = {
        'file_data': file_data
    }
    return render(request, 'file/read.html', context)


# Create
@login_required
@allowed_users(allowed_roles=['admin', 'merchandiser', 'store'])
def file_update(request, pk):
    get_file_data = get_object_or_404(File, pk=pk)
    form = FileForm(instance=get_file_data)
    if request.method == 'POST':
        form = FileForm(request.POST, instance=get_file_data)
        if form.is_valid():
            form.save()
            messages.success(request, 'File updated successfully')
            return redirect('file_read')
    context = {
        'form': form
    }    
    return render(request, 'file/update.html', context)

# Delete
@login_required
@allowed_users(allowed_roles=['admin'])
def file_delete(request, pk):
    get_file = get_object_or_404(File, pk=pk)
    get_file.delete()
    messages.error(request, 'File deleted successfully')
    return redirect('file_read')


@method_decorator(login_required, name='dispatch')
class FileDetailView(APIView):
    def get(self, request, pk):
        try:
            person = File.objects.get(pk=pk)
            serializer = FileSerializer(person)
            return Response(serializer.data)
        except File.DoesNotExist:
            return Response(status=404)