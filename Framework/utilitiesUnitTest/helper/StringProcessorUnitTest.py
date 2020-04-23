import unittest
from Framework.utilities.helper import StringProcessor

class StringProcessorUnitTest(unittest.TestCase):
    def testSafeFormatter(self):
        successful = StringProcessor.safe_formatter("This is a %s message.", "successful")
        self.assertEquals(successful, "This is a successful message.")

    def testSafeFormatterMessage(self):
        successful = StringProcessor.safe_formatter("This is a message.")
        self.assertEquals(successful, "This is a message.")

    def testSafeFormatterMessageNull(self):
        string = StringProcessor.safe_formatter(None, "Message", "String", "Null")
        self.assertEquals(string, "Message: null Arguments: Message String Null ")