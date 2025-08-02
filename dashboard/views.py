from django.shortcuts import render,redirect
from login.models import Register

def dashboard(request):
    user_id = request.session.get('new_user')

    if not user_id:
        return redirect('login:login')  # Redirect back if no session

    user_data = Register.objects.get(id=user_id)

    return render(request, 'dashboard.html', {'user': user_data})

def leaderboard(request):
    return render(request, 'leaderboard.html')