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
version = "0.1"
debug = False

#
# GPIO Pin belegung: https://pinout.xyz/
#
pins = {
    "input": [31, 33, 35, 37],  # Input-Pins
    "RX": [0, 0, 0, 0],         # Input-Values
    "output": [3, 5, 7],  # Output-Pins
    "TX":  [0, 0, 0],     # Output-Values
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
    for key, value in pins.items():
        if debug: print("    " + key + " " + str(value) )
        if key == "input":
            for i in value:
                GPIO.setup(i, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        elif key == "output":
            for i in value:
                GPIO.setup(i, GPIO.OUT)
                
    if debug: print("[I] Konfigurien der GPIOs abgeschlossen\n[I] Starte 'while True'-Schleife\n")
    while True:
        sleep(0.1)
        #
        # ermittle GPIO Input Signale
        #
        i = 0
        while i < len(pins["input"]):
            pins["RX"][i] = GPIO.input(pins["input"][i])
            if debug: print("GPIO Input: " + str(pins["input"][i]) + " = " + str(pins["RX"][i]))
            i = i + 1


        #
        # Schalte GPIO Output
        #




        

#
# main() ausführen
#
try:
    main()
except KeyboardInterrupt:
    if debug: print("\n[I] KeyboardInterrupt erkannt\n")
    print("\n\nProgramm wird abgebrochen!\n\n Auf Wiedersehen...\n\n")
    exit()
