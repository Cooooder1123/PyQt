import pathlib,os
import binascii
import json

def is_exists(path):
    if path.exists():
        return True
    else:
        return False

def crc32asii(str):
    """
    �����ַ�����CRCУ�飬�ַ�����GBK���룬����У�����ַ���
    :param str:
    :return:
    """
    str=str.encode('GBK')
    return '0x%8x' % (binascii.crc32(str) & 0xffffffff)

def crc32hex(str):
    return '%08x' % (binascii.crc32(binascii.a2b_hex(str)) & 0xffffffff)

def getChstr(msg):
    """
    ����msg�Ѿ���json��ʽ���ǲ���json��ʽ������һ��json.load
    !!!ע��Ҫ��json �﷨�涨 ��������֮�е��ַ�������ʹ��˫���ţ�����ʹ�õ�����
    :param msg:
    :return:
    """
    #���ַ�����json����
    dictmsg=json.load(msg)
    dictmsg.pop("chsum")

if __name__=="__main__":
    str='{"filename":"123"}'.encode("GBK")
    print(json.load(str))