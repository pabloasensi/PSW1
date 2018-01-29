#!/bin/bash
if [[ $1 = "-c" ]]; then
	java -jar jplag.jar -l $2 -s $3 ; python batchparse.py;
	echo -n "Would you like to remove the results folder? (Y/N) ";
	read answer
	if echo "$answer" | grep -iq "^y" ; then
	rm -rf result;
	fi
	
elif [[ $1 = "-s" ]]; then
	cp -r $3 ./aux/ ;
	cp -r $4 ./aux/ ;
	java -jar jplag.jar -l $2 -s ./aux/;
	python parse.py;
	echo -n "Would you like to show the code? (Y/N) ";
	read answer
	if echo "$answer" | grep -iq "^y" ; then
	python codedisplay.py;
	fi

	echo -n "Would you like to remove the results folder? (Y/N) ";
	read answer
	if echo "$answer" | grep -iq "^y" ; then
	rm -rf result;
	fi

	rm -rf aux;
fi
