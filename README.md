# BAG2_cds_ff_mpt
BAG2 setup for cds_ff_mpt (cadence generic PDK for finfet and multi-patterned technology)

## Installation
1. Download cds_ff_mpt PDK from [Cadence Support](https://support.cadence.com) 
and install it.

2. Clone BAG2_cds_ff_mpt repo.

    ```
    $ git clone git@github.com:ucb-art/BAG2_cds_ff_mpt.git
    ```
    
3. Update the PDK symbolic link to point the cds_ff_mpt installation path. 
For BWRC users, the link is already set to point the correct path.

4. Open following files and update path variables.

  * .cshrc
  * .cshrc_bag
  * cds.lib
  * cds_ff_mpt/corners_setup.sdb

5. The BAG2_cds_ff_mpt repo has 2 submodules in it: BAG_framework and
laygo. Let's update the submodules. Go into the BAG2_cds_ff_mpt
directory and type this:

    ```
    $ git submodule init
    $ git submodule update
    $ git submodule foreach git pull origin master
    ```
