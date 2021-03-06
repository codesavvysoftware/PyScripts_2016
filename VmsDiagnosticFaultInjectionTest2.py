#/////////////////////////////////////////////////////////////////////////////
#/// @file VmsDiagnosticFaultInjectionTest2.py
#///
#/// This Python script verifies that VMS validation diagnostics will fail
#/// if the OV/UV tests succeed but the OV/UV data is actually bad.
#///
#/// @if REVISION_HISTORY_INCLUDED
#/// @par Edit History
#/// abritto  05-NOV-2013 Created.
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
    'BspVmsDataCollector.cpp': [ \
    # # # # # # # # # # # # # # # # # # # # # # # # #
    '''
    // Start Fault Injection Point 1
    // End Fault Injection Point 1
    // Fault Injection Code Start
    for (uint32_t j = 0; j < ConfigData::NUM_ADC_CONVERSIONS; j++)
    {
        m_VmsData.m_OvData[j].m_Adc = 0;
    }
    // Fault Injection Code End
    '''
    ],
	'VmsDiagnosticTest.cpp': [ \
	# # # # # # # # # # # # # # # # # # # # # # # # #
	'''
	// Start Slices Between Activations Adjustment
	// End Slices Between Activations Adjustment
	// Fault Injection Code Start
	SetSlicesBetweenActivations(1);
	// Fault Injection Code End
	'''
	]
}

# Call the procedure to modify and build the test firmware code with the
# above modifications.
faultInjectionUtils.FaultInjectionUtils().ModifyAndBuildFaultInjectionFile(fileModificationsDictionary, __file__)
