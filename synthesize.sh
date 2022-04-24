#!/bin/bash

echo " ***** Yes I got your command, synthesizing now *****"

export ESTDIR=/Users/ogayo/dev/build/speech_tools
export FLITEDIR=/Users/ogayo/dev/build/flite
export FESTVOXDIR=/Users/ogayo/dev/build/festvox
export SPTKDIR=/Users/ogayo/dev/build/SPTK


while getopts v:i:o:f: flag
do
    case "${flag}" in
        v) voice=${OPTARG};;
        i) input=${OPTARG};;
        o) output=${OPTARG};;
        f) format=${OPTARG};;
    esac
done
echo "voice: $voice";
echo "input: $input";
echo "output: $output";

echo $input > $output.txt
_$voice  $output.txt $output.wav

#convert to audio format
if [ $format == "mp3" ]; then
    echo "Converting to mp3"
    ffmpeg -i $output.wav  -f mp3 $output.mp3\
    echo "finished converting"
    rm $output.wav
fi
rm -r $output.txt

Ṣé dáadáa ni