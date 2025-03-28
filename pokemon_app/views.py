from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.http import JsonResponse
from .models import User, City  # только те модели, которые реально существуют
from .forms import RegistrationForm, ApplicationForm
from django.shortcuts import render

def fullpage_view(request):
    return render(request, 'pokemon_app/fullpage.html')

def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('user_profile', user_id=user.id)
    else:
        form = RegistrationForm()

    cities = City.objects.all()
    pokemon_types = PokemonType.objects.all()
    return render(request, 'register.html', {
        'form': form,
        'cities': cities,
        'pokemon_types': pokemon_types
    })


@login_required
def user_profile(request, user_id):
    user = get_object_or_404(User, id=user_id)
    applications = Application.objects.filter(user=user).order_by('-created_at')
    return render(request, 'user_profile.html', {
        'user': user,
        'applications': applications
    })


@login_required
def create_application(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.user = request.user
            application.save()

            for file in request.FILES.getlist('files'):
                ApplicationFile.objects.create(application=application, file=file)

            return redirect('user_profile', user_id=request.user.id)
    return redirect('user_profile', user_id=request.user.id)


@login_required
def submit_application(request, app_id):
    if request.method == 'POST':
        application = get_object_or_404(Application, id=app_id, user=request.user)
        application.status = 'submitted'
        application.save()
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'}, status=400)


def subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        phone = request.POST.get('phone')

        # Update user if authenticated
        if request.user.is_authenticated:
            if email and not request.user.email:
                request.user.email = email
            if phone and not request.user.phone:
                request.user.phone = phone
            request.user.save()

        # Create subscription
        Subscription.objects.create(email=email, phone=phone)

        return JsonResponse({'status': 'success'})

    return JsonResponse({'status': 'error'}, status=400)