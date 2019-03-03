#!/bin/bash

# for clas in *
# do
# 	class_type=$(echo $clas | sed 's/ //g')
#  	cd $clas
# 	for f in *\ *; do mv "$f" "${f// /_}"; done
# 	cd annotations
# 	for f in *\ *; do mv "$f" "${f// /_}"; done
# 	cd ..
# done
# exit 0

for clas in $(echo javelina person fox)
do
  class_type=$(echo $clas | sed 's/ //g')
  cd $clas
  for f in *
  do
    uuid=$(uuidgen)
    base=$(echo $f | sed 's/.$//')
    filename=$(basename -- "$f")
	extension="${f##*.}"
	filename="${f%.*}"
	base="${f%%.*}"

    echo mv ${base}.${extension} ../../cleaned_training_photos/${class_type}-${uuid}.${extension}
    echo mv ${base}.${extension} ../../cleaned_training_photos/${class_type}-${uuid}.xml
    mv ${base}.xml ../../cleaned_training_photos/${class_type}-${uuid}.xml
    if [[ $? -gt 0 ]]; then
    	echo Skipping mv ${base}.${extension}
    else 
	  	mv ${base}.${extension} ../../cleaned_training_photos/${class_type}-${uuid}.${extension}
	    if [[ $? -gt 0 ]]; then
	    	echo error
	    	mv ../../cleaned_training_photos/${class_type}-${uuid}.xml annotations/${base}.xml 
	    	exit 1
	    fi
	fi
    # read dum	
  done
  cd ..
done