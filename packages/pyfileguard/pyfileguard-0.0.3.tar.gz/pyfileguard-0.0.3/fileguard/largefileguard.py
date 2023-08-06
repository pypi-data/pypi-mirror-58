
import os

import binascii
import struct
import textwrap


SEG_FORMT = ">QQQ"
SEG_SIZE = struct.calcsize(SEG_FORMT)
SEG_MAGIC = 0xdeadbeef


class LargeFileGuard():
    
    def __init__(self,fnam,mode="r",always_restore=False,debug=False
                 ,blksize=512,keep_bim=False,**kwargs):
        self.fnam = fnam
        self.fd = None
        self.flen = None
        self.mode = mode
        self.kwargs = kwargs
        self.bimfd = None
        self.bimfile = None
        self.keep_bim = keep_bim
        self.debug = debug
        self.blksize = blksize
        self.always_restore = always_restore
        
        self.binary = self.mode.find("b")>=0
        
        
    def _print_d(self,*args):
        if self.debug:
            print(*args)
            
    def __enter__(self):
        self._print_d("__enter__")
        self.open()
        return self
    
    def __exit__( self, exception_type, exception_value, traceback ):
        self._print_d("__exit__", exception_type, exception_value, traceback)
        if exception_type is not None:
            self.rollback()
        self.close()
        
    def close(self):
        self._print_d("close")
        
        if self.fd and self.always_restore:
            self.rollback()
        
        if self.fd:
            self.fd.close()
            self.fd = None
        self._close()
            
    def _close(self):
        self._print_d("_close")
        if self.bimfd:
            if not self.keep_bim:
                self.bimfd.truncate()
            self.bimfd.close()
            self.bimfd = None
            if not self.keep_bim:
                os.remove( self.bimfile )
    
    def open(self):
        self._print_d("open")
        
        if self.fd:
            raise Exception("file already open")
        
        mode = self.mode
        if not self.binary:
            mode += "b"
            
        self.flen = os.path.getsize( self.fnam )        
        self.fd = open(self.fnam,mode)
        
        self.bimfile = self.fnam + ".bim"
        self.bimfd = open( self.bimfile, "+wb" )

        buf = self._pack( SEG_FORMT, self.flen, SEG_MAGIC, SEG_MAGIC )
        self._writebim(buf)
        
    def seek(self,offset, whence=0):
        return self.fd.seek(offset, whence)
    
    def tell(self):
        return self.fd.tell()
        
    def flush(self):
        self.fd.flush()
        
    def read(self,size=None):
        return self.fd.read(size)
        
    def write(self,buf):
        self._print_d("write")
        fpos = self.tell()
        
        if fpos < self.flen: # changing, not appending
            
            # preserve the content
            l = len(buf)
            while l > 0:
                toread = min( l, self.blksize )
                self._print_d(f"write next block size={toread}")
                bb = self.read(toread)
                self._writebim(bb)
                l -= len(bb)
            
            blen = len(buf)
            bb = self._pack( SEG_FORMT, fpos, blen, SEG_MAGIC )
            self._writebim(bb)
            self._print_d(f"write segment seek={fpos} len={blen}" )
            
            cpos = self.seek(fpos)
            if cpos != fpos:
                raise Exception(f"seek failed cpos={cpos}, expected={fpos}")
        
        if not isinstance(buf, bytearray):
            buf = buf.encode()
        self.fd.write(buf)
        
    def rollback(self):
        self._print_d("rollback")
        
        if self.fd and self.bimfd:
            
            blen = self.bimfd.seek(0,2)
            bpos = blen - SEG_SIZE
            
            while bpos > SEG_SIZE:
                fpos, blen, bpos = self._searchsegment( bpos )
                
                self._print_d( f"found segment seek={fpos}, len={blen}, bim={bpos}" )
                
                self.fd.seek(fpos)
                self.bimfd.seek(bpos-blen)
            
                l = blen
                while l>0:
                    toread = min( l, self.blksize )
                    self._print_d(f"restore next block size={toread}")
                    buf = self.bimfd.read(toread)
                    self.fd.write(buf)
                    l -= len(buf)
                
                bpos -= blen
                
            flen, dead1, dead2 = self._searchsegment( 0 )
            if dead1 != SEG_MAGIC:
                raise Exception("invalid bim file format")
            
            # preserve old file size
            self.fd.truncate( flen )
            # close bim file
            self._close()


    def _searchsegment( self, bpos ): # search a segment 
        while True:            
            if bpos < 0:
                raise Exception("invalid bim file format")            
            self.bimfd.seek(bpos)
            buf = self.bimfd.read(SEG_SIZE)
            fpos, blen, deadbeef = struct.unpack( SEG_FORMT, buf )
            if deadbeef == SEG_MAGIC:
                break
            # continue searching one below
            bpos-=1            
        return fpos, blen, bpos
    
    def _pack(self,format,*args):
        buf = bytearray(struct.calcsize(format))
        struct.pack_into(format, buf, 0, *args )
        return buf
    
    def _writebim(self,buf):
        self.bimfd.write( buf )
        self.bimfd.flush()
        

def dumpbim(fnam):
    try:
        with open(fnam+".bim", "rb" ) as f:
            cb = f.read()
            hb = binascii.hexlify( cb ).decode()
            return textwrap.wrap( hb, width=8*4*2 )
    except Exception as ex:
        return ex
    
    
    