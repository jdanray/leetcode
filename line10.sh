#!/bin/bash

i=1
while IFS= read -r line; do
	if [ $i -eq 10 ]
	then
		echo "$line"
	fi
	let i++
done < file.txt
