##############################################################################################################
#####  
#####                                         PVS LVS COMPARISON
#####  
#####  Version                       :   15.17-s604
#####  NVN Run Start                 :   Thu Jun  1 20:55:24 2017
#####  ERC Summary File              :   latch_2ck_2x.sum
#####  Extraction Report File        :   latch_2ck_2x.rep
#####  Comparison Report File        :   latch_2ck_2x.rep.cls
#####  Top Cell                      :   latch_2ck_2x  <vs>  latch_2ck_2x
#####  
#####                                :      @     @
#####                                :       @   @ 
#####                                :        @ @  
#####  Run Result                    :     MISMATCH
#####                                :        @ @  
#####                                :       @   @ 
#####                                :      @     @
#####  
#####  Run Summary                   :   [ERROR] Connectivity Mismatches
#####                                :   [ERROR] Parameter Mismatches
#####                                :   [INFO]  ERC Results: Empty
#####                                :   [INFO]  Extraction Clean
#####  
#####  Layout Design                 :   cds_ff_mpt_logic_templates latch_2ck_2x layout
#####  Schematic File                :   /tools/projects/jdhan/BAG/BAG2_cds_ff_mpt/pvs_run/latch_2ck_2x.cdl (cdl)
#####  Rules File                    :   .technology.rul
#####  Pin Swap File                 :   latch_2ck_2x.rep.cps
#####  
#####  Extraction CPU Time           :   0h 0m 0s - (0s)
#####  Extraction Exec Time          :   0h 0m 0s - (0s)
#####  Extraction Peak Memory Usage  :   17.00MB
#####  NVN CPU Time                  :   0h 0m 0s - (0s)                 
#####  NVN Exec Time                 :   0h 0m 2s - (2s)                 
#####  NVN Peak Memory Usage         :   220.35MB
#####  LVS Total CPU Time            :   0h 0m 0s - (0s)                 
#####  LVS Total Exec Time           :   0h 0m 2s - (2s)                 
#####  LVS Total Peak Memory Usage   :   220.35MB
#####  
##############################################################################################################


##############################################################################################################
#
#                                            CELL MATCH STATISTICS                                            
#
##############################################################################################################

Cell Statistic Descriptions                  | Count
---------------------------------------------+----------
Cells matched                                |         0
Cells expanded                               |         0
Cells not run                                |         0
Cells which mismatch                         |         1
---------------------------------------------+----------
Total                                        |         1


Cell Statistic Detail                        | Count
---------------------------------------------+----------
Cells with parameter mismatches              |         1
Cells with mismatched instance subtypes      |         0
Cells that have been blackboxed              |         0


##############################################################################################################
#
#                                             CELL MATCH SUMMARY                                              
#
##############################################################################################################

                 |     Initial Pins     |     Compare Pins     |              | 
Cell             |   lay    :    sch    |   lay    :    sch    | Status       | Detail
-----------------+----------+-----------+----------+-----------+--------------+-----------
latch_2ck_2x     |        6 :         6 |        6 :         6 | mismatch     | 


##############################################################################################################
#
#                                                  LVS RULES                                                  
#
##############################################################################################################

Command Line LVS Rule Values
----------------------------

    layout_primary                          latch_2ck_2x {-top_cell latch_2ck_2x}
    schematic_primary                       latch_2ck_2x {-source_top_cell latch_2ck_2x}

