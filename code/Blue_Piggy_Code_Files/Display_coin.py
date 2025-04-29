#_____Display Variables_____________________________________________________________________________________________________________

SSD1306_LCDWIDTH                    = 128 
SSD1306_LCDHEIGHT                   = 64 
SSD1306_SETCONTRAST                 = 0x81 
SSD1306_DISPLAYALLON_RESUME         = 0xA4 
SSD1306_DISPLAYALLON                = 0xA5 
SSD1306_NORMALDISPLAY               = 0xA6 
SSD1306_INVERTDISPLAY               = 0xA7 
SSD1306_DISPLAYOFF                  = 0xAE 
SSD1306_DISPLAYON                   = 0xAF 
SSD1306_SETDISPLAYOFFSET            = 0xD3 
SSD1306_SETCOMPINS                  = 0xDA 
SSD1306_SETVCOMDETECT               = 0xDB 
SSD1306_SETDISPLAYCLOCKDIV          = 0xD5 
SSD1306_SETPRECHARGE                = 0xD9 
SSD1306_SETMULTIPLEX                = 0xA8 
SSD1306_SETLOWCOLUMN                = 0x00 
SSD1306_SETHIGHCOLUMN               = 0x10 
SSD1306_SETSTARTLINE                = 0x40 
SSD1306_MEMORYMODE                  = 0x20 
SSD1306_COLUMNADDR                  = 0x21 
SSD1306_PAGEADDR                    = 0x22 
SSD1306_COMSCANINC                  = 0xC0 
SSD1306_COMSCANDEC                  = 0xC8 
SSD1306_SEGREMAP                    = 0xA0 
SSD1306_CHARGEPUMP                  = 0x8D 
SSD1306_EXTERNALVCC                 = 0x1 
SSD1306_SWITCHCAPVCC                = 0x2

CURRENT_RAW_COUNTER=0 #CURRENT_RAW_COUNTER_posizioni
TOTAL_RAW_COUNTER=128
balance=5                                                 
string_balance=str(balance)
FILL_DISPLAY_COUNTER=0
flag=0


#_____Import File___________________________________________________________________________________________________________________

import Coin              #this file must be in the same folder of this script 
import serial
import i2c
import Servo
import close_cod
import open_cod
import available_balance
import last_opening

#_____I2C Inizialization____________________________________________________________________________________________________________

serial.serial()
i2c_scan_buf = i2c.scan()
port = i2c.I2c(0x3C)

#_____Display Inizialization and Functions__________________________________________________________________________________________

