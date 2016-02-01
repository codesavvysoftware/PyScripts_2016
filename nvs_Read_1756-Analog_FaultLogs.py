# ***************************************************************************
#
#  This script reads the Fault Log information from a 1756-Analog (IF8I, IRT8I
#   or OF8I) module, parses the data into a readable formatted file
#   FIT_Results.txt.  This script was created for the FIT tests, but could be
#   used to read any fault log from the module.  If there are multiple faults
#   in the log, they will all be read out and stored in the file FIT_Results.txt.
#
#  Some things to note about this script;
#
#   1.  It needs to be run from the Release directory with the firmware bin files
#   2.  If the firmware bin file, Dsp_L1_data_a.bin, is available, it will read
#       the source file name. (see below for how to produce this file)
#   3.  If the firmware bin file, Apex_Async0.bin, is available, it will read
#       the source file name.  (see below for how to produce this file)
#   4.  It dumps the fault log information to a file, FIT_Results.txt
#   5.  The script needs to be modified for the RSLinx path to the module under test.
#       (see PrepareNodePaths at the top of the script)
#   
#   \Analog\NextGen\Blackfin\1756IRT8I\Release_FIT_Apex_Stack>"C:\Program
#    Files\Analog Devices\VisualDSP 5.0\elfpatch" -get L1_data_a -o Dsp_L1_data_a.bin IRT8I.dxe
#
#   \Analog\NextGen\Blackfin\1756IRT8I\Release_FIT_Apex_Stack>"C:\Program
#    Files\Analog Devices\VisualDSP 5.0\elfpatch" -get ASYNC0_ApexBinary -o Apex_Async0.bin IRT8I.dxe
#   
#   
#  This program is the property of The Allen-Bradley Company and it shall
#  not be reproduced, distributed, or used without permission of an
#  authorized company official. This is an unpublished work subject to
#  Trade Secret and Copyright protection.
#
#     ----- Copyright 2016 Allen-Bradley Company Inc. -----
#
# ***************************************************************************

from struct import unpack
import ratools.cip.channel as channel
import ratools.cip.utils as utils


# ********************************
# Fault Log Parameters
# ********************************
faultLogAddress    = 0x200E0000
faultLogAddressEnd = 0x200F0000
oldFaultLogSize    = 0x160
maxFaultLogSize    = 0x1f0
faultLogSize       = oldFaultLogSize

nodes = {}

def PrepareNodePaths():
    nodes[0] = channel.create(path=r'AB_VBP-1\16\1\1',authenticate=[])  # 1756-OF8I
    nodes[1] = channel.create(path=r'AB_VBP-1\16\1\2',authenticate=[])  # 1756-IF8I
    nodes[2] = channel.create(path=r'AB_VBP-1\16\1\3',authenticate=[])  # 1756-IF8I

def sendCipRequest(node, cip):
    loop = 4
    response = str(0)
    for i in range(loop):
        try:
            response = nodes[node].cipMessage(utils.packAdr(cip))
            break
        except utils.CipResponseError, exception_data:
            if i == (loop-1):
                print exception_data
                print 'error from node: %d \n' % node
            response = '0xDEADBEEF'
        except:
            if i == (loop-1):       
                print 'unknown error from Node: %d Cip request: %s ' % (node, cip)
            response = str('9999')
    return response
    

def GetIdString(node):
    cip = 'GET_ATTRIBUTE_SINGLE:0x1.1.7'  # attribute 7 - product name string
    return sendCipRequest(node, cip)


def GetIdAll(node):
    cip = 'GET_ATTRIBUTES_ALL:0x1.1'
    return sendCipRequest(node, cip)
    

def sendCipMessage(node, message):
    loop = 4
    response = str(0)
    for i in range(loop):
        try:
            response = nodes[node].cipMessage(message)
            break
        except utils.CipResponseError, exception_data:
            if i == (loop-1):
                print exception_data
                print 'error from node %d \n' % node
            response = str('0xDEADBEEF')
        except:
            if i == (loop-1):
                print 'unknown  NVS Read error from Node: %d ' % node
            response = str('9999')
    return response


def nvs_Read(node, address, size):
    """
    NVS Object Read Service, Instance 4
    :rtype: str
    :param node: Node number to read
    :type node: int
    :param address: Physical Memory Address into NVS device
    :type address: int
    :param size: Amount of memory to read in bytes
    :type size: int
    """
    cls,ins = 0xA1, 4   # Nvs Object Class Code, Instance
    service = 0x4F      # Nvs Read service
    data = [service, [[cls,ins]], address, size]  # Nvs address to read, size
    fmt  = ['SINT' ,   'IOI'    ,  'DINT', 'UINT']
    message = utils.packdata(data,fmt)
    return sendCipMessage(node, message)


def GetStringFromBin(file, addr):
    try:
        f = open(file, 'rb')
    except IOError:
        return "---------- ERROR: could not open file %s" % file
    f.seek(addr)
    r = ''
    while True :
        try:
            c = '\0'
            c = f.read(1)
            if (c == '\0'):
                break
            elif (c== ''):
                break
        except:
           break
        r += c
    f.close
    return r
    

# these parse statements assume data is type 'str'
# 'str' appears to be the format of data returned from cipMessage
def parse1(data, i):
    return unpack('B',data[i:i+1]), i+1

def parse2(data, i):
    return unpack('H',data[i:i+2]), i+2

def parse4(data, i):
    return unpack('L',data[i:i+4]), i+4


