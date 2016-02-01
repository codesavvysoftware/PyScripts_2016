#/////////////////////////////////////////////////////////////////////////////
#/// @file TimerDiagnosticFaultInjectionTest1.py
#///
#/// This Python script verifies that when ApexHw.cpp does not set the
#/// watchdog pointer (pWatchdog) to a non-zero value, the Apex2 Timer
#/// Diagnostic (apxDiagTimer.cpp) will assert via a call to firmExcept()
#/// when it checks pWatchdog.
#///
#/// @if REVISION_HISTORY_INCLUDED
#/// @par Edit History
#/// wmpeloso 30-SEP-2013 Created.
#/// wmpeloso 07-OCT-2013 Updated filesModifyBuildLoad second parameter,
#///                      removed import os.
#/// wmpeloso 13-OCT-2013 Updated per Collaborator code review #26377.
#/// wmpeloso 17-OCT-2013 Re-added "#"s comment line in apxParameters.hpp
#///                      block.
#/// wmpeloso 21-OCT-2013 Added DGN_TIMER_INITIAL_TRIG_VAL and DGN_TIMER_STEP
#///                      fault injections to speed up this fault injection
#///                      testing.
#/// wmpeloso 06-NOV-2013 Removed setting of INTERACTIVE_WATCHDOG_ENABLED in
#///                      apxParameters.hpp.
#///                      This flag is considered part of the code under test
#///                      so it should not be modified in the fault injection
#///                      script file.
#/// wmpeloso 12-NOV-2013 Added fault injection point to remove the assert that
#///                      the Apex side of the interactive watchdog has not
#///                      responded because we didn't start it.
#/// pszramo  17-DEC-2013 Adjustments after MISRA fixes.
#/// @endif
#///
#/// @par Copyright (c) 2013 Rockwell Automation Technologies, Inc.  All rights reserved.
#///
#/////////////////////////////////////////////////////////////////////////////

import faultInjectionUtils
#
# NOTE:
# This is a fault injection that will cause an error that should never actually
# happen during runtime because ICE2 will detect a software interactive
# watchdog timeout before the timer diagnostic detects that the watchdog
# pointer (pWatchdog) has not been changed to a non-zero value. We are only
# testing using this script file for completeness.
#
#------------------------------------------------------------------------------
# Here is the list of files to be modified by this script, along with
# blocks of new code (first two lines of block are start and end text to
# search for and replace between) for each of the modified files.
fileModificationsDictionary = { \
    'ApexHw.cpp': [ \
    # # # # # # # # # # # # # # # # # # # # # # # # # 
    '''
    // Start Fault Injection Point 1
    // End Fault Injection Point 1
    // Fault Injection Code Start
    // Fault Injection Code End
    '''
    ,
    '''
    // Start Fault Injection Point 5
    // End Fault Injection Point 5
    // Fault Injection Code Start
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
