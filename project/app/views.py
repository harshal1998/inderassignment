from django.shortcuts import render
from django.views.generic import TemplateView
import pandas as pd


class MainPage(TemplateView):
    template_name = 'home.html'


def mainpage(request):
    file = pd.read_excel("Data Records.xlsx")
    # print(file)
    return render(request, "display.html", {"string": file})


def output(request):
    file = pd.read_excel("Data Records.xlsx")
    # print(file)
    var1 = request.POST['dropdown1']
    # print(var1)
    var2 = request.POST['dropdown2']
    # print(var2)
    data1 = file[var1]
    print(data1)
    data2 = file[var2]
    # a= pd.pivot_table(file, index =['var1', 'var2'])
    return render(request, "output.html", {"data1": data1, "data2": data2, "var1": var1, "var2": var2})
