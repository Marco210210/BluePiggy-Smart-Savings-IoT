<?php
	// PRENDO I DATI
    include "config.php";
    #ini_set('error_reporting',E_ALL);
    $dieci=$_GET['dieci'];
    $venti=$_GET['venti'];
    $cinquanta=$_GET['cinquanta'];
    $uno=$_GET['uno'];
    $due=$_GET['due'];
    $saldo=$_GET['saldo'];
    $password=$_GET['password'];
	// PRENDO LA DATA E ORA ATTUALI
    echo $dieci." ".$venti." ".$cinquanta." ".$uno." ".$due." ".$password;
    // QUERY DI INSERIMENTO
    $connessione->query("UPDATE telegram SET dieci=$dieci,venti=$venti,cinquanta=$cinquanta,uno=$uno,due=$due,password='$password',saldo='$saldo';");
    
?>