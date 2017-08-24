# BAG2_cds_ff_mpt
BAG2 setup for cds_ff_mpt (cadence generic PDK for finfet and multi-patterned technology)

## Installation
1. Download cds_ff_mpt PDK from [Cadence Support](https://support.cadence.com) 
and install it.

2. Clone BAG2_cds_ff_mpt repo.

    ```
    $ git clone https://github.com/ucb-art/BAG2_cds_ff_mpt.git
    ```
3. (non-BWRC users) Update the following symbolic links to point to the cds_ff_mpt PDK installation location.
   For BWRC useres, the links are already pointed to the correct path.

   PDK -> point to cds_ff_mpt_v_0.3 folder
   cds_ff_mpt/pvs_setup/pvs_rules -> point to cds_ff_mpt_v_0.3/pvs/pvsLVS.rul

4. (non-BWRC users) Update .cshrc to point to your tools locations.
   The tools needed by this demo are:

   - Virtuoso ICADV 12.3 (or 12.1)
   - PVS 15.1
   - (Optional) OpenAccess 2.2
   
5. (non-BWRC users) Update .cshrc_bag to point to the Anaconda Python installation location used to
   run BAG.  See BAG_framework documentation on how to install Anaconda Python for BAG.

6. (non-BWRC users) Update cds.lib.core to point to avTech library.

7. (non-BWRC users) Update cds_ff_mpt.corners_setup.sdb, which sets up model files and process corners for BAG,
   to point to the correct model file location.

8. Clone all dependent git submodules.  Run the following commands:

    ```
    $ git submodule init
    $ git submodule update
    $ git submodule foreach git pull origin master
    ```

