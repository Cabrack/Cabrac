class CabracObject:
  def __init__(self, data):
    self.object = data

class CabracNumber(CabracObject):
  pass

class CabracString(CabracObject):
  pass

class CabracDict(CabracObject):
  pass

class CabracList(CabracObject):
  pass

class CabracBool(CabracObject):
  pass

class CabracFunction(CabracObject):
  pass

class CabracClass(CabracObject):
  pass

class CabracBuiltinFunction(CabracFunction):
  pass

class CabracError(CabracObject):
  pass

class CabracWarning(CabracError):
  pass

class CabracExit(CabracBuiltinFunction):
  pass
