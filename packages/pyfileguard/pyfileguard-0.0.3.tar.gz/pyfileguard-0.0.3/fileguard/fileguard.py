
import os

from tempfile import TemporaryFile


class FileGuard():
    
    def __init__(self,fnam,mode="r",always_restore=False,debug=False,blksize=512,**kwargs):
        self.fnam = fnam
        self.mode = mode
        self.kwargs = kwargs
        self.tmpfile = None
        self.fd = None
        self.debug = debug
        self.blksize = blksize
        self.always_restore = always_restore
        
    def _print_d(self,*args):
        if self.debug:
            print(*args)
        
    def open(self):
        self._print_d("open")
        self.tmpfile = TemporaryFile()
        with open(self.fnam,"rb") as f:
            while True:
                buf = f.read(self.blksize)
                if len(buf)==0:
                    break
                self._print_d(f"copy next block size={len(buf)}")
                self.tmpfile.write(buf)
                #print(">",buf)
        self.fd = open( self.fnam, self.mode, **self.kwargs )
        return self.fd
            
    def close(self):
        self._print_d("close always_restore=", self.always_restore)
        
        if self.always_restore:
            self.rollback()
            
        if self.fd:
            self.fd.close()
            self.fd = None
        if self.tmpfile:
            self.tmpfile.close()
            self.tmpfile = None
        
    def rollback(self):
        self._print_d("rollback")
        
        if self.fd:
            self._print_d("do rollback")
            
            # close current file
            self.fd.close()
            self.fd = None
            
            # copy old content back
            with open( self.fnam, "wb" ) as f:
                self._print_d("copy back")
                self.tmpfile.seek(0)
                while True:
                    buf = self.tmpfile.read(self.blksize)
                    if len(buf)==0:
                        break
                    self._print_d(f"restore next block size={len(buf)}")
                    f.write(buf)
                    
            self._print_d("done rollback")
            
    def __enter__(self):
        self._print_d("__enter__")
        return self.open()
    
    def __exit__( self, exception_type, exception_value, traceback ):
        self._print_d("__exit__", exception_type, exception_value, traceback)
        if exception_type is not None:
            self.rollback()
        self.close()
        
        