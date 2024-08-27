import uuid

class JSONRPC:
  # Códigos de error estándar
  PARSE_ERROR = -32700
  INVALID_REQUEST = -32600
  METHOD_NOT_FOUND = -32601
  INVALID_PARAMS = -32602
  INTERNAL_ERROR = -32603

  @staticmethod
  def create_request(method, params, id=None):
    return {
      "jsonrpc": "2.0",
      "method": method,
      "params": params,
      "id": id or str(uuid.uuid4())
    }
  
  @staticmethod
  def create_response(result, id):
    return {
      "jsonrpc": "2.0",
      "result": result,
      "id": id
    }
  
  @staticmethod
  def create_notification(method, params): 
    return {
      "jsonrpc": "2.0",
      "method": method,
      "params": params
    }
  
  @staticmethod
  def create_error_response(code, message, id, data=None):
    error = {
      "code": code,
      "message": message
    }
    if data is not None:
      error['data'] = data
    return {
      "jsonrpc": "2.0",
      "error": error,
      "id": id
    }
  
  @classmethod
  def parse_error(cls, id=None):
      return cls.create_error_response(cls.PARSE_ERROR, "Parse error", id)

  @classmethod
  def invalid_request(cls, id=None):
      return cls.create_error_response(cls.INVALID_REQUEST, "Invalid Request", id)

  @classmethod
  def method_not_found(cls, id):
      return cls.create_error_response(cls.METHOD_NOT_FOUND, "Method not found", id)

  @classmethod
  def invalid_params(cls, id):
      return cls.create_error_response(cls.INVALID_PARAMS, "Invalid params", id)

  @classmethod
  def internal_error(cls, id):
      return cls.create_error_response(cls.INTERNAL_ERROR, "Internal error", id)


