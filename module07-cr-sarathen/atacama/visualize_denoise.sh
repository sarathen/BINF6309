#!/usr/bin/env bash
#visualize_denoise.sh


qiime metadata tabulate \
  --m-input-file denoising-stats.qza \
  --o-visualization denoising-stats.qzv
