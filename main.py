# TO CONFIGURE:
# UPLOAD A IMAGE TO USE AS A FAVICON INTO THE 'TEMPLATES' FOLDER
# THEN RENAME IT TO 'favicon.png'
# IT WILL AUTOMATICALLY BE SET AS THE FAVICON
# GOTO ALL OF THE HTML DOCUMENTS IN THE 'TEMPLATES' FOLDER AND EDIT THE TEXT.
# TELL PEOPLE ABOUT YOUR SITE!
# !!! UNTIL YOU UPLOAD A FAVICON YOU WILL GET AN ERROR IN THE CONSOLE !!!

from flask import Flask, render_template, send_file, flash, request, url_for, flash, redirect
#from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField

import os

#from firebase import firebase
import pyrebase
import json
from collections import OrderedDict

from datetime import datetime

firebaseConfig = {
    "apiKey": "AIzaSyCXSRxt4I_C7ctLuUSlgupU_Ufrdap9VyQ",
    "authDomain": "leavingcertproject-23455.firebaseapp.com",
    "databaseURL":
    "https://leavingcertproject-23455-default-rtdb.europe-west1.firebasedatabase.app",
    "projectId": "leavingcertproject-23455",
    "storageBucket": "leavingcertproject-23455.appspot.com",
    "messagingSenderId": "995568612468",
    "appId": "1:995568612468:web:956124145855eee1a84d21",
    "measurementId": "G-YTS9GE5YXQ"
}

account = False
userid = 'guest'
#result = firebase.get('/Users', 'JimBoy')

app = Flask('app')
app.config['SECRET_KEY'] = '123456789012345678901234'


