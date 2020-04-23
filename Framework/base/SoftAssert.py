from Framework.utilities.logger import ConsoleLogger, Logger
from Framework.base import SoftAssertException
from Framework.utilities.helper import StringProcessor
import os
from Framework.utilities.logger.constants import MessageType

class SoftAssert():
# Initializes a new instance of the SoftAssert class.
# Setup the Logger
# @param logger Logger to be used
    def __init__(self, logger):
        self.Log = logger;

# Initializes a new instance of the <see cref="SoftAssert"/> class
    def __init__(self):
        self.Log = ConsoleLogger()
        
# List of all asserted exceptions 
    listOfExceptions = []
    
# Gets a value indicating whether the user checked for failures
    DidUserCheckForFailures = False

# Gets a count of total number of Asserts
    NumberOfAsserts = 0

# Gets a count of total number of Passed Asserts
    NumberOfPassedAsserts = 0
    
# Gets a count of total number of Failed Asserts
    NumberOfFailedAsserts = 0

# Gets the logger being used
    Log = None

# Gets a value indicating whether the user checked for failures
    DidUserCheckForFailures = False;

# Gets a count of total number of Asserts
    NumberOfAsserts

# Gets a count of total number of Passed Asserts
    NumberOfPassedAsserts

# Gets a count of total number of Failed Asserts
    NumberOfFailedAsserts

# Gets the logger being used
    ##protected Logger Log { get; private set; }
    Log
    
# Override the logger
# @param log The new logger
    def override_Logger(self, log):
        self.Log = log

# Gets a value indicating whether the boolean if the user checks for failures at the end of the test.
# @returns If the user checked for failures.  If the number of asserts is 0, it returns true.
    def did_user_check(self):
        if NumberOfAsserts > 0:
            return DidUserCheckForFailures;
        else:
            return True

# Check if there are any failed soft asserts.
# @returns>True if there are failed soft asserts
    def did_soft_asserts_fail(self):
        return NumberOfFailedAsserts > 0

# Asserts if two strings are equal
# @param expectedText Expected value of the string
# @param actualText Actual value of the string
# @param message Message to be used when logging</param>
# @returns Boolean if they are equal
    def are_equal(self, expectedText, actualText, message = ""):
        return are_equal(expectedText, actualText, "", message)

# Asserts if two strings are equal
# @param expectedText Expected value of the string
# @param actualText Actual value of the string
# @param softAssertName Soft assert name
# @param message Message to be used when logging
# @returns Boolean if they are equal
    def are_equal(self, expectedText, actualText, softAssertName, message = ""):
        #void test()
        if expectedText != actualText:
            if (message == "" or message == None):
                raise SoftAssertException(StringProcessor.SafeFormatter("SoftAssert.AreEqual failed for {0}.  Expected '{1}' but got '{2}'", softAssertName, expectedText, actualText))
            raise SoftAssertException(StringProcessor.SafeFormatter("SoftAssert.AreEqual failed for {0}.  Expected '{1}' but got '{2}'.  {3}", softAssertName, expectedText, actualText, message))
        return invoke_test(test, expectedText, actualText, message)

# Soft assert for IsTrue
# @param condition">Boolean condition
# @param softAssertName Soft assert name
# @param failureMessage Failure message
# @returns Boolean if condition is met
    def is_true(self, condition, softAssertName, failureMessage = ""):
        #void test()
        if not condition:
            if not failureMessage or failureMessage == "":
                raise SoftAssertException(StringProcessor.SafeFormatter("SoftAssert.IsTrue failed for: {0}", softAssertName))
            raise SoftAssertException(StringProcessor.SafeFormatter("SoftAssert.IsTrue failed for: {0}. {1}", softAssertName, failureMessage))
        return invoke_test(test, softAssertName, failureMessage)

# Soft assert for IsFalse
# @param condition Boolean condition
# @param softAssertName Soft assert name
# @param failureMessage Failure message
# @returns Boolean if condition is met
    def is_false(self, condition, softAssertName, failureMessage = ""):
        # void test()
        if condition:
            if not failureMessage or failureMessage == "":
                raise SoftAssertException(StringProcessor.SafeFormatter("SoftAssert.IsFalse failed for: {0}", softAssertName))
            raise SoftAssertException(StringProcessor.SafeFormatter("SoftAssert.IsFalse failed for: {0}. {1}", softAssertName, failureMessage))
        return invoke_test(test, softAssertName, failureMessage);

# Log final assert count summary
    def log_final_assert_data(self):
        message = []
        ##MessageType type

        message.AppendLine(StringProcessor.SafeFormatter(
            "Total number of Asserts: {0}. {3}Passed Asserts = {1} {3}Failed Asserts = {2}{3}",
        NumberOfAsserts, NumberOfPassedAsserts, NumberOfFailedAsserts, os.linesep))

        if listOfExceptions.Count > 0:
            type = MessageType.ERROR
            message.AppendLine("List of failed exceptions:")

            for exception in listOfExceptions:
                # Will log all the exceptions that were caught in Asserts to the log file.
                message.AppendLine(exception)

        else:
            # There are no exceptions that were caught in Asserts.
            type = MessageType.INFORMATION;
            message.AppendLine("There are no failed exceptions in the Asserts.")

        Log.LogMessage(type, message.ToString().TrimEnd())

# Fail test if there were one or more failures
    def fail_Test_if_assert_failed(self):
        fail_Test_if_assert_failed("*See log for more details")

