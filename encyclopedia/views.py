from django.shortcuts import render
from django.http import HttpResponseRedirect as redirect
from django import forms
from markdown2 import Markdown
from . import util
from random import randint

class NewPage(forms.Form):
    title = forms.CharField(label="Title", 
    widget=forms.TextInput(attrs={'placeholder': 'Insert Title...'}))
    content = forms.CharField(label="Content", 
    widget=forms.Textarea(attrs={'placeholder': 'Insert content using Markdown...',"style":"height:400px"}))


def index(request, boolean=None):

    entries = util.list_entries()

    if boolean=="True": 

        index = randint(0, len(entries)-1)
        title = entries[index]
        return redirect(f"/wiki/{title}")

    else: 
        
        return render(request, "encyclopedia/index.html", {
            "entries": entries
        })

def entry(request,title):

    #no idea why I can't write CSS in the search box without it automaticaly converting it into css
    if title == "css":
        title = "CSS"

    content = util.get_entry(title)

    if content: context = {"content":Markdown().convert(content), "title":title}

    else: context = {"content":None}

    return render(request, "encyclopedia/entry.html",context)

def search(request):

    #q is the value and '' default in case None
    to_search = request.GET.get('q','')
    results = []

    #prevents search if empty
    if to_search=="": return index(request)

    for i in util.list_entries():
        i = i.lower()
        if i.find(to_search)>=0: results.append(i)

    #if no results you get a 404 if just one result, you get the page if 1+ you get the list

    if len(results)<1: return entry(request, to_search)
    if len(results)==1: return entry(request, results[0])
    if len(results)>1: return render(request, "encyclopedia/index.html", {"results":results})

def addPage(request):
    if request.method=="POST": 

        form = NewPage(request.POST)
        if form.is_valid():

            if not util.get_entry(form.cleaned_data["title"]):
                util.save_entry(form.cleaned_data["title"].title(), 
                                form.cleaned_data["content"])
                return redirect(f"/wiki/{form.cleaned_data['title']}")

            else:
                return render(request, "encyclopedia/newpage.html", {"form":form, "error":True})

        else:
            return render(request, "encyclopedia/newpage.html", {"form":form})


    return render(request, "encyclopedia/newpage.html", {"form":NewPage()})

def editPage(request,title):

    #los \r me estaban agregando nueva linea por alguna razon
    content = {"title":title,"content":util.get_entry(title).replace("\r","")}
    context = {"form":NewPage(content),"title":title}


    if request.method=="POST":
        form = NewPage({"title":title,"content":request.POST["content"]})

        if form.is_valid():

            util.save_entry(form.cleaned_data["title"], form.cleaned_data["content"])
            return redirect(f"/wiki/{title}")

        else:
            return render(request, "encyclopedia/editpage.html",{"form":form,"title":title})



    return render(request, "encyclopedia/editpage.html",context)

