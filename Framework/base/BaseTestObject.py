 
from Framework.utilities.logger.constants import MessageType
from Framework.utilities.logger import Logger
from Framework.base import ManagerDictionary
import os

class BaseTestObject():
# Initializes a new instance of the BaseTestObject class
# param logger The test's logger
# param softAssert The test's soft assert
# fullyQualifiedTestName The test's fully qualified test name</param>
    def __init__(self, logger, softAssert, fullyQualifiedTestName):
        self.log = logger;
        self.SoftAssert = softAssert;
        self.PerfTimerCollection = PerfTimerCollection(logger, fullyQualifiedTestName)
        self.Values = {}
        self.Objects = {}
        self.ManagerStore = ManagerDictionary()
        self.AssociatedFiles = []
        logger.log_Message(MessageType.INFORMATION, "Setup test object for " + fullyQualifiedTestName)

# Initializes a new instance of the BaseTestObject class
# param logger The test's logger
# param fullyQualifiedTestName The test's fully qualified name
    def __init__(self, logger, fullyQualifiedTestName):
        self.Log = logger
        self.SoftAssert = SoftAssert(self.Log)
        self.PerfTimerCollection = PerfTimerCollection(logger, fullyQualifiedTestName)
        self.Values = {}
        self.Objects = []
        self.ManagerStore = ManagerDictionary()
        self.AssociatedFiles = []
        logger.LogMessage(MessageType.INFORMATION, "Setup test object for " + fullyQualifiedTestName)

# Initializes a new instance of the BaseTestObject class
# param baseTestObject An existing base test object
    def __init__(self, baseTestObject):
        self.Log = baseTestObject.Log
        self.SoftAssert = baseTestObject.SoftAssert
        self.PerfTimerCollection = baseTestObject.PerfTimerCollection
        self.Values = baseTestObject.Values
        self.Objects = baseTestObject.Objects
        self.ManagerStore = baseTestObject.ManagerStore
        self.AssociatedFiles = baseTestObject.AssociatedFiles
        baseTestObject.Log.LogMessage(MessageType.INFORMATION, "Setup test object")

    # Gets or sets the logger
    Log = Logger()

    # Gets or sets the performance timer collection
    PerfTimerCollection = PerfTimerCollection()
    
    # Gets or sets soft assert
    # public SoftAssert SoftAssert { get; set; }
    SoftAssert = SoftAssert()

    #Gets a dictionary of string key value pairs
    # public Dictionary<string, string> Values { get; private set; }
    
    # Gets a dictionary of string key and object value pairs
    ## public Dictionary<string, object> Objects { get; private set; }

    # Gets a dictionary of string key and driver value pairs
    ## public ManagerDictionary ManagerStore { get; private set; }

    # Gets a hash set of unique associated files to attach to the test context
    ## protected HashSet<string> AssociatedFiles { get; private set; }

# Sets a string value, will replace if the key already exists
# param key The key
# param value The value to associate with the key
    def SetValue(self, key, value):
        if (Values.ContainsKey(key)):
            this.Values[key] = value
        else:
            Values.Add(key, value)

# Sets an object value, will replace if the key already exists
# param key The key
# param value The value to associate with the key
    def set_object(self, key, value):
        if (Objects.ContainsKey(key)):
            this.Objects[key] = value
        else:
            Objects.Add(key, value)

# Get a driver manager of the specific type
# param DriverManager The type of driver manager</typeparam>
# returns The driver manager
    def get_driver_manager(self, driverManager):
        return ManagerStore[type(driverManager).FullName]

# Add a new driver
# param driver The new driver
# param overrideIfExists Should we override if this driver exists.  If it exists and we don't override than an error will be thrown.</param>
    def add_driver_manager(self, driver, driverManager, overrideIfExists = false):
        if overrideIfExists:
           self.override_driver_Manager(type(driverManager).FullName, driver)
        else:
            self.add_driver_manager(type(driverManager).FullName, driver)

# Add a new driver
# param key Key for the new driver
# param driver The new driver
    def add_driver_manager(self, key, driver):
        ManagerStore.Add(key, driver)

# Checks if the file exists and if so attempts to add it to the associated files set
# @param pathpath of the file
# @returns> True if the file exists and was successfully added, false if the file doesn't exist or was already added
    def add_associated_file(self, path):
        if os.path.exists(path):
            return AssociatedFiles.Add(path)
        return False

# Removes the file path from the associated file set
# @param path path of the file
# @returns True if the file path was successfully removed, false if the file wasn't in the set
    def remove_associated_file(self, path):
        return AssociatedFiles.Remove(path);

# Returns an array of the file paths associated with the test object
# @returns An array of the associated files
    def get_array_of_associated_files(self):
        associatedFiles = AssociatedFiles.Count
        AssociatedFiles.CopyTo(associatedFiles, 0);
        return associatedFiles

# Returns an array of the file paths associated with the test object
# @param path" The file path to search for
# @returns Whether the exact file path is contained in the set
    def contains_associated_file(self, path):
        return AssociatedFiles.Contains(path)

# Override a specific driver
# @param key The driver key
# @param driver The new driver
    def override_driver_manager(self, key, driver):
        if (ManagerStore.ContainsKey(key)):
            ManagerStore[key].Dispose()
            ManagerStore[key] = driver
        else:
            ManagerStore.Add(key, driver);

# Dispose the of the driver store
    def dispose(self):
        dispose(True);
        # GC.SuppressFinalize(self);

# Dispose the of the driver store
# @param disposing True if you want to release managed resources
    def dispose(self, disposing):
        if not disposing or ManagerStore is None:
            return;

        Log.LogMessage(MessageType.VERBOSE, "Start dispose");

        # Make sure all of the individual drivers are disposed
        for singleDrive in ManagerStore.Values:
            if (singleDrive != None):
                singleDrive.dispose()

        self.ManagerStore = None

        self.Log.LogMessage(MessageType.VERBOSE, "End dispose");