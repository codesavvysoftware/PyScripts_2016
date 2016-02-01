#/////////////////////////////////////////////////////////////////////////////
#/// @file Ice2CompletionTimeChecksDiagnosticFaultInjectionTest1.py
#///
#/// This Python script verifies that timeout of ICE diagnostic
#/// test is properly recognized (i.e. test data manager -
#/// DiagnosticTestDataManager.cpp - raises exception).
#/// The script injects fake information to set the last completed value
#/// of a long-running diagnostic to a value that makes the test timeouted.
#///
#/// @if REVISION_HISTORY_INCLUDED
#/// @par Edit History
#/// pgrzywn 30-SEP-2013 Created.
#/// pszramo 21-OCT-2013 Modified to match updated faultInjectionUtils.
#/// mstasia 05-NOV-2013 Changed approach to simulating this fault.
#/// pszramo 07-NOV-2013 Updated description to match modified injection.
#/// @endif
#///
#/// @par Copyright (c) 2013 Rockwell Automation Technologies, Inc.  All rights reserved.
#///
#/////////////////////////////////////////////////////////////////////////////

import faultInjectionUtils

#------------------------------------------------------------------------------
# Here is the list of files to be modified by this script, along with
# blocks of new code (first two lines of block are start and end text to
# search for and replace between) for each of the modified files.
fileModificationsDictionary = {\
    'SystemDiagnostic.hpp': [ \
    # # # # # # # # # # # # # # # # # # # # # # # # #
    '''
    // Start Fault Injection Point 1
    // End Fault Injection Point 1
    // Fault Injection Code Start
    static const uint32_t DIAGNOSTIC_COMPLETION_TIME_INTERVAL_IN_THREAD_CYCLES = 1 * 60 * 1000 / DIAGNOSTICS_THREAD_CYCLE_PERIOD_IN_MS;
    // Fault Injection Code End
    '''
    ],
    'DiagnosticTest.hpp': [ \
    # # # # # # # # # # # # # # # # # # # # # # # # #
    '''
    // Start Fault Injection Point 2
    // End Fault Injection Point 2
    // Fault Injection Code Start
    INLINE void SetLastTestCompletionSlice(uint64_t sliceNumber) { m_pDiagnosticTestData->m_LastSliceCompleted = sliceNumber - m_pDiagnosticTestData->m_SlicesBeforeTimeout - 1; }
    // Fault Injection Code End
    '''
    ],
   'DiagnosticTest.cpp': [ \
    # # # # # # # # # # # # # # # # # # # # # # # # #
    '''
    // Start Fault Injection Point 1
    // End Fault Injection Point 1
    // Fault Injection Code Start
    m_pDiagnosticTestData->m_LastSliceCompleted -= (m_pDiagnosticTestData->m_SlicesBeforeTimeout + 1);
    // Fault Injection Code End
    '''
    ]
}

# Call the procedure to modify and build the test firmware code with the
# above modifications.
faultInjectionUtils.FaultInjectionUtils().ModifyAndBuildFaultInjectionFile(fileModificationsDictionary, __file__)