def init_display():

    port.write(bytearray([0x00,SSD1306_DISPLAYOFF]))              
    
    port.write(bytearray([0x00,SSD1306_SETDISPLAYCLOCKDIV]))          
    port.write(bytearray([0x00,0x80]))             
        
    port.write(bytearray([0x00,SSD1306_SETMULTIPLEX]))               
    port.write(bytearray([0x00,0x3F]))
        
    port.write(bytearray([0x00,SSD1306_SETDISPLAYOFFSET]))           
    port.write(bytearray([0x00,0x0]))                              
        
    port.write(bytearray([0x00,SSD1306_SETSTARTLINE]))
        
    port.write(bytearray([0x00,SSD1306_CHARGEPUMP]))                  
    port.write(bytearray([0x00,0x14]))

    port.write(bytearray([0x00,SSD1306_MEMORYMODE]))                 
    port.write(bytearray([0x00,0x00]))        
        
    port.write(bytearray([0x00,SSD1306_SEGREMAP | 0x1]))
    port.write(bytearray([0x00,SSD1306_COMSCANDEC]))
        
    port.write(bytearray([0x00,SSD1306_SETCOMPINS]))                 
    port.write(bytearray([0x00,0x12]))
        
    port.write(bytearray([0x00,SSD1306_SETCONTRAST]))                 
    port.write(bytearray([0x00,0xCF]))
        
    port.write(bytearray([0x00,SSD1306_SETPRECHARGE]))                
    port.write(bytearray([0x00,0xF1]))
        
    port.write(bytearray([0x00,SSD1306_SETVCOMDETECT]))               
    port.write(bytearray([0x00,0x40]))

    port.write(bytearray([0x00,SSD1306_DISPLAYALLON_RESUME]))        
        
    port.write(bytearray([0x00,SSD1306_NORMALDISPLAY]))  

    port.write(bytearray([0x00,SSD1306_DISPLAYON]))      

    port.write(bytearray([0x00,SSD1306_COLUMNADDR]))           
    port.write(bytearray([0x00,0]))                  
    port.write(bytearray([0x00,127]))    

    port.write(bytearray([0x00,SSD1306_PAGEADDR]))           
    port.write(bytearray([0x00,0]))                  
    port.write(bytearray([0x00,64//8 -1]))    

def clear_display():
    for i in range(1024):
        port.write(bytearray([0x40,0x00]))             

def spinning_coin():
        for i in range(0,1024):
            port.write(bytearray([0x40,Coin.Coin1[i]]))

        for i in range(0,1024):
            port.write(bytearray([0x40,Coin.Coin2[i]]))

        for i in range(0,1024):
            port.write(bytearray([0x40,Coin.Coin3[i]]))

        for i in range(0,1024):
            port.write(bytearray([0x40,Coin.Coin4[i]]))

        for i in range(0,1024):
            port.write(bytearray([0x40,Coin.Coin5[i]]))   

        for i in range(0,1024):
            port.write(bytearray([0x40,Coin.Coin6[i]]))
        
        for i in range(0,1024):
            port.write(bytearray([0x40,Coin.Coin1[i]]))
        
        clear_display()

def close_vano():
    for i in range(0,1024):
            port.write(bytearray([0x40,close_cod.Vano_chiuso[i]]))

def open_vano():
    for i in range(0,1024):
            port.write(bytearray([0x40,open_cod.Vano_aperto[i]]))

def available_animation():
    for i in range(0,1024):
            port.write(bytearray([0x40,available_balance.Available[i]]))

def last_animation():
    for i in range(0,1024):
            port.write(bytearray([0x40,last_opening.last[i]]))


def ten_cent_stamp():
        for i in range(0,1024):
            port.write(bytearray([0x40,Coin.Plus_10_cent[i]])) 
        sleep(1000)
        clear_display()

def twenty_cent_stamp():
        for i in range(0,1024):
            port.write(bytearray([0x40,Coin.Plus_20_cent[i]])) 
        sleep(1000)
        clear_display()

def fifty_cent_stamp():
        for i in range(0,1024):
            port.write(bytearray([0x40,Coin.Plus_50_cent[i]])) 
        sleep(1000)
        clear_display()

def one_eur_stamp():
        for i in range(0,1024):
            port.write(bytearray([0x40,Coin.Plus_1_eur[i]])) 
        sleep(1000)
        clear_display()

def two_eur_stamp():
        for i in range(0,1024):
            port.write(bytearray([0x40,Coin.Plus_2_eur[i]])) 
        sleep(1000)
        clear_display()


def print_character(c):
    if c == "A":
        ##A
        port.write(bytearray([0x40,0x7E]))
        port.write(bytearray([0x40,0x09]))
        port.write(bytearray([0x40,0x09]))
        port.write(bytearray([0x40,0x7E]))
        port.write(bytearray([0x40,0x00]))
        CURRENT_RAW_COUNTER+=5
        FILL_DISPLAY_COUNTER+=5

    if c =='B':
        ##B
        port.write(bytearray([0x40,0x7F]))
        port.write(bytearray([0x40,0x49]))
        port.write(bytearray([0x40,0x49]))
        port.write(bytearray([0x40,0x36]))
        port.write(bytearray([0x40,0x00]))
        CURRENT_RAW_COUNTER+=5
        FILL_DISPLAY_COUNTER+=5

    if c == 'C':
        ##C
        port.write(bytearray([0x40,0x3E]))
        port.write(bytearray([0x40,0x41]))
        port.write(bytearray([0x40,0x41]))
        port.write(bytearray([0x40,0x22]))
        port.write(bytearray([0x40,0x00]))
        CURRENT_RAW_COUNTER+=5
        FILL_DISPLAY_COUNTER+=5
    
    if c == 'D':
        ##D
        port.write(bytearray([0x40,0x7F]))
        port.write(bytearray([0x40,0x41]))
        port.write(bytearray([0x40,0x41]))
        port.write(bytearray([0x40,0x3E]))
        port.write(bytearray([0x40,0x00]))
        CURRENT_RAW_COUNTER+=5
        FILL_DISPLAY_COUNTER+=5

    if c == 'E':
        ##E
        port.write(bytearray([0x40,0x7F]))
        port.write(bytearray([0x40,0x49]))
        port.write(bytearray([0x40,0x49]))
        port.write(bytearray([0x40,0x41]))
        port.write(bytearray([0x40,0x00]))
        CURRENT_RAW_COUNTER+=5
        FILL_DISPLAY_COUNTER+=5

    if c == 'F':
        ##F
        port.write(bytearray([0x40,0x7F]))
        port.write(bytearray([0x40,0x09]))
        port.write(bytearray([0x40,0x09]))
        port.write(bytearray([0x40,0x01]))
        port.write(bytearray([0x40,0x00]))
        CURRENT_RAW_COUNTER+=5
        FILL_DISPLAY_COUNTER+=5

    if c == 'G':
        ##G
        port.write(bytearray([0x40,0x3E]))
        port.write(bytearray([0x40,0x41]))
        port.write(bytearray([0x40,0x51]))
        port.write(bytearray([0x40,0x32]))
        port.write(bytearray([0x40,0x00]))
        CURRENT_RAW_COUNTER+=5
        FILL_DISPLAY_COUNTER+=5

    if c == 'H':
        ##H
        port.write(bytearray([0x40,0x7F]))
        port.write(bytearray([0x40,0x08]))
        port.write(bytearray([0x40,0x08]))
        port.write(bytearray([0x40,0x7F]))
        port.write(bytearray([0x40,0x00]))
        CURRENT_RAW_COUNTER+=5
        FILL_DISPLAY_COUNTER+=5

    if c == 'I':
        ##I
        port.write(bytearray([0x40,0x41]))
        port.write(bytearray([0x40,0x7F]))
        port.write(bytearray([0x40,0x41]))
        port.write(bytearray([0x40,0x00]))
        CURRENT_RAW_COUNTER+=4
        FILL_DISPLAY_COUNTER+=4

    if c == 'J':
        ##J
        port.write(bytearray([0x40,0x30]))
        port.write(bytearray([0x40,0x40]))
        port.write(bytearray([0x40,0x40]))
        port.write(bytearray([0x40,0x3F]))
        port.write(bytearray([0x40,0x00]))
        CURRENT_RAW_COUNTER+=5
        FILL_DISPLAY_COUNTER+=5

    if c == 'K':
        ##K
        port.write(bytearray([0x40,0x7F]))
        port.write(bytearray([0x40,0x08]))
        port.write(bytearray([0x40,0x14]))
        port.write(bytearray([0x40,0x63]))
        port.write(bytearray([0x40,0x00]))
        CURRENT_RAW_COUNTER+=5
        FILL_DISPLAY_COUNTER+=5

    if c == 'L':
        ##L
        port.write(bytearray([0x40,0x7F]))
        port.write(bytearray([0x40,0x40]))
        port.write(bytearray([0x40,0x40]))
        port.write(bytearray([0x40,0x40]))
        port.write(bytearray([0x40,0x00]))
        CURRENT_RAW_COUNTER+=5
        FILL_DISPLAY_COUNTER+=5

    if c == 'M':
        ##M
        port.write(bytearray([0x40,0x7F]))
        port.write(bytearray([0x40,0x02]))
        port.write(bytearray([0x40,0x0C]))
        port.write(bytearray([0x40,0x02]))
        port.write(bytearray([0x40,0x7F]))
        port.write(bytearray([0x40,0x00]))
        CURRENT_RAW_COUNTER+=6
        FILL_DISPLAY_COUNTER+=6

    if c == 'N':
        ##N
        port.write(bytearray([0x40,0x7F]))
        port.write(bytearray([0x40,0x04]))
        port.write(bytearray([0x40,0x08]))
        port.write(bytearray([0x40,0x7F]))
        port.write(bytearray([0x40,0x00]))
        CURRENT_RAW_COUNTER+=5
        FILL_DISPLAY_COUNTER+=5

    if c == 'O':
        ##O
        port.write(bytearray([0x40,0x3E]))
        port.write(bytearray([0x40,0x41]))
        port.write(bytearray([0x40,0x41]))
        port.write(bytearray([0x40,0x3E]))
        port.write(bytearray([0x40,0x00]))
        CURRENT_RAW_COUNTER+=5
        FILL_DISPLAY_COUNTER+=5

    if c == 'P':
        ##P
        port.write(bytearray([0x40,0x7F]))
        port.write(bytearray([0x40,0x09]))
        port.write(bytearray([0x40,0x09]))
        port.write(bytearray([0x40,0x06]))
        port.write(bytearray([0x40,0x00]))
        CURRENT_RAW_COUNTER+=5
        FILL_DISPLAY_COUNTER+=5

    if c == 'Q':
        ##Q
        port.write(bytearray([0x40,0x3E]))
        port.write(bytearray([0x40,0x41]))
        port.write(bytearray([0x40,0x21]))
        port.write(bytearray([0x40,0x5E]))
        port.write(bytearray([0x40,0x00]))
        CURRENT_RAW_COUNTER+=5
        FILL_DISPLAY_COUNTER+=5

    if c == 'R':
        ##R
        port.write(bytearray([0x40,0x7F]))
        port.write(bytearray([0x40,0x09]))
        port.write(bytearray([0x40,0x09]))
        port.write(bytearray([0x40,0x76]))
        port.write(bytearray([0x40,0x00]))
        CURRENT_RAW_COUNTER+=5
        FILL_DISPLAY_COUNTER+=5

    if c == 'S':
        ##S
        port.write(bytearray([0x40,0X26]))
        port.write(bytearray([0x40,0x49]))
        port.write(bytearray([0x40,0x49]))
        port.write(bytearray([0x40,0x32]))
        port.write(bytearray([0x40,0x00]))
        CURRENT_RAW_COUNTER+=5
        FILL_DISPLAY_COUNTER+=5

    if c == 'T':
        ##T
        port.write(bytearray([0x40,0x01]))
        port.write(bytearray([0x40,0x01]))
        port.write(bytearray([0x40,0x7F]))
        port.write(bytearray([0x40,0x01]))
        port.write(bytearray([0x40,0x01]))
        port.write(bytearray([0x40,0x00]))
        CURRENT_RAW_COUNTER+=6
        FILL_DISPLAY_COUNTER+=6

    if c == "U":
        ##U
        port.write(bytearray([0x40,0x3F]))
        port.write(bytearray([0x40,0x40]))
        port.write(bytearray([0x40,0x40]))
        port.write(bytearray([0x40,0x3F]))
        port.write(bytearray([0x40,0x00]))
        CURRENT_RAW_COUNTER+=5
        FILL_DISPLAY_COUNTER+=5

    if c == 'V':
        ##V
        port.write(bytearray([0x40,0x1F]))
        port.write(bytearray([0x40,0x20]))
        port.write(bytearray([0x40,0x40]))
        port.write(bytearray([0x40,0x20]))
        port.write(bytearray([0x40,0x1F]))
        port.write(bytearray([0x40,0x00]))
        CURRENT_RAW_COUNTER+=6
        FILL_DISPLAY_COUNTER+=6
    

    if c == 'W':
        ##W
        port.write(bytearray([0x40,0x7F]))
        port.write(bytearray([0x40,0x20]))
        port.write(bytearray([0x40,0x18]))
        port.write(bytearray([0x40,0x20]))
        port.write(bytearray([0x40,0x7F]))
        port.write(bytearray([0x40,0x00]))
        CURRENT_RAW_COUNTER+=6
        FILL_DISPLAY_COUNTER+=6

    if c == 'X':
        ##X
        port.write(bytearray([0x40,0x77]))
        port.write(bytearray([0x40,0x08]))
        port.write(bytearray([0x40,0x08]))
        port.write(bytearray([0x40,0x77]))
        port.write(bytearray([0x40,0x00]))
        CURRENT_RAW_COUNTER+=5
        FILL_DISPLAY_COUNTER+=5

    if c == 'Y':
        ##Y
        port.write(bytearray([0x40,0x2F]))
        port.write(bytearray([0x40,0x48]))
        port.write(bytearray([0x40,0x48]))
        port.write(bytearray([0x40,0x3F]))
        port.write(bytearray([0x40,0x00]))
        CURRENT_RAW_COUNTER+=5
        FILL_DISPLAY_COUNTER+=5

    if c == 'Z':
        ##Z
        port.write(bytearray([0x40,0x71]))
        port.write(bytearray([0x40,0x49]))
        port.write(bytearray([0x40,0x49]))
        port.write(bytearray([0x40,0x47]))
        port.write(bytearray([0x40,0x00]))
        CURRENT_RAW_COUNTER+=5
        FILL_DISPLAY_COUNTER+=5

    if c == ' ':
        ##SPAZIO
        port.write(bytearray([0x40,0x00]))
        port.write(bytearray([0x40,0x00]))
        CURRENT_RAW_COUNTER+=2
        FILL_DISPLAY_COUNTER+=2

    if c == '1':
        ##1
        port.write(bytearray([0x40,0x42]))
        port.write(bytearray([0x40,0x7F]))
        port.write(bytearray([0x40,0x40]))
        port.write(bytearray([0x40,0x00]))
        CURRENT_RAW_COUNTER+=4
        FILL_DISPLAY_COUNTER+=4

    if c == '2':
        ##2
        port.write(bytearray([0x40,0x62]))
        port.write(bytearray([0x40,0x51]))
        port.write(bytearray([0x40,0x49]))
        port.write(bytearray([0x40,0x46]))
        port.write(bytearray([0x40,0x00]))
        CURRENT_RAW_COUNTER+=5
        FILL_DISPLAY_COUNTER+=5

    if c == '3':
        ##3
        port.write(bytearray([0x40,0x22]))
        port.write(bytearray([0x40,0x49]))
        port.write(bytearray([0x40,0x49]))
        port.write(bytearray([0x40,0x36]))
        port.write(bytearray([0x40,0x00]))
        CURRENT_RAW_COUNTER+=5
        FILL_DISPLAY_COUNTER+=5

    if c == '4':
        ##4
        port.write(bytearray([0x40,0x0C]))
        port.write(bytearray([0x40,0x0A]))
        port.write(bytearray([0x40,0x09]))
        port.write(bytearray([0x40,0x7F]))
        port.write(bytearray([0x40,0x00]))
        CURRENT_RAW_COUNTER+=5
        FILL_DISPLAY_COUNTER+=5

    if c == '5':
        ##5
        port.write(bytearray([0x40,0x47]))
        port.write(bytearray([0x40,0x45]))
        port.write(bytearray([0x40,0x45]))
        port.write(bytearray([0x40,0x39]))
        port.write(bytearray([0x40,0x00]))
        CURRENT_RAW_COUNTER+=5
        FILL_DISPLAY_COUNTER+=5

    if c == '6':
        ##6
        port.write(bytearray([0x40,0x3C]))
        port.write(bytearray([0x40,0x4A]))
        port.write(bytearray([0x40,0x49]))
        port.write(bytearray([0x40,0x30]))
        port.write(bytearray([0x40,0x00]))
        CURRENT_RAW_COUNTER+=5
        FILL_DISPLAY_COUNTER+=5

    if c == '7':
        ##7
        port.write(bytearray([0x40,0x01]))
        port.write(bytearray([0x40,0x71]))
        port.write(bytearray([0x40,0x09]))
        port.write(bytearray([0x40,0x07]))
        port.write(bytearray([0x40,0x00]))
        CURRENT_RAW_COUNTER+=5
        FILL_DISPLAY_COUNTER+=5

    if c == '8':
        ##8
        port.write(bytearray([0x40,0x36]))
        port.write(bytearray([0x40,0x49]))
        port.write(bytearray([0x40,0x49]))
        port.write(bytearray([0x40,0x36]))
        port.write(bytearray([0x40,0x00]))
        CURRENT_RAW_COUNTER+=5
        FILL_DISPLAY_COUNTER+=5

    if c == '9':
        ##9
        port.write(bytearray([0x40,0x06]))
        port.write(bytearray([0x40,0x49]))
        port.write(bytearray([0x40,0x29]))
        port.write(bytearray([0x40,0x1E]))
        port.write(bytearray([0x40,0x00]))
        CURRENT_RAW_COUNTER+=5
        FILL_DISPLAY_COUNTER+=5

    if c == '0':
        port.write(bytearray([0x40,0x3E]))
        port.write(bytearray([0x40,0x51]))
        port.write(bytearray([0x40,0x49]))
        port.write(bytearray([0x40,0x3E]))
        port.write(bytearray([0x40,0x00]))
        CURRENT_RAW_COUNTER+=5
        FILL_DISPLAY_COUNTER+=5

    if c == '.':
        port.write(bytearray([0x40,0x58]))
        port.write(bytearray([0x40,0x38]))
        port.write(bytearray([0x40,0x00]))
        CURRENT_RAW_COUNTER+=3
        FILL_DISPLAY_COUNTER+=3

    if c == ':':
        port.write(bytearray([0x40,0x63]))
        port.write(bytearray([0x40,0x00]))
        CURRENT_RAW_COUNTER+=2
        FILL_DISPLAY_COUNTER+=2

    if c == '/':
        port.write(bytearray([0x40,0x01]))
        port.write(bytearray([0x40,0x01]))
        CURRENT_RAW_COUNTER+=2
        FILL_DISPLAY_COUNTER+=2

    if c == '_':
        port.write(bytearray([0x40,0x40]))
        port.write(bytearray([0x40,0x40]))
        CURRENT_RAW_COUNTER+=2
        FILL_DISPLAY_COUNTER+=2
    

    if c == '€':
        port.write(bytearray([0x40,0x14]))
        port.write(bytearray([0x40,0x3E]))
        port.write(bytearray([0x40,0x55]))
        port.write(bytearray([0x40,0x55]))
        port.write(bytearray([0x40,0x41]))
        port.write(bytearray([0x40,0x00]))
        CURRENT_RAW_COUNTER+=6   
        FILL_DISPLAY_COUNTER+=6
    
    if c == '-':
        port.write(bytearray([0x40,0x40]))
        port.write(bytearray([0x40,0x20]))
        port.write(bytearray([0x40,0x10]))
        port.write(bytearray([0x40,0x08]))
        port.write(bytearray([0x40,0x04]))
        port.write(bytearray([0x40,0x02]))
        port.write(bytearray([0x40,0x01]))
        port.write(bytearray([0x40,0x00]))
        CURRENT_RAW_COUNTER+=8
        FILL_DISPLAY_COUNTER+=8


def new_line():
        global flag
        if(flag==0):
            for i in range(TOTAL_RAW_COUNTER-CURRENT_RAW_COUNTER):
                port.write(bytearray([0x40,0x00]))
            FILL_DISPLAY_COUNTER+=TOTAL_RAW_COUNTER-CURRENT_RAW_COUNTER
            CURRENT_RAW_COUNTER=0
        else: 
            print("You can't wrap, you're on the last line!")
            flag=0


def count_character_columns(char):
    if(char=='M'or char=='T' or char=='V' or char=='W'or char=='€'):
        return 6
    if(char=='I' or char=='1'):
        return 4
    if(char=='.'):
        return 3
    if(char==':' or char=='_' or char=='-' or char==' '):
        return 2
    if(char=='/'):
        return 8
    else:
        return 5


def print_string(string,IS_LAST_STRING):
        global flag
        global FILL_DISPLAY_COUNTER
        if (IS_LAST_STRING == 0):
            for character in string:
                    if(CURRENT_RAW_COUNTER + count_character_columns(character) >= TOTAL_RAW_COUNTER):
                        new_line()
                        print_character(character)
                    else:
                        print_character(character)
        else:
            for character in string:
                    if(CURRENT_RAW_COUNTER + count_character_columns(character) >= TOTAL_RAW_COUNTER):
                        new_line()
                        print_character(character)
                    else:
                        print_character(character)
            for i in range(1024-FILL_DISPLAY_COUNTER):
                port.write(bytearray([0x40,0x00]))
            if(FILL_DISPLAY_COUNTER >= 896):
                flag=1
            FILL_DISPLAY_COUNTER=0
            CURRENT_RAW_COUNTER=0


def print_balance(numero):
    print_string('AVAILABLE BALANCE:',0)
    new_line()
    if(numero==0.000000e-308):
        print_string('0.00000',0)
    else:
        print_string(str(numero),0)
    print_string('€',0)
    new_line()
    new_line()
    print_string('USE TELEGRAM BOT FOR MORE ',0)
    new_line()
    print_string('INFO',1)

def print_last_opening(data):
    print_string('LAST OPENING:',0)
    new_line()
    print_string(str(data)[0:19],0)
    new_line()
    new_line()
    print_string('USE TELEGRAM BOT FOR MORE ',0)
    new_line()
    print_string('INFO',1)

def print_alert():
    print_string("WARNING",0)
    new_line()
    print_string("THE COMPARTMENT IS OPEN, DO NOT INSERT COINS",1)




    