LVS Rules Given in the Rules File
---------------------------------

    lvs_abort                               -softchk      no  
    lvs_abort                               -supply_error no  
    layout_path                             /tools/projects/jdhan/BAG/BAG2_cds_ff_mpt/pvs_run/latch_2ck_2x.gds
    layout_format                           gdsii
    schematic_path                          /tools/projects/jdhan/BAG/BAG2_cds_ff_mpt/pvs_run/latch_2ck_2x.cdl
    schematic_format                        cdl
    lvs_write_netlist                       -layout lvs.sp
    lvs_write_netlist                       -source sch.sp
                                             
    lvs_ignore_ports                        no  
    lvs_compare_port_names                  no  
    lvs_find_shorts                         no  
    lvs_break_ambig_max                     32
                                             
    lvs_reduce_split_gates                  yes ...
    lvs_recognize_gates                     -all
    lvs_reduce                              yes -parallel_mos ...
    lvs_reduce_device                       C ( cmim ) -series PLUS MINUS no 
    lvs_reduce_device                       C ( cmim ) -parallel yes ...
                                             
    lvs_expand_cell_on_error                no  
                                             
    lvs_check_property                      R r r -tolerance 0
    lvs_check_property                      R l l -tolerance 0 -absolute
    lvs_check_property                      R w w -tolerance 0 -absolute
    lvs_check_property                      C ( cmim ) w w -absolute -tolerance 0
    lvs_check_property                      C ( cmim ) l l -absolute -tolerance 0
    lvs_check_property                      C ( cmim ) c c -tolerance 0
    lvs_check_property                      Q ( npn ) A A -absolute -tolerance 0
    lvs_check_property                      D A A -tolerance 0 -absolute
    lvs_check_property                      D P P -tolerance 0 -absolute
    lvs_check_property                      MN l l -absolute -tolerance 0
    lvs_check_property                      MN nf nf -absolute -tolerance 0
    lvs_check_property                      MN nfin nfin -absolute -tolerance 0
    lvs_check_property                      MP l l -absolute -tolerance 0
    lvs_check_property                      MP nf nf -absolute -tolerance 0
    lvs_check_property                      MP nfin nfin -absolute -tolerance 0
    lvs_report_file                         latch_2ck_2x.rep
    lvs_report_max                          50 -mismatched_net_limit 100 
    unit                                    -length u
    input_scale                             2000
    virtual_connect                         no  -colon
    virtual_connect                         yes -semicolon_as_colon
    virtual_connect                         no  -report
    virtual_connect                         -depth primary
                                             

Default LVS Rule Values
-----------------------

    layout_case_sensitive                   no
    // layout_cpf_file                       
    // schematic_cpf_file                    
    schematic_case_sensitive                no
    // hcell_file                            
    // hcell                                 
    // lvs_exclude_hcell                     
    lvs_push_devices                        yes
    lvs_push_devices_properties             no
    lvs_netlist                             yes -substrate_comment
    lvs_netlist                             yes -box_contents
    lvs_netlist                             yes -unnamed_box_pins
    lvs_netlist                             no -allow_inconsistent_model
    // lvs_write_netlist_reduced             
    // lvs_delete_cell_pin                   
    // lvs_black_box                         
    lvs_spice                               yes -allow_floating_pins
    lvs_spice                               yes -allow_duplicate_subcircuit_names
    lvs_spice                               no  -conditional_ldd
    lvs_spice                               no  -prefer_pins
    lvs_spice                               no  -override_globals
    lvs_spice                               no  -redefine_param
    lvs_spice                               no  -replicate_devices
    lvs_spice                               yes -slash_is_space
    lvs_spice                               yes -keep_back_slash
    lvs_spice                               no  -allow_unquoted_strings
    lvs_spice                               no  -allow_inline_parameters
    lvs_spice                               no  -calculate_mos_area
    lvs_spice                               no  -strict_wl
    lvs_spice                               no  -cull_primitive_subcircuits
    lvs_spice                               no  -ignore_option_scale
    lvs_spice                               no  -show_neg_param_warning
    lvs_spice                               no  -scale_x_parameters
    // lvs_spice_option                      
    lvs_reverse_wl                          no
    // lvs_spice_multiplier_name             
                                             
    lvs_compare_case                        no
    lvs_cname                               no  -cell
    lvs_cname                               yes -pin
    lvs_cname                               yes -net
    lvs_cname                               no  -instance
    lvs_non_user_name                       -port "^[0-9]+$"
    lvs_non_user_name                       -net  "^[0-9]+$"
    // lvs_non_user_name                    -instance 
    lvs_out_of_range_exclude_zero           no
    // lvs_group_models                      
    lvs_strict_subtypes                     no
    // lvs_cpoint                            
    // lvs_power_name                        
    // lvs_ground_name                       
    // lvs_cell_list                         
    // lvs_device_type                       
                                             
    lvs_auto_pin_swap                       yes -swap_threshold 4000000
    lvs_swap_non_cpoint_pins                yes
    // lvs_swap_pins                         
    lvs_all_cap_pins_swappable              no
    lvs_builtin_device_pin_swap             yes
    // lvs_join_nets                         
    lvs_global_sigs_are_ports               yes
    lvs_discard_pins                        no
                                             
    lvs_filter                              no  -bipolar
    lvs_filter                              no  -capacitors
    lvs_filter                              no  -diodes
    lvs_filter                              no  -mos
    lvs_filter                              no  -resistors
    // lvs_filter_option                     
    // lvs_filter_device                     
                                             
    lvs_reduction_priority                  -parallel
    lvs_derive_logic                        yes -sram
    lvs_derive_logic                        no  -dram
    lvs_derive_logic                        no  -rom
    // lvs_recognize_gates_tolerance         
    lvs_reduce                              yes -parallel_bipolar
    lvs_reduce                              yes -parallel_caps
    lvs_reduce                              yes -series_caps
    lvs_reduce                              yes -parallel_diodes
    lvs_reduce                              no  -series_diodes
    lvs_reduce                              no  -series_mos
    lvs_reduce                              yes -parallel_resistors
    lvs_reduce                              yes -series_resistors
    // lvs_reduce_do_not_merge               
                                             
    lvs_expand_on_device_climbing           no
    lvs_expand_unbalanced_cells             yes
                                             
    // lvs_property_map                      
    // lvs_report_opt                        
    lvs_report_units                        yes
    lvs_keep_data                           no
    lvs_keep_source_cells                   no
    lvs_create_match_db                     no
    // lvs_map_device                        
    unit                                    -resistance ohm
    unit                                    -capacitance pf
    lvs_verilog_bus_map_by_position         no
    lvs_verilog_keep_backslash              no
    lvs_do_not_normalize                    no
    // lvs_generic_device                    
    virtual_connect                         no  -colon
    virtual_connect                         yes -semicolon_as_colon
    // virtual_connect                      -name 
    virtual_connect                         no -report
    virtual_connect                         no -incremental
    lvs_preserve_parameterized_cells        no
    lvs_check_color                         no
    // lvs_schematic_color_path              
    // lvs_assign_conflict_layer             
    // lvs_conflict_layer_check             
    lvs_check_color_label                   no
                                             

