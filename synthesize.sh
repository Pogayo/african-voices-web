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

echo $input > file
$FLITEDIR/bin/flite  -voice $voice  file  $output.wav

#convert to audio format
if [ $format == "mp3" ]; then
    echo "Converting to wav"
    ffmpeg -i $output.wav  -f mp3 $output.mp3
    rm $output.wav
fi
