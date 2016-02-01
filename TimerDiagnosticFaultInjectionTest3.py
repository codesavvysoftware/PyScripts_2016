#/////////////////////////////////////////////////////////////////////////////
#/// @file TimerDiagnosticFaultInjectionTest3.py
#///
#/// This Python script verifies that when Apex2 diagnostic initialization
#/// values are modified to cause the Apex2 Timer Diagnostic to compare the
#/// wrong values, the Apex2 Timer Diagnostic will assert when it checks if
#/// any of the elapsed times for the timers that it checks are bad.
#///
#/// @if REVISION_HISTORY_INCLUDED
#/// @par Edit History
#/// wmpeloso 21-OCT-2013 Created.
#/// wmpeloso 22-OCT-2013 Added missing '#' in "#define INTERACTIVE_WATCHDOG_ENABLED 1".
#/// wmpeloso 06-NOV-2013 Removed setting of INTERACTIVE_WATCHDOG_ENABLED in apxParameters.hpp.
#///                      This flag is considered part of the code under test so it should
#///                      not be modified in the fault injection script file.
#/// pszramo  17-DEC-2013 Adjustments after MISRA fixes.
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
    'ApexDiagnostic.cpp': [ \
    # # # # # # # # # # # # # # # # # # # # # # # # # 
    '''
    // Start Fault Injection Point 7
    // End Fault Injection Point 7
    // Fault Injection Code Start
    DgnList[DGN_TIMER].triggerValueTimeslice = MsToDgnSlices(DGN_FI_ONE_MIN_MS);
    DgnList[DGN_TIMER].stepValueTimeslice = MsToDgnSlices(DGN_FI_ONE_MIN_MS);
    // Fault Injection Code End
    '''
    ]
}

# Call the procedure to modify and build the test firmware code with the 
# above modifications.
faultInjectionUtils.FaultInjectionUtils().ModifyAndBuildFaultInjectionFile(fileModificationsDictionary, __file__)
