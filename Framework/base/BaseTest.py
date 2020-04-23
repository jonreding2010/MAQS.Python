
from Framework.utilities.logger.constants import LoggingEnabled, MessageType, TestResultType
from Framework.utilities.logger import ConsoleLogger, FileLogger, LoggingConfig, Logger
from Framework.utilities.helper import StringProcessor
from Framework.base import BaseTestObject
from unittest import TestResult
import os
import traceback
import datetime

class BaseTest():

# All logged exceptions caught and saved to be thrown later.
  loggedExceptions = []

# Logging Enabled Setting from Config file.
  loggingEnabledSetting = []

# The test result object.
  testResult = []

# The Collection of Base Test Objects to use.
  baseTestObjects = None

# The Performance Timer Collection.
  perfTimerCollection = []
    
# The TestNG Test Context.
  testContextInstance = ""

# The Fully Qualified Test Class Name.
  fullyQualifiedTestClassName = ""

# Gets the Performance Timer Collection.
# @return Performance Timer Collection
  def get_perf_timer_collection(self):
      return perfTimerCollection

# Sets the Performance Timer Collection.
# @param perfTimerCollection Performance Timer Collection to use
  def set_perf_timer_collection(self, perfTimerCollection):
    perfTimerCollection = perfTimerCollection

# Gets the Logger for this test.
# @return Logger object
  def get_logger(self):
    return self.get_test_object().getLog()

# Set the Logger for this test.
# @param log The Logger object
  def set_logger(self, log):
    self.get_test_object().setLog(log)

# Gets the Logging Enabled setting.
# @return Logging Enabled setting
  def get_logging_enabled_setting(self):
    return loggingEnabledSetting

# Set the Logging Enabled setting.
# @param setting The LoggingEnabled enum
  def set_Logging_Enabled(self, setting):
    loggingEnabledSetting = setting

# Get logged exceptions for this test.
# @return ArrayList of logged exceptions for this test
  def get_logged_exceptions(self):
    result = []
    if loggedExceptions.containsKey(fullyQualifiedTestClassName):
      result = loggedExceptions.get(fullyQualifiedTestClassName);
    return result

# Set Logged Exception List - Add/Update entry in Hash Map with test class name as key.
# param loggedExceptionList ArrayList of logged exceptions to use.
  def set_logged_exceptions(self, loggedExceptionList):
    loggedExceptions.append(fullyQualifiedTestClassName, loggedExceptionList)

# Gets the Driver Store.
# @return The Driver Store
  def get_manager_store(self):
    return self.get_test_object().get_manager_store()

# Gets the TestNG Test Context.
# @return The TestNG Test Context
  def get_test_context(self):
    return testContextInstance

# Sets the TestNG Test context.
# @param testContext The TestNG Test Context to use
  def set_test_context(self, testContext):
    testContextInstance = testContext

# Get the BaseTestObject for this test.
# @return The BaseTestObject
  def get_test_object(self):
    if self.fullyQualifiedTestName in BaseTestObject:
    # if (!baseTestObjects.containsKey(fullyQualifiedTestClassName.get())):
      self.create_new_test_object()
    return baseTestObjects.get(self.fullyQualifiedTestClassName.get())

# Sets the Test Object.
# @param baseTestObject The Base Test Object to use
  def set_test_object(self, baseTestObject):
    key = fullyQualifiedTestClassName
    if (baseTestObjects.containsKey(key)):
      baseTestObjects.replace(key, baseTestObject)
    else:
      baseTestObjects.put(key, baseTestObject)

# Setup before a test.
# @param method The initial executing Method object
# @param testContext The initial executing Test Context object
  ## @BeforeMethod(alwaysRun = true)
  def set_up(self, method, testContext):
    this.testContextInstance = testContext;

    # Get the Fully Qualified Test Class Name and set it in the object
    testName = method.getDeclaringClass() + "." + method.getName()
    testName = testName.replaceFirst("class ", "")
    fullyQualifiedTestClassName = testName
    self.create_new_test_object()

