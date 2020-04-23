
from Framework.utilities.helper import Config, StringProcessor
from Framework.utilities.logger import ConsoleLogger, FileLogger, LoggingEnabled, MessageType
import os

class LoggingConfig:

# Get our logging state - Yes, no or on failure.
# @return The log enabled state
  def get_logging_enabled_setting(self):
    enabledSetting = Config.getGeneralValue("Log", "NO").toUpperCase()
    
    if enabledSetting == "YES":
        return LoggingEnabled.YES
    elif enabledSetting == "ONFAIL":
        return LoggingEnabled.ONFAIL
    elif enabledSetting == "NO":
        return LoggingEnabled.NO
    else:
        raise ValueError(StringProcessor.safeFormatter("Log value %s is not a valid option", Config.get_general_value("Log", "NO")))

# Get our logging level.
# @return MessageType - The current log level.
  def get_logging_level_setting(self):
    loggingLevel = Config.getGeneralValue("LogLevel", "INFORMATION").toUpperCase()
        
    if loggingLevel == "VERBOSE":
         # Includes this and all of those below
        return MessageType.VERBOSE
    elif loggingLevel == "INFORMATION":
        # Includes this and all of those below
        return MessageType.INFORMATION
    elif loggingLevel == "GENERIC":
        # Includes this and all of those below
        return MessageType.GENERIC
    elif loggingLevel ==  "SUCCESS":
        # Includes this and all of those below
        return MessageType.SUCCESS
    elif loggingLevel == "WARNING":
        # Includes this and all of those below
        return MessageType.WARNING
    elif loggingLevel == "ERROR":
        # Includes errors only
        return MessageType.ERROR
    elif loggingLevel ==  "SUSPENDED":
        # All logging is suspended
        return MessageType.SUSPENDED     
    else:
        raise ValueError(StringProcessor.safeFormatter("Logging level value '{0}' is not a valid option", Config.getGeneralValue("LogLevel")));

# Get the logger.
# @param fileName File name to use for the log
# @return The logger
  def get_logger(self, fileName):
    # Disable logging means we just send any logged messages to the console
    if (get_logging_enabled_setting() == LoggingEnabled.NO):
      return ConsoleLogger();

    logDirectory = get_log_directory()
    loggingLevel = get_logging_level_setting()
    logType = Config.getGeneralValue("LogType", "CONSOLE").toUpperCase()
    
    if logType == "CONSOLE":
        return ConsoleLogger(loggingLevel);
    elif logType == "TXT":
        return FileLogger(False, logDirectory, fileName, loggingLevel);
    else:
         raise ValueError(StringProcessor.safeFormatter("Log type %s is not a valid option", Config.get_general_value("LogType", "CONSOLE")));

# Gets the File Directory to store log files.
# @return String of file path
  def get_log_directory(self):
    path = os.path.abspath("").concat("\\Logs")
    return Config.get_general_value("FileLoggerPath", path)