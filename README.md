# GPIO-ATV-Steuerung
Zur Steuerung der GPIO Signale für den ATV Sender

# Setup:

```bash
# Pakete aktualisieren:
sudo apt update
sudo apt upgrade -y
sudo apt install -y git vim tmux python3 
echo -e "set expandtab\nset tabstop=4\
  \nset shiftwidth=4\nset fileencoding=utf-8\ 
  \nset encoding=utf-8\ncolorscheme elflord\
  \nsyntax on" > ~/.vimrc

# Git clonen:
git clone https://github.com/DO1JLR/GPIO-ATV-Steuerung.git

# Hilfetext:
~/GPIO-ATV-Steuerung/main.py --help

# Programm Ausführen:
~/GPIO-ATV-Steuerung/main.py 
```

# Updaten

```bash
# Aktualisieren des Programms:
cd ~/GPIO-ATV-Steuerung
git pull
```

# Weitere Informationen
Als erstes erkennt das Programm, welche der Pins ein Signal haben.
## Input-Pins:
| **Funktion** | **Pin** |
| Input  | 31  |
| Input  | 33  |
| Input  | 35  |
| Input  | 37  |

Diese Pins werden als Binärzahl gespeichert *(0b0000 bis 0b1111)*
     Liste 'binary': Key: 0b1110, Value: False
     Liste 'binary': Key: 0b1000, Value: False
     Liste 'binary': Key: 0b1011, Value: False
     Liste 'binary': Key: 0b1001, Value: False
     Liste 'binary': Key: 0b1010, Value: False
     Liste 'binary': Key: 0b0110, Value: False
     Liste 'binary': Key: 0b0010, Value: False
     Liste 'binary': Key: 0b0001, Value: False
     Liste 'binary': Key: 0b0111, Value: False
     Liste 'binary': Key: 0b1101, Value: False
     Liste 'binary': Key: 0b0000, Value: True
     Liste 'binary': Key: 0b0100, Value: False
     Liste 'binary': Key: 0b0101, Value: False
     Liste 'binary': Key: 0b0011, Value: False
     Liste 'binary': Key: 0b1100, Value: False
     Liste 'binary': Key: 0b1111, Value: False
