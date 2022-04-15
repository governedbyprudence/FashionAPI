import random
from .models import fashion
from django.db.models import Q
def apt_query(data):
    queryset=[]
    try:        
        if "random" in data:
            l=len(fashion.objects.all())
            queryset=fashion.objects.get(id=random.randint(1,l))
        elif "type" in data and "gender" in data and "place" in data and "shirt_color" in data:
            queryset=fashion.objects.filter(type=data["type"],place__contains=data["place"],shirt_color=data["shirt_color"]).filter(Q(gender=data["gender"]) | Q(gender="unisex"))
        elif "type" in data and "gender" in data and "place"in data and "shirt_type" in data:
            queryset=fashion.objects.filter(type=data["type"],place__contains=data["place"],shirt_type=["shirt_type"]).filter(Q(gender=data["gender"]) | Q(gender="unisex"))
        elif "type" in data and "gender" in data and "place"in data and "pant_color" in data:
            queryset=fashion.objects.filter(type=data["type"],place__contains=data["place"],pant_color=data["pant_color"]).filter(Q(gender=data["gender"]) | Q(gender="unisex"))
        elif "type" in data and "gender" in data and "place"in data and "pant_type" in data:
            queryset=fashion.objects.filter(type=data["type"],place__contains=data["place"],pant_type=["pant_type"]).filter(Q(gender=data["gender"]) | Q(gender="unisex"))
        elif "type" in data and "gender" in data and "place"in data and "shirt_color"in data and "shirt_type" in data:
            queryset=fashion.objects.filter(type=data["type"],place__contains=data["place"],shirt_color=data["shirt_color"],shirt_type=["shirt_type"]).filter(Q(gender=data["gender"]) | Q(gender="unisex"))
        elif "type" in data and "gender" in data and "place"in data and "pant_color"in data and "pant_type" in data:
            queryset=fashion.objects.filter(type=data["type"],place__contains=data["place"],pant_color=data["pant_color"],pant_type=["pant_type"]).filter(Q(gender=data["gender"]) | Q(gender="unisex"))
        elif "type"  in data and "place" in data and "shirt_color"in data and "shirt_type" in data:
            queryset=fashion.objects.filter(type=data["type"],place__contains=data["place"],shirt_color=data["shirt_color"],shirt_type=["shirt_type"])
        elif "type" in data and  "place" in data and "pant_color"in data and "pant_type" in data:
            queryset=fashion.objects.filter(type=data["type"],place__contains=data["place"],pant_color=data["shirt_color"],pant_type=["shirt_type"])
        elif "type" in data and  "gender" in data and "shirt_color"in data and "shirt_type" in data:
            queryset=fashion.objects.filter(type=data["type"],shirt_color=data["shirt_color"],shirt_type=["shirt_type"]).filter(Q(gender=data["gender"]) | Q(gender="unisex"))
        elif "type" in data and  "gender"in data and "pant_color"in data and "pant_type" in data:
            queryset=fashion.objects.filter(type=data["type"],pant_color=data["pant_color"],pant_type=["pant_type"]).filter(Q(gender=data["gender"]) | Q(gender="unisex"))
        elif "type"  in data and "place" in data and "shirt_color"  in data:
            queryset=fashion.objects.filter(type=data["type"],place__contains=data["place"],shirt_color=data["shirt_color"])
        elif "type"  in data and "place"in data and "shirt_type"  in data:
            queryset=fashion.objects.filter(type=data["type"],place__contains=data["place"],shirt_type=["shirt_type"])
        elif "type"  in data and  "place"in data and "pant_color"  in data:
            queryset=fashion.objects.filter(type=data["type"],place__contains=data["place"],pant_color=data["pant_color"])
        elif "type" in data and  "place" in data and "pant_type" in data:
            queryset=fashion.objects.filter(type=data["type"],place__contains=data["place"],pant_type=["pant_type"])
        elif "type"  in data and  "gender" in data and "shirt_color"  in data:
            queryset=fashion.objects.filter(type=data["type"],shirt_color=data["shirt_color"]).filter(Q(gender=data["gender"]) | Q(gender="unisex"))  
        elif "type"  in data and "gender" in data and "shirt_type" in data:
            queryset=fashion.objects.filter(type=data["type"],shirt_type=["shirt_type"]).filter(Q(gender=data["gender"]) | Q(gender="unisex"))
        elif "type"  in data and  "gender" in data and "pant_color"  in data:
            queryset=fashion.objects.filter(type=data["type"],place__contains=data["place"],pant_color=data["pant_color"]).filter(Q(gender=data["gender"]) | Q(gender="unisex"))
        elif "type" in data and  "gender" in data and "pant_type" in data:
            queryset=fashion.objects.filter(type=data["type"],pant_type=["pant_type"]).filter(Q(gender=data["gender"]) | Q(gender="unisex"))
        elif "type" in data and "gender"in data and "place" in data:
            queryset=fashion.objects.filter(type=data["type"],place__contains=data["place"]).filter(Q(gender=data["gender"]) | Q(gender="unisex"))
        elif "type" in data and  "place"  in data:
            queryset=fashion.objects.filter(type=data["type"],place__contains=data["place"])
        elif "type" in data and  "gender" in data:
            queryset=fashion.objects.filter(type=data["type"]).filter(Q(gender=data["gender"]) | Q(gender="unisex"))
        elif "gender" in data and  "place" in data:
            queryset=fashion.objects.filter(type=data["type"]).filter(Q(gender=data["gender"]) | Q(gender="unisex"))
        elif "shirt_color"in data and "shirt_type" in data:
            queryset=fashion.objects.filter(shirt_color=data["shirt_color"],shirt_type=data["shirt_type"])
        elif "pant_color"in data and "pant_type" in data:
            queryset=fashion.objects.filter(pant_color=data["pant_color"],pant_type=data["pant_type"])  
        elif "type" in data:
            print("in type")
            queryset=fashion.objects.filter(type=data["type"])
        elif "place" in data:
            queryset=fashion.objects.filter(place__contains=data["place"])
        elif "gender" in data:
            queryset=fashion.objects.filter(Q(gender=data["gender"]) | Q(gender="unisex"))
        elif "shirt_color"in data:
            queryset=fashion.objects.filter(shirt_color=data["shirt_color"])
        elif "shirt_type" in data:
            queryset=fashion.objects.filter(shirt_type=data["shirt_type"])
        elif "pant_color"in data:
            queryset=fashion.objects.filter(pant_color=data["pant_color"])
        elif "pant_type" in data:
            queryset=fashion.objects.filter(pant_type=data["pant_type"])
        elif "accessories"  in data:
            queryset=fashion.objects.filter(accessories__contains=data["accessories"])
    except fashion.DoesNotExist:
        return ([],"Does not Exist")    
    return (queryset,"Found")