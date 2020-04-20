
from Framework.utilities.logging import Logger, MessageType
from Framework.utilities.helper import StringProcessor

class ConsoleLogger(Logger):
# Initializes a new instance of the ConsoleLogger class.
  def ConsoleLogger(self):
    self(MessageType.INFORMATION);

# Initializes a new instance of the ConsoleLogger class.
# @param level The logging level./
  def ConsoleLogger(self, level):
    super(level)

# Write the formatted message (one line) to the console as a generic message.
# @param message The message text
# @param args String format arguments
# @Override
  def log_message(self, message, args):
    self.write_line(message, args)

# Write the formatted message (one line) to the console as the specified type.
# @param messageType The type of message
# @param message The message text
# @param args String format arguments 
# @Override
  def logMessage(self, messageType, message, args):
    self.write_line(messageType, message, args)

# Write the formatted message to the console as a generic message. 
# @param message The message text
# @param args String format arguments
  def write(self, message, args):
    self.write_to_console(MessageType.INFORMATION, False, message, args)

# Write the formatted message to the console as the given message type.
# @param type The type of message
# @param message The message text
# @param args Message string format arguments
  def write(self, type, message, args):
    self.write_to_console(type, False, message, args)

# Write the formatted message followed by a line break to the console as a generic message.
# @param message The message text
# @param args String format arguments
  def write_line(self, message, args):
    self.write_to_console(MessageType.INFORMATION, True, message, args);

# Write the formatted message followed by a line break to the console as the given message type.
# @param type The type of message
# @param message The message text
# @param args Message string format arguments
  def write_line(self, type, message, args):
    self.write_to_console(type, True, message, args);

# write the message to the console.
# @param type The type of message
# @param line Is this a write-line command, else it is just a write
# @param message The log message
# @param args Message string format arguments
  def write_to_console(self, type, line, message, args):
    # Just return if there is no message
    if message == None or message == "" or self.should_message_be_logged(type) == True:
      return;

    result = StringProcessor.safeFormatter(message, args);
    try:
      # If this a write-line command
      if (line):
        print(result);
      else:
        print(result);
    except Exception as e:
        print(StringProcessor.safeFormatter("Failed to write to the console because: " + e.args))