def set_test_db_data():
    #fireb = firebase.FirebaseApplication('https://leavingcertproject-23455-default-rtdb.europe-west1.firebasedatabase.app')

    firebase = pyrebase.initialize_app(firebaseConfig)
    db = firebase.database()

    dddd = {
	  "Bedroom1":
	  {
		   "Sensor1":
        { "AlarmActive": "True",
		      "AlarmRaised": "False",
          "AlarmSchedule":  [{ "Off Time" : "07:30-19:00"}],
          "AlarmRaisedTime": "2022-03-17 15:00",
          "LastUpdateTime": "2022-03-17 16:00",
		      "AlarmType": "Floor Sensor"       

        }
	  },
	  "Bedroom2":
	  {
				"Sensor2":
        { "AlarmActive": "True",
		      "AlarmRaised": "False",
          "AlarmSchedule": "Always On",
          "AlarmRaisedTime": "",
          "LastUpdateTime": "2022-03-17 16:00",
		      "AlarmType": "Floor Sensor"
        }
    },
 	  "Bedroom3":
	  {
				"Sensor3":
        { "AlarmActive": "True",
		      "AlarmRaised": "False",
          "AlarmSchedule": "Always On",
          "AlarmRaisedTime": "",
          "LastUpdateTime": "2022-03-17 16:00",
		      "AlarmType": "Floor Sensor"
        }  
    }, 
    "Kitchen":
	  {
				"Sensor4":
        { "AlarmActive": "True",
		      "AlarmRaised": "False",
		      "AlarmSchedule": "Always On",
          "AlarmRaisedTime": "",
	        "LastUpdateTime": "2022-03-17 16:00",
         "AlarmType": "Floor Sensor"	
        }

	  },

    "Sitting Room":
	  {
				"Sensor5":
        { "AlarmActive": "True",
		      "AlarmRaised": "True",
          "AlarmSchedule": "Always On",
          "AlarmRaisedTime": "",
          "LastUpdateTime": "2022-03-17 16:00",
		      "AlarmType": "Floor Sensor"
        }
	  }
    }

    

    db.child("/Users/Profile/guest/DevicesDeployed").set(dddd)
    
    dddd = {
    "DayMode":
	  {
		   "Sensor1": { "On": "Off" },
       "Sensor2": { "On": "Off" },
       "Sensor3": { "On": "On" },
       "Sensor4": { "On": "Off" },
       "Sensor5": { "On": "Off" }
	  },
    
      "NightMode":
	  {
		   "Sensor1": { "On": "On" },
       "Sensor2": { "On": "On" },
       "Sensor3": { "On": "On" },
       "Sensor4": { "On": "On" },
       "Sensor5": { "On": "On" }
	  },
      "OutMode":
	  {
		   "Sensor1": { "On": "On" },
       "Sensor2": { "On": "On" },
       "Sensor3": { "On": "On" },
       "Sensor4": { "On": "On" },
       "Sensor5": { "On": "On" }
	  },
    "OffMode":
	  {
		   "Sensor1": { "On": "Off" },
       "Sensor2": { "On": "Off" },
       "Sensor3": { "On": "On" },
       "Sensor4": { "On": "Off" },
       "Sensor5": { "On": "Off" }
	  },
    }      

    db.child("/Users/Profile/guest/SecurityMode").set(dddd)
 

    dddd = { "DevicesDeployed" : {
	  "Bedroom1":
	  {
		   "Sensor1":
        { "AlarmActive": "True",
		      "AlarmRaised": "False",
          "AlarmSchedule":  [{ "Off Time" : "07:30-19:00"}],
          "AlarmRaisedTime": "2022-03-17 15:00",
          "LastUpdateTime": "2022-03-17 16:00",
		      "AlarmType": "Floor Sensor"       

        }
	  },
	  "Bedroom2":
	  {
				"Sensor2":
        { "AlarmActive": "True",
		      "AlarmRaised": "False",
          "AlarmSchedule": "Always On",
          "AlarmRaisedTime": "",
          "LastUpdateTime": "2022-03-17 16:00",
		      "AlarmType": "Floor Sensor"
        }
    },
 	  "Bedroom3":
	  {
				"Sensor3":
        { "AlarmActive": "True",
		      "AlarmRaised": "False",
          "AlarmSchedule": "Always On",
          "AlarmRaisedTime": "",
          "LastUpdateTime": "2022-03-17 16:00",
		      "AlarmType": "Floor Sensor"
        }  
    }, 
    "Kitchen":
	  {
				"Sensor4":
        { "AlarmActive": "True",
		      "AlarmRaised": "False",
		      "AlarmSchedule": "Always On",
          "AlarmRaisedTime": "",
	        "LastUpdateTime": "2022-03-17 16:00",
         "AlarmType": "Floor Sensor"	
        }

	  },
	  "DownStairs Bathroom":
	  {
				"Sensor5":
        { 
          "AlarmActive": "True",
		      "AlarmRaised": "False",
          "AlarmSchedule": "Always On", 
          "AlarmRaisedTime": "",
          "LastUpdateTime": "2022-03-17 16:00",
      		"AlarmType": "Floor Sensor"
        }
	  },
	  "Hallway":
	  {
				"Sensor6":
        { "AlarmActive": "True",
		      "AlarmRaised": "False",
          "AlarmSchedule": "Always On",
          "AlarmRaisedTime": "",
          "LastUpdateTime": "2022-03-17 16:00",
		      "AlarmType": "Floor Sensor"
        }
	  },
    "Sitting Room":
	  {
				"Sensor7":
        { "AlarmActive": "True",
		      "AlarmRaised": "False",
          "AlarmSchedule": "Always On",
          "AlarmRaisedTime": "",
          "LastUpdateTime": "2022-03-17 16:00",
		      "AlarmType": "Floor Sensor"
        }
	  }
    }}

    db.child("/Users/Profile/Granny/").set(dddd)
            
    return db

def get_db_connection():
    #fireb = firebase.FirebaseApplication('https://leavingcertproject-23455-default-rtdb.europe-west1.firebasedatabase.app')

    firebase = pyrebase.initialize_app(firebaseConfig)
    db = firebase.database()

    
    return db


    
@app.route('/')
def index():
  return render_template('index.html')


