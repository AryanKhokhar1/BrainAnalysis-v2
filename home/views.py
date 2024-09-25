from .models import Question
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect
# from .utils import savetoserver  
# # Import the function if it's in a different module

def home(request):
    return render(request, "index.html")


def registerpage(request):

    if request.method == "POST" :
        firtsname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
    
        if User.objects.filter(username = username).exists():
            messages.error(request,"User already exist")
            return redirect(login_view)
        else:
            user = User.objects.create_user(username=username,email=email,password=password)
            user.first_name = firtsname
            user.last_name = lastname
            user.save()
            messages.success(request,"Account created Successfully . Now You can login")
            return redirect(login_view)
    else:
        return render(request,"register.html")


def login_view(request):
    if request.method == 'POST':
        # Handle the POST request when user submits the form
        emailid = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']

        print(emailid, len(emailid))
        print(username, len(username))
        print(password, len(password))
        try:
            user = User.objects.get(email = emailid, username = username)
        except:
            return render(request, 'login.html', {'error': 'email or Username is invalid'})
        
        user = authenticate(request, username=username, password=password)
        # print(user.is_authenticated)

        print(emailid, len(emailid))
        print(username, len(username))
        print(password, len(password))
    
        if user is not None:
            login(request, user)  # This will initialize the session
            print("Login Done")
            return redirect('home')  # Redirect to the home page
        else:
            # If login fails, re-render the login page with an error message
            return render(request, 'login.html', {'error': 'Invalid login'})
    else:
        # If request is GET, display the login form
        return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect(home)

def test(request):
    if 'n' not in request.session:
            request.session['n'] = 1
            request.session['optionvalue'] = dict()

    if request.method == "POST":
        request.session["optionvalue"][request.session['n']-1] = int(request.POST['option'])
        request.session.modified = True
        # get_data(request)

        if 'option' in request.POST:
            if(request.session['n'] < 10):
                request.session['n'] += 1
                # request.session['p'] = 1
                data = Question.objects.filter(question_number = request.session['n']).values('question_text').first() #1
                print(request.POST['option'])
                return render(request,"questions.html",context={"data": data, "question_number":request.session['n']})
            else:                
                messages.success(request,"Test Completed")
                return redirect(result_view)
            
        else:
            print("Select a option")
            data = Question.objects.filter(question_number = request.session['n']).values('question_text').first() #1
            return render(request,"questions.html",context={"data": data, "question_number":request.session['n'], 'instruction':"Select a Option"})

    else:
        # request.session['n'] += 1
        data = Question.objects.filter(question_number = request.session['n']).values('question_text').first()
        return render(request,"questions.html",context={"data": data, "question_number":request.session['n']})



def prev_question(request):
    
    if 'n' in request.session:
        print(True)
        request.session['n'] -= 1
        data = Question.objects.filter(question_number = request.session['n']).values('question_text').first() #1
        return render(request,"questions.html",context={"data": data, "question_number":request.session['n']})
    else:
        print(False)
        return redirect(test)

# def get_data(request):
#     print(request.session['optionvalue'])

def result_view(request):
    # O C E A N
    My_ans = [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
    
    all_question = Question.objects.filter(question_number__in = range(121)).values_list()
    print(all_question)
    for x in range(10):
        question = all_question[x]
        if(question[4] == 'O'):
            if(question[3] == "minus"):
                My_ans[0][question[5]-1] = (6 - (request.session["optionvalue"][str(x)])) + My_ans[3][question[5]-1]
            else:
                My_ans[0][question[5]-1] = request.session["optionvalue"][str(x)] + My_ans[3][question[5]-1]

        elif(question[4] == 'C'):
            if(question[3] == "minus"):
                My_ans[1][question[5]-1] = (6 - (request.session["optionvalue"][str(x)])) + My_ans[3][question[5]-1]
            else:
                My_ans[1][question[5]-1] = request.session["optionvalue"][str(x)] + My_ans[3][question[5]-1]
        elif(question[4] == 'E'):
            if(question[3] == "minus"):
                My_ans[2][question[5]-1] = (6 - int(request.session["optionvalue"][str(x)])) + My_ans[3][question[5]-1]
            else:
                My_ans[2][question[5]-1] = request.session["optionvalue"][str(x)] + My_ans[2][question[5]-1]
        elif(question[4] == 'A'):
            if(question[3] == "minus"):
                My_ans[3][question[5]-1] = (6 - int(request.session["optionvalue"][str(x)])) + My_ans[3][question[5]-1]
            else:
                My_ans[3][question[5]-1] = request.session["optionvalue"][str(x)] + My_ans[3][question[5]-1]
        elif(question[4] == 'N'):
            if(question[3] == "minus"):
                My_ans[4][question[5]-1] = (6 -  int(request.session["optionvalue"][str(x)])) + My_ans[4][question[5]-1]
            else:
                My_ans[4][question[5]-1] = request.session["optionvalue"][str(x)] + My_ans[4][question[5]-1]
        # print(question[0]," Selected Option: ",request.session["optionvalue"][str(x)])
    # return render(request,"result.html",context={"data":request.session["optionvalue"]})
        print(My_ans)

    ocean = []
    tsum = 0
    for x in My_ans:
        tsum = 0
        for ele in x:
            tsum += ele
        ocean.append(tsum/6)
    return render(request,"result.html",context={"ocean":ocean,"o":My_ans[0],"c":My_ans[1],"e":My_ans[2], "a":My_ans[3], "n":My_ans[4]})














# def ask_Question(request):
#     data = Question.objects.filter(question_number = 1).values('question_text').first()
#     print(data)
#     return render(request, "questions.html",context={"data": data})



















# def save_question(request):
#     savetoserver()
#     return HttpResponse("Questions have been saved.")


# import os
# import json
# from .models import Question

# def savetoserver():
#     # Get the directory where the current script is located
#     base_dir = os.path.dirname(os.path.abspath(__file__))
#     # Construct the full path to the JSON file
#     file_path = os.path.join(base_dir, 'questions.json')

#     try:
#         with open(file_path, 'r') as file:
#             data = json.load(file)
#             print(data[0].get("id")) 

#             for x in range(len(data)):
#                 question = Question()
#                 question.question_number = x + 1
#                 question.question_id = data[x].get("id")
#                 question.question_text = data[x].get("text")
#                 question.keyed = data[x].get("keyed")
#                 question.domain = data[x].get("domain")
#                 question.facet = (data[x].get("facet"))

#                 question.save()

#     except FileNotFoundError:
#         print(f'File not found: {file_path}')
