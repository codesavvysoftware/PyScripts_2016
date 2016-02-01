#/////////////////////////////////////////////////////////////////////////////
#/// @file Of8iDacWriteDiagnosticFaultInjectionTest1.py
#///
#/// This Python script verifies that a mismatch between data written to the
#///  DAC and the data read back, is detected by the DSP.
#/// Verify that the "Fault" and "Uncertain" status bits are set in the
#///  appropriate input tag.
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
      /* Start Fault Injection Point 1 */
      /* End Fault Injection Point 1 */
      /* Fault Injection Code Start */
      /* For each Odd channel number, corrupt a bit in the data read back. */
      /* 30 seconds after power up, verify that these channels have their */
      /*  "Fault" and "Uncertain" status bit set in the input tag. */
      if ( ((dac_num & 1) == 1) &&
           ((The_Rolling_Timestamp > 30000)  ||
            (Diag_Assy.Channel[ dac_num ].CRCTxErrorCount > 10)) )
      {
          DAC_read_data[dac_num] ^= 1;
      }
      /* Fault Injection Code End */
    '''
    ]
}

# Call the procedure to modify and build the test firmware code with the
# above modifications.
faultInjectionUtils.FaultInjectionUtils().ModifyAndBuildFaultInjectionFile(fileModificationsDictionary, __file__)