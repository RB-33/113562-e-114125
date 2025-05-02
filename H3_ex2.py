# -*- coding: utf-8 -*-
"""
Created on Fri Mar 14 14:09:37 2025

@author: Rodrigo Barradas
"""

def main():
 
 print("This program calculates the future value of a n−year investment.")
 principal = eval(input("Enter the initial principal: "))
 apr = eval(input("Enter the annual interest rate in perecents: "))
 year = eval(input("Enter the length of investment in years: "))
 for i in range (year):
  principal = principal * (1 + (apr * .01))
 print("The value in", year, "years is", principal,"€")

main()
