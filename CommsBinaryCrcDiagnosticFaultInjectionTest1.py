#/////////////////////////////////////////////////////////////////////////////
#/// @file CommsBinaryCrcDiagnosticFaultInjectionTest1.py
#///
#/// This Python script verifies that the Comms Binary CRC Diagnostic will
#/// fail if the CRC calculated at runtime doesn't match the CRC  calculated
#/// at powerup.
#///
#/// @if REVISION_HISTORY_INCLUDED
#/// @par Edit History
#/// abritto  31-OCT-2013 Created.
#/// pelosow  28-FEB-2014 Added reinterpret_cast per real code misra changes.
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
    'BinaryCrcDiagnostic.cpp': [ \
    # # # # # # # # # # # # # # # # # # # # # # # # #
    '''
    // Start Fault Injection Point 1
    // End Fault Injection Point 1
    // Fault Injection Code Start
    if (std::strncmp(reinterpret_cast<const char*>(m_pDiagnosticTestData->m_TestName), "CommsBinaryCrc", DiagnosticTestData::MAX_TEST_NAME_LENGTH-1) == 0)
    {
        m_pCrcLocation = m_pBinaryEnd;
    }
    // Fault Injection Code End
    '''
    ]
}

# Call the procedure to modify and build the test firmware code with the
# above modifications.
faultInjectionUtils.FaultInjectionUtils().ModifyAndBuildFaultInjectionFile(fileModificationsDictionary, __file__)
