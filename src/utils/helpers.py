import datetime
import uuid

def generate_session_id():
    """Generates a unique ID for server sessions."""
    return str(uuid.uuid4())

def get_timestamp():
    """Returns standard ISO format timestamp."""
    return datetime.datetime.now().isoformat()

def validate_payload(data):
    """Basic check for incoming server packets."""
    required_fields = ['header', 'timestamp', 'payload']
    return all(field in data for field in required_fields)
