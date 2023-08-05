import ctypes
from enum import IntEnum



CONST_FIRMWARE_RELEASE_TYPE = ["Test","Alpha","Beta","RC","RTM","GA"]

class SmTesterConstants(object):
    # This is converted to bytes and used as salt with the PBKDF2 key generation algortihm.
    # Resulting Key must be stored in the smtster device so that smtester can decrypt the special formatted hex data.
    CONST__DEVICE_KEY_SALT = "SONM-Fixed-Salt@"




class EnumPartId(IntEnum):
    PART_ID_STM32F100 = 0x00000103,
    PART_ID_PSOC4124_16KB = 0x41240000


class ENUM_CHIP_LEVEL_PROTECTION(IntEnum):
    VIRGIN = 0,
    OPEN = 1,
    PROTECTED = 2,
    KILL = 4


class EnumIntelPurpose(IntEnum):
    FOR_DIRECT_HEX_PROGRAMMING = 0,
    FOR_UPGRADE = 1

class ENUM_SPECIAL_RECORD_ADDRESSES(IntEnum):
    # 002-22325_CY8C4xxx_CYBLxxxx_Programming_Specifications
    PSOC4_CHECKSUM_ADDRESS = 0x90300000,        # 2BYTES
    PSOC4_FLASH_PROTECTION_ROWS = 0x90400000,   # SIZE VARIES
    PSOC4_METADATA = 0x90500000,                # 12 BYTES
    PSOC4_CHIP_LEVEL_PROTECTION = 0x90600000,   # 1 BYTE

class SMTESTER_HEX_FILE_HEADER_PSOC4124(ctypes.Structure):
    def __init__(self):
        self.signature = 0x52588B45
        self.target_chip = 0
        self.sector_count = 0
        self.sector_size = 0
        #self.random_encryption_key = [0,]*4  #[0x00000000,0x00000000,0x00000000,0x00000000]
        self.hex_protection_data_length = 0
        self.hex_protection_data = (ctypes.c_uint8 * 64)() #(ctypes.c_uint8 * 16)() #()

        #self.hex_protection_data = [0,]*16
        self.hex_silicon_id = 0x00000000
        self.hex_checksum = 0x0000
        self.chip_protection_level = 2 # 2-Z Protected

        #super().__init__(target_chip = self.target_chip)

    # Order of types are important for number of bytes inside the structure
    # Header is considered to  be 128 byte. Device will read first 128 byte for header reconstruction
    _fields_ = [("signature", ctypes.c_uint32),
                ("hex_silicon_id", ctypes.c_uint32),
                ("target_chip", ctypes.c_uint32),
                ("sector_count", ctypes.c_uint16),
                ("sector_size", ctypes.c_uint16),
                ("hex_checksum", ctypes.c_uint16),
                ("chip_protection_level", ctypes.c_uint16),
                ("hex_protection_data_length", ctypes.c_uint16),
                ("hex_protection_data", (ctypes.c_uint8*64)),
                ("reserved_data", (ctypes.c_uint8 * 42))]  # Structure is completed to 128 byte


class SMTESTER_BOOTLOADER_KEYS(ctypes.Structure):
    def __init__(self):
        self.masterkeys = (ctypes.c_uint32 * 4)()
        self.firstimekeys = (ctypes.c_uint32 * 4)()
        self.statickeys = (ctypes.c_uint32 * 4)()

        #super().__init__(target_chip = self.target_chip)

    # Order of types are important for number of bytes inside the structure
    # Header is considered to  be 128 byte. Device will read first 128 byte for header reconstruction
    _fields_ = [("masterkeys", ctypes.c_uint32*4),
                ("firstimekeys", ctypes.c_uint32*4),
                ("statickeys", ctypes.c_uint32*4)]

