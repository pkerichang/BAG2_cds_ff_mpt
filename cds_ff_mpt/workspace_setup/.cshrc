#! /usr/local/bin/tcsh -f

source /tools/flexlm/flexlm.cshrc

setenv SPECTRE_DEFAULTS -E
setenv CDS_Netlisting_Mode "Analog"

# setup virtuoso
setenv CDS_INST_DIR /tools/cadence/ICADV/ICADV123
setenv MMSIM_HOME   /tools/cadence/MMSIM/MMSIM151
setenv CDSHOME      $CDS_INST_DIR
setenv PVSHOME      /tools/cadence/PVS/PVS151
setenv QRC_HOME      /tools/cadence/EXT/EXT151
setenv IUSHOME      /tools/cadence/INCISIV/INCISIVE152
setenv AMSHOME      $IUSHOME

set path = ( ${MMSIM_HOME}/tools/bin \
    ${CDS_INST_DIR}/tools/bin \
    ${CDS_INST_DIR}/tools/dfII/bin \
    ${CDS_INST_DIR}/tools/plot/bin \
    ${PVSHOME}/tools/bin \
    ${QRC_HOME}/tools/bin \
    $path \
     )

### Setup BAG
source .cshrc_bag
