from flask import Flask, request
app = Flask(__name__)

response = ""

@app.route('/', methods=['POST', 'GET'])
def ussd_callback():
  global response
  session_id = request.values.get("sessionId", None)
  service_code = request.values.get("serviceCode", None)
  phone_number = request.values.get("phoneNumber", None)
  text = request.values.get("text", "default")

  if text == ' ':
    response  = "CON What would you want to order \n"
    response += "1. Chips Plain @ Kshs.100 \n"
    response += "2. Soda 300ml @ kshs. 30 \n"
    response += "3. Soda 500ml @ Kshs. 40 \n"
    response += "4. Smokies @ kshs. 25 \n"
    response += "5. Chicken @ Kshs. 100 "

  if text != ' ':
    response = "CON Choose your location \n"
    response += "1.  Kiboswa \n"
    response += "2.  Dago \n"
    response += "3.  Nyangori \n"
    

  if text == '1':
     response = "End We have received your order and its being processed"
 
  if text == '2':
     response = "End We have received your order and its being processed"

  if text == '3':
     response = "End We have received your order and its being processed"

  return response 




