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
    ```

## Running BAG

Once you finish setting up the workspace, try to run the demo as follows:

1. in the directory, run the following command

   ```
   $ source .cshrc
   ```

   to set up environment variables for running BAG/Virtuoso.  This needs to be done everytime you st   art a new terminal.

2. start virtuoso

   ```
   $ virtuoso &
   ```

3. in virtuoso CIW window, run

   ```
   load("start_bag.il")
   ```
   
4. in the terminal, run

   ```
   $ ./start_bag.sh
   ```

   this will start a IPython interactive session.

5. in the IPython interpreter, run:

   ```
   In [1]: run -i BAG_XBase_demo/demo_scrpts/bootcamp_demo.py
   ```

   if everything works correctly, a DEMO_AMP_CS library will be generated with a schematic
   and layout of a common-source amplifier, and two testbenches will be created.  3 plots
   will also pop up displaying the testbench simulation results.
