#/////////////////////////////////////////////////////////////////////////////
#/// @file TimerDiagnosticFaultInjectionTest2.py
#///
#/// This Python script verifies that when ICE2 writes a bad value into its
#/// side of the ICE2/Apex2 interactive watchdog, the Apex2 Timer Diagnostic
#/// will assert when it checks if any of the elapsed times for the timers
#/// that it checks are bad.
#///
#/// @if REVISION_HISTORY_INCLUDED
#/// @par Edit History
#/// wmpeloso 21-OCT-2013 Created.
#/// wmpeloso 22-OCT-2013 Added missing '#' in "#define INTERACTIVE_WATCHDOG_ENABLED 1".
#/// wmpeloso 06-NOV-2013 Removed setting of INTERACTIVE_WATCHDOG_ENABLED in apxParameters.hpp.
#///                      This flag is considered part of the code under test so it should
#///                      not be modified in the fault injection script file.
#/// pszramo  10-DEC-2013 Adjustments after MISRA fixes.
#/// @endif
#///
#/// @par Copyright (c) 2013 Rockwell Automation Technologies, Inc.  All rights reserved.
#///
#/////////////////////////////////////////////////////////////////////////////

#------------------------------------------------------------------------------
import faultInjectionUtils

#------------------------------------------------------------------------------
# Here is the list of files to be modified by this script, along with
# blocks of new code (first two lines of block are start and end text to
# search for and replace between) for each of the modified files.
fileModificationsDictionary = { \
    'ApexHw.cpp': [ \
    # # # # # # # # # # # # # # # # # # # # # # # # # 
    '''
            // Start Fault Injection Point 3
            // End Fault Injection Point 3
            // Fault Injection Code Start
            ulTestValue += ( ( BSP_GetTimeStampUs() - ulTestValue ) * 110 )/100;
            // Fault Injection Code End
    '''
    ],
    'ApexDiagnostic.hpp': [ \
    # # # # # # # # # # # # # # # # # # # # # # # # # 
    '''
    // Start Fault Injection Point 4
    // End Fault Injection Point 4
    // Fault Injection Code Start
    static const UINT32 DGN_TIMER_INITIAL_TRIG_VAL_MS = 60000; // 1 min
    // Fault Injection Code End
    ''',
    # # # # # # # # # # # # # # # # # # # # # # # # # 
    '''
    // Start Fault Injection Point 5
    // End Fault Injection Point 5
    // Fault Injection Code Start
    static const UINT32 DGN_TIMER_STEP_MS = 60000; // 1 min
    // Fault Injection Code End
    '''
    ]
}

# Call the procedure to modify and build the test firmware code with the 
# above modifications.
faultInjectionUtils.FaultInjectionUtils().ModifyAndBuildFaultInjectionFile(fileModificationsDictionary, __file__)