@app.route('/about')
def about():
    if account:
      return render_template("about.html")
    else:
      return render_template("base.html")

@app.route('/shop')
def shop():
    if account:
      return render_template("shop.html")
    else:
      return render_template("base.html")
  
@app.route('/contact')
def contact():
    if account:
      return render_template("contact.html")
    else:
      return render_template("base.html")
    

def checkuser(username, password):
  global userid
  db = get_db_connection()
  
  #
  # get  username
  #
  path = "/Users/User/" + username + "/Password"
  dpass = db.child(path).get()
  
  print(dpass.val())
  if dpass is None:
    return False
  else:  
    if password == dpass.val():
      userid = username
      return True
    else:
      return False
    
@app.route('/login', methods=['GET', 'POST'])
def login():
  global account
  msg='' 
  if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
    # Create variables for easy access
    username = request.form['username']
    password = request.form['password']
    
    account = checkuser(username, password)

    if account:
      set_test_db_data()
      # Create session data, we can access this data in other routes
      #session['loggedin'] = True
      #session['id'] = account['id']
      #session['username'] = account['username']
      # Redirect to main monitor page
      return monitor()
        
    else:
      # Account doesnt exist or username/password incorrect
      msg = 'Incorrect username/password! Try again please'
  
  
  
  
  return render_template("login.html", msg = msg)


@app.route('/handle_login', methods=['POST'])
def handle_login():
    # flash('Hello Jkkkkkmmy')
    #projectpath = request.form['projectFilepath']
    return render_template("login.html")


@app.route('/control', methods=['GET','POST'])
def control():
    if account:
      return render_template("control.html")
    else:
      return render_template("base.html")



      
@app.route('/monitor')
def monitor():

  if account == 'False':
    return render_template("base.html")
  
  #
  # Use to tranfer data structure to form
  #
  
  class UserDevices:
    def __init__(self, locname, devname, alarmraised,   alarmraisedtime, alarmactive, lastupdatetime):
      self.locname = locname
      self.devname = devname
      self.alarmraised = alarmraised
      self.alarmraisedtime = alarmraisedtime
      self.alarmactive = alarmactive
      self.lastupdatetime = lastupdatetime

      lastupdatetime = "20220317123107"
      if alarmraisedtime is None:
        self.alarmraisedtime =  " "

      diff = datetime.now() - datetime.strptime(lastupdatetime, '%Y%m%d%H%M%S')
      hours = diff.total_seconds()/3600
      print(hours)
      if hours  > 1:
  
        self.lastupdatetime = " not Working for over " + str(int(hours)) + " hours"
      else:
        self.lastupdatetime = "Recent Update"
      
  # Connect to the DB
      
  db = get_db_connection()

  # Get User Mode
  pathuser = "/Users/User/" + userid +  "/SecurityMode"
  umode = db.child(pathuser).get()
  pathuser = "/Users/User/" + userid +  "/RefNo"
  udesc = db.child(pathuser).get()
  udesc = userid + " RefNo: " + udesc.val()
  
  print(umode.val())
  pathuser = "/Users/Profile/" + userid +"/DevicesDeployed"
  locs = db.child(pathuser).shallow().get()


  # Root Location foe location/devices
   
  scrdatas = []
  for l in locs.val():

    # name/room loc
    devpath = pathuser + "/" + l
    dev = db.child(devpath).shallow().get()
    print(devpath)
    # Put dev detail
    
    for d in dev.val():
      
      aa = devpath + "/" + d  + "/AlarmActive"
      ar = devpath + "/" + d  + "/AlarmRaised"
      art = devpath + "/" + d  + "/AlarmRaisedTime" 
      dt = devpath + "/" + d  + "/LastUpdateTime" 
      ar = db.child(ar).get()
      aa = db.child(aa).get()
      art = db.child(art).get()
      dt = db.child(dt).get()
 
     
      print(l, d, ar.val(), art.val(),aa.val(), dt.val()) 
      ll = UserDevices(l, d,  ar.val(), art.val(), aa.val(), dt.val())
      scrdatas.append( ll )
      
  adesc  ="Granny RefNo: 100=9000"

  
  pathuser = "/Users/Profile/" + "Granny" +"/DevicesDeployed"
  locs = db.child(pathuser).shallow().get()


  # Root Location foe location/devices
   
  scrdatas2 = []
  for l in locs.val():

    # name/room loc
    devpath = pathuser + "/" + l
    dev = db.child(devpath).shallow().get()
    print(devpath)
    # Put dev detail
    
    for d in dev.val():
      
      aa = devpath + "/" + d  + "/AlarmActive"
      ar = devpath + "/" + d  + "/AlarmRaised"
      art = devpath + "/" + d  + "/AlarmRaisedTime" 
      dt = devpath + "/" + d  + "/LastUpdateTime" 
      ar = db.child(ar).get()
      aa = db.child(aa).get()
      art = db.child(art).get()
      dt = db.child(dt).get()
 
     
      print(l, d, ar.val(), art.val(),aa.val(), dt.val()) 
      ll = UserDevices(l, d,  ar.val(), art.val(), aa.val(), dt.val())
      scrdatas2.append( ll )
      
  updatetime =  datetime.now() 
  print(updatetime)

  #print(posts.keys())

  if account:
    return render_template("monitor.html", umode=umode.val(), adesc=adesc, udesc=udesc, md=scrdatas, md2=scrdatas2, updatetime=updatetime)
  


