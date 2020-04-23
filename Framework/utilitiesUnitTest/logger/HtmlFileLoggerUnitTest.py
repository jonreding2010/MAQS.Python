import unittest
from Framework.utilities.logger import HtmlFileLogger, LoggingConfig
from Framework.utilities.logger.constants import MessageType
from Framework.utilities.helper import StringProcessor
from Framework.base import SoftAssert
import os
import shutil

class HtmlFileLoggerUnitTest(unittest.TestCase):
# Test logging to a new file.
# @Test
    def HtmlFileLoggerNoAppendTest(self):
        logger = HtmlFileLogger(False, "", "WriteToHtmlFileLogger")
        logger.logMessage(MessageType.WARNING, "Hello, this is a test.")
        file = logger.getFilePath()
        file.delete()

# Test logging to an existing file.
  # @Test
    def HtmlFileLoggerAppendFileTest(self):
        logger = HtmlFileLogger(True, "", "WriteToExistingHtmlFileLogger")
        logger.logMessage(MessageType.WARNING, "This is a test to write to an existing file.")
        logger.logMessage(MessageType.WARNING, "This is a test to append to current file.")
        
        file = logger.getFilePath()
        file.delete()

# Test Writing to the Html File Logger
  # @Test
    def WriteToHtmlFileLogger(self):
        logger = HtmlFileLogger("", "WriteToHtmlFileLogger")
        logger.logMessage(MessageType.WARNING, "Hello, this is a test.")

        file = logger.getFilePath()
        file.delete()

# Test Writing to an Existing Html File Logger
  # @Test
    def WriteToExistingHtmlFileLogger(self):
        logger = HtmlFileLogger(True, "", "WriteToExistingHtmlFileLogger", MessageType.GENERIC)
        logger.logMessage(MessageType.WARNING, "This is a test.")
        logger.logMessage(MessageType.WARNING, "This is a test to write to an existing file.")

        file = logger.getFilePath()
        file.delete()

# Verify HtmlFileLogger constructor creates the correct directory if it does not already exist.
# Delete Directory after each run.
# @Test
    def HtmlFileLoggerConstructorCreateDirectory(self):
        logger = HtmlFileLogger(True, LoggingConfig.getLogDirectory(),
                "HtmlFileLoggerCreateDirectoryDelete").toString(), "HtmlFileLoggerCreateDirectory", MessageType.GENERIC
        logger.logMessage(MessageType.WARNING, "Test to ensure that the file in the created directory can be written to.")

        file = logger.getFilePath()
        self.assertTrue(self.readTextFile(logger.getFilePath()).contains(
                "Test to ensure that the file in the created directory can be written to."));
        file.delete();

        file = logger.getDirectory()
        try:
            os.rename(file)
        except OSError as e:
            e.with_traceback

# Verify that HtmlFileLogger can log message without defining a Message Type
   #@Test
    def HtmlFileLoggerLogMessage(self):
        logger = HtmlFileLogger(True, "", "HtmlFileLoggerLogMessage")
        logger.logMessage("Test to ensure LogMessage works as expected.")
        htmlText = self.readTextFile(logger.getFilePath())


        file = logger.getFilePath()
        file.delete()

        self.assertTrue(htmlText.contains("Test to ensure LogMessage works as expected."),
                "Expected Log Message to be contained in log.")

# Verify that HTML File Logger can log message and defining a Message Type.
#   @Test
    def HtmlFileLoggerLogMessageSelectType(self):
        logger = HtmlFileLogger(True, "", "HtmlFileLoggerLogMessageType")
        logger.logMessage(MessageType.GENERIC, "Test to ensure LogMessage works as expected.")
        htmlText = self.readTextFile(logger.getFilePath())

        file = logger.getFilePath()
        file.delete()

        self.assertTrue(htmlText.contains("Test to ensure LogMessage works as expected."),
                "Expected Log Message to be contained in log.")

# Verify that File Path field can be accessed and updated
  # @Test
    def HtmlFileLoggerSetFilePath(self):
        logger = HtmlFileLogger(True, "", "HtmlFileLoggerSetFilePath", MessageType.GENERIC)
        logger.setFilePath("test file path")
        filePath = logger.getFilePath()

        file = logger.getFilePath()
        file.delete();
        self.assertEquals(filePath, "test file path", "Expected 'test file path' as file path")

