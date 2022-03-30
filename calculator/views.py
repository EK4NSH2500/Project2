from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "calculator.html")

def index1(request):
    return render(request, "air.html")

def index2(request):
    return render(request, "water.html")

def index3(request):
    return render(request, "solids.html")

def calculateair(request):
    t = float(request.GET['time'])
    veltime = 340*t
    dst = veltime/2

    if dst<=16.5:
        dst = "The Distance is too Low to Produce an Echo"
    
    
            
        

    return render(request, "result.html", {'result':dst})


def calculatewater(request):
    t = float(request.GET['time'])
    veltime1 = 1480*t
    dst1 = veltime1/2

    if dst1<=16.5:
        dst1 = "The Distance is too Low to Produce an Echo"
    
    
            
        

    return render(request, "waterresult.html", {'result1':dst1})


def calculatesolid(request):
    t = float(request.GET['time'])
    veltime2 = 6000*t
    dst2 = veltime2/2

    if dst2<=16.5:
        dst2 = "The Distance is too Low to Produce an Echo"
    
    
            
        

    return render(request, "solidresult.html", {'result2':dst2})

    