from Framework.utilities.logger import MessageType

class Logger():
    
    # Default date format.
    DEFAULT_DATE_FORMAT = "yyyy-MM-dd HH:mm:ss"

    # Log Level value area.
    logLevel = MessageType.INFORMATION

    # Log Level value save area.
    logLevelSaved = MessageType.SUSPENDED
        
# Set the logging level.
# @param level The logging level.
    def set_logging_level(self, level):
        self.logLevel = level

# Suspends logging.
    def suspend_logging(self):
        if (self.logLevel != MessageType.SUSPENDED):
            self.logLevelSaved = self.logLevel
            self.logLevel = MessageType.SUSPENDED
            log_message(MessageType.VERBOSE, "Suspending Logging..")

# Continue logging after it was suspended.
    def continue_logging(self):
    # Check if the logging was suspended
        if (self.logLevelSaved != MessageType.SUSPENDED):
            # Return to the log level at the suspension of logging
            logLevel = self.logLevelSaved;

        logLevelSaved = MessageType.SUSPENDED;
        log_message(MessageType.VERBOSE, "Logging Continued..")
        
    def log_message(self, messageType, message):
        raise NotImplementedError
        
# Write the formatted message (one line) to the console as a generic message. 
# @param messageType The type of message
# @param message The message text
# @param args String format arguments          
    def log_message(self, messageType, message, args):
        raise NotImplementedError

# Write the formatted message (one line) to the console as a generic message.
# @param message The message text
# @param args String format arguments
    def log_message(self, messageType, message, args):
        raise NotImplementedError 

# Determine if the message should be logged.
# The message should be logged if it's level is greater than or equal to the current logging level.
# @param messageType The type of message being logged.
# @return True if the message should be logged.
    def should_message_be_logged(self, messageType):
        # The message should be logged if it's level is less than or equal to the current logging level
        return messageType.getValue() <= logLevel.getValue();