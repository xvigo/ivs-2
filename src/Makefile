#!/bin/sh

###################################################################
# Project name: Gazorpazorp calculator
# File: Makefile
# Authors: Pavel Marek
# Description: Makefile for idk
# Date: 30. 3. 2020
###################################################################


#all (spustí progam)
all:
	python3 gui.py
#pack (zabalí projekt tak, aby mohl být odevzdán)
pack:
#clean (smaže všechny soubory, co nemají být odevzdány)
clean:
#run (spustí program - lze předpokládat, že jej před tím někdo manuálně zkompiluje ve VS)
run:
#profile (spustí program pro výpočet směrodatné odchylky s ukázkovým testovacím vstupem)
profile:
	python3 profilling.py <"10 20 30 40" 
#help (vypíše nápovědu s popisem, co je potřeba udělat před spuštěním programu)
help:
	$(info Program is ready to run)
#test spusti testy matematicke knihovny
test: LibMath_Tests.py
	python3 LibMath_Tests.py

# install
# sudo apt-get install python3-tk
# sudo apt-get install python3-pil python3-pil.imagetk
