from pkg_resources import ensure_directory


a="I am Akirachix"
b=a.split()
start=0
end=len(b)-1
while start<end:
    b[start],b[end]=b[end],b[start]
    start+=1
    end-=1
    str=" "
print(str.join(b))

def name(x):
    z=x.split()
    start=0
    end=len(z)-1
    while start<end:
       z[start],z[end]=z[end],z[start]
    start+=1
    end-=1
    str=""
    w=(str.join(z))
    if(w==x):
        print("its a palindrome")
    else:
        print("its not a palindrome")
name=("malayami mum")


    







       
       
    
      
    


