from django.shortcuts import render , redirect
from django.contrib import messages
from User.forms import UserRegisterForm
from User.models import UserRegister
from django.core.files.storage import FileSystemStorage
from django.conf import settings

# Create your views here.
def base(request):
    return render(request , 'base.html')

def index(request):
    return render(request , "index.html")

def userlogin(request):
    if request.method=='POST':
        username = request.POST.get("username")
        password = request.POST.get('password')
        print(username , password)
        try:
            check = UserRegister.objects.get(User_Name=username , Pass_Word=password)
            status = check.Status
            if status=='activated' or status=='Activated': 
                return redirect('UserHome')
            
            else:
                print("Something problem is there")
                messages.success(request , 'You are not Activated')
        except Exception as e:
            messages.success(request , e)
            
    return render(request , 'userlogin.html')


def Registration(request):
    if request.method=='POST':
        name=request.POST.get('name')
        username=request.POST.get('username')
        password = request.POST.get("password")
        mobile  = request.POST.get('phon')
        mail = request.POST.get('mail')
        locality = request.POST.get('locality')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        status = request.POST.get("status")
        
        print(name , username,password , mobile, mail, locality, address , city , state , status)
        try:
            
            if name and username and password and mobile and mail and locality and address and city and state and status:
                    data  = UserRegister.objects.create(Name= name , User_Name=username , Pass_Word=password ,
                                                        Mobile_No=mobile , Mail_Id= mail , Locality=locality, Address=address , 
                                                            City=city , State=state , Status=status)
                    data.save()
                    messages.success(request , 'You Are Sucessfully Registered')    
            else:
                messages.warning(request , 'Something went Wrong! --Check It Once---')
        except:
            print("Some")
            
     
    
    return render(request , 'Register.html' )



def UserHome(request):
    return render(request , 'User/Userhome.html')



def stream(request):
    import subprocess
    try:
        
         command = ["python", "User/yolo/v8/detect/detect_and_trk.py", "model=yolov8m.pt", "source=0", "show=True"]
         result = subprocess.run(command, capture_output=True, text=True, check=True)
         return result
    except Exception as e:
        print(e) 

    return render(request , 'User/Userhome.html')




# from django.shortcuts import render
# from django.http import HttpResponse
# import subprocess
# import logging

# # Set up logging
# # logger = logging.getLogger(__name__)

# def stream(request):
#     # Define the command and arguments
#     command = ["python", "User/yolo/v8/detect/detect_and_trk.py", "model=yolov8m.pt", "source=0", "show=True"]

#     try:
#         # Run the command
#         result = subprocess.run(command, capture_output=True, text=True, check=True)

#         # Log the standard output
#         # logger.info(f"Command output: {result.stdout}")

#         # Return the output as an HTTP response
#         return HttpResponse(f"Command output: {result.stdout}")

#     except subprocess.CalledProcessError as e:
#         # Log the error details
#         # logger.error(f"Command failed with error: {e.stderr}")

#         # Return the error message as an HTTP response
#         return HttpResponse(f"Command failed with error: {e.stderr}", status=500)

#     except Exception as e:
#         pass
#         # Log unexpected errors
#         # logger.exception("An unexpected error occurred")

#         # Return the error message as an HTTP response
#         # return HttpResponse(f"An unexpected error occurred: {str(e)}", status=500)

#     # Render the template if the command fails
#     return render(request, 'User/Userhome.html')


# def UploadVideo(request):
#     if request.method=='POST':
#         file = request.FILES.get('file')
#         if file:
#             fs=FileSystemStorage(settings.MEIDA_ROOT)
#             file =fs.save(file.name , file)
#             fileurl = fs.url(file)
#             print(fileurl)
#             command = ["python" "User/yolo/v8/detect/detect_and_trk.py model=yolov8s.pt source='fileurl' show=True"]
#             result = subprocess.run(command, text=True, check=True)
#             return HttpResponse(f"Command output: {result.stdout}")
        # print(file)
    # return render(request , 'User/video.html')
        
    #  command = ["python" 'User\yolo\v8\detect\detect_and_trk.py model=yolov8s.pt source="test.mp4" show=True']
    #  try:
    #     # Run the command
    #     result = subprocess.run(command, capture_output=True, text=True, check=True)
    #     return HttpResponse(f"Command output: {result.stdout}")
    #  except Exception as e:
      

     


import subprocess
def UploadVideo(request):
    if request.method == 'POST':
        file = request.FILES.get('file')
        if file:
            fs = FileSystemStorage(location=settings.MEDIA_ROOT)
            filename = fs.save(file.name, file)
            fileurl = fs.url(filename)
            file_path = fs.path(filename)

            print(fileurl)  # For debugging purposes

            # Ensure the command is correctly formatted and separated
            command = ["python", "User/yolo/v8/detect/detect_and_trk.py", f"model=yolov8s.pt", f"source={file_path}", "show=True"]
            
            try:
                result = subprocess.run(command, capture_output=True, text=True, check=True)
                return HttpResponse(f"Command output: {result.stdout}")
            except subprocess.CalledProcessError as e:
                return HttpResponse(f"Command failed with error: {e.stderr}", status=500)
            except Exception as e:
                return HttpResponse(f"An unexpected error occurred: {str(e)}", status=500)

    return render(request, 'User/video.html')