# Verify that HTML File Logger catches and handles errors caused by incorrect file Paths
   # @Test
    def HtmlFileLoggerCatchThrownException(self):
        logger = HtmlFileLogger(True, "", "HtmlFileLoggerCatchThrownException",
            MessageType.GENERIC)
        logger.setFilePath("<>")

        logger.logMessage(MessageType.GENERIC, "Test throws error as expected.")
        file = logger.getFilePath()
        file.delete()

# Verify that HTML File Logger catches and handles errors caused by incorrect file Paths.
  # @Test(expectedExceptions = IllegalArgumentException.class)
  # TODO: fail test with exceptions
    def FileLoggerEmptyFileNameException(self):
        logger = HtmlFileLogger("")
  
# Verify File Logger with No Parameters assigns the correct default values.
   # @Test
    def FileLoggerNoParameters(self):
        logger = HtmlFileLogger();

        softAssert = SoftAssert()
        softAssert.assertEquals(LoggingConfig.getLogDirectory(), logger.getDirectory(), StringProcessor.safeFormatter(
                "Expected Directory '%s'.", System.getProperty("java.io.tmpdir")))
        softAssert.assertEquals("FileLog.html", logger.getFileName(), "Expected correct File Name.")
        softAssert.assertEquals(MessageType.INFORMATION, logger.getMessageType(), "Expected Information Message Type.")

        softAssert.assertAll()

        file = logger.getFilePath()
        file.delete()

# Verify File Logger with only append parameter assigns the correct default values.
   # @Test
    def FileLoggerAppendOnly(self):
        logger = HtmlFileLogger(True)

        softAssert = SoftAssert()
        softAssert.assertEquals(System.getProperty("java.io.tmpdir"), logger.getDirectory(), StringProcessor.safeFormatter(
                "Expected Directory '%s'.", System.getProperty("java.io.tmpdir")));
        softAssert.assertEquals("FileLog.html", logger.getFileName(), "Expected correct File Name.");
        softAssert.assertEquals(MessageType.INFORMATION, logger.getMessageType(), "Expected Information Message Type.");

        softAssert.assertAll();

        file = logger.getFilePath()
        file.delete();

# Verify File Logger with only File Name parameter assigns the correct default values.
## Verify default extension is added '.html'
 # @Test
    def FileLoggerNameOnlyAddExtension(self):
        logger = HtmlFileLogger("FileNameOnly");

        softAssert = SoftAssert()
        softAssert.assertEquals(System.getProperty("java.io.tmpdir"), logger.getDirectory(), StringProcessor.safeFormatter(
                "Expected Directory '%s'.", System.getProperty("java.io.tmpdir")));
        softAssert.assertEquals("FileNameOnly.html", logger.getFileName(), "Expected correct File Name.");
        softAssert.assertEquals(MessageType.INFORMATION, logger.getMessageType(), "Expected Information Message Type.");

        softAssert.assertAll();

        file = logger.getFilePath()
        file.delete();

# Verify File Logger with only Message Type parameter assigns the correct default values.
   # @Test
    def FileLoggerMessageTypeOnly(self):
        logger = HtmlFileLogger(MessageType.WARNING)

        softAssert = SoftAssert()
        softAssert.assertEquals(System.getProperty("java.io.tmpdir"), logger.getDirectory(), StringProcessor.safeFormatter(
                "Expected Directory '%s'.", System.getProperty("java.io.tmpdir")))
        softAssert.assertEquals("FileLog.html", logger.getFileName(), "Expected correct File Name.")
        softAssert.assertEquals(MessageType.WARNING, logger.getMessageType(), "Expected Warning Message Type.")

        softAssert.assertAll()
        
        file = logger.getFilePath()
        file.delete()

# Verify File Logger with only Append and File Name parameters assigns the correct default values.
   # @Test
    def FileLoggerAppendFileName(self):
        logger = HtmlFileLogger(True, "AppendFileName")

        softAssert = SoftAssert()
        softAssert.assertEquals(System.getProperty("java.io.tmpdir"), logger.getDirectory(), StringProcessor.safeFormatter(
                "Expected Directory '%s'.", System.getProperty("java.io.tmpdir")))
        softAssert.assertEquals("AppendFileName.html", logger.getFileName(), "Expected correct File Name.")
        softAssert.assertEquals(MessageType.INFORMATION, logger.getMessageType(), "Expected Information Message Type.")

        softAssert.assertAll()

        file = logger.getFilePath()
        file.delete()

