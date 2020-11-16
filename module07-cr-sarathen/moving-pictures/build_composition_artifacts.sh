#/!usr/bin/env bash
#build_composition_artifacts.sh

qiime composition add-pseudocount \
  --i-table gut-table.qza \
  --o-composition-table comp-gut-table.qza

qiime composition ancom \
  --i-table comp-gut-table.qza \
  --m-metadata-file sample-metadata.tsv \
  --m-metadata-column subject \
  --o-visualization ancom-subject.qzv

