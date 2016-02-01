    @echo off
    rem
    @echo.
    call python ApexArmDataCacheDiagnosticFaultInjectionTest1.py ApexDiagIRT8I
    call python ApexArmInstructionCacheDiagnosticFaultInjectionTest1.py ApexDiagIRT8I
    call python ApexArmInstructionDiagnosticFaultInjectionTest1.py ApexDiagIRT8I
    call python ApexArmInstructionDiagnosticFaultInjectionTest2.py ApexDiagIRT8I
    call python ApexArmRegisterDiagnosticFaultInjectionTest1.py ApexDiagIRT8I
    rem
    call python ApexArmRegisterDiagnosticFaultInjectionTest2.py ApexDiagIRT8I
    call python ApexCompletionTimeDiagnosticFaultInjectionTest1.py ApexDiagIRT8I
    call python ApexFirmwareBinaryCrcDiagnosticFaultInjectionTest1.py ApexDiagIRT8I
    call python ApexFirmwareBinaryCrcDiagnosticFaultInjectionTest2.py ApexDiagIRT8I
    call python ApexInteractiveWatchdogFaultInjectionTest1.py ApexDiagIRT8I
    rem
    call python ApexInternalRamAddressLineDiagnosticFaultInjectionTest1.py ApexDiagIRT8I
    call python ApexInternalRamAddressLineDiagnosticFaultInjectionTest2.py ApexDiagIRT8I
    call python ApexInternalRamEccCircuitDiagnosticFaultInjectionTest1.py ApexDiagIRT8I
    call python ApexInternalRamEccCircuitDiagnosticFaultInjectionTest2.py ApexDiagIRT8I
    call python ApexInternalRamScrubberDiagnosticFaultInjectionTest1.py ApexDiagIRT8I
    rem
    call python ApexInternalRamShadowFaultInjectionTest1.py ApexDiagIRT8I
    call python ApexInternalSafeRamDiagnosticFaultInjectionTest1.py ApexDiagIRT8I
    call python ApexInternalRamShadowFaultInjectionTest2.py ApexDiagIRT8I
    call python ApexArmDataCacheDiagnosticFaultInjectionTest1.py ApexDiagIF8I
    call python ApexArmInstructionCacheDiagnosticFaultInjectionTest1.py ApexDiagIF8I
    rem
    call python ApexArmInstructionDiagnosticFaultInjectionTest1.py ApexDiagIF8I
    call python ApexArmInstructionDiagnosticFaultInjectionTest2.py ApexDiagIF8I
    call python ApexArmRegisterDiagnosticFaultInjectionTest1.py ApexDiagIF8I
    call python ApexArmRegisterDiagnosticFaultInjectionTest2.py ApexDiagIF8I
    call python ApexCompletionTimeDiagnosticFaultInjectionTest1.py ApexDiagIF8I
    rem
    call python ApexFirmwareBinaryCrcDiagnosticFaultInjectionTest1.py ApexDiagIF8I
    call python ApexFirmwareBinaryCrcDiagnosticFaultInjectionTest2.py ApexDiagIF8I
    call python ApexInteractiveWatchdogFaultInjectionTest1.py ApexDiagIF8I    
    call python ApexInternalRamAddressLineDiagnosticFaultInjectionTest1.py ApexDiagIF8I
    call python ApexInternalRamAddressLineDiagnosticFaultInjectionTest2.py ApexDiagIF8I
    rem
    call python ApexInternalRamEccCircuitDiagnosticFaultInjectionTest1.py ApexDiagIF8I
    call python ApexInternalRamEccCircuitDiagnosticFaultInjectionTest2.py ApexDiagIF8I
    call python ApexInternalRamScrubberDiagnosticFaultInjectionTest1.py ApexDiagIF8I
    call python ApexInternalRamShadowFaultInjectionTest1.py ApexDiagIF8I
    call python ApexInternalSafeRamDiagnosticFaultInjectionTest1.py ApexDiagIF8I
    rem
    call python ApexInternalRamShadowFaultInjectionTest2.py ApexDiagIF8I
    call python ApexArmDataCacheDiagnosticFaultInjectionTest1.py ApexDiagOF8I
    call python ApexArmInstructionCacheDiagnosticFaultInjectionTest1.py ApexDiagOF8I
    call python ApexArmInstructionDiagnosticFaultInjectionTest1.py ApexDiagOF8I
    call python ApexArmInstructionDiagnosticFaultInjectionTest2.py ApexDiagOF8I
    rem
    call python ApexArmRegisterDiagnosticFaultInjectionTest1.py ApexDiagOF8I
    call python ApexArmRegisterDiagnosticFaultInjectionTest2.py ApexDiagOF8I
    call python ApexCompletionTimeDiagnosticFaultInjectionTest1.py ApexDiagOF8I
    call python ApexFirmwareBinaryCrcDiagnosticFaultInjectionTest1.py ApexDiagOF8I
    call python ApexFirmwareBinaryCrcDiagnosticFaultInjectionTest2.py ApexDiagOF8I
    rem
    call python ApexInteractiveWatchdogFaultInjectionTest1.py ApexDiagOF8I    
    call python ApexInternalRamAddressLineDiagnosticFaultInjectionTest1.py ApexDiagOF8I
    call python ApexInternalRamAddressLineDiagnosticFaultInjectionTest2.py ApexDiagOF8I
    call python ApexInternalRamEccCircuitDiagnosticFaultInjectionTest1.py ApexDiagOF8I
    call python ApexInternalRamEccCircuitDiagnosticFaultInjectionTest2.py ApexDiagOF8I
    rem
    call python ApexInternalRamScrubberDiagnosticFaultInjectionTest1.py ApexDiagOF8I
    call python ApexInternalRamShadowFaultInjectionTest1.py ApexDiagOF8I
    call python ApexInternalSafeRamDiagnosticFaultInjectionTest1.py ApexDiagOF8I
    call python ApexInternalRamShadowFaultInjectionTest2.py ApexDiagOF8I
    call python ApexStackDiagnosticFaultInjectionTest1.py ApexOsIRT8I
    rem
    call python ApexStackDiagnosticFaultInjectionTest1.py ApexOsIF8I
    call python ApexStackDiagnosticFaultInjectionTest1.py ApexOsOF8I
    call python BlackfinDataRamAsmFaultInjectionTest1.py BlackfinDiagIRT8I
    call python BlackfinInstructionAsmFaultInjectionTest1.py BlackfinDiagIRT8I
    call python BlackfinInstructionRamFaultInjectionTest1.py BlackfinDiagIRT8I
    rem
    call python BlackfinRegisterAsmFaultInjectionTest1.py BlackfinDiagIRT8I
    call python BlackfinTimerFaultInjectionTest1.py BlackfinDiagIRT8I
    call python BlackfinSchedulerFaultInjectionTest1.py BlackfinDiagIRT8I
    call python DspStackDiagnosticFaultInjectionTest1.py BlackfinOsIRT8I
    call python DSPInteractiveWatchdogFaultInjectionTest1.py BlackfinToolkitIRT8I
    rem
    call python BlackfinDataRamAsmFaultInjectionTest1.py BlackfinDiagIF8I
    call python BlackfinInstructionAsmFaultInjectionTest1.py BlackfinDiagIF8I
    call python BlackfinInstructionRamFaultInjectionTest1.py BlackfinDiagIF8I
    call python BlackfinRegisterAsmFaultInjectionTest1.py BlackfinDiagIF8I
    call python BlackfinTimerFaultInjectionTest1.py BlackfinDiagIF8I
    rem
    call python BlackfinSchedulerFaultInjectionTest1.py BlackfinDiagIF8I
    call python DspStackDiagnosticFaultInjectionTest1.py BlackfinOsIF8I
    call python DSPInteractiveWatchdogFaultInjectionTest1.py BlackfinToolkitIF8I
    call python BlackfinDataRamAsmFaultInjectionTest1.py BlackfinDiagOF8I
    call python BlackfinInstructionAsmFaultInjectionTest1.py BlackfinDiagOF8I
    rem
    call python BlackfinInstructionRamFaultInjectionTest1.py BlackfinDiagOF8I
    call python BlackfinRegisterAsmFaultInjectionTest1.py BlackfinDiagOF8I
    call python BlackfinTimerFaultInjectionTest1.py BlackfinDiagOF8I
    call python BlackfinSchedulerFaultInjectionTest1.py BlackfinDiagOF8I
    call python DspStackDiagnosticFaultInjectionTest1.py BlackfinOsOF8I
    rem
    call python DSPInteractiveWatchdogFaultInjectionTest1.py BlackfinToolkitOF8I
    call python If8iAdcCrcDiagnosticFaultInjectionTest1.py BlackfinProjectIF8I
    call python If8iAdcCrcDiagnosticFaultInjectionTest2.py BlackfinProjectIF8I
    call python If8iAdcWriteDiagnosticFaultInjectionTest1.py BlackfinProjectIF8I
    call python Irt8iAdcCrcDiagnosticFaultInjectionTest1.py BlackfinProjectIRT8I
    rem
    call python Irt8iAdcCrcDiagnosticFaultInjectionTest2.py BlackfinProjectIRT8I
    call python Irt8iAdcWriteDiagnosticFaultInjectionTest1.py BlackfinProjectIRT8I   
    call python Of8iDacCrcDiagnosticFaultInjectionTest1.py BlackfinProjectOF8I
    call python Of8iDacCrcDiagnosticFaultInjectionTest2.py BlackfinProjectOF8I
    call python Of8iDacWriteDiagnosticFaultInjectionTest1.py BlackfinProjectOF8I