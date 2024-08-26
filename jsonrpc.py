import uuid

class JSONRPC:

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


