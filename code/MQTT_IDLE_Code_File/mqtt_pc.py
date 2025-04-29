import paho.mqtt.client as mqtt
import time
import datetime
import sys
import random
import string

#variables
password=""
var=0

def get_random_string(length):
    # choose from all lowercase letter
    randomstr = ''.join(random.choices(string.ascii_letters+string.digits,k=length))
    return randomstr

# The callback for when the client receives a
# CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    print("\n connected with client "+ str(client))
    print("\n connected with userdata "+str(userdata))
    print("\n connected with flags "+str(flags))


def on_publish(client,userdata,result): #create function for callback
    print("data published \n")


try:
    client = mqtt.Client("UniSAIoT22PubD22")
    client.on_connect = on_connect
    client.on_publish = on_publish
    client.connect("test.mosquitto.org", 1883, 60)
    client.loop_start()   # the loop() method periodically checks the callback events
    time.sleep(2)   # per non sovrapporre le stampe 
    
    print("\n\nBenvenuto/a in Blue Piggy manager MQTT!")

    while True:
        print("\n_________________________SCEGLI UN'OPERAZIONE_________________________\n")
        print("\n1 Inserisci la password corrente per sbloccare il vano conta monete.");
        print("\n2 Inserisci SEND PASSWORD per ottenere via telegram la password per lo sblocco del vano conta monete.")
        print("\n3 Inserisci CLOSE per bloccare il vano conta monete.");
        print("\n4 Inserisci LAST OPENING per stampare sul display l'ultima apertura.")
        print("\n5 inserisci AVAILABLE BALANCE per stampare sul display il saldo disponibile.")
        print("\n6 Inserisci QUIT per chiudere l'applicazione.\n")

        a = input("Scelta: ");
        while (a!=password and a!="CLOSE" and a!="QUIT" and a!="LAST OPENING" and a!="SEND PASSWORD" and a!="AVAILABLE BALANCE"):   #inserisco le lettere o i numeri per aprire e chiudere il servo
            a = input("Inserisci un valore valido: ");


        if (a==password and password!=""):
            # SBLOCCO VANO CONTA_MONETE
            print("\nSblocco vano conta monete in corso...")
            resL=client.publish("/IoT22/setServo_gruppo18", "ON", qos=1, retain=False)
            a = 0   # reset scelta
            var=datetime.datetime.now()
            time.sleep(2)
            print("\nVano sbloccato.\n")

        if(password==""):
            print("Per aprire il vano conta monete inserisci SEND PASSWORD per ottenere la password di apertura!")

        if (a=="LAST OPENING" and var!=0):
            # ULTIMA APERTURA
            print("\nTi mostro sul display l'ultima apertura.")
            client.publish("/IoT22/setOrario_gruppo18",str(var), qos=2, retain=False)
            a = 0   # reset scelta
            time.sleep(2)

        if (a=="LAST OPENING" and var==0):  
            print("\nPer richiedere l'ultima data d'apertura devi aver aperto almeno una volta il vano conta monete.")

        if (a=="AVAILABLE BALANCE"):
            # SALDO DISPONIBILE
            print("\nTi mostro sul display il saldo disponibile.")
            client.publish("/IoT22/setBalance_gruppo18","Balance", qos=2, retain=False)
            a = 0   # reset scelta
            time.sleep(2)

        if (a=="SEND PASSWORD"):
            # INVIO PASSWORD
            print("\nTi mostro via telegram la password di sblocco.")
            password=get_random_string(6)
            client.publish("/IoT22/setPassword_gruppo18",str(password), qos=2, retain=False)
            a = 0   # reset scelta
            time.sleep(2)

        if (a=="CLOSE"):
            # BLOCCO VANO CONTA_MONETE
            print("\nBlocco vano conta monete in corso...")
            resL=client.publish("/IoT22/setServo_gruppo18", "OFF", qos=1, retain=False)
            a = 0   # reset scelta
            time.sleep(2)
            print("\nVano bloccato.\n")

        if (a=="QUIT"):
            print("\nGrazie per aver usato Blue Piggy manager MQTT!\n")
            quit()
        
except Exception as e:
    print('exception ', e)
finally:
    client.loop_stop()
    client.disconnect()
