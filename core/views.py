# Import necessary modules and functions for handling user authentication
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as app_login, logout as app_logout
from django.contrib import messages

# View function for rendering the login page
def login(request):
    # Return the rendered login.html template
    return render(request, "login.html")

# View function for processing user login submission
def submit_login(request):
    # Check if the request method is POST
    if request.POST:
        # Assign the submitted username and password to variables
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate the user with the provided username and password
        user = authenticate(username=username, password=password)

        # If the user exists, log them in and redirect to the index page
        if user:
            app_login(request, user)
            return redirect("index")
        # If the user doesn't exist, display an error message and redirect to the login page
        else:
            messages.error(request, 'Usuário ou senha inválidos. Por favor tente novamente')

    # If the request method is not POST, redirect to the login page
    return redirect("login")

# View function for logging out the user and redirecting to the login page
def logout(request):
    # Log out the user
    app_logout(request)
    # Redirect to the login page
    return redirect('login')