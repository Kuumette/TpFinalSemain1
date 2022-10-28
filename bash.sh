#!/bin/bash

if [ `find . -type f | wc -l` -ge 10 ]; then
	echo "Plus de 10 Fichier"
elif [ `find . -type f | wc -l` -lt 10 ]; then
 	echo "Moins de 10 Fichier"
fi