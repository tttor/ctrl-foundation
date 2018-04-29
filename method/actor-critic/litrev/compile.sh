#!/bin/sh

ROOT_TEX=main
BUILD_DIR=/home/tor/tmp/build-litrevactorcritic
OUT_DIR=/home/tor/tmp
OUT_FNAME=litrevactorcritic_vektor.pdf

mkdir -p $BUILD_DIR
rm -rf $BUILD_DIR/*

cp -r ./* $BUILD_DIR/

cd $BUILD_DIR
pdflatex $ROOT_TEX.tex
bibtex $ROOT_TEX.aux
pdflatex $ROOT_TEX.tex
pdflatex $ROOT_TEX.tex

cp $ROOT_TEX.pdf $OUT_DIR/$OUT_FNAME
