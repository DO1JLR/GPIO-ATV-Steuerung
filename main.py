#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# https://github.com/DO1JLR/GPIO-ATV-Steuerung
#
# Licence: GPL-3.0
#
from sys import argv         # fuer die kommandozeilenargumente
from time import time, sleep # fuer zeit und so...
try:
    import RPi.GPIO as GPIO      # raspi gpio-pins
except:
    print("\nFehler beim Laden des GPIO Moduls.\n\tLaueft dieses Script auf einem Raspberry Pi 3?\n\tIst Python3 installiert?\n\tSind die GPIOs vorhanden?\n")
    print("\nWenn du der meinung bist, dass es sich hierbei um\n einen Fehler handelt, dann sag bescheid unter\n'https://github.com/DO1JLR/GPIO-ATV-Steuerung/issues'!\n\tDanke!\n\n")
    exit()
#
# Globale Variabeln:
#
version = "0.3"
debug = False

#
# GPIO Pin belegung: https://pinout.xyz/
#
# Erstmal definieren welche Pins Input sind...
inputpin = {
    "33": 0,
    "35": 0, 
    "37": 0, 
    "31": 0,
    "29": 0, 
    "21": 0,
    "23": 0, 
    "13": 0, 
    "15": 0, 
    "7":  0,
    "11": 0, 
    "19": 0, 
    "3": 0, 
}
# 
# Fuer jeden Output die Gruppe der Input-Pins:
#
output = [36, 32, 22, 15, 8, 12, 18, 5]
outputpin = {
    "36": [33, 35, 37],
    "32": [31, 29],
    "22": [21, 23],
    "15": [13, 15],
    "8":  [7],
    "12": [11],
    "18": [19],
    "5":  [3],
}
#
# Komandozeilenargumente Auslesen
#
for i in argv:
    if i in ["--help", "-h", "/h", "/help", "?", "h"]:
        print("\nMoegliche Befehle:\n -h\t--help   \tZeige diese Hilfe")
        print(" -v\t--version \tZeigt die Version dieser Software")
        print("\t--debug   \tAktiviere den Debugging Modus")
        exit()
    elif i in ["-v", "--version"]:
        print("Version:\t{0}\n".format(version))
        print("Dieser Code wird verwaltet via GitHub unter:\n'https://github.com/DO1JLR/GPIO-ATV-Steuerung'.\n\nIst etwas kaputt?\nDann reparier es doch oder sag zumindest beschei unter 'https://github.com/DO1JLR/GPIO-ATV-Steuerung/issues'")
        exit()
    elif i == "--debug":
        debug = True
        print("\n[I] Aktiviere den Debugging-Modus!\n\n")

#
# Den eigendlichen Code des Programmes:
#
def main():
    #
    # GPIOs einstellen
    # https://sourceforge.net/p/raspberry-gpio-python/wiki/Inputs/
    #
    GPIO.setwarnings(False) #  Keine nerfigen sinnlosen Meldungen
    GPIO.setmode(GPIO.BOARD) # Nutze BOARD nicht BCM.
    if debug: print("[I] Einrichten der Raspberry Pi GPIOs:")
    for key, value in inputpin.items():
        if debug: print("    Input: " + str(key) )
        GPIO.setup(int(key), GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    for key in output:
        if debug: print("    Output: " + str(key) )
        GPIO.setup(key, GPIO.OUT)
                
    if debug: print("[I] Konfigurien der GPIOs abgeschlossen\n[I] Starte 'while True'-Schleife\n")
    while True:
        sleep(0.1)
        #
        # ermittle GPIO Input Signale
        #  ...und schreibe sie in die RX Liste!
        #
        i = 0
        for key, value in inputpin.items():
            value = GPIO.input(int(key))
            if debug: print("GPIO Input: " + str(key) + " = " + str(value))

        #
        # Schalte GPIO Output
        #
        for key in output:
            makeOutput = True
            if debug: print(key)
            for a, i in outputpin.items():
                if a == key:
                    if debug: print("GPIO Output: " + str(key) + " - benoetigt wird " + str(i))
                    if (inputpin[int(i)] == 0):
                        makeOutput = False
            if makeOutput == True:
                print("Setze den Output... [BALD]")
                
            



        

#
# main() ausführen
#
try:
    main()
except KeyboardInterrupt:
    if debug: print("\n[I] KeyboardInterrupt erkannt\n")
    print("\n\nProgramm wird abgebrochen!\n\n Auf Wiedersehen...\n\n")
    exit()
