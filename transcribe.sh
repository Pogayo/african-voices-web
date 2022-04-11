#!/bin/bash

echo " ***** Yes I got your command, synthesizing now *****"

export ESTDIR=/Users/ogayo/dev/build/speech_tools
export FLITEDIR=/Users/ogayo/dev/build/flite
export FESTVOXDIR=/Users/ogayo/dev/build/festvox
export SPTKDIR=/Users/ogayo/dev/build/SPTK


while getopts v:i:o: flag
do
    case "${flag}" in
        v) voice=${OPTARG};;
        i) input=${OPTARG};;
        o) output=${OPTARG};;
    esac
done
echo "voice: $voice";
echo "input: $input";
echo "output: $output";

echo $input > file
  $FLITEDIR/bin/flite  -voice $voice  file  $output