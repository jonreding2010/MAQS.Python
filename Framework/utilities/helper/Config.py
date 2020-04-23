import os.path 
from os import path
from Framework.utilities.helper import ConfigSection as ConfigSection
from Framework.utilities.helper import StringProcessor as StringProcessor
from binascii import Error
import xml.etree.ElementTree as et 

# Configuration class.
class Config:

    # The default section MagenicMaqs.
    DEFAULT_MAQS_SECTION = ConfigSection.MagenicMaqs
    # default config.xml file name.
    CONFIG_FILE = "config.xml"  
    # The configuration containing values loaded in from the config.xml file.
    configValues = []
    # The configuration containing values that were added to the configuration.
    overrideConfig = []
    # The base configs object.
    configs = []
    
    @staticmethod
    def config(parameter_list):
        try:
            if path.exists(CONFIG_FILE):
                tree = et.parse(CONFIG_FILE)
                root = tree.getroot()
                
                for node in root:
                    configValues.add(node)
                '''
                builder = configs.xmlBuilder(CONFIG_FILE)
                configValues = builder.getConfiguration();
                configValues.setSynchronizer(ReadWriteSynchronizer())
                '''
        except Exception as e:
            raise TimeoutError(StringProcessor.safeFormatter("Exception creating the xml configuration object from the file : " + e.message))

    # Gets a section from the configuration.
    # @param section The desired section
    # @return A HashMap of the values in the section
    def get_section(self, section):
        sectionValues = []
        # first parse the override config
        overridePaths = overrideConfig.getKeys(section);
        while (overridePaths.hasNext()):
            key = overridePaths.next()
            sectionValues.put(key.replaceFirst(section + "\\.", ""), overrideConfig.getString(key))

        # then parse the base config, ignoring duplicates
        configValuePaths = configValues.getKeys(section);

        while (configValuePaths.hasNext()):
            key = configValuePaths.next();
            editedKey = key.replaceFirst(section + "\\.", "");
            if (editedKey not in sectionValues):
                sectionValues.put(editedKey, configValues.getString(key))
        return sectionValues

    # Add dictionary of values to maqs section.
    # @param configurations   Dictionary of configuration values
    # @param overrideExisting True to override existing values, False otherwise
    def addGeneralTestSettingValues(self, configurations, overrideExisting):
        add_test_setting_values(configurations, DEFAULT_MAQS_SECTION, overrideExisting)

    # Add dictionary of values to specified section.
    # @param configurations   Dictionary of configuration values
    # @param section          Section to add the value to
    # @param overrideExisting True to override existing values, False otherwise
    def add_test_setting_values(self, configurations, section, overrideExisting):
        for entry in configurations:
            sectionedKey = section + "." + entry.getKey()
            if sectionedKey not in overrideConfig or overrideExisting == True:
                overrideConfig.setProperty(sectionedKey, entry.getValue())


    # Get the specified value out of the default section.
    # @param key The key
    # @return The configuration value
    def get_general_value(self, key):
        return get_value_for_section(DEFAULT_MAQS_SECTION, key)

    # Get the specified value out of the default section.
    # @param key          The key
    # @param defaultValue The value to return if the key does not exist
    # @return The configuration value
    def get_general_value(self, key,defaultValue):
        return get_value_for_section(DEFAULT_MAQS_SECTION, key, defaultValue)

    # Get the specified value out of the specified section.
    # @param section The section to search
    # @param key     The key
    # @return The configuration value
    def get_value_for_section(self, section, key):
        return get_value_for_section(section, key, "")

    # Get the specified value out of the specified section.
    # @param section      The section to search
    # @param key          The key
    # @param defaultValue The value to return if the key is not found
    # @return The configuration value
    def get_value_for_section(self, section, key, defaultValue):
        return get_value_for_section(section.toString(), key, defaultValue)

    # Get the specified value out of the specified section.
    # @param section      The section to search
    # @param key          The key
    # @param defaultValue The value to return if the key is not found
    # @return The configuration value
    def get_value_for_section(self, section, key, defaultValue):
        keyWithSection = section + "." + key;
        return get_value(keyWithSection, defaultValue);

    # Get the configuration value for a specific key. Does not assume a section.
    # @param key The key
    # @return The configuration value - Returns the empty string if the key is not found
    def get_value(self, key):
        retVal = overrideConfig.getString(key, "");

        if len(retVal) == 0:
            return configValues.getString(key, "")
        else:
            return retVal

    # Get the configuration value for a specific key. Does not assume a section.
    #  @param key          The key
    # @param defaultValue Value to return if the key does not exist
    # @return The configuration value - Returns the default string if the key is not found
    def get_value(self, key, defaultValue):
        retVal = get_value(key);

        if len(retVal) == 0:
            return defaultValue
        else:
            return retVal

    # Check the config for a specific key. Does not assume a section.
    # @param key The key
    # @return True if the key exists, false otherwise
    def does_key_exist(self, key):
        if  overrideConfig.containsKey(key): 
            return True
        else:
            return key in configValues

    # Check the config for a specific key. Searches the specified section.
    # @param key     The key
    # @param section The specified section
    # @return True if the key exists, false otherwise
    def does_key_exist(self, key, section):
        keyWithSection = section + "." + key;
        return does_key_exist(keyWithSection)


    # Check the config for a specific key. Searches the default section.
    # @param key The key
    # @return True if the key exists, false otherwise
    def does_general_key_exist(self, key):
        return does_key_exist(key, DEFAULT_MAQS_SECTION)