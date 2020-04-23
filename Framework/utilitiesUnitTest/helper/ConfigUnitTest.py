import unittest
from Framework.utilities.helper import Config, ConfigSection

class ConfigUnitTest(unittest.TestCase):
# Test getting an entire section from the config.
  # @Test(groups = TestCategories.UTILITIES)
    def getSectionWithConfigSecEnumTest(self):
        testSection = Config.getSection(ConfigSection.SeleniumMaqs)
        self.assertEquals(testSection.get("TestKey"), "testValueTwo")
        self.assertEquals(testSection.get("Browser"), "Internet Explorer")

# Test adding a list of test settings to the config.
    @Test(groups = TestCategories.UTILITIES)
    def addTestSettingValuesNewSectionTest(self):
        newValueMap = {}
        newValueMap.put("BROWSER1", "CHROME1")
        newValueMap.put("DBString2", "Dbstring2222")

        Config.addTestSettingValues(newValueMap, "NewSection", False);
        self.assertEquals(Config.getSection("NewSection").get("BROWSER1"), "CHROME1")
        self.assertEquals(Config.getSection("NewSection").get("DBString2"), "Dbstring2222")

# Test overriding existing values in the config.
  # @Test(groups = TestCategories.UTILITIES)
    def addGeneralTestSettingValuesOverrideValuesTest(self):
        newValueMap = {}
        newValueMap.put("BrowserOverride", "CHROME")
        newValueMap.put("TimeoutOverride", "13333333")

        Config.addGeneralTestSettingValues(newValueMap, True);
        self.assertEquals(Config.getGeneralValue("BrowserOverride"), "CHROME")
        self.assertEquals(Config.getGeneralValue("TimeoutOverride"), "13333333")

# Test not overriding existing values in the config.
  # @Test(groups = TestCategories.UTILITIES)
    def addGeneralTestSettingValuesDontOverrideValuesTest(self):
        newValueMap = {}
        newValueMap.put("DontBrowserOverride", "CHROME")
        newValueMap.put("DontTimeoutOverride", "13333333")

        newValueMapTwo = {}
        newValueMapTwo.put("DontBrowserOverride", "IE")
        newValueMapTwo.put("DontTimeoutOverride", "5555")

        # add values to the override config since the values don't exist in the override config
        Config.addGeneralTestSettingValues(newValueMap, False)
        self.assertEquals(Config.getGeneralValue("DontBrowserOverride"), "CHROME")
        self.assertEquals(Config.getGeneralValue("DontTimeoutOverride"), "13333333")

    # don't add the values to the override config since the values do exist in the override config
        Config.addGeneralTestSettingValues(newValueMapTwo, False)
        self.assertEquals(Config.getGeneralValue("DontBrowserOverride"), "CHROME")
        self.assertEquals(Config.getGeneralValue("DontTimeoutOverride"), "13333333")

        # do add the values because of the override flag
        Config.addGeneralTestSettingValues(newValueMapTwo, True)
        self.assertEquals(Config.getGeneralValue("DontBrowserOverride"), "IE")
        self.assertEquals(Config.getGeneralValue("DontTimeoutOverride"), "5555")

# Test getting a value out of the default section of the config.
  #@Test(groups = TestCategories.UTILITIES)
    def getGeneralValueTest(self):
        self.assertEquals(Config.getGeneralValue("TestKey"), "testValue")
        self.assertEquals(Config.getGeneralValue("nonExistentKey", "defaultValue"), "defaultValue")

# Test getting a value of a specified section of the config.
  # @Test(groups = TestCategories.UTILITIES)
    def getValueForSectionTest(self):
        self.assertEquals(Config.getValueForSection("SeleniumMaqs", "TestKey"), "testValueTwo")
        self.assertEquals(Config.getValueForSection(ConfigSection.SeleniumMaqs, "Browser"), "Internet Explorer")
        self.assertEquals(Config.getValueForSection("SeleniumMaqs", "nonExistentKey", "defaultValue"), "defaultValue")

# Test getting a value from the config using the full defined path.
  # @Test(groups = TestCategories.UTILITIES)
    def getValueTest(self):
        self.assertEquals(Config.getValue("TestKey", "defaultValue"), "defaultValue")
        self.assertEquals(Config.getValue("SeleniumMaqs.TestKey"), "testValueTwo")

# Test checking if the key exists.
  #@Test(groups = TestCategories.UTILITIES)
    def doesKeyExistTest(self):
        self.assertTrue(Config.doesKeyExist("SeleniumMaqs.TestKey"))
        self.assertTrue(Config.doesGeneralKeyExist("TimeoutOverride"))
        self.assertTrue(Config.doesKeyExist("HubAddress", ConfigSection.SeleniumMaqs))
        self.assertFalse(Config.doesKeyExist("HubAddress", ConfigSection.MagenicMaqs))