@app.route('/style.css')
def style():
    return send_file('templates/style.css')


@app.route('/script.js')
def script():
    return send_file('templates/script.js')

@app.route('/checkout1.html')
def checkout1():
    return render_template('checkout1.html')

@app.route('/checkout.html')
def checkout():
    return render_template('checkout.html')

@app.route('/configdevices.html')
def configdevices():
    return render_template('configdevices.html')

class UserDetails:
    def __init__(self, userid, firstname, surname, email, email2, telno, telno2, refno, contract, addaccount, address1, city, county, eircode, country, addaccounts):
      self.userid = userid
      self.firstname = firstname
      self.surname = surname
      self.email = email
      self.email2 = email2
      self.telno = telno
      self.telno2 = telno2
      self.refno = refno
      self.contract = contract
      self.addrefs = addaccount
      self.address1 = address1
      self.city = city
      self.county = county
      self.eircode = eircode
      self.country = country
      self.addaccounts = addaccounts
      
@app.route('/userdetails.html')
def userdetails():
  scrdatas = []
  db = get_db_connection()
  
  dpath = "/Users/User/" + userid
  fn = db.child(dpath + "/FirstName").get()
  sn = db.child(dpath + "/Surname").get()
  ad = db.child(dpath + "/Address/Address1").get()
  ci = db.child(dpath + "/Address/City").get()
  ct = db.child(dpath + "/Address/County").get()
  ec = db.child(dpath + "/Address/Eircode").get()
  country = db.child(dpath + "/Address/Country").get()
  em = db.child(dpath + "/EMail").get()
  email2 = db.child(dpath + "/EMail2").get()
  telno = db.child(dpath + "/TelNo2").get()
  telno2 = db.child(dpath + "/TelNo2").get()
  rn = db.child(dpath + "/RefNo").get()
  co = db.child(dpath + "/Contract").get()
  ac = db.child(dpath + "/AddAccounts").get()
  
  print(userid)
  print(ac.val())
  ll = UserDetails(userid, fn.val(), sn.val(), em.val(), email2.val(), telno.val(), telno2.val(), rn.val(), co.val(), ac.val(), ad.val(), ci.val(), ct.val(), ec.val(), country.val(), ac.val())
  print(userid)
  scrdatas.append( ll )

  # Root Location foe devices
  rootpath = "/Users/Profile/" + userid + "/DevicesDeployed/"
  dd = db.child(rootpath).shallow().get()

    
  return render_template('userdetails.html', md=scrdatas, dvs = dd.val() )  

