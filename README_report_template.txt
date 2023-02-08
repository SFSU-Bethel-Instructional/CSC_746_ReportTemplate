
# CSC_746_ReportTemplate Latex Template
W. Bethel, SFSU
Feb 2023

## Overview

This distribution contains several types of files -- LaTeX sources, an image file, scripts and source data to generate matplotlib plots -- that form a "generic tech paper" skeleton.

The intention is for you to begin with this template, and then add your own content into the sections provided. There are some hints of the kind of content to go into each section.

Writing tip: as you compose your own content, focus on articulating your ideas as clearly and succinctly as possible. Don't use 100 words when 10 will do. 

Writing tip: try to compose paragraphs where you lead off with a main idea, then limit yourself to no more than 5-6 sentences to fill out the paragraph. 

## Building a PDF from these LaTeX sources

One option is to import these files into your own project on Overleaf.com. 

Another option is to manually build the PDF from the command line:
% pdflatex 00_main
% bibtex 00_main
% pdflatex 00_main
% pdflatex 00_main

On MacOS and using homebrew, these commands are part of the mactex cask (e.g., brew install mactex). 
