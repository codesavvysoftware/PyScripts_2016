rem DeleteFITObjAndDepFiles.bat
rem
rem Deletes the object and dependency files for all of the files that are modified for any of the fault injection tests.
rem
rem This is a work around for the issue where new object files are not built when their source files are reverted when
rem unchecked out.
rem
rem Do a remove all on everything except Apex\Release and Apex\ControlBus\Release. Use rmdir for all of these.
rem For Apex\Release and Apex\ControlBus\Release, remove only all *.o and *.d. Use either del or rm for these. Probably del *.o and del *.d
rem
rem Flash memory diagnostics cannot be included in batch file and must be built manually with cleans before every build.
rem
echo Entering DeleteFITObjAndDepFiles.bat
echo.
echo Removing %1\LNX\NetLinxUCS\Proj_ARM_A9_NetLinxUCS_CNzR_DKM\ARMARCH7gnu\Proj_NetLinxUCS\NonDebug\Objects\NcsSrc\CommPorts\Backplane
echo.
rmdir /s /q %1\LNX\NetLinxUCS\Proj_ARM_A9_NetLinxUCS_CNzR_DKM\ARMARCH7gnu\Proj_NetLinxUCS\NonDebug\Objects\NcsSrc\CommPorts\Backplane
echo.
echo Removing %1\LNX\NetLinxUCS\Proj_ARM_A9_NetLinxUCS_CNzR_DKM\ARMARCH7gnu\Proj_NetLinxUCS\NonDebug\Objects\NcsSrc\PlatformCommon
echo.
rmdir /s /q %1\LNX\NetLinxUCS\Proj_ARM_A9_NetLinxUCS_CNzR_DKM\ARMARCH7gnu\Proj_NetLinxUCS\NonDebug\Objects\NcsSrc\PlatformCommon
echo.
echo Removing %1\LNX\NetLinxUCS\Proj_ARM_A9_NetLinxUCS_CNzR_DKM\ARMARCH7gnu\Proj_NetLinxUCS\NonDebug\Objects\NcsSrc\Diagnostic
echo.
rmdir /s /q %1\LNX\NetLinxUCS\Proj_ARM_A9_NetLinxUCS_CNzR_DKM\ARMARCH7gnu\Proj_NetLinxUCS\NonDebug\Objects\NcsSrc\Diagnostic
echo.
echo Removing %1\LNX\Platform\BSP\Board\Ice2_CNzR\PV\Proj_CNzR_PV_BSP_DKM\ARMARCH7gnu\Proj_CNzR_PV_BSP_DKM_partialImage\NonDebug\Objects\RaSupport
echo.
rmdir /s /q %1\LNX\Platform\BSP\Board\Ice2_CNzR\PV\Proj_CNzR_PV_BSP_DKM\ARMARCH7gnu\Proj_CNzR_PV_BSP_DKM_partialImage\NonDebug\Objects\RaSupport
echo.
echo Removing %1\LNX\NetLinxUCS\Proj_Diagnostics_DKM\ARMARCH7gnu
echo.
rmdir /s /q %1\LNX\NetLinxUCS\Proj_Diagnostics_DKM\ARMARCH7gnu
echo.
echo Deleting %1\LNX\Logix\Engine\Subsystems\Apex\Release\*.o
echo.
del %1\LNX\Logix\Engine\Subsystems\Apex\Release\*.o
echo.
echo Deleting %1\LNX\Logix\Engine\Subsystems\Apex\Release\*.d
echo.
del %1\LNX\Logix\Engine\Subsystems\Apex\Release\*.d
echo.
echo Deleting %1\LNX\Logix\Engine\Subsystems\Apex\ControlBus\Release\*.o
echo.
del %1\LNX\Logix\Engine\Subsystems\Apex\ControlBus\Release\*.o
echo.
echo Deleting %1\LNX\Logix\Engine\Subsystems\Apex\ControlBus\Release\*.d
echo.
del %1\LNX\Logix\Engine\Subsystems\Apex\ControlBus\Release\*.d
echo.
echo Exiting DeleteFITObjAndDepFiles.bat
echo.