@app.route('/password.html')
def password():
   
  return render_template('password.html' )  

@app.route('/securitymode.html')
def securitymode():

  if account == 'False':
    return render_template("base.html")
  
  #
  # Use to tranfer data structure to form
  #
  
  class UserDevicesMode:
    def __init__(self, locname, devname, daymode,  nightmode, outmode, offmode):
      self.locname = locname
      self.devname = devname
      self.daymode = daymode
      self.nightmode = nightmode
      self.outmode = outmode
      self.offmode = offmode

  
  # Connect to the DB
      
  db = get_db_connection()

   # Get User Mode
  pathuser = "/Users/User/" + userid +  "/SecurityMode"
  umode = db.child(pathuser).get()
  pathuser = "/Users/User/" + userid +  "/RefNo"
  udesc = db.child(pathuser).get()
  udesc = userid + " RefNo: " + udesc.val()
  
  # Get User Mode
  pathuser = "/Users/Profile/" + userid +"/DevicesDeployed"
  locs = db.child(pathuser).shallow().get()


  # Root Location foe location/devices
   
  scrdatas = []
  for l in locs.val():

    # name/room loc
    devpath = pathuser + "/" + l
    dev = db.child(devpath).shallow().get()
    print(devpath)
    # Put dev detail

    rootmodepath = "/Users/Profile/" + userid +"/SecurityMode/"
    
    for d in dev.val():
      
      daypath = rootmodepath + "DayMode/" + d + "/On"
      print(daypath)
      nightpath = rootmodepath  + "NightMode/" + d +"/On"
      outpath = rootmodepath + "OutMode/" + d +"/On"
      offpath = rootmodepath + "OffMode/" + d +"/On"


      day = db.child(daypath).get().val()
      night = db.child(nightpath).get().val()
      out = db.child(outpath).get().val()
      off1 = db.child(offpath).get().val()
 
     
      print(l, d, day, night, out, off1)
      ll = UserDevicesMode(l, d, day, night, out, off1)
      scrdatas.append( ll )




  updatetime =  datetime.now() 
  print(updatetime)

  #print(posts.keys())


    
  return render_template('securitymode.html', md=scrdatas,  udesc = udesc )  

@app.route('/form_set_mode', methods=['GET','POST'])
def form_set_mode():
  print("Got Here3")
  # Products.query.filter_by(german_name=request.form.get('search')).all()
  
  db = get_db_connection()

 


  wmodename = request.args.get('modename')
  dpath = "Users/User/" + userid
  rs = db.child(dpath).update({"SecurityMode": wmodename})
  
  dpath = "/Users/Profile/" + userid + "/DevicesDeployed/Bedroom1/Sensor1"
 
  rs = db.child(dpath).update({"AlarmActive": "False"})
  dpath = "/Users/Profile/" + userid + "/DevicesDeployed/Bedroom2/Sensor4"
 
  rs = db.child(dpath).update({"AlarmActive": "False"})
  #print(rs)
                                
  return monitor()


@app.route('/form_set_securitymode', methods=['GET','POST'])
def form_set_securitymode():
  print("Got Here3")
  # Products.query.filter_by(german_name=request.form.get('search')).all()
  
  db = get_db_connection()

 
  wlocname = request.args.get('locname')
  wdevname = request.args.get('devname')
  wmodename = request.args.get('secmode')
  dpath = "Users/User/" + userid
  #rs = db.child(dpath).update({"SecurityMode": wmodename})
  
  dpath = "/Users/Profile/" + userid + "/SecurityMode/"  + wmodename + "/" + wdevname
  modestatus = db.child(dpath + "/On").get()
  print(dpath)
  if modestatus == "On":
    modestatus == "Off"
  else:  
    modestatus == "On"

  rs = db.child(dpath).update({"On": modestatus })
  #rs = db.child(dpath).update({"AlarmActive": "False"})
  #dpath = "/Users/Profile/" + userid + "/DevicesDeployed/Bedroom2/Sensor4"
 
  #rs = db.child(dpath).update({"AlarmActive": "False"})
  #print(rs)
                                
  return monitor()

  

