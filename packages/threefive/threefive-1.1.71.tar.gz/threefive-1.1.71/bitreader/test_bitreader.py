#try:
#    from _bitreader import *
#except ImportError:
from bitreader import *

def testBasicWithProfiling():
    
    for x in xrange(1000):
        result = BitData(['test1',4,'test2',4])
        result.test1 = 0xF
        result.test2 = 0xE
        assert result.dump() == array('B', [0xfe])
    
    try:
        result = BitData(['test1',4,'test2',4])
        result.test1 = 0xFF
        result.test2 = 0xE
        result.dump()    
    except OverflowError:
        pass
    else:
        assert False, "OverflowError expected"
    
    for x in xrange(5000):
        
        reader = BitReader(['test1', 4, 'dummy',4, 'test2', 8])
        result = reader.read([0xf0, 0x0e])
        
        assert result.test1 == 0xf
        assert result.dummy == 0x0
        
        # Test reading value larger than 1 byte
        reader = BitReader(['test1', 12, 'test2', 4])
        result = reader.read([0xfe, 0xda])
        assert result.test1 == 0xFED
        assert result.test2 == 0xA
        assert result.dump() == array('B', [0xfe, 0xda])
        data = ( 1 << 3 ) | ( 1 << 2 ) | ( 1 )
        assert data == 0xD, hex(data)

    print "Tests passed"

def testLittleEndianData():
    print "testLittleEndianData"
    data = open("../testdata/little-endian-data.bin",'rb').read()
    
    # Reading 24b integer( 0x123456 as value, but 0x563412 in file\memory )
    spec = ["int24", 24]
    r = BitReader(spec, endianess = BitReader.LITTLE_ENDIAN)
    d = r.read(map(ord,data))
    
    assert d.int24 == 0x123456, hex(d.int24)
    
    return d

def testLittleEndianDump():
    print "testLittleEndianDump"
    
    spec = ["int24", 24, "int8", 8]
    r = BitReader(spec, endianess = BitReader.LITTLE_ENDIAN)
    d = r.read(0x123456FF)
    
    data = d.dump()
    
    assert data[0] ==0x56, map(hex,data)
    assert data[1] ==0x34, map(hex,data)
    assert data[2] ==0x12, map(hex,data)
    assert data[3] ==0xFF, map(hex,data)

def testBigEndianDump():
    print "testBigEndianDump"

    spec = ["int24", 24, "int8", 8]
    r = BitReader(spec, endianess = BitReader.BIG_ENDIAN)
    d = r.read(0x123456FF)

    data = d.dump()

    assert data[0] ==0x12, map(hex,data)
    assert data[1] ==0x34, map(hex,data)
    assert data[2] ==0x56, map(hex,data)
    assert data[3] ==0xFF, map(hex,data)
    
def testCompareSpeedWithBitShifts(iterations = 100000):
    import time
    
    print "With %d iterations" % ( iterations )
    # The BitReader stores the data into a container so we must do
    # it here as well to have the results match with real life.
    data      = 0xFEDCBA         # 3 bytes of data    
    start = time.clock()
    i = iterations
    while i:
        i-=1
        d = {}
        d["sync_byte"]  = data >> 16       # Get first 8 bits
        d["tei"]        = data >> 15 & 0x1 # Read 1 bit
        d["payl_start"] = data >> 14 & 0x1 # Read 1 bit
        d["tp"]         = data >> 13 & 0x1 # Read 1 bit
        d["pid"]        = data & 0x1FFF    # Get last 13 bits
    print "Normal bitshifts took:", time.clock() - start
    
    data      = (0xFE,0xDC,0xBA)
    spec = (
        # Name of the data to read
        'sync_byte',
        # How many bits to read( 8 bits = 1 byte )
        8,
        'tei',
        1,
        'payl_start',
        1,
        'tp',
        1,
        'pid',
        13
    )
    reader = BitReader(spec)
    
    start = time.clock()
    i = iterations
    while i:
        i-=1
        result = reader.read(data)
        
    print "BitReader took:", time.clock() - start
    
    assert result.sync_byte == 0xFE

