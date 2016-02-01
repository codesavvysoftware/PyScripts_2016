#/////////////////////////////////////////////////////////////////////////////
#/// @file Ice2PowerupCompletionChecksDiagnosticFaultInjectionTest1.py
#///
#/// This Python script verifies that ICE2 power-up completion test
#/// (DiagnosticsPowerUpCompletion.cpp) operates, i.e. checks
#/// diagnostic tests in terms of completion during power-up.
#///
#/// @if REVISION_HISTORY_INCLUDED
#/// @par Edit History
#/// dtstalte 23-JUN-2014 Created.
#/// @endif
#///
#/// @par Copyright (c) 2014 Rockwell Automation Technologies, Inc.  All rights reserved.
#///
#/////////////////////////////////////////////////////////////////////////////

#------------------------------------------------------------------------------
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
    'Diagnostics.cpp': [ \
    # # # # # # # # # # # # # # # # # # # # # # # # # 
    '''
    // Start Fault Injection Point 1
    // End Fault Injection Point 1
    // Fault Injection Code Start
    DiagnosticTest* pFirstPowerUpTest = pTestToRun;
    // Fault Injection Code End
    ''',
    # # # # # # # # # # # # # # # # # # # # # # # # # 
    '''
    // Start Fault Injection Point 2
    // End Fault Injection Point 2
    // Fault Injection Code Start
    pFirstPowerUpTest->UnsetCompletedPowerUpTest();
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