Effective LVS Rule Values
-------------------------

    lvs_swap_non_cpoint_pins                yes -unbound_pin_threshold 10000
    virtual_connect                         no  -report


##############################################################################################################
#
#                                               CELL COMPARISON                                               
#
##############################################################################################################

                              ##################################################
                              #                                                #
                              #       ------->>> $ MISMATCH $ <<<-------       #
                              #                                                #
                              #        latch_2ck_2x  <vs>  latch_2ck_2x        #
                              #                                                #
                              #            CONNECTIVITY MISMATCHES             #
                              #              PARAMETER MISMATCHES              #
                              #                                                #
                              ##################################################

+===[latch_2ck_2x]============================================================================================
|                                                 STATISTICS                                                  
+=============================================================================================================


                  |     Original      |      Reduced      |     Unmatched     
Cell              |   lay   :   sch   |   lay   :   sch   |   lay   :   sch
------------------+---------+---------+---------+---------+---------+---------
MP [4 pins]       |         :         |         :         |         :         
 MP(P1LVT)        |      *8 :       5 |       1 :       1 |       0 :        0
 MP:SerMos2#1     |       - :       - |       2 :       2 |       0 :        0
MN [4 pins]       |         :         |         :         |         :         
 MN(N1LVT)        |      *8 :       5 |       1 :       1 |       0 :        0
 MN:SerMos2#1     |       - :       - |       2 :       2 |       0 :        0
------------------+---------+---------+---------+---------+---------+---------
Total             |      16 :      10 |       6 :       6 |       0 :        0
==================+=========+=========+=========+=========+=========+=========
Pins              |         :         |       6 :       6 |       0 :        0
Nets              |         :         |      *3 :       1 |      *2 :        0
==================+=========+=========+=========+=========+=========+=========

+===[latch_2ck_2x]============================================================================================
|                                      DEVICES REMOVED DURING REDUCTION                                       
+=============================================================================================================


                |     Parallel      |      Series       |     Split Gate     |     Deleted Nets     
Cell            |   lay   :   sch   |   lay   :   sch   |   lay   :   sch    |    lay    :   sch
----------------+---------+---------+---------+---------+---------+----------+-----------+----------
MP [4 pins]     |         :         |         :         |         :          |           :          
 MP(P1LVT)      |       3 :       - |       - :       - |       - :        - |         0 :         0
