from enum import Enum

class MessageType(Enum):
    
# Suspended message.
  SUSPENDED = -1

# Error message.
  ERROR = 0

# Warning message.
  WARNING = 1

# Success message.
  SUCCESS = 2

# Generic message.
  GENERIC = 3

# Informational message - Our default message type.
  INFORMATION = 4

# Verbose message.
  VERBOSE = 5