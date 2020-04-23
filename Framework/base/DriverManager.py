
class DriverManager(): 
 
# The test object associated with the driver
    # private readonly BaseTestObject testObject
    testObject = []
    
    # Gets or sets the underlying driver; like the web driver or database connection driver
    BaseDriver = None
    
    # Gets or sets the function for getting the underlying driver
    GetDriver = None

# Initializes a new instance of the <see cref="DriverManager"/> class
# @param funcToRun How to get the underlying driver
# @param testObject The associate test object
    def __init__(self, funcToRun, testObject):
        self.GetDriver = funcToRun
        self.testObject = testObject

# Gets the testing object
    def log(self):
        return self.testObject.Log;
        
# Gets the underlying driver; like the web driver or database connection driver
    def get_base_driver(self):
        return BaseDriver
    
# Sets the underlying driver; like the web driver or database connection driver   
    def set_base_driver(self, baseDriver):
        self.BaseDriver = baseDriver
        
    def override_driver_get(self, driverGet):
            self.driver_dispose()
            self.BaseDriver = None
            this.GetDriver = driverGet

# Check if the underlying driver has been initialized
# returns True if the underlying driver has already been initialized
    def is_driver_intialized(self):
        self.BaseDriver != None;

# Get the driver
# @returns The driver
        ## public abstract object Get();

# Cleanup the driver
    def dispose(self):

# Cleanup the driver
# @param disposing Dispose managed objects
        def dispose(self, disposing):
            # Only dealing with managed objects
            if (disposing):
                self.driver_dispose()

# Dispose driver specific objects
        #protected abstract void DriverDispose();

# Get the underlying driver
# @returns The underlying driver
    def get_Base(self):
        # Initialize the driver if we haven't already
        if (self.BaseDriver == None):
            self.BaseDriver = self.GetDriver()
        return self.BaseDriver