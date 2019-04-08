from django.shortcuts import render, get_object_or_404
# Create your views here.
from .models import Horse, Owner, Color, Lab, Genotype, CustomUser
from .forms import PostForm, OwnForm, GenForm, ColorForm, LabForm
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create your views here.
def post_list(request):
    posts = Horse.objects.all()

    return render(request, 'baback/post_list.html', {'posts': posts})

def color(request):
    color = Color.objects.all()
    return render(request, 'baback/color_list.html', {'color': color})

# def color(request):
#     color = Color.objects.all()
#     return render(request, 'baback/color_list.html', {'color': color})

def gen(request):
    gen = Genotype.objects.all()
    return render(request, 'baback/gen_list.html', {'gen': gen})
    
def lab(request):
    lab = Lab.objects.all()
    return render(request, 'baback/lab_list.html', {'lab': lab})

def owner(request):
    owners = Owner.objects.all()
    return render(request, 'baback/own_list.html', {'owners': owners})

def usr_list(request):
    users = User.objects.all()
    return render(request, 'baback/usr_list.html', {'users': users})


def post_detail(request, pk):
    post = get_object_or_404(Horse, pk=pk)
    return render(request, 'baback/post_detail.html', {'post':post})

def own_detail(request, pk):
    owner = get_object_or_404(Owner, pk=pk)
    return render(request, 'baback/own_detail.html', {'owner':owner})

def lab_detail(request, pk):
    lab = get_object_or_404(Lab, pk=pk)
    return render(request, 'baback/lab_detail.html', {'lab':lab})

def gen_detail(request, pk):
    gen = get_object_or_404(Genotype, pk=pk)
    return render(request, 'baback/gen_detail.html', {'gen':gen})

def color_detail(request, pk):
    color = get_object_or_404(Color, pk=pk)
    return render(request, 'baback/color_detail.html', {'color':color})


def post_new(request):
    name = 'New Horse'
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'baback/post_edit.html', {'form': form, 'name':name})

def own_new(request):
    name = "New Owner"
    if  (request.user.is_authenticated()) and ((request.user.customuser.usr) or (request.user.customuser.admin)):
        if request.method == "POST":
            form = OwnForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.save()
                return redirect('own_detail', pk=post.pk)
        else:
            form = OwnForm()
        return render(request, 'baback/post_edit.html', {'form': form, 'name':name})
    else:
        return render(request, 'baback/perm.html')

def gen_new(request):
    name = 'New Genotype'
    if  (request.user.is_authenticated()) and ((request.user.customuser.usr) or (request.user.customuser.admin)):
        if request.method == "POST":
            form = GenForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                #post.author = request.user
                post.save()
                return HttpResponseRedirect('/')
                #return redirect('own_detail', pk=post.pk)
        else:
            form = GenForm()
        return render(request, 'baback/post_edit.html', {'form': form, 'name':name})
    else:
        return render(request, 'baback/perm.html')

def color_new(request):
    name = 'New Color'
    if  (request.user.is_authenticated()) and ((request.user.customuser.usr) or (request.user.customuser.admin)):
        if request.method == "POST":
            form = ColorForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                #post.author = request.user
                post.save()
                return HttpResponseRedirect('/')
                #return redirect('own_detail', pk=post.pk)
        else:
            form = ColorForm()
        return render(request, 'baback/post_edit.html', {'form': form, 'name':name})
    else:
        return render(request, 'baback/perm.html')

def lab_new(request):
    name = 'New Lab'
    if (request.user.is_authenticated()) and ((request.user.customuser.usr) or (request.user.customuser.admin)):
        if request.method == "POST":
            form = LabForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                #post.author = request.user
                post.save()
                return HttpResponseRedirect('/')
                #return redirect('own_detail', pk=post.pk)
        else:
            form = LabForm()
        return render(request, 'baback/post_edit.html', {'form': form, 'name':name})
    else:
        return render(request, 'baback/perm.html')


