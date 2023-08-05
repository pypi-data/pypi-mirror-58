
import os
from . import _nighresjava

__module_dir__ = os.path.abspath(os.path.dirname(__file__))

class JavaError(Exception):
  def getJavaException(self):
    return self.args[0]
  def __str__(self):
    writer = StringWriter()
    self.getJavaException().printStackTrace(PrintWriter(writer))
    return "\n".join((str(super(JavaError, self)), "    Java stacktrace:", str(writer)))

class InvalidArgsError(Exception):
  pass

_nighresjava._set_exception_types(JavaError, InvalidArgsError)
CLASSPATH = [os.path.join(__module_dir__, "nighresjava.jar"), os.path.join(__module_dir__, "cbstools-lib.jar"), os.path.join(__module_dir__, "imcntk-lib.jar"), os.path.join(__module_dir__, "commons-math3-3.5.jar"), os.path.join(__module_dir__, "Jama-mipav.jar")]
CLASSPATH = os.pathsep.join(CLASSPATH)
_nighresjava.CLASSPATH = CLASSPATH
_nighresjava._set_function_self(_nighresjava.initVM, _nighresjava)

from ._nighresjava import *
