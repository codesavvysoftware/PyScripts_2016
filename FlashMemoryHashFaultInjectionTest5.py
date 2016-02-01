#/////////////////////////////////////////////////////////////////////////////
#/// @file FlashMemoryHashTestFaultInjectionTest5.py
#///
#/// This Python script allows to verify HyperLoader's ability to verify
#/// firmware images using their certificates and prevent further operation 
#/// if none is valid.
#/// The script injects code which corrupts both normal firmware's and 
#/// Safeboot's certificates during power up.
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
#include <fcntl.h>          // For open()
#include <unistd.h>         // For write(), close()
#include <sys/types.h>
#include "AssertPrivate.h"  // For bsp_ASSERT()

static void f_CorruptImageCertificate(const char* pPath)
{
    const char corruptedData[] = { 0xDE, 0xAD, 0xC0, 0xDE };
    int fd;
    
    fd = open(pPath, O_WRONLY, 0);
    bsp_ASSERT(-1 != fd);
    bsp_ASSERT(-1 != lseek(fd, 0x05, SEEK_SET));    // Skip a few first bytes
    bsp_ASSERT(sizeof(corruptedData) == write(fd, &corruptedData[0], sizeof(corruptedData)));
    close(fd);
}
// Fault Injection Code End
    ''',
    # # # # # # # # # # # # # # # # # # # # # # # # #
    '''
    // Start Fault Injection Point 2
    // End Fault Injection Point 2
    // Fault Injection Code Start
    f_CorruptImageCertificate("/boot/system.der");  // Normal firmware
    f_CorruptImageCertificate("/alt/system.der");   // Safeboot
    // Fault Injection Code End
    '''
    ]
}

# Call the procedure to modify and build the test firmware code with the
# above modifications.
faultInjectionUtils.FaultInjectionUtils().ModifyAndBuildFaultInjectionFile(fileModificationsDictionary, __file__)