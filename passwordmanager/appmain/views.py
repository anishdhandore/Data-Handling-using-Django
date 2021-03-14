from django.shortcuts import render, HttpResponse
from .models import Password

# Create your views here.
def home(request):
    return render(request, 'home.html')

def passwords(request):
    if request.method == "POST":
        account = request.POST.get('account')
        username = request.POST.get('username')
        passw = request.POST.get('password')

        password = Password(
            account=account,
            username=username,
            password=passw
        )
        password.save()

        # all_pass = Password.objects.all()
        accounts = Password.objects.values('account')
        usernames = Password.objects.values('username')
        passwords = Password.objects.values('password')

        acclist = [i['account'] for i in accounts]
        userlist = [i['username'] for i in usernames]
        passlist = [i['password'] for i in passwords]
        
        allpasslist = []
        # print(list1)
        for acc,users,pas in zip(acclist, userlist, passlist):
            allpasslist.append([acc,users,pas])

        print(allpasslist)

        parameters = {'all_pass': allpasslist}
        return render(request, 'passwords.html', context=parameters)

    else:
        accounts = Password.objects.values('account')
        usernames = Password.objects.values('username')
        passwords = Password.objects.values('password')

        acclist = [i['account'] for i in accounts]
        userlist = [i['username'] for i in usernames]
        passlist = [i['password'] for i in passwords]
        
        allpasslist = []
        # print(list1)
        for acc,users,pas in zip(acclist, userlist, passlist):
            allpasslist.append([acc,users,pas])

        print(allpasslist)

        parameters = {'all_pass': allpasslist}
        return render(request, 'passwords.html', context=parameters)