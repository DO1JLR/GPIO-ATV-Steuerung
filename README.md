# GPIO-ATV-Steuerung
Zur Steuerung der GPIO Signale für den ATV Sender

## Bekannte Angaben:

Es gibt mehrere Signale, die als GPIO Input vom Raspberry Pi gelesen werden. Wenn bei allen der Signale ein Signal sein soll, dann soll der Raspberry Pi dort ein Outputsignal geben.

# Setup:
*Wie wird das Programm installiert* ***(bei Internet in der Bash auf dem Raspberry Pi)***

```bash
# Pakete aktualisieren:
sudo apt update
sudo apt upgrade -y
sudo apt install -y git vim tmux python3 
echo -e "set expandtab\nset tabstop=4\
  \nset shiftwidth=4\nset fileencoding=utf-8\ 
  \nset encoding=utf-8\ncolorscheme elflord\
  \nsyntax on" > ~/.vimrc

# Projekt herunterladen:
git clone https://github.com/DO1JLR/GPIO-ATV-Steuerung.git

# Hilfetext:
~/GPIO-ATV-Steuerung/main.py --help

# Programm Ausführen:
~/GPIO-ATV-Steuerung/main.py 
```

## Updaten

```bash
# Aktualisieren des Programms:
cd ~/GPIO-ATV-Steuerung
git pull
```

# Update ohne Netzwerkanbindung:

Herunterladen des letzten Releases: [Download](https://github.com/DO1JLR/GPIO-ATV-Steuerung/releases/latest)

# Weitere Informationen
Als erstes erkennt das Programm, welche Pins ein Input Signal haben. Basierend darauf wird dann ein oder kein Signal gegeben.
**[Pinbelegung](https://de.pinout.xyz/)**
*Tipp: Es wird die Kategorie: "Physical Pin" verwendet.*

```
Es gibt 4 Eingänge mit 1 Anschluss
Es gibt 3 Eingänge mit 2 Anschlüssen
Es gibt 1 Eingang mit 3 Anschlüssen
```
### 3 Eingänge:
| **GPIO-Input** | **GPIO-Output** |
|:--------------:|:---------------:|
|  33            |                 |
|  35            | 36              |
|  37            |                 |

### 2 Eingänge:
| **GPIO-Input** | **GPIO-Output** |
|:--------------:|:---------------:|
|  31            | 32              |
|  29            |                 |

| **GPIO-Input** | **GPIO-Output** |
|:--------------:|:---------------:|
|  21            | 22              |
|  23            |                 |


| **GPIO-Input** | **GPIO-Output** |
|:--------------:|:---------------:|
|  13            | 16              |
|  15            |                 |


### 1 Eingang:

| **GPIO-Input** | **GPIO-Output** |
|:--------------:|:---------------:|
|  7             | 8              |

| **GPIO-Input** | **GPIO-Output** |
|:--------------:|:---------------:|
|  11            | 12              |

| **GPIO-Input** | **GPIO-Output** |
|:--------------:|:---------------:|
|  19            | 18              |

| **GPIO-Input** | **GPIO-Output** |
|:--------------:|:---------------:|
|  3             | 5               |


