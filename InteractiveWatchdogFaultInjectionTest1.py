#/////////////////////////////////////////////////////////////////////////////
#/// @file InteractiveWatchdogFaultInjectionTest1.py
#///
#/// This Python script verifies that when code is modified on the ICE2
#/// side (only) to cause the ICE2/Apex2 interactive watchdog code to stop
#/// servicing the watchdog after several seconds of proper operation, the
#/// module should fault because the Apex2 hardware watchdog will time out,
#/// since ICE2 has not requested that Apex2 service it.
#///
#/// @if REVISION_HISTORY_INCLUDED
#/// @par Edit History
#/// wmpeloso 21-OCT-2013 Created.
#/// wmpeloso 22-OCT-2013 Added missing '#' in "#define INTERACTIVE_WATCHDOG_ENABLED 1".
#/// wmpeloso 06-NOV-2013 Removed setting of INTERACTIVE_WATCHDOG_ENABLED in apxParameters.hpp.
#///                      This flag is considered part of the code under test so it should
#///                      not be modified in the fault injection script file.
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
            // Start Fault Injection Point 2
            // End Fault Injection Point 2
            // Fault Injection Code Start
            if ( ulTestValue < 60000000 )
            {
                if ( m_pSharedRam->WatchDog.host != ulTestValue )
                {
                    NCS_LOG_EVENT2( APEX_WDOG, SEVERE, m_pSharedRam->WatchDog.host,
                                    m_pSharedRam->WatchDog.asic );
                    ASSERT( false, ASRT_CP_BP_WATCHDOG );
                }
            }
            // Fault Injection Code End
    ''',
    
    # # # # # # # # # # # # # # # # # # # # # # # # # 
    '''
            // Start Fault Injection Point 4
            // End Fault Injection Point 4
            // Fault Injection Code Start
            if ( ulTestValue < 60000000 )
            {
                m_pSharedRam->WatchDog.host = ulTestValue;
            }
            // Fault Injection Code End
            
    '''
    ]
}

# Call the procedure to modify and build the test firmware code with the 
# above modifications.
faultInjectionUtils.FaultInjectionUtils().ModifyAndBuildFaultInjectionFile(fileModificationsDictionary, __file__)
