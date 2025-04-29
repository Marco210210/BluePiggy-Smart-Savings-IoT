#MAIN BLUE PIGGY

from bsp import board
import Coin
import Display_coin
import gpio
import serial
import Servo
import time
import gpio
import close_cod
import open_cod

from zdm import zdm
from networking import wifi
from networking import socket
from protocols import http
from protocols import mqtt

# INIZIALIZZAZIONE PIN INFRAROSSI
gpio.mode(D5, INPUT_PULLUP)
gpio.mode(D18, INPUT_PULLUP)
gpio.mode(D23, INPUT_PULLUP)
gpio.mode(D19, INPUT_PULLUP)
gpio.mode(D21, INPUT_PULLUP)

# INIZIALIZZAZIONE VARIABILI
flag = 0
saldo = 0.00
data=0
mypassword=""
password = ""
errori = 0
flag_call=1
un_euro=0
due_euro=0
cinquanta_cent=0
venti_cent=0
dieci_cent=0
flag_servo=1

#functions

def inserted_1_eur():
    global flag_servo
    global saldo
    global un_euro
    if(flag_servo==1):
        Display_coin.clear_display()
        Display_coin.clear_display()
        Display_coin.spinning_coin()
        Display_coin.one_eur_stamp()
        Display_coin.clear_display()
        saldo+=float(1)
        un_euro+=1.00
        Display_coin.print_balance(saldo)
    else:
        Display_coin.clear_display()
        Display_coin.print_alert()
        sleep(3000)
        Display_coin.open_vano()

def inserted_2_eur():
    global flag_servo
    global saldo
    global due_euro
    if(flag_servo==1):
        Display_coin.clear_display()
        Display_coin.clear_display()
        Display_coin.spinning_coin()
        Display_coin.two_eur_stamp()
        Display_coin.clear_display()
        saldo+=2.00
        due_euro+=1
        Display_coin.print_balance(saldo)
    else:
        Display_coin.clear_display()
        Display_coin.print_alert()
        sleep(3000)
        Display_coin.open_vano()

def inserted_50_cent():
    global flag_servo
    global saldo
    global cinquanta_cent
    if(flag_servo==1):
        Display_coin.clear_display()
        Display_coin.clear_display()
        Display_coin.spinning_coin()
        Display_coin.fifty_cent_stamp()
        Display_coin.clear_display()
        saldo+=0.50
        cinquanta_cent+=1
        Display_coin.print_balance(saldo)
    else:
        Display_coin.clear_display()
        Display_coin.print_alert()
        sleep(3000)
        Display_coin.open_vano()

def inserted_10_cent():
    global flag_servo
    global dieci_cent
    global saldo
    if(flag_servo==1):
        Display_coin.clear_display()
        Display_coin.clear_display()
        Display_coin.spinning_coin()
        Display_coin.ten_cent_stamp()
        Display_coin.clear_display()
        saldo+=0.10
        dieci_cent+=1
        Display_coin.print_balance(saldo)
    else:
        Display_coin.clear_display()
        Display_coin.print_alert()
        sleep(3000)
        Display_coin.open_vano()

def inserted_20_cent():
    global flag_servo
    global saldo
    global venti_cent
    if(flag_servo==1):
        Display_coin.clear_display()
        Display_coin.clear_display()
        Display_coin.spinning_coin()
        Display_coin.twenty_cent_stamp()
        Display_coin.clear_display()
        saldo+=0.20
        venti_cent+=1
        Display_coin.print_balance(saldo)
    else:
        Display_coin.clear_display()
        Display_coin.print_alert()
        sleep(3000)
        Display_coin.open_vano()

# il metodo run contenente la client.loop() serve per rimanere in ascolto di messaggi provenienti dal broker MQTT
def run():
    try:
        client.loop()
    except Exception as e:
        print("run thread exec",e)
        sleep(6000)