# Verify File Logger with only Log Folder and Append parameters assigns the correct default values.
  # @Test
    def FileLoggerAppendLogFolder(self):
        append_file_directory_path = LoggingConfig.getLogDirectory() + "/" + "Append File Directory"
        logger = HtmlFileLogger(append_file_directory_path, True)

        softAssert = SoftAssert()
        softAssert.assertEquals(append_file_directory_path, logger.getDirectory(),
            "Expected Directory 'Append File Directory'.")
        softAssert.assertEquals("FileLog.html", logger.getFileName(), "Expected correct File Name.")
        softAssert.assertEquals(MessageType.INFORMATION, logger.getMessageType(),
            "Expected Information Message Type.")
        softAssert.assertAll()

# Verify File Logger with only Log Folder and File Name parameters assigns the correct default values.
  # @Test
    def FileLoggerLogFolderFileName(self):
        log_folder_file_name_directory = LoggingConfig.getLogDirectory() + "/" + "Log Folder File Name Directory"
        logger = HtmlFileLogger(log_folder_file_name_directory,"LogFolderFileName.html")

        softAssert = SoftAssert()
        softAssert.assertEquals(log_folder_file_name_directory, logger.getDirectory(),
            "Expected Directory 'Log Folder File Name Directory'.");
        softAssert.assertEquals("LogFolderFileName.html", logger.getFileName(),
            "Expected correct File Name.");
        softAssert.assertEquals(MessageType.INFORMATION, logger.getMessageType(),
            "Expected Information Message Type.");
        softAssert.assertAll();

 # Verify File Logger with only Log Folder and Messaging Level parameters assigns the correct default values.
  # @Test
    def FileLoggerLogFolderMessagingLevel(self):
        log_folder_messaging_level_directory_path = LoggingConfig.getLogDirectory() + "/" + "Log Folder Messaging Level Directory"
        logger = HtmlFileLogger(log_folder_messaging_level_directory_path, MessageType.WARNING)

        softAssert = SoftAssert()
        softAssert.assertEquals(log_folder_messaging_level_directory_path, logger.getDirectory(),
            "Expected Directory 'Log Folder Messaging Level Directory'.")
        softAssert.assertEquals("FileLog.html", logger.getFileName(), "Expected correct File Name.")
        softAssert.assertEquals(MessageType.WARNING, logger.getMessageType(),
            "Expected Warning Message Type.")
        softAssert.assertAll()

# Verify File Logger with only Append and Messaging Level parameters assigns the correct default values.
   # @Test
    def FileLoggerAppendMessagingLevel(self):
        logger = HtmlFileLogger(True, MessageType.WARNING)

        softAssert = SoftAssert()
        softAssert.assertEquals(System.getProperty("java.io.tmpdir"), logger.getDirectory(), StringProcessor.safeFormatter(
                "Expected Directory '%s'.", System.getProperty("java.io.tmpdir")))
        softAssert.assertEquals("FileLog.html", logger.getFileName(), "Expected correct File Name.")
        softAssert.assertEquals(MessageType.WARNING, logger.getMessageType(), "Expected Warning Message Type.")

        softAssert.assertAll();

        file = logger.getFilePath()
        file.delete()

# Verify File Logger with only Messaging Level and file name parameters assigns the correct default values.
   # @Test
    def FileLoggerMessagingLevelFileName(self):
        logger = HtmlFileLogger(MessageType.WARNING, "MessagingTypeFile.html")

        softAssert = SoftAssert()
        softAssert.assertEquals(System.getProperty("java.io.tmpdir"), logger.getDirectory(), StringProcessor.safeFormatter(
                "Expected Directory '%s'.", System.getProperty("java.io.tmpdir")));
        softAssert.assertEquals("MessagingTypeFile.html", logger.getFileName(), "Expected correct File Name.")
        softAssert.assertEquals(MessageType.WARNING, logger.getMessageType(), "Expected Warning Message Type.")

        softAssert.assertAll()

        file = logger.getFilePath()
        file.delete();
        
