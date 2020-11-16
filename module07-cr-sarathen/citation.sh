#!/usr/bin/env bash
#citation.sh

R -e "rmarkdown::render('citation.Rmd', output_format='all')"
