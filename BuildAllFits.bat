    @echo off
    rem BuildAllFits.bat
    rem
    rem Batch file that builds all of the fault injection test script files.
    rem
    rem Input Parameters:
    rem     %1: viewPath (Path to the view name being used
    rem                  (e.g., C:\Clearcase\SSVIEW\<view_name>))
    rem
    rem Note that the FlashMemoryHashFaultInjectionTest object and dependency
    rem files can not be easily deleted automatically so they can not be built
    rem using this batch file.
    rem
    rem Therefore, the FlashMemoryHashFaultInjectionTests need to be built
    rem manually and a complete clean needs to be done before each
    rem FlashMemoryHashFaultInjectionTest build.
    rem
    rem Note that the \LNX\Platform\BSP\Board\Ice2_CNzR\PV\obj_release folder
    rem must not be open when doing the complete cleans before each
    rem FlashMemoryHashFaultInjectionTests build or the following error
    rem will occur during the clean: "rm: cannot chdir from `obj_release/
    rem Clearcase/SSVIEW/pelosow_pb_pelosow_cnz_fault_injection_testing_view/
    rem LNX/Platform/BSP' to `Board': Permission denied"
    rem
    set viewPath=%1

:CHECK_SYNTAX
    if "%viewPath%" EQU "" GOTO Help

:BUILD_TESTS
    rem call python FlashMemoryHashFaultInjectionTest1.py
    rem call python FlashMemoryHashFaultInjectionTest2.py
    rem call python FlashMemoryHashFaultInjectionTest3.py
    rem call python FlashMemoryHashFaultInjectionTest4.py
    rem call python FlashMemoryHashFaultInjectionTest5.py
    rem
    @echo.
    call DeleteFITObjAndDepFiles.bat %viewPath%
    call python VmsDiagnosticFaultInjectionTest1.py
    call DeleteFITObjAndDepFiles.bat %viewPath%
    call python VmsDiagnosticFaultInjectionTest2.py
    call DeleteFITObjAndDepFiles.bat %viewPath%
    call python VmsDiagnosticFaultInjectionTest3.py
    call DeleteFITObjAndDepFiles.bat %viewPath%
    call python VmsDiagnosticFaultInjectionTest4.py
    call DeleteFITObjAndDepFiles.bat %viewPath%
    call python VmsDiagnosticFaultInjectionTest5.py
    call DeleteFITObjAndDepFiles.bat %viewPath%
    call python VmsDiagnosticFaultInjectionTest6.py
    call DeleteFITObjAndDepFiles.bat %viewPath%
    call python Ice2HypervisorPowerupCompletionChecksDiagnosticFaultInjectionTest1.py
    call DeleteFITObjAndDepFiles.bat %viewPath%
    call python Ice2PowerupCompletionChecksDiagnosticFaultInjectionTest1.py
    call DeleteFITObjAndDepFiles.bat %viewPath%
    call python Ice2CompletionTimeChecksDiagnosticFaultInjectionTest1.py
    call DeleteFITObjAndDepFiles.bat %viewPath%
    call python ApexFirmwareBinaryCrcDiagnosticFaultInjectionTest1.py
    call DeleteFITObjAndDepFiles.bat %viewPath%
    call python ApexFirmwareBinaryCrcDiagnosticFaultInjectionTest2.py
    call DeleteFITObjAndDepFiles.bat %viewPath%
    call python HypervisorBinaryCrcDiagnosticFaultInjectionTest1.py
    call DeleteFITObjAndDepFiles.bat %viewPath%
    call python CommsBinaryCrcDiagnosticFaultInjectionTest1.py
    call DeleteFITObjAndDepFiles.bat %viewPath%
    call python InteractiveWatchdogFaultInjectionTest1.py
    call DeleteFITObjAndDepFiles.bat %viewPath%
    call python InteractiveWatchdogFaultInjectionTest2.py
    call DeleteFITObjAndDepFiles.bat %viewPath%
    call python ApexInternalRamShadowFaultInjectionTest1.py
    call DeleteFITObjAndDepFiles.bat %viewPath%
    call python ApexInternalRamShadowFaultInjectionTest2.py
    call DeleteFITObjAndDepFiles.bat %viewPath%
    call python ApexInternalRamAddressLineDiagnosticFaultInjectionTest1.py
    call DeleteFITObjAndDepFiles.bat %viewPath%
    call python ApexInternalRamAddressLineDiagnosticFaultInjectionTest2.py
    call DeleteFITObjAndDepFiles.bat %viewPath%
    call python ApexInternalSafeRamDiagnosticFaultInjectionTest1.py
    call DeleteFITObjAndDepFiles.bat %viewPath%
    call python ApexInternalRamScrubberDiagnosticFaultInjectionTest1.py
    call DeleteFITObjAndDepFiles.bat %viewPath%
    call python ApexInternalRamEccCircuitDiagnosticFaultInjectionTest1.py
    call DeleteFITObjAndDepFiles.bat %viewPath%
    call python ApexInternalRamEccCircuitDiagnosticFaultInjectionTest2.py
    call DeleteFITObjAndDepFiles.bat %viewPath%
    call python ApexArmInstructionDiagnosticFaultInjectionTest1.py
    call DeleteFITObjAndDepFiles.bat %viewPath%
    call python ApexArmInstructionDiagnosticFaultInjectionTest2.py
    call DeleteFITObjAndDepFiles.bat %viewPath%
    call python ApexArmRegisterDiagnosticFaultInjectionTest1.py
    call DeleteFITObjAndDepFiles.bat %viewPath%
    call python ApexArmRegisterDiagnosticFaultInjectionTest2.py
    call DeleteFITObjAndDepFiles.bat %viewPath%
    call python TimerDiagnosticFaultInjectionTest1.py
    call DeleteFITObjAndDepFiles.bat %viewPath%
    call python TimerDiagnosticFaultInjectionTest2.py
    call DeleteFITObjAndDepFiles.bat %viewPath%
    call python TimerDiagnosticFaultInjectionTest3.py
    call DeleteFITObjAndDepFiles.bat %viewPath%
    call python ApexCompletionTimeDiagnosticFaultInjectionTest1.py
    call DeleteFITObjAndDepFiles.bat %viewPath%
    call python ApexArmDataCacheDiagnosticFaultInjectionTest1.py
    call DeleteFITObjAndDepFiles.bat %viewPath%
    call python ApexArmInstructionCacheDiagnosticFaultInjectionTest1.py
    call DeleteFITObjAndDepFiles.bat %viewPath%
    call python SysFailLineFaultInjectionTest1.py
    call DeleteFITObjAndDepFiles.bat %viewPath%
    GOTO END

:HELP
    @echo Proper syntax is:   
    @echo     BuildAllFits viewPath
    @echo         viewPath = Path to the view name being used (e.g., C:\Clearcase\SSVIEW\<view_name>)
    GOTO END

:END