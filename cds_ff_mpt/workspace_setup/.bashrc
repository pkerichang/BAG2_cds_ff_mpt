#! /usr/bin/env bash

source /tools/flexlm/flexlm.sh

export SPECTRE_DEFAULTS=-E
export CDS_Netlisting_Mode="Analog"

# setup virtuoso
export CDS_INST_DIR=/tools/cadence/ICADV/ICADV123
export MMSIM_HOME=/tools/cadence/MMSIM/MMSIM151
export CDSHOME=$CDS_INST_DIR
export PVSHOME=/tools/cadence/PVS/PVS151
export QRC_HOME=/tools/cadence/EXT/EXT151
export IUSHOME=/tools/cadence/INCISIV/INCISIVE152
export AMSHOME=$IUSHOME

# PATH setup
export PATH="${QRC_HOME}/tools/bin:${PATH}"
export PATH="${PVSHOME}/tools/bin:${PATH}"
export PATH="${CDS_INST_DIR}/tools/plot/bin:${PATH}"
export PATH="${CDS_INST_DIR}/tools/dfII/bin:${PATH}"
export PATH="${CDS_INST_DIR}/tools/bin:${PATH}"
export PATH="${MMSIN_HOME}/tools/bin:${PATH}"

### Setup BAG
source .bashrc_bag
