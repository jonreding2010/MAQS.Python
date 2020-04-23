import unittest
from Framework.utilities.logger import ConsoleLogger
from Framework.utilities.logger.constants import MessageType

class ConsoleLoggerUnitTest(unittest.TestCase):
# Log message to a new console logger
  #@Test
    def consoleLoggerLogMessage(self):
        console = ConsoleLogger()
        console.logMessage("Test String %s %s", "args1", "args2")

# Log message to a new console logger using defined message type
  # @Test
    def consoleLoggerLogMessageSelectType(self):
        console = ConsoleLogger()
        console.logMessage(MessageType.GENERIC, "Test String %s", "args1")

# Write message to new console logger
  # @Test
    def consoleLoggerWriteMessage(self):
        console = ConsoleLogger()
        console.write("Test String %s %s", "args1", "args2")

# Write message to new console logger using defined message type
  # @Test
    def consoleLoggerWriteMessageSelectType(self):
        console = ConsoleLogger()
        console.write(MessageType.GENERIC, "TestString %s", "args1")

# Write message with new line to new console logger
    # @Test
    def consoleLoggerWriteLineMessage(self):
        console = ConsoleLogger()
        console.write("Test String %s %s", "args1", "args2")

# Write message with new line to new console logger using defined message type
    # @Test
    def consoleLoggerWriteMessageLineSelectType(self):
        console = ConsoleLogger()
        console.write(MessageType.GENERIC, "TestString %s", "args1")
    