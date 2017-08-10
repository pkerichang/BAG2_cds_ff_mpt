#!/bin/tcsh

setenv PYTHONPATH ""

# disable QT session manager warnings
unsetenv SESSION_MANAGER

exec ${BAG_PYTHON} -m IPython # $argv:q
