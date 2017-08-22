#! /usr/local/bin/tcsh -f

setenv TSMCHOME /tools/tstech16/CLN16FFC/TSMCHOME
setenv TSMCPDK_OS_INSTALL_PATH /tools/tstech16/CLN16FFC/PDK

source /tools/flexlm/flexlm.cshrc

setenv SPECTRE_DEFAULTS -E
setenv CDS_Netlisting_Mode "Analog"

# setup virtuoso
#setenv CDS_INST_DIR /tools/cadence/ICADV/ICADV121
setenv CDS_INST_DIR /tools/cadence/ICADV/ICADV123
# setenv MMSIM_HOME   /tools/cadence/MMSIM/MMSIM131
setenv MMSIM_HOME   /tools/cadence/MMSIM/MMSIM151
setenv CDSHOME      $CDS_INST_DIR
setenv PVSHOME      /tools/cadence/PVS/PVS151
setenv QRC_HOME      /tools/cadence/EXT/EXT151
setenv IUSHOME      /tools/cadence/INCISIV/INCISIVE152
setenv AMSHOME      $IUSHOME

set path = ( $path \
    ${MMSIM_HOME}/tools/bin \
    ${CDS_INST_DIR}/tools/bin \
    ${CDS_INST_DIR}/tools/dfII/bin \
    ${CDS_INST_DIR}/tools/plot/bin \
    ${PVSHOME}/tools/bin \
    ${QRC_HOME}/tools/bin \
     )

# add open access
setenv OAROOT /tools/projects/eeis/BAG_2.0/oa_dist
setenv OA_LINK_DIR  ${OAROOT}/lib/linux_rhel50_gcc44x_64/opt
setenv OA_INCLUDE_DIR  ${OAROOT}/include/oa
setenv OALIB ${OA_LINK_DIR}

if ($?LD_LIBRARY_PATH) then
    setenv LD_LIBRARY_PATH "${OALIB}:${LD_LIBRARY_PATH}"
else
    setenv LD_LIBRARY_PATH "${OALIB}"
endif

### Setup BAG
source .cshrc_bag


