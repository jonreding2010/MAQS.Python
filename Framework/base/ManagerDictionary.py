
from Framework.base import BaseTest

class ManagerDictionary():

# Get the driver for the associated driver manager
# @param T Type of driver
# @param key Key for the manager
# @returns The managed driver
    def get_Driver(self, driverType, key):
        return driverType.key.Get()

# Get a driver
# @param T The type of driver
# @param U The type of driver manager
# @returns The driver</returns>
    def GetDriver(self, driverType, driverManager):
        # where U : DriverManager
        return self[type(driverManager).FullName].Get()

# Add a manager
# @param manager The manager
    def add(self, manager):
        self.Add(manager.GetType().FullName, manager);

# Add or replace a manager
# @param manager The manager
    def add_or_override(self, manager):
        self.add_or_override(manager.GetType().FullName, manager)

# Add or replace a manager
# @param Key for storing the manager
# @param manager The manager
    def add_or_override(self, key, manager):
        self.remove(key);
        self.add(key, manager);

# Remove a driver manager
# @param key Key for the manager you want removed
# @returns True if the manager was removed
    def remove(self, key):
        if (self.ContainsKey(key)):
            self[key].Dispose()
        return BaseTest.remove(key)

# Remove a driver manager
# @param type The type of manager
# @returns True if the manager was removed
    def remove(self, type):
        key = type.FullName;

        if (self.ContainsKey(key)):
            self[key].Dispose()
        return self.remove(key)

# Clear the dictionary
    def clear(self):
        for driver in self:
            driver.Value.Dispose();
        BaseTest.clear()


# Cleanup the driver
    def dispose(self):
        dispose(True);
        # GC.SuppressFinalize(self)

# Cleanup the driver
# @param disposing Dispose managed objects
    def dispose(self, disposing):
        # Only dealing with managed objects
        if (disposing):
            self.clear()