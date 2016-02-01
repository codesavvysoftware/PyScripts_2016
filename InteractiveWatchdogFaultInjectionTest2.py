#/////////////////////////////////////////////////////////////////////////////
#/// @file InteractiveWatchdogFaultInjectionTest2.py
#///
#/// This Python script verifies that when code is modified on the Apex2
#/// side (only) to cause Apex2 to stop responding to watchdog requests
#/// from ICE2 (while Apex2 continues to service its own hardware watchdog),
#/// the module should fault, based on major non-recoverable fault action
#/// from ICE2, since it has not seen the response from Apex2.
#///
#/// @if REVISION_HISTORY_INCLUDED
#/// @par Edit History
#/// wmpeloso 21-OCT-2013 Created.
#/// wmpeloso 22-OCT-2013 Added missing '#' in "#define
#///                      INTERACTIVE_WATCHDOG_ENABLED 1". Fixed indentation
#///                      of apxWatchdog.cpp code to be injected.
#/// wmpeloso 06-NOV-2013 Removed setting of INTERACTIVE_WATCHDOG_ENABLED in
#///                      apxParameters.hpp. This flag is considered part of
#///                      the code under test so it should not be modified in
#///                      the fault injection script file.
#/// wmpeloso 13-NOV-2013 Added fault injection to remove loop that causes
#///                      wrong fault to be reported from ApexHw.cpp.
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
fileModificationsDictionary = {\
    'ApexHw.cpp': [ \
    # # # # # # # # # # # # # # # # # # # # # # # # # 
    '''
    // Start Fault Injection Point 6
    // End Fault Injection Point 6
    // Fault Injection Code Start
    // Fault Injection Code End
    '''
    ],
    'ApexWatchdog.cpp': [ \
    # # # # # # # # # # # # # # # # # # # # # # # # # 
    '''
            // Start Fault Injection Point 1
            // End Fault Injection Point 1
            // Fault Injection Code Start
            if ( HI_ApexParam.pWatchdog->host < 60000000 )
            {
                HI_ApexParam.pWatchdog->asic = HI_ApexParam.pWatchdog->host;
            }
            // Fault Injection Code End
    '''
    ]
}

# Call the procedure to modify and build the test firmware code with the 
# above modifications.
faultInjectionUtils.FaultInjectionUtils().ModifyAndBuildFaultInjectionFile(fileModificationsDictionary, __file__)
