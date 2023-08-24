import os
import json
from flask import Flask, request, jsonify
from models import *
from db import app
from models import Response, OrderOptions


# app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])

response = ""
data = []


@app.route('/', methods=['POST', 'GET'])
def ussd_callback():
  global response
  session_id = request.values.get("sessionId", None)
  service_code = request.values.get("serviceCode", None)
  phone_number = request.values.get("phoneNumber", None)
  text = request.values.get("text", "default")

  orders = OrderOptions.query.all()
  
  if text == '':
     response  = "CON What would you want to order \n"
     for order in orders:
      response += f"{order.id}. {order.name} @ Kshs.{order.price} \n"
      # response += "2. Soda 300ml @ kshs. 30 \n"
      # response += "3. Soda 500ml @ Kshs. 40 \n"
      # response += "4. Smokies @ kshs. 25 \n"
      # response += "5. Chicken @ Kshs. 100 "
      



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
     response += "CON type your phone number \n"

     
  
  elif '1*1*07' in text:
    number = text[4:-1]
    phone = number
    order = text[0]
    location = text[2]
    data = Response(order=order, location=location, phone=phone)
    db.session.add(data)
    db.session.commit()
    response = "END Thank you for your order, we will be reaching you on: "+ number 

  return response

if __name__ == '__main__':
    app.run()

@app.route('/response', methods=['POST'])
def create_response():
   try:
      data = request.get_json()
   
      name = data.get('name')
      price = data.get('price')
      
      data = OrderOptions(name=name, price=price)
      db.session.add(data)
      db.session.commit()
      
      response_data = {
         "message": "Data submitted successfully",
         "name": name,
         "price": price
      }
      return jsonify(response_data), 200
   
   except json.JSONDecodeError:
      # Handle JSON parsing errors
      return jsonify({"error": "Invalid JSON data"}), 400

@app.route('/fetch-orders', methods=['GET'])
def Fetch_response():
   try:
      responses  = Response.query.all()
      response_list = []
      for response in responses:
         vals = {
            "id": response.id,
            "order": response.order,
            "location": response.location,
            "phone": response.phone, 
         }
         response_list.append(vals)
      return jsonify(response_list)
   
   except json.JSONDecodeError:
      # Handle JSON parsing errors
      return jsonify({"error": "Invalid JSON data"}), 400
   









