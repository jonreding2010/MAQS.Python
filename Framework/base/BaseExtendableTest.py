import Framework.base.BaseTest as BaseTest

class BaseExtendableTest():
# Gets the test object 
    def get_test_object(self):
        return BaseTest.TestObject

# Sets the test object 
    def set_test_object(self, value):
        BaseTest.BaseTestObjects = value

# Setup before a test
# [TestInitialize]
# [SetUp]
    def setup(self):
        # Do base generic setup
        BaseTest.setup()

# Create a test object
    def create_new_test_object(self):  
        return 
        #protected override abstract void CreateNewTestObject();