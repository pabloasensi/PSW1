#!/bin/bash
if [[ $1 = "-c" ]]; then
	java -jar jplag.jar -vq -l $2 -s $3 ; python batchparse.py;
	
elif [[ $1 = "-s" ]]; then
	cp -r $3 ./aux/ ;
	cp -r $4 ./aux/ ;
	java -jar jplag.jar -vq -l $2 -s ./aux/;
	python parse.py;
	rm -rf aux;
fi
