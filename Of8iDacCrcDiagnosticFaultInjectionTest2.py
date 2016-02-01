#/////////////////////////////////////////////////////////////////////////////
#/// @file Of8iDacCrcDiagnosticFaultInjectionTest2.py
#///
#/// This Python script verifies that a bad CRC read from the DAC will cause
#/// that channel to go uncertain.
#/// Verify that the "Uncertain" status bit is set in the appropriate input tag
#///
#/// @if REVISION_HISTORY_INCLUDED
#/// @par Edit History
#/// kolat   22-Jan-2016 Created.
#/// @endif
#///
#/// @par Copyright (c) 2016 Rockwell Automation Technologies, Inc.  All rights reserved.
#///
#/////////////////////////////////////////////////////////////////////////////

import faultInjectionUtils

#------------------------------------------------------------------------------
# Here is the list of files to be modified by this script, along with
# blocks of new code (first two lines of block are start and end text to
# search for and replace between) for each of the modified files.
fileModificationsDictionary = { \
    'OF8I.c': [ \
    # # # # # # # # # # # # # # # # # # # # # # # # # 
    '''
          /* Start Fault Injection Point 3 */
          /* End Fault Injection Point 3 */
          /* Fault Injection Code Start */
          /* For each Odd channel number, corrupt the read CRC value by */
          /*  incrementing it. */
          /* 30 seconds after power up, verify that these channels have their */
          /*  "Uncertain" status bit set in the input tag. */
          if ( ((dac_num & 1) == 1) && 
               ((The_Rolling_Timestamp > 30000) ||
                (Diag_Assy.Channel[ dac_num ].CRCRxErrorCount > 10)) )
          {
             calculated_CRC++;
          }
          /* Fault Injection Code End */
    '''
    ]
}

# Call the procedure to modify and build the test firmware code with the
# above modifications.
faultInjectionUtils.FaultInjectionUtils().ModifyAndBuildFaultInjectionFile(fileModificationsDictionary, __file__)