# Verify File Logger with only Append, log folder and file name parameters assigns the correct default values.
  # @Test
    def FileLoggerAppendLogFolderFileName(self):
        appendLogFolderFileNameDirectoryPath = LoggingConfig.getLogDirectory() + "/" + "AppendLogFolderFileNameDirectory";
        logger = HtmlFileLogger(True, appendLogFolderFileNameDirectoryPath,
            "AppendLogFolderFileName.html");

        softAssert = SoftAssert()
        softAssert.assertEquals(appendLogFolderFileNameDirectoryPath, logger.getDirectory(),
            " Expected Directory AppendLogFolderFileNameDirectory");
        softAssert.assertEquals("AppendLogFolderFileName.html", logger.getFileName(), "Expected correct File Name.");
        softAssert.assertEquals(MessageType.INFORMATION, logger.getMessageType(), "Expected Information Message Type.");
        softAssert.assertAll();

# Verify File Logger with only Append, log folder and Messaging Level parameters assigns the correct default values.
   #@Test
    def FileLoggerAppendLogFolderMessagingLevel(self):
        appendLogFolderFileNameDirectory = LoggingConfig.getLogDirectory() + "/" + "AppendLogFolderFileNameDirectory";
        logger = HtmlFileLogger(True, appendLogFolderFileNameDirectory, MessageType.WARNING);

        softAssert = SoftAssert();
        softAssert.assertEquals(appendLogFolderFileNameDirectory, logger.getDirectory(),
            " Expected Directory AppendLogFolderFileNameDirectory");
        softAssert.assertEquals("FileLog.html", logger.getFileName(), "Expected correct File Name.");
        softAssert.assertEquals(MessageType.WARNING, logger.getMessageType(), "Expected Warning Message Type.");

        softAssert.assertAll();

        file = logger.getFilePath()
        file.delete();

# Verify File Logger with only File Name, Append and Messaging Level parameters assigns the correct default values.
   # @Test
    def FileLoggerFileNameAppendMessagingLevel(self):
        logger = HtmlFileLogger("FileNameAppendMessagingLevel.html", True, MessageType.WARNING)

        softAssert = SoftAssert()
        softAssert.assertEquals(System.getProperty("java.io.tmpdir"), logger.getDirectory(), StringProcessor.safeFormatter(
                "Expected Directory '%s'.", System.getProperty("java.io.tmpdir")));
        softAssert.assertEquals("FileNameAppendMessagingLevel.html", logger.getFileName(),
                "Expected correct File Name.");
        softAssert.assertEquals(MessageType.WARNING, logger.getMessageType(), "Expected Warning Message Type.");
        softAssert.assertAll();

        file = logger.getFilePath()
        file.delete();

# Verify File Logger with only Log Folder, File Name and Messaging Level parameters assigns the correct default values.
   # @Test
    def FileLoggerLogFolderFileNameMessagingLevel(self):
        logFolderFileNameMessagingLevelDirectoryPath = LoggingConfig.getLogDirectory() + "/" + "LogFolderFileNameMessagingLevelDirectory";
        logger = HtmlFileLogger(logFolderFileNameMessagingLevelDirectoryPath,
            "LogFolderFileNameMessagingLevel.html", MessageType.WARNING);

        softAssert = SoftAssert()
        softAssert.assert_equals(logFolderFileNameMessagingLevelDirectoryPath, logger.getDirectory(),
            "Expected Directory 'LogFolderFileNameMessagingLevelDirectory'")
        softAssert.assert_equals("LogFolderFileNameMessagingLevel.html", logger.getFileName(),
            "Expected correct File Name.")
        softAssert.assert_equals(MessageType.WARNING, logger.getMessageType(),
            "Expected Warning Message Type.")

        softAssert.assert_all()

        file = logger.getFilePath()
        file.delete();

# Verify that HTML File Logger catches and handles errors caused by empty file name.
    # @Test(expectedExceptions = IllegalArgumentException.class)
  # TODO: fail test by catching exception
    def HtmlFileLoggerEmptyFileNameException(self):
     logger = HtmlFileLogger("")

# Read a file and return it as a string
# @param filePath The file path to read
#  @return The contents of the file
    def readTextFile(self, filePath):
        text = ""
        try:
            text = open(filePath).read()
        except Exception as e:
            e.printStackTrace();
        return text;