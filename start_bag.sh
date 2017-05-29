#!/bin/tcsh

setenv PYTHONPATH "${BAG_TECH_CONFIG_DIR}:${BAG_FRAMEWORK}:."
#setenv PYTHONPATH "${BAG_WORK_DIR}/adc_bag:${BAG_WORK_DIR}/BAG2_TEMPLATES_EC:${BAG_WORK_DIR}/bag_serdes_burst_mode:${BAG_TECH_CONFIG_DIR}:${BAG_FRAMEWORK}:."
# setenv PYTHONPATH "${OAROOT}/Si2oaScript-v3.1/python:${PYTHONPATH}"

# disable QT session manager warnings
unsetenv SESSION_MANAGER

# set cmd = "/tools/projects/erichang/programs/anaconda2/bin/ipython"
#set cmd = "/tools/projects/erichang/programs/anaconda3/bin/ipython"
# set cmd = "/tools/projects/erichang/programs/anaconda2/bin/jupyter qtconsole"
#exec $cmd # -m bag.io.gui
exec ${BAG_PYTHON} -m IPython # $argv:q
