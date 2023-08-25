from models import *

response = ""
data = []


@app.route('/', methods=['POST', 'GET'])
def ussd_callback():
  global response
  session_id = request.values.get("sessionId", None)
  service_code = request.values.get("serviceCode", None)
  phone_number = request.values.get("phoneNumber", None)
  text = request.values.get("text", "default")
  
  if text == '':
     response  = "CON What would you want to order \n"
     response += "1. Chips Plain @ Kshs.100 \n"
     response += "2. Soda 300ml @ kshs. 30 \n"
     response += "3. Soda 500ml @ Kshs. 40 \n"
     response += "4. Smokies @ kshs. 25 \n"
     response += "5. Chicken @ Kshs. 100 "
     



  elif text == '1':
     response = "CON Choose your location \n"
     response += "1.  Kiboswa \n"
     response += "2.  Dago \n"
     response += "3.  Nyangori \n"
     response += "4.  Kapko \n"
     response += "5.  Riat "
   
  
  elif text == '2':
     response = "CON Choose your location \n"
     response += "1.  Kiboswa \n"
     response += "2.  Dago \n"
     response += "3.  Nyangori \n"
     response += "4.  Kapko \n"
     response += "5.  Riat "
     
     
  elif text == '3':
     response = "CON Choose your location \n"
     response += "1.  Kiboswa \n"
     response += "2.  Dago \n"
     response += "3.  Nyangori \n"
     response += "4.  Kapko \n"
     response += "5.  Riat "
  
  elif text == '4':
     response = "CON Choose your location \n"
     response += "1.  Kiboswa \n"
     response += "2.  Dago \n"
     response += "3.  Nyangori \n"
     response += "4.  Kapko \n"
     response += "5.  Riat "

  elif text == '5':
     response = "CON Choose your location \n"
     response += "1.  Kiboswa \n"
     response += "2.  Dago \n"
     response += "3.  Nyangori \n"
     response += "4.  Kapko \n"
     response += "5.  Riat \n"

  elif text == '1*1':
     response = "CON How can we reach you \n"
     response += "type your phone number \n"
     data.append(text)
  
  elif '1*1*07' in text:
    content = Response("Chips Plain @ Kshs.100", "Kiboswa", text[4:13])
    response = "END Thank you for your order"

  return response
  

 
if __name__ == '__main__':
    app.run()

