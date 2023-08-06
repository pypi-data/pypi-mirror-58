from .splice_commands import *
from .descriptors import *
from .splice_info_section import *
from  bitslicer9k import Slicer9k

class Splice:
    def __init__(self,mesg):
        mesg=mk_bits(mesg)
        bs=Slicer9k(mesg)
        self.descriptors=[]
        self.info_section=Splice_Info_Section(bs)
        self.set_splice_command(bs) 
        self.info_section.descriptor_loop_length = bs.asint(16) 
        tag_plus_header_size=2 # 1 byte for descriptor_tag, 1 byte for header?
        dll=self.info_section.descriptor_loop_length
        while dll> 0:
            try: 
                sd=self.set_splice_descriptor(bs)
                sdl=sd.descriptor_length
                self.descriptors.append(sd)
            except: sdl=0
            bit_move=sdl+ tag_plus_header_size
            dll -=(bit_move)
        self.info_section.crc=bs.ashex(32)

    def set_splice_command(self,bs):
        cmd_types={ 0: Splice_Null,
		4: Splice_Schedule,
		5: Splice_Insert,
		6: Time_Signal,
		7: Bandwidth_Reservation,
		255: Private_Command}
        self.command=False
        sct=self.info_section.splice_command_type
        if sct in cmd_types.keys(): self.command=cmd_types[sct](bs,sct)
   
    def set_splice_descriptor(self,bs):
        dscr_types={0: Avail_Descriptor,
		1: Dtmf_Descriptor,
		2: Segmentation_Descriptor,
		3: Time_Descriptor,
		4: Audio_Descriptor}   
        # splice_descriptor_tag 8 uimsbf
        tag= bs.asint(8)
        if tag in dscr_types.keys(): return dscr_types[tag](bs,tag)
                
    def show_info_section(self):
        print('\n Splice Info Section:')
        kv_print(self.info_section)

    def show_command(self):
        print('\n Splice Command:')
        kv_print(self.command)
		
    def show_descriptors(self):
        for d in self.descriptors:
            idx=self.descriptors.index(d)
            print(f'\n Splice Descriptor {idx}:')
            kv_print(d)
		
    def show(self):
        print('\n\n[SCTE 35 Message]')
        self.show_info_section()
        self.show_command()
        self.show_descriptors()
	