def post_edit(request, pk):
    if (request.user.is_authenticated()) and ((request.user.customuser.usr) or (request.user.customuser.admin)):
        post = get_object_or_404(Horse, pk=pk)
        if request.method == "POST":
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                #post.author = request.user
                post.save()
                return redirect('post_detail', pk=post.pk)
        else:
            form = PostForm(instance=post)
        return render(request, 'baback/post_edit.html', {'form': form})
    else:
        return render(request, 'baback/perm.html')

def lab_edit(request, pk):
    if (request.user.is_authenticated()) and ((request.user.customuser.usr) or (request.user.customuser.admin)):
        post = get_object_or_404(Lab, pk=pk)
        if request.method == "POST":
            form = LabForm(request.POST, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                #post.author = request.user
                post.save()
                return redirect('lab_detail', pk=post.pk)
        else:
            form = LabForm(instance=post)
        return render(request, 'baback/post_edit.html', {'form': form})
    return render(request, 'baback/perm.html')

def owner_edit(request, pk):
    if  (request.user.is_authenticated()) and ((request.user.customuser.usr) or (request.user.customuser.admin)):
        post = get_object_or_404(Owner, pk=pk)
        if request.method == "POST":
            form = OwnForm(request.POST, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                #post.author = request.user
                post.save()
                return redirect('own_detail', pk=post.pk)
        else:
            form = OwnForm(instance=post)
        return render(request, 'baback/post_edit.html', {'form': form})
    return render(request, 'baback/perm.html')

def gen_edit(request, pk):
    if (request.user.is_authenticated()) and ((request.user.customuser.usr) or (request.user.customuser.admin)):
        post = get_object_or_404(Genotype, pk=pk)
        if request.method == "POST":
            form = GenForm(request.POST, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                #post.author = request.user
                post.save()
                return redirect('gen_detail', pk=post.pk)
        else:
            form = GenForm(instance=post)
        return render(request, 'baback/post_edit.html', {'form': form})
    return render(request, 'baback/perm.html')

def color_edit(request, pk):
    if  (request.user.is_authenticated()) and ((request.user.customuser.usr) or (request.user.customuser.admin)):
        post = get_object_or_404(Color, pk=pk)
        if request.method == "POST":
            form = ColorForm(request.POST, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                #post.author = request.user
                post.save()
                return redirect('color_detail', pk=post.pk)
        else:
            form = ColorForm(instance=post)
        return render(request, 'baback/post_edit.html', {'form': form})
    return render(request, 'baback/perm.html')


def post_delete(request, pk):
    if request.user.is_authenticated() and request.user.customuser.admin:
        post = get_object_or_404(Horse, pk=pk)
        try:
            post.delete()
            return HttpResponseRedirect("/")
        except Horse.DoesNotExist:
            return HttpResponseNotFound("<h2>Not found</h2>")
    return render(request, 'baback/perm.html')

def own_delete(request, pk):
    if request.user.is_authenticated() and request.user.customuser.admin:
        post = get_object_or_404(Owner, pk=pk)
        try:
            post.delete()
            return HttpResponseRedirect("/")
        except Owner.DoesNotExist:
            return HttpResponseNotFound("<h2>Not found</h2>")
    return render(request, 'baback/perm.html')

def gen_delete(request, pk):
    if request.user.is_authenticated() and request.user.customuser.admin:
        post = get_object_or_404(Genotype, pk=pk)
        try:
            post.delete()
            return HttpResponseRedirect("/")
        except Genotype.DoesNotExist:
            return HttpResponseNotFound("<h2>Not found</h2>")
    return render(request, 'baback/perm.html')

def color_delete(request, pk):
    if request.user.is_authenticated() and request.user.customuser.admin:
        post = get_object_or_404(Color, pk=pk)
        try:
            post.delete()
            return HttpResponseRedirect("/")
        except Color.DoesNotExist:
            return HttpResponseNotFound("<h2>Not found</h2>")
    return render(request, 'baback/perm.html')

def lab_delete(request, pk):
    if request.user.is_authenticated() and request.user.customuser.admin:
        post = get_object_or_404(Lab, pk=pk)
        try:
            post.delete()
            return HttpResponseRedirect("/")
        except Lab.DoesNotExist:
            return HttpResponseNotFound("<h2>Not found</h2>")
    return render(request, 'baback/perm.html')

# def perm(request):
#     return render(request, 'baback/perm.html')
