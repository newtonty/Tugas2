import datetime
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.core import serializers
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from study_tracker.models import AssignmentRecord
from study_tracker.forms import AssignmentRecordForm, CustomUserCreationForm


# Create your views here.

@login_required(login_url='/tracker/login/')
def show_tracker(request):
    assignment_data = AssignmentRecord.objects.all()
    context = {
        'list_of_assignments': assignment_data,
        'name': request.user.username,
        'last_login': request.COOKIES['last_login'],
        'jumlah' : assignment_data.count()

    }
    return render(request, "tracker.html", context)

def create_assignment(request):
    form = AssignmentRecordForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('study_tracker:show_tracker'))

    context = {'form': form}
    return render(request, "create_assignment.html", context)

def show_xml(request):
    data = AssignmentRecord.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = AssignmentRecord.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request):
    data = AssignmentRecord.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request):
    data = AssignmentRecord.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('study_tracker:login')
    else:
        form = CustomUserCreationForm
    context = {'form':form}
    return render(request, 'register.html', context)

def modify_assignment(request, id):
    # Get data berdasarkan ID
    assignment = AssignmentRecord.objects.get(pk = id)

    # Set instance pada form dengan data dari assignment
    form = AssignmentRecordForm(request.POST or None, instance=assignment)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('study_tracker:show_tracker'))

    context = {'form': form}
    return render(request, "modify_assignment.html", context)

def delete_assignment(request, id):
    # Get data berdasarkan ID
    assignment = AssignmentRecord.objects.get(pk = id)
    # Hapus data
    assignment.delete()
    # Kembali ke halaman awal
    return HttpResponseRedirect(reverse('study_tracker:show_tracker'))

@csrf_exempt
def create_assignment_ajax(request):  
# create object of form
    form = AssignmentRecordForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        data = AssignmentRecord.objects.last()

        # parsing the form data into json
        result = {
            'id':data.id,
            'name':data.name,
            'subject':data.subject,
            'date':data.date,
            'progress':data.progress,
            'description':data.description,
        }
        return JsonResponse(result)

    context = {'form': form}
    return render(request, "create_assignment.html", context)


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("study_tracker:show_tracker")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('study_tracker:login'))
    response.delete_cookie('last_login')
    return response