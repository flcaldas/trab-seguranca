# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""
import re 
import time
from dialog import Dialog
import cifrar as ci
import ICMP_Ping as ipi
import io
from contextlib import redirect_stdout
# re module provides support 
# for regular expressions 

  
# Make a regular expression 
# for validating an Ip-address 

      
# Define a function for 
# validate an Ip addess 
def check(Ip):  
    regex = '''^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)'''
    # pass the regular expression 
    # and the string in search() method 
    if(re.search(regex, Ip)):  
        return True 
          
    else:  
        return False 

def tela():
    d = Dialog() 
    code, ip = d.inputbox("Informe o Endereço IP de destino", height=10, width=45,title="Enviando Dados Cifrados por ICMP")
    while True:
        if check(ip):
            d.infobox("Parabens")
            break
        else:
            code, ip = d.inputbox("Endereço IP Invalido, favor informar um IP de destino válido", height=10, width=45,title="Enviando Dados Cifrados por ICMP")
    code, msg = d.inputbox("Informe a mensagem que deseja cifrar", height=10, width=45,title="Enviando Dados Cifrados por ICMP")
    with io.StringIO() as buf, redirect_stdout(buf):
        ipi.remote_test(ip,msg)
        output = buf.getvalue()
    d.infobox(output,title="Resultado do Ping ",height=14,width=45)

if __name__ == '__main__':
    
    tela()
    


        