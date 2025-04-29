<?php
    include "config.php";
    ini_set('error_reporting',E_ALL);
//INFPRMAZIONI TELEGRAM
    $botToken = "";
    $website = "https://api.telegram.org/bot".$botToken;

    $FilejSon = file_get_contents("php://input");
    $FilejSon = json_decode($FilejSon,TRUE);

//INFORMAZIONI UTENTE TELEGRAM E MESSAGGI

    $FirstName = $FilejSon["message"]["chat"]["first_name"]; // Get the name that user set
	$UserChatId = $FilejSon["message"]["chat"]["id"]; // get the User ID, this is unique
	$Message = $FilejSon["message"]["text"]; // Get the message sent from user
    

//GESTIONE MESSAGGI COMANDI


    switch(strtolower($Message))
    {
            case '/start':
				$msg = "Benvenuto in Blue Piggy!\n\nPer visualizzare il saldo disponibile e il numero di monete nella Blue Piggy scrivere 'saldo'.\nPer ottenere la password di apertura scrivere 'password'.";                
                sendMessage($UserChatId, $msg, "help");
				break;
                
           	case "chatid":
              $msg = $UserChatId;
              sendMessage($UserChatId, $msg, "help");
              break;

            case "saldo":
            	$Search = $connessione->query("SELECT dieci,venti,cinquanta,uno,due,saldo FROM telegram ");
                while ($Row = $Search->fetch_assoc())
                {
                	$saldo_tot=$Row['saldo'];
                    $msg="0,10€ : ".$Row['dieci']."\n0,20€ : ".$Row['venti']."\n0,50€ : ".$Row['cinquanta']."\n1,00€ : ".$Row['uno']."\n2,00€ : ".$Row['due']."\n\nSALDO : ".$saldo_tot."€";
                    sendMessage($UserChatId, $msg, "help");
                }
                break;
                
             case "password":
            	$Search = $connessione->query("SELECT password FROM telegram ");
                while ($Row = $Search->fetch_assoc())
                {
                	
                    $msg="Password: ".$Row['password'];
                    sendMessage($UserChatId, $msg, "help");
                }
                break;
              
            default:
            $Search = $connessione->query("SELECT dieci,venti,cinquanta,uno,due,password FROM telegram");
            while ($Row = $Search->fetch_assoc())
            {
            	$saldo_tot=$Row['dieci']*0.1+$Row['venti']*0.2+$Row['cinquanta']*0.5+$Row['uno']+$Row['due']*2;
            	echo "0,10€ : ".$Row['dieci']; 
                echo '<br>';
                echo "0,20€ : ".$Row['venti'];
                echo '<br>';
                echo "0,50€ : ".$Row['cinquanta'];
                echo '<br>';
                echo "1,00€ : ".$Row['uno'];
                echo '<br>';
                echo "2,00€ : ".$Row['due'];
                echo '<br>';
                echo '<br>';
                echo "SALDO : ".$saldo_tot;
            }
            sendMessage($UserChatId, $Text);
            break;

    }

    function sendMessage($chat_id, $text)
    {
        $url = $GLOBALS[website]."/sendMessage?chat_id=".$chat_id."&text=".urlencode($text);
        file_get_contents($url);
    }


?>