MN [4 pins]     |         :         |         :         |         :          |           :          
 MN(N1LVT)      |       3 :       - |       - :       - |       - :        - |         0 :         0
----------------+---------+---------+---------+---------+---------+----------+-----------+----------

+===[latch_2ck_2x]============================================================================================
|                                           INITIAL CORRESPONDENCES                                           
+=============================================================================================================

Type     | Name
---------+-------------------------
Pin      | CLK CLKB I O VDD VSS


+===[latch_2ck_2x]============================================================================================
|                                              SHORTS AND OPENS                                               
+=============================================================================================================
                                            
                                            
Layout Pin: VSS     | Schematic Pin: VSS
====================+================(sao 1)
Layout Net: 5       |         OPEN
====================+=======================
                                            
                                            
Layout Pin: VDD     | Schematic Pin: VDD
====================+================(sao 2)
Layout Net: 11      |         OPEN
====================+=======================


+===[latch_2ck_2x]============================================================================================
|                                       MISMATCHED INSTANCE PARAMETERS                                        
+=============================================================================================================


                 Merged Instance Detail                  
=========+=====================+=========================
         |                     | 
Side     | Master Instance     | Instances
---------+---------------------+-----------------(midl 1)
Lay      | <X10/X24/M0>        | X10/X24/M0
         |                     +-------------------------
         |                     | X10/X25/M0
---------+---------------------+-----------------(midl 2)
Lay      | <X10/X15/M0>        | X10/X15/M0
         |                     +-------------------------
         |                     | X10/X16/M0
---------+---------------------+-----------------(midl 3)
Lay      | <X9/X23/X4/M0>      | X9/X23/X4/M0
         |                     +-------------------------
         |                     | X9/X23/X5/M0
---------+---------------------+-----------------(midl 4)
Lay      | <X9/X22/X4/M0>      | X9/X22/X4/M0
         |                     +-------------------------
         |                     | X9/X22/X5/M0
---------+---------------------+-----------------(midl 5)
Lay      | <X9/X16/X4/M0>      | X9/X16/X4/M0
         |                     +-------------------------
         |                     | X9/X16/X5/M0
---------+---------------------+-----------------(midl 6)
Lay      | <X9/X15/X4/M0>      | X9/X15/X4/M0
         |                     +-------------------------
         |                     | X9/X15/X5/M0


Layout Instance                             | Schematic Instance         |     Parameter Error     
--------------------------------------------+----------------------------+------------------(mip 1)
<X10/X24/M0> @(1.324,0.847) MP(P1LVT)       | XI1/XIP0/MM0 MP(P1LVT)     |                         
nf: 2                                       | nf: 8                      | 6                       
--------------------------------------------+----------------------------+------------------(mip 2)
<X10/X15/M0> @(1.324,0.113) MN(N1LVT)       | XI1/XIN0/MM0 MN(N1LVT)     |                         
nf: 2                                       | nf: 8                      | 6                       
--------------------------------------------+----------------------------+------------------(mip 3)
<X9/X23/X4/M0> @(0.464,0.847) MP(P1LVT)     | XI0/XIP1/MM0 MP(P1LVT)     |                         
nf: 2                                       | nf: 4                      | 2                       
--------------------------------------------+----------------------------+------------------(mip 4)
<X9/X22/X4/M0> @(0.120,0.847) MP(P1LVT)     | XI0/XIP0/MM0 MP(P1LVT)     |                         
nf: 2                                       | nf: 4                      | 2                       
--------------------------------------------+----------------------------+------------------(mip 5)
<X9/X16/X4/M0> @(0.464,0.113) MN(N1LVT)     | XI0/XIN0/MM0 MN(N1LVT)     |                         
nf: 2                                       | nf: 4                      | 2                       
--------------------------------------------+----------------------------+------------------(mip 6)
<X9/X15/X4/M0> @(0.120,0.113) MN(N1LVT)     | XI0/XIN1/MM0 MN(N1LVT)     |                         
nf: 2                                       | nf: 4                      | 2                       


##############################################################################################################
#
#                                                END OF REPORT                                                
#
##############################################################################################################