# Fail test if there were one or more failures
# @param message Customer error message
    def fail_Test_if_assert_failed(self, message):
        log_final_assert_data()
        this.DidUserCheckForFailures = True

        if (did_soft_asserts_fail()):
            errors = ''.Join(os.linesep, listOfExceptions)
            raise Exception("Soft Asserts failed:" + os.linesep + errors + os.linesep + message)

# Wrap an assert inside a soft assert
# @param assertFunction The assert function
# @returns True if the asset passed
    def Assert(self, assertFunction):
        # Resetting every time we invoke a test to verify the user checked for failures
        DidUserCheckForFailures = False
        result = False

        try:
            assertFunction.Invoke()
            this.NumberOfPassedAsserts = ++NumberOfPassedAsserts
            result = True
            Log.LogMessage(MessageType.SUCCESS, "SoftAssert passed for: {0}.", assertFunction.Method.Name)
        except Exception as ex:
            this.NumberOfFailedAsserts = ++NumberOfFailedAsserts
            result = False
            Log.LogMessage(MessageType.WARNING, "SoftAssert failed for: {0}. {1}", assertFunction.Method.Name, ex.Message)
            listOfExceptions.Add(ex.Message)
        finally:
            this.NumberOfAsserts = ++NumberOfAsserts
        return result

# Wrap an assert that is expected to fail and the expected failure 
# @param assertFunction The assert function
# @param expectedException The type of expected exception
# @param assertName soft assert name
# @param failureMessage Failure message
# @returns True if the assert failed
    def assert_fails(self, assertFunction, expectedException, assertName, failureMessage = ""):
        # Resetting every time we invoke a test to verify the user checked for failures
        this.DidUserCheckForFailures = False
        result = False

        try:
            assertFunction.Invoke()
            this.NumberOfFailedAsserts = ++self.NumberOfFailedAsserts
            result = False
            Log.LogMessage(MessageType.WARNING, "SoftAssert failed for assert {0}:  {1} passed.  Expected failure type {2}.", assertName, assertFunction.Method.Name, expectedException)
        except Exception as ex:
            if ex.GetType().Equals(expectedException):
                NumberOfPassedAsserts = ++NumberOfPassedAsserts
                result = True
                Log.LogMessage(MessageType.SUCCESS, "SoftAssert passed for assert {0}: {1}.", assertName, assertFunction.Method.Name)
            else:
                NumberOfFailedAsserts = ++NumberOfFailedAsserts
                result = False;
                Log.LogMessage(MessageType.WARNING, "SoftAssert failed for assert {0}: {1}. Expected failure:{2} Actual failure: {3}", assertName, assertFunction.Method.Name, expectedException, ex.Message)
                listOfExceptions.Add(ex.Message)
        finally:
            NumberOfAsserts = ++NumberOfAsserts
        return result;

# Executes the assert type passed as parameter and updates the total assert count
# @param test Test method Action
# @param expectedText Expected value of the string
# @param actualText Actual value of the string
# @param message Test Name or Message
# @returns Boolean if the assert is true
    def invoke_test(self, test, expectedText, actualText, message):
        # Resetting every time we invoke a test to verify the user checked for failures
        this.DidUserCheckForFailures = False
        result = False

        try:
            test.invoke();
            this.NumberOfPassedAsserts = ++NumberOfPassedAsserts
            result = True
            Log.LogMessage(expectedText, actualText, message, result)
        except Exception as ex:
            this.NumberOfFailedAsserts = ++NumberOfFailedAsserts
            result = False;
            Log.LogMessage(expectedText, actualText, message, result)
            listOfExceptions.Add(ex.Message);
        finally:
            this.NumberOfAsserts = ++NumberOfAsserts
        return result;

# Executes the assert type passed as parameter and updates the total assert count
# @param test Test method Action
# @param softAssertName Soft assert name
# @param message Test Name or Message
# @returns Boolean if the assert is true
    def invoke_test(self, test, softAssertName, message):
        # Resetting every time we invoke a test to verify the user checked for failures
        this.DidUserCheckForFailures = False
        result = False

        try:
            test.Invoke()
            this.NumberOfPassedAsserts = ++NumberOfPassedAsserts
            result = True
            Log.LogMessage(MessageType.SUCCESS, "SoftAssert passed for: {0}.", softAssertName)
        except Exception as ex:
            NumberOfFailedAsserts = ++NumberOfFailedAsserts
            result = False
            Log.LogMessage(MessageType.WARNING, "SoftAssert failed for: {0}. {1}", softAssertName, message)
            listOfExceptions.Add(ex.Message)
        finally:
            this.NumberOfAsserts = ++NumberOfAsserts
        return result

# Logs the message to the logger
# @param expectedText Expected value of the string
# @param actualText Actual value of the string
# @param message Test Name or Message
# @param result Decides the message type to be logged
    def log_message(self, expectedText, actualText, message, result):
        if result:
            Log.LogMessage(MessageType.SUCCESS, StringProcessor.SafeFormatter("Soft Assert '{0}' passed. Expected Value = '{1}', Actual Value = '{2}'.", message, expectedText, actualText))
        else:
            Log.LogMessage(MessageType.WARNING, StringProcessor.SafeFormatter("Soft Assert '{0}' failed. Expected Value = '{1}', Actual Value = '{2}'.", message, expectedText, actualText))