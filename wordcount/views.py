from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request, 'about.html')

def result(request): 
    text = request.GET['fulltext']
    words = text.split()
    words_dictionary = {}

    #단어 종류및 숫자 새기
    for word in words:
        if word in words_dictionary:
            #increase
            words_dictionary[word]+=1
        else :
            # add to dictionary
            words_dictionary[word] = 1

    return render(request, 'result.html', {'full':text, 'total' : len(words),'dictionary' : words_dictionary.items()})