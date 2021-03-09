<?php

error_reporting(E_ALL);
ini_set('display_errors', 'On');
header('Content-Type: application/json');

$client = new SoapClient('http://localhost:8000/?WSDL');

$response = $client->say_hello(array('name' => 'Peeter', 'times' => '3'));

echo json_encode($response, JSON_PRETTY_PRINT);

?>