from pkg_resources import ensure_directory


a="I am a student at Akirachix persuing software development "
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
    start=0
    end=len(x)-1
    while start<end:
        if x[start]!=x[end]:
            print("its not a palindrome")
            break
        else:
            start+=1
            end-=1
            print("its a palindrome")    
name("civic")   
 


    







       
       
    
      
    


