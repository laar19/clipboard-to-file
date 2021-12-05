# Clipboard to file

## Based gui application that copy every change from clipboard to a text file

## Luis Acevedo  <laar@pm.me>

## Technical information:

- Developed in python 3.8
- PySide2 as graphic library
- Distributed under the GNU General Public License (GPLv3)

## Binaries and installers
https://sourceforge.net/projects/clipboard-to-file/
		
## Edit and testing:
### Anaconda
1.- Clone or download this repository   
2.- Creating a new virtual environment: __conda env create -n    env_name -f environment.yml__   
3.- Activate the environment   
4.- Launch the application: __python main.py__   

## Pyinstaller build
### Linux and windows
1.- pyinstaller --noconsole --icon=ui/resources/img/icon.ico main.py   
2.- Copy __/ui__ folder into __main__ folder generated   