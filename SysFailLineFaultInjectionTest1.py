#/////////////////////////////////////////////////////////////////////////////
#/// @file SysFailLineFaultInjectionTest1.py
#///
#/// This Python script causes the module to ASSERT so that an oscilloscope can
#/// be attached to verify the SYS_FAIL line has been triggered.
#///
#/// @if REVISION_HISTORY_INCLUDED
#/// @par Edit History
#/// dtstalte  25-JUN-2014 Created.
#/// @endif
#///
#/// @par Copyright (c) 2014 Rockwell Automation Technologies, Inc.  All rights reserved.
#///
#/////////////////////////////////////////////////////////////////////////////

import faultInjectionUtils

#------------------------------------------------------------------------------
# Here is the list of files to be modified by this script, along with
# blocks of new code (first two lines of block are start and end text to
# search for and replace between) for each of the modified files.
fileModificationsDictionary = {\
    'SystemDiagnostic.cpp': [ \
    # # # # # # # # # # # # # # # # # # # # # # # # #
    '''
    // Start Fault Injection Point 1
    // End Fault Injection Point 1
    // Fault Injection Code Start
    ASSERT(false);
    // Fault Injection Code End
    '''
	],
    'WatchdogManager.cpp': [ \
    # # # # # # # # # # # # # # # # # # # # # # # # # 
    '''
    // Start Fault Injection Point 1
    // End Fault Injection Point 1
    // Fault Injection Code Start
    // Fault Injection Code End
    '''
    ]
}

# Call the procedure to modify and build the test firmware code with the
# above modifications.
faultInjectionUtils.FaultInjectionUtils().ModifyAndBuildFaultInjectionFile(fileModificationsDictionary, __file__)
