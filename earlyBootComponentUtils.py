#/////////////////////////////////////////////////////////////////////////////
#/// @file earlyBootComponentUtils.py
#///
#/// This script file contains file modifications dictionary used to inject
#/// a global function capable of corrupting an early boot component in SPI
#/// NOR. This is a common functionality required by a few of flash memory
#/// hash fault injection tests.
#/// This script should be imported by a script which requires such a
#/// functionality and the dictionary it provides should be merged with
#/// importers dictionary.
#///
#/// @if REVISION_HISTORY_INCLUDED
#/// @par Edit History
#/// pszramo  25-OCT-2013 Created.
#/// pszramo  05-NOV-2013 Modified according to comments in Review #27092.
#/// @endif
#///
#/// @par Copyright (c) 2013 Rockwell Automation Technologies, Inc.  All rights reserved.
#///
#/////////////////////////////////////////////////////////////////////////////

fileModificationsDictionary = {\
    'bsp_SpiNorImpl.hpp': [\
    # # # # # # # # # # # # # # # # # # # # # # # # #
    '''
    // Start Fault Injection Point 1
    // End Fault Injection Point 1
// Fault Injection Code Start
extern "C" int g_CorruptEarlyBootComponent(int);
// Fault Injection Code End
    ''',
    # # # # # # # # # # # # # # # # # # # # # # # # #
    '''
    // Start Fault Injection Point 2
    // End Fault Injection Point 2
    // Fault Injection Code Start
    friend int g_CorruptEarlyBootComponent(int);
    // Fault Injection Code End
    '''
    ],
    'bsp_SpiNorImpl.cpp': [\
    # # # # # # # # # # # # # # # # # # # # # # # # #
    '''
    // Start Fault Injection Point 1
    // End Fault Injection Point 1
// Fault Injection Code Start
#include "Flash.hpp"        // For image offsets

int g_CorruptEarlyBootComponent(int imageNum)
{
    uint32_t        corruptedData[] = { 0xDEADC0DE };
    unsigned int    offset          = 0;
    BSP_Status      retVal          = BSP_SUCCESS;

    switch (imageNum)
    {
        case 0:
            offset  = FLASH_HYPERLOADERINIT_OFFSET;
            break;
        case 1:
            offset  = FLASH_HYPERLOADERINIT_BACKUP_OFFSET;
            break;
        case 2:
            offset  = FLASH_SYSTEM_MANIFEST_OFFSET;
            break;
        case 3:
            offset  = FLASH_SYSTEM_MANIFEST_BACKUP_OFFSET;
            break;
        case 4:
            offset  = FLASH_HYPERLOADER_OFFSET;
            break;
        case 5:
            offset  = FLASH_HYPERLOADER_BACKUP_OFFSET;
            break;
        default:
            retVal  = BSP_INVALID_PARAMETER;
            break;
    }
    if (BSP_SUCCESS == retVal)
    {
        retVal  = bsp_SpiNorImpl::Startup();
    }
    if (BSP_SUCCESS == retVal)
    {
        retVal  = bsp_SpiNorImpl::Write(&corruptedData[0], offset, sizeof(corruptedData));
    }
    return (BSP_SUCCESS == retVal) ? 0 : -1;
}
// Fault Injection Code End
    '''
    ]
}