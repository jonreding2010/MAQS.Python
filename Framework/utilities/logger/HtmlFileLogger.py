from asyncio.streams import StreamWriter
import os
from Framework.utilities.logger import ConsoleLogger, Logger, FileLogger, MessageType
from datetime import datetime
from Framework.utilities.helper import StringProcessor

class HtmlFileLogger(FileLogger):
    
    # The default log name.
    DEFAULTLOGNAME = "FileLog.html"
    # Default header for the HTML file, this gives us our colored text.
    DEFAULTHTMLHEADER = "<!DOCTYPE html><html><header><title>Test Log</title></header><body>"
    # Gets the file extension
    extension = ".html"
    # Gets or sets the FilePath value
    filePath = ""
        
        
# Initializes a new instance of the HtmlFileLogger class
# @param logFolder Where log files should be saved
# @param name File Name
# @param messageLevel Messaging level
# @param append True to append to an existing log file or false to overwrite it - If the file does not exist this, flag will have no affect
    def __init__(self, logFolder, name = DEFAULTLOGNAME, messageLevel = MessageType.INFORMATION, append = false):
        writer = StreamWriter(filePath, True)
        writer.Write(DEFAULTHTMLHEADER);
        writer.Flush();
        writer.Close();



# Write the formatted message (one line) to the console as a generic message
# @param messageType The type of message
# @param message The message text
# @param args String format arguments
    def log_message(self, messageType, message, args):
        # If the message level is greater that the current log level then do not log it.
        if (Logger.should_message_be_logged(messageType)):
            # Log the message
            
        # lock (this.FileLock): 
            date = datetime.now().strftime(Logger.DEFAULTDATEFORMAT)
            #date = dateTime.now().UtcNow()ToString(Logger.DEFAULTDATEFORMAT, CultureInfo.InvariantCulture);

            writer = []

            try:
                #using (StreamWriter writer = new StreamWriter(this.FilePath, true)):
                 # Set the style
                writer.append(get_text_with_color_flag(messageType))

                # Add the content
                writer.WriteLine(StringProcessor.SafeFormatter("{0}{1}", os.linesep, date))
                writer.Write(StringProcessor.SafeFormatter("{0}:\t", messageType.ToString()))
                writer.WriteLine(StringProcessor.SafeFormatter(message, args))

                # Close off the style
                writer.Write("</p>");

                # Close the pre tag when logging Errors
                if (messageType == "ERROR"):
                    writer.Write("</pre>");
            except Exception as e:
                # Failed to write to the event log, write error to the console instead
                console = ConsoleLogger()
                console.LogMessage(MessageType.ERROR, StringProcessor.SafeFormatter("Failed to write to event log because: {0}", e.message));
                console.LogMessage(messageType, message, args);


# Dispose the class
    def dispose(self):
        dispose(True)
        #GC.SuppressFinalize(self)

# Dispose the class
# @param disposing True if you want to release managed resources
    def dispose(self, disposing):
        if (disposing and os.path.isfile(filePath)):
            writer = StreamWriter(filePath, True)
            writer.WriteLine("</body></html>");
            writer.Flush();
            writer.Close();

# Get the HTML style key for the given message type
# @param type The message type</param>
# @return string - The HTML style key for the given message type
    def get_text_with_color_flag(self, type):
        if type == MessageType.VERBOSE:
                return "<p style =\"color:purple\">"
        elif type == MessageType.ACTION:
                return "<p style =\"color:gold\">"
        elif type == MessageType.STEP:
                return "<p style =\"color:orange\">"
        elif type == MessageType.ERROR:
                return "<pre><p style=\"color:red\">"
        elif type == MessageType.GENERIC:
                return "<p style =\"color:black\">"
        elif type == MessageType.INFORMATION:
                return "<p style =\"color:blue\">"
        elif type == MessageType.SUCCESS:
                return "<p style=\"color:green\">"
        elif type == MessageType.WARNING:
                return "<p style=\"color:orange\">"
        else:
                print(FileLogger.unknown_message_type_message(type));
                return "<p style=\"color:hotpink\">"