def testHavingIntegerAsData():

    print "testHavingIntegerAsData"

    spec = ["val1", 8, "val2", 8, "val3", 8, "val4", 4, "val5", 4]
    
    r = BitReader(spec)
    d1 = r.read(0xAABBCCDE)
    d2 = r.read([0xAA,0xBB,0xCC,0xDE])
    
    assert d1.val1 == 0xAA, d1.val1
    assert d1.val2 == 0xBB, d1.val2
    assert d1.val3 == 0xCC, d1.val3
    assert d1.val4 == 0xD,  d1.val4
    assert d1.val5 == 0xE,  d1.val5
    
    assert d1.val1 == d2.val1
    assert d1.val2 == d2.val2
    assert d1.val3 == d2.val3
    assert d1.val4 == d2.val4
    assert d1.val5 == d2.val5
    
from StringIO import StringIO

def testSubspec():
    # A specification defines names of variables and how many bits they need
    spec    = ['test1', 12, 'test2', 4,
               "countinfo",
               4,
               'data',
               {
                "countby" : "countinfo",
                "spec"    : [
                    "value",
                    8
                ]
               },
               'data2',
               {
                "count"   : 1,
                "spec"    : [
                    "value",
                    4
                ]
               },
               'subspec_size',
               4,
               'subspec_sizeby',
               {
                # Sizeby as size in bytes
                "sizeby" : "subspec_size",
                "spec"    : [
                    "value1",
                    4,
                    "value2",
                    4
                ]
               },
               'subspec_size',
               {
                # Size as size in bytes
                "size"    : 2,
                "spec"    : [
                    "value1",
                    4,
                    "value2",
                    4
                ]
               },
              ]
    
    reader = BitReader(spec)
    result = reader.read([0xfe, 0xda,0x2A,0xBC,0xD8,0x21,0x23,0x45,0x67,0x80])
    
    # The result contains the variables as attributes
    print hex(result.test1)
    print hex(result.test2)
    print hex(result.countinfo)
    print hex(result.data[0].value)
    assert result.data[0].value == 0xAB, hex(result.data[0].value)
    assert result.data[1].value == 0xCD, hex(result.data[1].value)
    assert result.data2[0].value == 0x8, hex(result.data2[0].value)
    
    assert result.subspec_sizeby[0].value1 == 0x1, hex(result.subspec_sizeby[0].value1)
    assert result.subspec_sizeby[0].value2 == 0x2, hex(result.subspec_sizeby[0].value2)
    assert result.subspec_sizeby[1].value1 == 0x3, hex(result.subspec_sizeby[1].value1)
    assert result.subspec_sizeby[1].value2 == 0x4, hex(result.subspec_sizeby[1].value2)
    
    assert result.subspec_size[0].value1 == 0x5, hex(result.subspec_sizeby[0].value1)
    assert result.subspec_size[0].value2 == 0x6, hex(result.subspec_sizeby[0].value2)
    assert result.subspec_size[1].value1 == 0x7, hex(result.subspec_sizeby[1].value1)
    assert result.subspec_size[1].value2 == 0x8, hex(result.subspec_sizeby[1].value2)
    
    reader = BitReader(['test1', 4, 'dummy',4, 'test2', 8])
    result = reader.read([0xfe,0xFF])
    #result = reader.read([0xe])
    assert result.test1 == 0xf , result.test1
    assert result.dummy == 0xe , result.dummy
    
    spec = [
        'size', 8,
        'text',
        {
          "sizeby" : "size",
          "spec"   : [
             "char", 8
          ]
        }
    ]

    text = "Hello World!"
    
    data = [len(text)]+map(ord,text)
    #print map(hex,data)
    reader = BitReader(spec)
    result = reader.read(data)
    print "".join([chr(x.char) for x in result.text])

def main():
    testSubspec()
    testHavingIntegerAsData()
    testLittleEndianData()
    testLittleEndianDump()
    testBigEndianDump()
    testCompareSpeedWithBitShifts()

    import doctest
    doctest.testmod()
    
    import hotshot
    prof = hotshot.Profile("BitReader.stats")
    prof.runcall(testBasicWithProfiling)
    prof.close()
    
    # 400001 function calls in 37.529 CPU seconds
    from hotshot import stats
    s = stats.load("BitReader.stats")
    s.sort_stats("time").print_stats()

    
if __name__ == '__main__':
    main()
    