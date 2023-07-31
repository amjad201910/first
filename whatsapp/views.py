from django.shortcuts import render
from rest_framework import generics,viewsets,views
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import redirect
import base64
from core.models import User
from advertiser.models import advertisement, seen_advertisement
from .utils import CustomThread
from .models import chat
from rest_framework.reverse import reverse
from django.db import IntegrityError

import openai





def get_url_redirect(user,pku):
          try:
                
               seen_advertisement.objects.create(user=user, advertisement=advertisement(pk=pku))
          except IntegrityError:
                pass

      





# Create your views here.

class  redirectTO (views.APIView):


    def get(self, request, *args, **kwargs):
        pku=kwargs['pk']
        
      



        try:
            decoded_phone = base64.b64decode(kwargs['uuid'])
            decoded_phone = decoded_phone.decode('utf-8')
        except:
            return Response({"detail": "error"}, status=status.HTTP_400_BAD_REQUEST)
        user=User.objects.get(phone=decoded_phone)
        if user is None:
               return Response({"detail": "error in URL"}, status=status.HTTP_400_BAD_REQUEST)
        url=advertisement.objects.values('URL').filter(pk=pku).first()   
        if url is None:     
               return Response({"detail": "error in URL"}, status=status.HTTP_400_BAD_REQUEST)
     #    if not user.seen_advertisement_set.filter(advertisement=pku).exists():

        t10 = CustomThread(target=get_url_redirect, args=(user,pku,))     
        t10.start() 

             

  
        
     #    url=t10.join()
                

        # return redirect ("https://poe.com/ChatGPT")
        return Response ({"url": url,"p":decoded_phone})

def send_chatgpt(conv):
      response=openai.ChatCompletion.create(model="gpt-3.5-turbo",messages=conv)

      return response['choices'][0]['message']['content']


def minus_one_of_free_message(user):
     user.number_of_free_message=user.number_of_free_message-1
     user.use=True
     user.save()
      
     
def get_advertisement(country):
     #####################################active
     return advertisement.objects.values('pk','name','description','image').filter(country=country).order_by('?').first()
 
def get_chat(id):
      chats=[]
      all_chats=chat.objects.values('system_chat','user_chat').filter(user=id).order_by('-pk')[:3]#########
      for one_chat in all_chats:
            chats.append({"role":"user","content":one_chat['user_chat']})
            chats.append({"role":"assistant","content":one_chat['system_chat'].strip("\n").strip()})
      return chats
def save_chat(s,u,id):
     chat.objects.create(user_chat=s,system_chat=u,user=id)
class  chatSU (views.APIView):
        def post(self, request, *args, **kwargs):
                
                data = request.data
                userC=data['q']
                   
                try:
                    user=User.objects.get(phone=data['phone'])
                except:
                      user=User.objects.create(phone=data['phone'],is_active=False,group='user',use=True)#################number
                
                if user.active==True or user.number_of_free_message > 0:

                     t1 = CustomThread(target=get_chat, args=(user.pk,))     
                     t1.start()  
                     if user.active==False:
                            t2 = CustomThread(target=minus_one_of_free_message, args=(user,))     
                            t2.start()  
                            t3 =CustomThread(target=get_advertisement, args=(user.country,))     
                            t3.start() 
                          
                     
                     
                     conv=t1.join()
                     print("//////////////////////////////////////////////////////////////////////////")
                     print(conv)

                     conv.append({"role":"user","content":userC})
                     print("//////////////////////////////////////////////////////////////////////////")
                     print(conv)
                     t4=CustomThread(target=send_chatgpt, args=(conv,))     
                     t4.start() 
                          

                     






                     if user.active==False:

                            t2.join()
                            advertisement_data = t3.join()
                            print("////////////////////////////////////////////////////////")
                            try:
                                 
                                 seen_advertisement_bool=user.seen_advertisement_set.filter(advertisement=advertisement_data['pk']).exists()
                            except:
                                  seen_advertisement_bool=False 
                     

                     system= t4.join()
                     t5 =CustomThread(target=save_chat, args=(system,userC,user))     
                     t5.start() 
                     encoded_phone =base64.b64encode(user.phone.encode())
                     
                     
                  


                return Response({"q":system,"x":reverse('redirectTO', kwargs={"pk":advertisement_data['pk'],"uuid":encoded_phone.decode('utf-8')},request=request)})
                     

                          

                


            # t1 = threading.Thread(target=func1)
            # t2 = threading.Thread(target=func2)

            # # Start the threads
            # t1.start()
            # t2.start()

            # # Wait for both threads to finish
            # t1.join()
            # t2.join()

            