# Cleanup after a test.
  ## @AfterMethod(alwaysRun = true)
  def tear_down(self):
    try:
      self.before_logging_teardown(testResult);
    except Exception as e:
      self.try_to_log(MessageType.WARNING, "Failed before logging teardown because: %s", e.getMessage())

    # Log the test result
    if testResult.getStatus() == "SUCCESS":
      tryToLog(MessageType.SUCCESS, "Test Passed")
    elif testResult.getStatus() == "FAILURE":
      tryToLog(MessageType.ERROR, "Test Failed")
    elif testResult.getStatus() == "SKIP":
      tryToLog(MessageType.INFORMATION, "Test was skipped");
    else:
      tryToLog(MessageType.WARNING, "Test had an unexpected result.")

  # Cleanup log files we don't want
    try:
        if self.Log is FileLogger and testResult == TestResultType.PASS and self.LoggingEnabledSetting == LoggingEnabled.ONFAIL:
          os.remove(FileLogger.Log.getFilePath)
    except Exception as e:
      tryToLog(MessageType.WARNING, "Failed to cleanup log files because: %s", e.getMessage())

    # Get the Fully Qualified Test Name
    fullyQualifiedTestName = fullyQualifiedTestClassName

    try:
      baseTestObject = get_test_object()
      # Release logged messages
      loggedExceptions.remove(fullyQualifiedTestName)

      # Release the Base Test Object
      baseTestObjects.remove(fullyQualifiedTestName, baseTestObject)

    # Create console logger to log subsequent messages
    self.set_test_object(BaseTestObject(ConsoleLogger(), fullyQualifiedTestName))
    fullyQualifiedTestClassName.remove()

# Set the test result after each test execution.
# @param testResult The result object
  ##@AfterMethod(alwaysRun = true)
  def set_test_result(self, testResult):
    this.testContextInstance = testResult.getTestContext()
    this.testResult = testResult

# Steps to do before logging teardown results.
# @param resultType The test result
  def before_Logging_Teardown(self, resultType):
        NotImplementedError

# Setup logging data.
# @return Logger
  def create_Logger(self):
    loggingEnabledSetting = LoggingConfig.get_LoggingEnabled_Setting();
    self.set_Logged_Exceptions([])

    if (loggingEnabledSetting != LoggingEnabled.NO):
      return LoggingConfig.getLogger(StringProcessor
          .safeFormatter("%s - %s", fullyQualifiedTestClassName.get(),
              datetime.utcnow().strftime("uuuu-MM-dd-HH-mm-ss-SSSS")))
    else:
      return ConsoleLogger()

# Get the type of test result.
# @return The type of test result
  def getResultType(self):
    result = testResult.getStatus()
      
    if result == TestResult.Success:
      return TestResultType.PASS
    elif result == TestResult.FAILURE:
      return TestResultType.FAIL
    elif result == TestResult.SKIP:
      return TestResultType.SKIP;
    else:
      return TestResultType.OTHER

# Get the test result type as text.
# @return The test result type as text
  def getResultText(self):
    result = testResult.getStatus()
  
    if result == TestResult.SUCCESS:
        return "SUCCESS"
    elif result == TestResult.FAILURE:
        return "FAILURE"
    elif result == TestResult.SKIP:
        return "SKIP"
    else:
        return "OTHER"

# Get the fully qualified test name.
# @return The test name including class
  def getFullyQualifiedTestClassName(self):
    return fullyQualifiedTestClassName

# Try to log a message - Do not fail if the message is not logged.
# @param messageType The type of message
# @param message     The message text
# @param args        String format arguments
  def tryToLog(self, messageType, message, args):
    # Get the formatted message
    formattedMessage = StringProcessor.safeFormatter(message, args)

    try:
    # Write to the log
      get_logger().logMessage(messageType, formattedMessage)

      # If this was an error and written to a file, add it to the console output as well
      if messageType == MessageType.ERROR and not isinstance(get_logger(), ConsoleLogger):
        print(formattedMessage)
    except Exception as e:
      print(formattedMessage);
      print("Logging failed because: " + e.getMessage())

# Log a verbose message and include the automation specific call stack data.
# @param message The message text
# @param args String format arguments
  def logVerbose(self, message, args):
    messages = []
    messages.append(StringProcessor.safeFormatter(message, args) + os.linesep)

    for element in traceback.format_stack():
      # If the stack trace element is from the com.magenic package (excluding this method) append the stack trace line 
      if (element.toString().startsWith("com.magenic") and not element.contains("BaseTest.logVerbose")):
        messages.append(element + os.linesep)
    get_logger().logMessage(MessageType.VERBOSE, messages)

# Create a Base test object.
  def create_new_test_object(self):
    newLogger = create_Logger()
    set_test_object(BaseTestObject(newLogger, fullyQualifiedTestClassName))