def ParseFaultLog(data):
    global faultLogSize
    length = len(data)
    i = 0
    s = ''
    v,i = parse4(data,i) ; s += 'Marker         0x%08x \n' % v
    if ((v[0] == 0xa0a0a0a0) | (v[0] == 0xb0b0b0b0)) :
        v,i = parse2(data,i) ; s += 'Size                 %4d \n' % v
        faultLogSize = v[0]
        v,i = parse1(data,i) ; s += 'Major Rev             %3d \n' % v
        v,i = parse1(data,i) ; s += 'Minor Rev             %3d \n' % v
        v,i = parse4(data,i) ; s += 'Sub Minor Rev        %4d \n' % v
    v,i = parse2(data,i) ; s += 'Error Num            %4d \n' % v
    v,i = parse2(data,i)
    v,i = parse4(data,i) ; s += 'BF File *      0x%08x \n' % v
    if ((v[0] > 0xff800000) & (v[0] < 0xff808000)) :
        addr = (v[0] & 0x7fff) - 20
        s += 'BF File Name   %s \n' % GetStringFromBin('Dsp_L1_data_a.bin', addr)
    v,i = parse2(data,i) ; s += 'BF Line Num          %4d \n' % v
    v,i = parse2(data,i)
    v,i = parse4(data,i) ; s += 'Seq Stat       0x%08x \n' % v
    v,i = parse4(data,i) ; s += 'Reti           0x%08x \n' % v
    v,i = parse4(data,i) ; s += 'Retx           0x%08x \n' % v
    v,i = parse4(data,i) ; s += 'Rete           0x%08x \n' % v
    v,i = parse4(data,i) ; s += 'Retn           0x%08x \n' % v
    v,i = parse4(data,i) ; s += 'Frame *        0x%08x \n' % v
    v,i = parse4(data,i) ; s += 'Stack *        0x%08x \n' % v
    v,i = parse4(data,i) ; s += 'preserved1     0x%08x \n' % v
    v,i = parse4(data,i) ; s += 'preserved2     0x%08x \n' % v
    v,i = parse4(data,i) ; s += 'preserved3     0x%08x \n' % v
    v,i = parse4(data,i) ; s += 'preserved4     0x%08x \n' % v
    v,i = parse4(data,i) ; s += 'preserved5     0x%08x \n' % v
    v,i = parse4(data,i) ; s += 'preserved6     0x%08x \n' % v
    v,i = parse4(data,i) ; s += 'preserved7     0x%08x \n' % v
    v,i = parse4(data,i) ; s += 'Port G         0x%08x \n' % v
    v,i = parse4(data,i) ; s += 'Apex File *    0x%08x \n' % v
    if ((v[0] > 0x20000) & (v[0] < 0x30000)) :
        addr = v[0] - 0x20000
        s += 'Apex File Name %s \n' % GetStringFromBin('Apex_Async0.bin', addr)
    v,i = parse2(data,i) ; s += 'Apex Line Num        %4d \n' % v
    v,i = parse2(data,i)
    v,i = parse2(data,i) ; s += 'User param 1         %4d \n' % v
    v,i = parse2(data,i)
    v,i = parse4(data,i) ; s += 'User param 2   0x%08x \n' % v
    v,i = parse4(data,i) ; s += 'User param 3 * 0x%08x \n' % v
    s += '\nStack, values in hex\n'
    m = (length - i)/4/4  # 64 bytes /4 DINTs per row
    while m :
        m -= 1
        n = 4
        while n :
            n -= 1
            v,i = parse4(data,i) ; s += '  %08x' % v
        s += '\n'
        
    s += '\n'
    return s
    

def ParseIdObjAll(data):
    length = len(data)
    i = 0
    s = ''
    v,i = parse2(data,i) ; s += 'Vendor ID:           %4d \n' % v
    v,i = parse2(data,i) ; s += 'Product Type:        %4d \n' % v
    v,i = parse2(data,i) ; s += 'Product Code:        %4d \n' % v
    v,i = parse1(data,i) ; s += 'Revision:        %4d.' % v
    v,i = parse1(data,i) ; s += '%03d \n' % v
    v,i = parse2(data,i) ; s += 'Status:            0x%04x \n' % v
    v,i = parse4(data,i) ; s += 'Serial Num:      %08x \n' % v
    v,i = parse1(data,i)
    s += 'Device Name:   '
    s += data[i:length]

    s += '\n\n'
    return s
    

# main

PrepareNodePaths()  # sets paths for nodes to scan

try:
    fo = open('FIT_Results.txt', 'a')
except IOError:
    print "\nERROR: could not open file %s" % 'FIT_Results.txt'
    exit()

for n in nodes :  # collect data from 1 or multiple nodes
    fo.write('node path: %s \n' % nodes[n].path)
    s = GetIdString(n)
    if (s == '0xDEADBEEF') | (s == '9999') :
        continue
    fo.write(s[1:] + '\n')  # drop the first byte, its the size of the string
    s = GetIdAll(n)
    if (s == '0xDEADBEEF') | (s == '9999') :
        continue
    s = ParseIdObjAll(s)
    fo.write(s)
    m = ''
    i = 0
    memoryAddress = faultLogAddress
    while True :
        faultLogSize = oldFaultLogSize
        r = nvs_Read(n, memoryAddress, maxFaultLogSize)
        m,i = parse4(r,0)
        if m[0] == 0xffffffff :
            break
        s = ParseFaultLog(r)
        fo.write(s)
        memoryAddress += faultLogSize

        memoryAddrCalc = faultLogAddressEnd - faultLogSize
        print memoryAddress

        if memoryAddress >= memoryAddrCalc :
            r = nvs_Read(n, memoryAddress, 4)
            m,i = parse4(r,0)
            break
        if memoryAddrCalc < 0 :
            r = nvs_Read(n, memoryAddress, 4)
            m,i = parse4(r,0)
            break
    fo.write('Done 0x%08x = %x \n\n' % (memoryAddress, m[0]))

fo.close()
