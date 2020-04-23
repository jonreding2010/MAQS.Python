from Framework.utilities.logger import ConsoleLogger as ConsoleLogger
from Framework.utilities.logger import MessageType as MessageType
from Framework.utilities.helper import StringProcessor as StringProcessor
from os import path
from pathlib import Path
import os
import pathlib
from ctypes import FormatError
from test.support import Error

class FileLogger(Logger):
    
    # The default log file save location.
    DEFAULTLOGFOLDER = Path.gettempdir()
    # Initializes a new instance of the FileLogger class.
    DEFAULTLOGNAME = "FileLog.txt"
    # Creates a private string for the name of the file.
    fileName = ""
    # Create a private string for the path of the file.
    filePath = ""       
    # Creates a private Message Type.
    messageType = None
    # Creates a private string for the directory of the folder.
    directory = ""
        
# Initializes a new instance of the FileLogger class.
    def file_logger(self):
       self(False, "", DEFAULTLOGNAME, MessageType.INFORMATION)

# Initializes a new instance of the FileLogger class.
# @param append       True to append to an existing log file or false to overwrite it.
#                    If the file does not exist this, flag will have no affect.
# @param logFolder    Where log files should be saved
# @param name         File Name
# @param messageLevel Messaging Level
    def file_logger(self, append, logFolder, name, messageLevel):
        super(messageLevel);

        if (logFolder == None or logFolder == ""):
            directory = DEFAULTLOGFOLDER;
        else:
            directory = logFolder;       
        if not os.path.exists(directory):
            pathlib.Path(directory).mkdir(parents=True, exist_ok=True)

        newName = make_valid_file_name(name);

        # if (!name.toLowerCase().endsWith(this.getExtension())):
        if (not name.lower().endswith(get_extension())):
            name += get_extension()

        fileName = name;
        filePath = Path.get(directory, name).normalize().toString();
        messageType = messageLevel;
        
        if (path.exists(filePath) and not append):
            try:
                writer = [filePath, False]
                writer.write("")
                writer.flush()
            except Exception as e:
                # Failed to write to the event log, write error to the console instead
                console = ConsoleLogger()
                console.log_message(MessageType.ERROR, StringProcessor.safeFormatter("Failed to write to event log because: " + e.args))

# Gets the FilePath value.
# @return returns the file path
    def get_file_path(self):
        return filePath

# Gets the Message Type value.
# @return The Message Type.
    def get_message_type(self):
        return messageType

# Gets the Directory Path.
# @return Returns the Directory
    def get_directory(self):
        return directory

# Sets the FilePath value.
# @param path sets the file path
    def set_file_path(self, path):
        this.filePath = path

# Gets the File Name value.
# @return Returns the File Name.
    def get_file_name(self):
        return fileName

# Gets the file extension.
# @return File Extension
    def get_extension(self):
        return ".txt"

# @see com.magenic.jmaqs.utilities.Logging.Logger#logMessage(java.lang.String,
# java.lang.Object[])
#  @Override
    def log_message(self, message, args):
        log_message(MessageType.INFORMATION, message, args);

# @see com.magenic.jmaqs.utilities.Logging.Logger#logMessage(com.magenic.jmaqs.utilities.
# Logging.MessageType, java.lang.String, java.lang.Object[])
        # @Override
    def log_message(self, messageType, message, args):
        # If the message level is greater that the current log level then do not log it.
        if (self.should_message_be_logged(messageType)):
            try:
                '''
                 (FileWriter fw = new FileWriter(this.filePath, true);
                BufferedWriter bw = new BufferedWriter(fw);
                PrintWriter writer = new PrintWriter(bw)) 
                writer.println(
                StringProcessor.safeFormatter("%s%s", Config.NEW_LINE, System.currentTimeMillis()));
                writer.print(StringProcessor.safeFormatter("%s:\t", messageType.toString()));

                writer.println(StringProcessor.safeFormatter(message, args));
                writer.flush();
                '''
            except Error as e:
                # Failed to write to the event log, write error to the console instead
                console = ConsoleLogger()
                console.logMessage(MessageType.ERROR,
                StringProcessor.safeFormatter("Failed to write to event log because: " + e.args))
                console.logMessage(messageType, message, args)
  


# Take a name sting and make it a valid file name.
# @param name The string to cleanup
# @return returns the string of a valid filename
    @staticmethod
    def make_valid_file_name(name):
        if name == None or name == "":
            raise FormatError("Blank or null file name was provided")

        # Replace invalid characters
        replacedName = name
        try:
            replacedName = name.replaceAll("[^a-zA-Z0-9\\._\\- ]+", "~")
        except Error as e:
            console = ConsoleLogger()
            console.logMessage(MessageType.ERROR, StringProcessor.safeFormatter("Failed to Replace Invalid Characters because: " + e.args))
        return replacedName

# Get the message for an unknown message type.
# @param type The Message Type.
# @return The Unknown Message Type Message.
    def unknown_message_type_message(self, type):
        return StringProcessor.safeFormatter("Unknown MessageType: %s%s%s%s", type.name(), os.linesep,
            "Message will be displayed with the MessageType of: ", MessageType.GENERIC.name())