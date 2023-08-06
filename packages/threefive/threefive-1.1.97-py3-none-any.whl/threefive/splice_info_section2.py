from util import *


class Splice_Info_Section:    
    def __init__(self,chunk):
        self.table_id =hex(chunk[0])
        self.section_syntax_indicator = bitslice(chunk,103,1) 
        self.private = bitslice(chunk,102,1)
        self.reserved=bitslice(chunk,101,2)  
        self.section_length = bitslice(chunk,99,12)
        
        self.protocol_version = bitslice(chunk,87,8)
        self.encrypted_packet = bitslice(chunk,79,1) 
        self.encryption_algorithm = bitslice(chunk,78,6) 
        self.pts_adjustment = time_90k( bitslice(chunk,72,33)) 
        
        self.cw_index = hex( bitslice(chunk,39,8)) 
        self.tier = hex( bitslice(chunk,31,12))  
        self.splice_command_length =bitslice(chunk,19,12)

        self.splice_command_type = bitslice(chunk,7,8) 
        
        
chunked=bytes.fromhex('FC302F000000000000FFFFF014054800008F7FEFFE7369C02EFE0052CCF500000000000A0008435545490000013562DBA30A')[:14]

sis=Splice_Info_Section(chunked)
print(vars(sis))