#!/usr/bin/env bash
#vis_denoise.sh

qiime metadata tabulate \
  --m-input-file stats-dada2.qza \
  --o-visualization stats-dada2.qzv


