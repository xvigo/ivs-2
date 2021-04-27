#!/bin/sh

###################################################################
# Project name: Gazorpazorp calculator
# File: Makefile
# Authors: Pavel Marek
# Description: Makefile for GazorPazorp Calculator project
# Date: 30. 3. 2021
# Last Edit: 27. 04. 2021
###################################################################


#all (prelozit program)
all:
	sudo apt-get install python3
	sudo apt-get install python3-tk
	sudo apt-get install python3-pil python3-pil.imagetk
#pack (zabalí projekt tak, aby mohl být odevzdán)
pack: doc update-installer folder clean

#vytvori slozky install,repo, doc
folder:
	mkdir -p ../../xbilek25_xmarek75_xgottw07/repo
	mkdir ../../xbilek25_xmarek75_xgottw07/install
	mkdir ../../xbilek25_xmarek75_xgottw07/doc
	cp -a ../../ivs-2/. ../../xbilek25_xmarek75_xgottw07/repo/
	cp ../dokumentace.pdf ../../xbilek25_xmarek75_xgottw07/doc/
	cp -a ../installer/. ../../xbilek25_xmarek75_xgottw07/install/
	cd ../../xbilek25_xmarek75_xgottw07/repo && rm -rf installer
	cd ../.. && zip -r xbilek25_xmarek75_xgottw07.zip xbilek25_xmarek75_xgottw07
	cd ../.. && rm -rf xbilek25_xmarek75_xgottw07	
	
#clean (smaže všechny soubory, co nemají být odevzdány)
clean:
	#cd .. && rm -rf installer

#run (spustí program - lze předpokládat, že jej před tím někdo manuálně zkompiluje ve VS)
run:
	python3 gui.py
#profile (spustí program pro výpočet směrodatné odchylky s ukázkovým testovacím vstupem)
profile:
	echo "10 20 30 40 50" | python3 profiling.py 
#help (vypíše nápovědu s popisem, co je potřeba udělat před spuštěním programu)
help:
	$(info 	Programme can be installed only on Linux Ubuntu distribution.)
	$(info 	Before first run of the program run command "make all" in folder src)
#test spusti testy matematicke knihovny
test: LibMath_Tests.py
	python3 LibMath_Tests.py
#aktualizuje installer 	
update-installer:
	cp gui.py LibMath.py LibProcExpr.py ../installer/usr/share/gazorpazorp
	(cd ../installer; dpkg-deb --build ./ gapacalc_inst.deb)
#vygeneruje doxygen dokumentaci
doc:
