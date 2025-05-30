# -*- coding: utf-8 -*-
"""
Created on Fri May 30 15:00:47 2025

@author: rodri
"""

def verificar_data_valida(data_str):
    try:
        partes = data_str.split('/')
        
        # Verificar se temos exatamente 3 partes
        if len(partes) != 3:
            return False
            
        dia = int(partes[0])
        mes = int(partes[1])
        ano = int(partes[2])
        
        if ano < 1 or mes < 1 or mes > 12 or dia < 1:
            return False
            
        # Meses com 31 dias
        if mes in [1, 3, 5, 7, 8, 10, 12]:
            return dia <= 31
            
        # Meses com 30 dias
        elif mes in [4, 6, 9, 11]:
            return dia <= 30
            
        # Fevereiro 
        else:  
            # Verificar se é ano bissexto
            if ano % 4 == 0:
                return dia <= 29
            else:
                return dia <= 28
                
    except (ValueError, IndexError):
        return False


data = input("Digite uma data no formato dia/mês/ano (ex: 28/2/1945): ")

if verificar_data_valida(data):
    print(f"{data} é uma data válida.")
else:
    print(f"{data} não é uma data válida.")