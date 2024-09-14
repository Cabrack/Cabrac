from types import *

class NoEquivalentObject:
  def __init__(self, _class):
    self._class = _class

class CabracObject:
  __type = object
  def __init__(self, data):
    self.object = data

class CabracNull(CabracObject):
  __type = NoneType

class CabracNumber(CabracObject):
  __type = float

class CabracString(CabracObject):
  __type = str

class CabracDict(CabracObject):
  __type = dict

class CabracList(CabracObject):
  __type = list

class CabracBool(CabracObject):
  __type = bool

class CabracFunction(CabracObject):
  __type = FunctionType

class CabracClass(CabracObject):
  __type = type

class CabracError(CabracObject):
  __type = Exception

class CabracWarning(CabracError):
  __type = Warning

class CabracGet(CabracObject):
  __type = NoEquivalentObject(CabracGet)

class CabracLiteralObj(CabracObject):
  __type = NoEquivalentObject(CabracLiteralObj)

def inheritors(_class):
    subclasses = set()
    work = [_class]
    while work:
        parent = work.pop()
        try:
            subclasses = parent.__subclasses__(parent)
        except:
            subclasses = parent.__subclasses__()
        for child in subclasses:
            if child not in subclasses:
                subclasses.add(child)
                work.append(child)
    return subclasses

def get_class_from_python_type(python_type):
  for child in inheritors(CabracObject):
    if issubclass(python_type, child.__type):
      return child
  return NoEquivalentObject