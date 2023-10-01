import pickle
#from models import Origin,Proverb,OriginConnection
import os
import django
import sys

#create_proverbs(proverbs,origin=origin)
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir=os.path.dirname(current_dir)
sys.path.append(parent_dir)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sortit.settings')  # Replace 'myproject.settings' with your project's settings module
django.setup()

from proverbs.models import Origin,Proverb,OriginConnection

#os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sortit.settings')  # Replace 'myproject.settings' with your project's settings module
#django.setup()


file=r"D:\Dev\pdfs\amish.pickle"

origin="amish"

tags=[]

def load_proverbs(file):
    """importing proverbs texts from a pickle file"""
    with open(file, 'rb') as f:
        proverbs = pickle.load(f)
    return proverbs

def create_proverb(proverb_text):
    """create raw Proverb instances without origin and tag"""
    proverb=Proverb(text=proverb_text)

def check_origin(origin):
    if origin:
        if not  Origin.objects.filter(cathegory=origin).count():
            o=Origin(cathegory=origin)
            o.save()
            return o
        else:
            return Origin.objects.filter(cathegory=origin)[0]
    return None

def create_proverbs(proverbs,origin=None):
    raw_proverbs=[Proverb(text=text) for text in proverbs ]
    saving_proverbs=[proverb.save() for proverb in raw_proverbs]

    if origin:
        o=check_origin(origin)
        raw_connections=[OriginConnection(proverb=proverb,origin=o) for proverb in raw_proverbs]
        saving_connections=[connection.save() for connection in raw_connections]

if __name__ == "__main__":
    proverbs=set(load_proverbs(file))
    #create_proverbs(proverbs,origin=origin)
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir=os.path.dirname(current_dir)
    #print(parent_dir)
    sys.path.append(parent_dir)
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sortit.settings')  # Replace 'myproject.settings' with your project's settings module
    django.setup()
    create_proverbs(proverbs,origin=origin)

    
    

    
    


    