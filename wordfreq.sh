#!/bin/bash

declare -A count

while read line; do
	for word in $line; do
		if [ ${count[$word]+_} ]; then
			count[$word]=$((count[$word] + 1))
		else
			count[$word]=1
		fi
	done
done < words.txt

for word in "${!count[@]}"; do
	echo $word ${count[$word]};
done | sort -rn -k2

# The above script is my solution
# After I solve a problem, I like to study other people's solutions
# I found a very elegant one-liner here: https://leetcode.com/problems/word-frequency/discuss/55443/My-simple-solution-(one-line-with-pipe)

cat words.txt | tr -s ' ' '\n' | sort | uniq -c | sort -r | awk '{ print $2, $1 }'
