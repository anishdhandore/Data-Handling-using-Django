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

        list1 = [i['account'] for i in accounts]
        list2 = [i['username'] for i in usernames]
        list3 = [i['password'] for i in passwords]
        
        emptylist = []
        # print(list1)
        for x,y,z in zip(list1, list2, list3):
            emptylist.append([x,y,z])

        print(emptylist)

        parameters = {'all_pass': emptylist}
        password == None
        return render(request, 'passwords.html', context=parameters)

    else:
        accounts = Password.objects.values('account')
        usernames = Password.objects.values('username')
        passwords = Password.objects.values('password')

        list1 = [i['account'] for i in accounts]
        list2 = [i['username'] for i in usernames]
        list3 = [i['password'] for i in passwords]
        
        emptylist = []
        # print(list1)
        for x,y,z in zip(list1, list2, list3):
            emptylist.append([x,y,z])

        print(emptylist)

        parameters = {'all_pass': emptylist}
        return render(request, 'passwords.html', context=parameters)