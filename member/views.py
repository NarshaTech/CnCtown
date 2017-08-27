from django.shortcuts import render

# Create your views here.
    if request.method == "POST":
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Login failed. Try again.')
            return HttpResponse("Login fail.")
    else:
        form = LoginForm()
        return render(request, 'login/login.html', {'form': form})