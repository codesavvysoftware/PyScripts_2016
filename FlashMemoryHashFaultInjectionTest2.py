#/////////////////////////////////////////////////////////////////////////////
#/// @file FlashMemoryHashTestFaultInjectionTest2.py
#///
#/// This Python script allows to verify HyperLoaderInit's ability to detect 
#/// that both images of HyperLoader are corrupted. HLI should refrain from 
#/// loading either copy in such case.
#/// The script injects code which corrupts both images of HL in SPI NOR 
#/// during power up.
#///
#/// @if REVISION_HISTORY_INCLUDED
#/// @par Edit History
#/// pszramo 25-OCT-2013 Created.
#/// @endif
#///
#/// @par Copyright (c) 2013 Rockwell Automation Technologies, Inc.  All rights reserved.
#///
#/////////////////////////////////////////////////////////////////////////////

import faultInjectionUtils
import earlyBootComponentUtils

#------------------------------------------------------------------------------
# Here is the list of files to be modified by this script, along with
# blocks of new code (first two lines of block are start and end text to
# search for and replace between) for each of the modified files.
fileModificationsDictionary = {\
    'usrAppInit.c': [\
    # # # # # # # # # # # # # # # # # # # # # # # # #
    '''
    // Start Fault Injection Point 1
    // End Fault Injection Point 1
// Fault Injection Code Start
#include "AssertPrivate.h"  // For bsp_ASSERT()

extern int  g_CorruptEarlyBootComponent(int);
// Fault Injection Code End
    ''',
    # # # # # # # # # # # # # # # # # # # # # # # # #
    '''
    // Start Fault Injection Point 2
    // End Fault Injection Point 2
    // Fault Injection Code Start
    bsp_ASSERT(-1 != g_CorruptEarlyBootComponent(4));   // Primary HL
    bsp_ASSERT(-1 != g_CorruptEarlyBootComponent(5));   // Backup HL
    // Fault Injection Code End
    '''
    ]
}

# Merge the above dictionary with the imported one which provides a common
# functionality of corrupting an early boot component.
# Note: entries for existing keys (file names) will be overwritten.
fileModificationsDictionary.update(earlyBootComponentUtils.fileModificationsDictionary)

# Call the procedure to modify and build the test firmware code with the
# above modifications.
faultInjectionUtils.FaultInjectionUtils().ModifyAndBuildFaultInjectionFile(fileModificationsDictionary, __file__)