#callback per l'azionamento del servo motore
def callback_S(client, topic, message):
    global saldo
    global dieci_cent
    global venti_cent
    global cinquanta_cent
    global un_euro
    global due_euro
    global flag_servo
    if topic=="/IoT22/setServo_gruppo18":
        if message=="ON":
            Servo.apri()#qui dentro va messa la funzione del servo motore APRI
            sleep(1000)
            flag_servo=0
            Display_coin.clear_display()
            Display_coin.open_vano()
        elif message=="OFF":
            Display_coin.clear_display()
            Display_coin.close_vano()
            Servo.chiudi()
            saldo=0.00
            dieci_cent=0
            venti_cent=0
            cinquanta_cent=0
            un_euro=0
            due_euro=0
            sleep(3000)
            Display_coin.clear_display()
            Display_coin.print_balance(saldo)
            flag_call=1
            flag_servo=1

#callback per reperire e stampare la data di ultima apertura via MQTT
def callback_O(client, topic, message):
    global data
    if topic=="/IoT22/setOrario_gruppo18":
        data=str(message)
        Display_coin.clear_display()
        Display_coin.last_animation()
        sleep(2000)
        Display_coin.print_last_opening(data)

#callback per reperire la password via MQTT
def callback_P(client, topic, message):
    global password
    if topic=="/IoT22/setPassword_gruppo18":
        password=message

#callback per stampare il saldo dopo il comando MQTT
def callback_B(client, topic, message):
    global saldo
    if topic=="/IoT22/setBalance_gruppo18":
        if message=="Balance":
            Display_coin.clear_display()
            Display_coin.available_animation()
            sleep(2000)
            Display_coin.print_balance(saldo)

#configurazione e connessione wifi
wifi.configure(ssid= "WiFi-Studio",password= "0000000001")
print("Wi-fi: Creating connection...")
wifi.start()
print("Connected!")

agent = zdm.Agent()
agent.start()

#inizializzazione display e funzioni a fronte di discesa per gli infrarossi
Display_coin.init_display()
Display_coin.clear_display()
Display_coin.print_balance(saldo)
gpio.on_fall(D19, inserted_1_eur, debounce=120)
gpio.on_fall(D23, inserted_2_eur, debounce=120)
gpio.on_fall(D21, inserted_50_cent, debounce=180)
gpio.on_fall(D5, inserted_10_cent, debounce=100)
gpio.on_fall(D18, inserted_20_cent, debounce=110)

while True:
    
    try:

        client = mqtt.MQTT("test.mosquitto.org","IoT22_ZM1")
        #avvio il client che controllera se gli sono stati mandati i dati con la callback
        client.on("/IoT22/setServo_gruppo18", callback_S,0)
        client.on("/IoT22/setOrario_gruppo18", callback_O,2)
        client.on("/IoT22/setPassword_gruppo18", callback_P,2)
        client.on("/IoT22/setBalance_gruppo18", callback_B,2)
        #connette il client
        client.connect()
        #avviamo il metodo run tramite un thread per far si che rimanga sempre in ascolto
        thread(run)
        
        while True:
            print("Still running...")
            agent.publish({"Saldo": saldo}, "test")
            agent.publish({"10 cent": dieci_cent}, "test")
            agent.publish({"20 cent": venti_cent}, "test")
            agent.publish({"50 cent": cinquanta_cent}, "test")
            agent.publish({"1 euro": un_euro}, "test")
            agent.publish({"2 euro": due_euro}, "test")
            connection=http.HTTP()

            #inviamo i dati sul bot di telegram
            url="http://contamoneta.altervista.org/inserimento.php?dieci="+str(dieci_cent)+"&venti="+str(venti_cent)+"&cinquanta="+str(cinquanta_cent)+"&uno="+str(un_euro)+"&due="+str(due_euro)+"&password="+str(password)+"&saldo="+str(saldo)
            connection.get(url)
            connection.destroy()
            sleep(500)

    except WifiBadPassword:
        print("Bad Password")
    except WifiBadSSID:
        print("Bad SSID")
    except WifiException:
        print("Generic Wifi Exception")
    except Exception as e:
        raise e
    sleep(10000)

