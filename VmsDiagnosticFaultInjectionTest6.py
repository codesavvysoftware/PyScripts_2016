#/////////////////////////////////////////////////////////////////////////////
#/// @file VmsDiagnosticFaultInjectionTest6.py
#///
#/// This Python script verifies that VMS validation diagnostics will fail
#/// if the data from the VMS is stale.
#///
#/// @if REVISION_HISTORY_INCLUDED
#/// @par Edit History
#/// abritto  28-OCT-2013 Created.
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
fileModificationsDictionary1 = {\
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

fileModificationsDictionary2 = {\
	'VmsDiagnosticTest.cpp': [ \
	# # # # # # # # # # # # # # # # # # # # # # # # #
	'''
	// Start Stale Data Fault Injection
	// End Stale Data Fault Injection
	// Fault Injection Code Start
	CurrentTimeUs += VMS_DATA_REFRESH_TOLERANCE_US;
	// Fault Injection Code End
	'''
	]
}

# Call the procedure to modify and build the test firmware code with the
# above modifications.
utils = faultInjectionUtils.FaultInjectionUtils()
fileModificationsDictionary = utils.MergeDictionaries(fileModificationsDictionary1, fileModificationsDictionary2)
utils.ModifyAndBuildFaultInjectionFile(fileModificationsDictionary, __file__)
