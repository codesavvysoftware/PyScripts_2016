#/////////////////////////////////////////////////////////////////////////////
#/// @file Ice2HypervisorPowerupCompletionChecksDiagnosticFaultInjectionTest1.py
#///
#/// This Python script verifies that ICE2 power-up completion test
#/// (DiagnosticsPowerUpCompletion.cpp) operates for the Hypervisor, i.e.
#/// checks diagnostic tests in terms of completion during power-up.
#///
#/// @if REVISION_HISTORY_INCLUDED
#/// @par Edit History
#/// pgrzywn  30-SEP-2013 Created.
#/// mstasia  02-OCT-2013 Description added.
#/// pszramo  21-OCT-2013 Modified to match updated faultInjectionUtils.
#/// mstasia  31-OCT-2013 Changed approach to simulating this fault.
#/// pszramo  07-NOV-2013 Updated description to match modified injection.
#/// dtstalte 23-JUN-2014 Rename file to add Hypervisor/non-Hypervisor versions.
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
    'DiagnosticTest.hpp': [ \
    # # # # # # # # # # # # # # # # # # # # # # # # #
    '''
    // Start Fault Injection Point 1
    // End Fault Injection Point 1
    // Fault Injection Code Start
    INLINE void             UnsetCompletedPowerUpTest()                                  { m_bCompletedPowerUpTest = false; }
    // Fault Injection Code End
    '''
    ],
    'HypervisorDiagnostics.cpp': [ \
    # # # # # # # # # # # # # # # # # # # # # # # # #
    '''
    // Start Fault Injection Point 1
    // End Fault Injection Point 1
        // Fault Injection Code Start
        if (index == 0)
        {
            pCurrentDiagnosticTest->UnsetCompletedPowerUpTest();
        }
        // Fault Injection Code End
    '''
    ]
}

# Call the procedure to modify and build the test firmware code with the
# above modifications.
faultInjectionUtils.FaultInjectionUtils().ModifyAndBuildFaultInjectionFile(fileModificationsDictionary, __file__)