@app.route('/form_updatepassword', methods=['GET','POST'])
def form_updatepassword():
  print("Got Here5")
  # Products.query.filter_by(german_name=request.form.get('search')).all()
  
  db = get_db_connection()

  wpass1 = request.args.get('pass1')
  wpass2 = request.args.get('pass2')

  print(wpass1)
  print(wpass2)

  if wpass1 != wpass2:
    return password()

  dpath = "Users/User/" + userid 

  #rs = db.child(dpath).update({"SecurityMode": wmodename})
  
  rs = db.child(dpath).update({"Password": wpass1})
 
  #rs = db.child(dpath).update({"AlarmActive": "False"})
  #print(rs)
                                
  return monitor()


@app.route('/form_dev_reset', methods=['GET','POST'])
def form_dev_reset():
  print("Got Here2")
  # Products.query.filter_by(german_name=request.form.get('search')).all()
  
  db = get_db_connection()

 

  wlocname = request.args.get('locname')
  wdevname = request.args.get('devname')
  dpath = "/Users/Profile/" + userid + "/DevicesDeployed/" + wlocname + "/" + wdevname
 
  rs = db.child(dpath).update({"AlarmRaised": "False"})
  print(rs)
                                
  return monitor()()


@app.route('/form_userdetails', methods=['GET','POST'])
def form_userdetails():
  print("Got Here")
  # Products.query.filter_by(german_name=request.form.get('search')).all()
  db = get_db_connection()
  dpath = "/Users/User/" + userid
  dpatha = "/Users/User/" + userid +"/Address"


  
  fn = db.child(dpath + "/FirstName").get()
  sn = db.child(dpath + "/Surname").get()
  ad = db.child(dpath + "/Address/Address1").get()
  ci = db.child(dpath + "/Address/City").get()
  ct = db.child(dpath + "/Address/County").get()
  ec = db.child(dpath + "/Address/Eircode").get()
  ec = db.child(dpath + "/Address/Country").get()
  em = db.child(dpath + "/Email").get()
  em = db.child(dpath + "/Email2").get()
  em = db.child(dpath + "/telno").get()
  em = db.child(dpath + "/telno2").get()  

  wfirstname = request.args.get('firstname')
  wsurname = request.args.get('surname')
  waddress1 = request.args.get('address')
  wcity = request.args.get('city')
  wcounty = request.args.get('county')
  weircode = request.args.get('eircode')
  wcountry = request.args.get('country')
  wemail = request.args.get('email')
  wemail2 = request.args.get('email2')
  wtelno = request.args.get('telno')
  wtelno2 = request.args.get('telno2')

  rs = db.child(dpath).update({"FirstName": wfirstname})
  rs = db.child(dpath).update({"Surname": wsurname})
  rs = db.child(dpatha).update({"Address1": waddress1})
  rs = db.child(dpatha).update({"City": wcity})
  rs = db.child(dpatha).update({"County": wcounty})
  rs = db.child(dpatha).update({"Eircode": weircode})
  rs = db.child(dpatha).update({"Country": wcountry})
  rs = db.child(dpath).update({"EMail": wemail})
  rs = db.child(dpath).update({"EMail2": wemail2})
  rs = db.child(dpath).update({"TelNo": wtelno})
  rs = db.child(dpath).update({"TelNo2": wtelno2})
  
  return render_template('about.html')
  

@app.route('/imgs/Dark_Mode.svg')
def dark_mode_svg():    
  return send_file('templates/imgs/Dark_Mode.svg')


@app.route('/favicon.png')
def favicon():
    return send_file('templates/favicon.png')


@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404


@app.errorhandler(500)
def server_overloaded(e):
    # note that we set the 500 status explicitly
    return render_template('500.html'), 500


#
app.run(host='0.0.0.0', port=8080)

#if '__name__' == '__main__':
# app.run(Debug=False)
