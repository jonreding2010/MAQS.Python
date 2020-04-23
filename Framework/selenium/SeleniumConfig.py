from Framework.utilities.helper import Config, ConfigSection, StringProcessor
import pathlib
from Framework.selenium.constants import BrowserType, RemoteBrowserType
from argparse import ArgumentError

class SeleniumConfig:
      
  # The web service configuration section.
  SELENIUM_SECTION = ConfigSection.SeleniumMaqs
  # The remote selenium configuration section.
  SELENIUM_CAPS_SECTION = ConfigSection.RemoteSeleniumCapsMaqs

# Get the browser type.
# @return The browser type
  def get_browser_Type(self):
    return get_browser_type(get_browser_name())

# Get the browser type based on the provided browser name.
# @param browserName Name of the browse as a string
# @return The browser type
  def get_browser_type(self, browserName):  
    browserName = browserName.ascii_uppercase()
    if browserName in  ["INTERNET EXPLORER", "INTERNETEXPLORER", "IE"]:
        return BrowserType.IE
    elif browserName == "FIREFOX":
        return BrowserType.FIREFOX
    elif browserName == "CHROME":
        return BrowserType.CHROME
    elif browserName == "HEADLESSCHROME":
        return BrowserType.HEADLESS_CHROME
    elif browserName == "SAFARI":
        return BrowserType.SAFARI
    elif browserName == "EDGE":
        return BrowserType.EDGE
    elif browserName in ["PHANTOMJS", "PHANTOM JS", "PHANTOM"]:
          raise ArgumentError("Selenium no longer supports PhantomJS")
    else:
        raise ArgumentError(StringProcessor.safeFormatter("Remote browser type '%s' is not supported", browserName))
  
# Get the remote browser type.
# @return The remote browser type
  def get_remote_browser_type(self):
    return getRemoteBrowserType(get_remote_browser_name())

# Get the remote browser type.
# @param remoteBrowser Name of the remote browser
# @return The remote browser type
  def getRemoteBrowserType(self, remoteBrowser):
    remoteBrowser = remoteBrowser.ascii_uppercase()
    if remoteBrowser in  ["INTERNET EXPLORER", "INTERNETEXPLORER", "IE"]:
        return RemoteBrowserType.IE
    elif remoteBrowser == "FIREFOX":
        return RemoteBrowserType.FIREFOX
    elif remoteBrowser == "CHROME":
        return RemoteBrowserType.CHROME
    elif remoteBrowser == "SAFARI":
        return RemoteBrowserType.SAFARI
    elif remoteBrowser == "EDGE":
        return RemoteBrowserType.EDGE
    else:
        raise ArgumentError(StringProcessor.safeFormatter("Remote browser type '%s' is not supported", remoteBrowser))

# Get the browser type name - Example: Chrome.
# @return The browser type
  def get_browser_name(self):
    return Config.get_value_for_section(SELENIUM_SECTION, "Browser", "Chrome")

# Get the hint path for the web driver.
# @return The hint path for the web driver
  def get_driver_hint_path(self):
    defaultPath = pathlib.Path("Resources").parent.absolute()
    return Config.get_value_for_section(SELENIUM_SECTION, "WebDriverHintPath", defaultPath)

# Get the remote browser type name.
# @return The browser type being used on grid
  def get_remote_browser_name(self):
    return Config.get_value_for_section(SELENIUM_SECTION, "RemoteBrowserName", "Chrome")

# Get the remote browser version.
# @return The browser version to run against on grid
  def get_Remote_Browser_Version(self):
    return Config.get_value_for_section(SELENIUM_SECTION, "RemoteVersion")

# Get the remote platform type name.
# @return The platform (or OS) to run remote tests against
  def get_remote_platform(self):
    return Config.get_value_for_section(SELENIUM_SECTION, "RemotePlatform");

# Get the hub URL.
# @return the hub URL
  def get_hub_url(self):
    return Config.get_value_for_section(SELENIUM_SECTION, "HubUrl")

# Get the web site base url.
# @return The web site base url
  def getWebSiteBase(self):
    return Config.get_value_for_section(SELENIUM_SECTION, "WebSiteBase")

# Get the SavePageSourceOnFail flag from config.
# @return True if the flag is set to "Yes"
  def get_save_pagesource_on_fail(self):
    return Config.get_value_for_section(SELENIUM_SECTION, "SavePagesourceOnFail").equalsIgnoreCase("Yes");

# Get the SoftAssertScreenshot flag from config.
# @return True if the flag is set to "Yes"
  def getSoftAssertScreenshot(self):
    return Config.get_value_for_section(SELENIUM_SECTION, "SoftAssertScreenshot").equalsIgnoreCase("Yes")

# Get the file extension for the screenshots.
# @return The type of file, defaults to .png
  def getImageFormat(self):
    return Config.get_value_for_section(SELENIUM_SECTION, "ImageFormat", ".png")

# Get the remote capabilities as a HashMap.
# @return HashMap of remote capabilities
  def get_remote_capabilities_as_strings(self):
    return Config.get_section(SELENIUM_CAPS_SECTION)

# Get the remote capabilities as a HashMap.
# @return HashMap of remote capabilities
  def get_remote_capabilities_as_objects(self):
    return self.get_remote_capabilities_as_Strings()

# Get wait from config.
# @return The wait time (in milliseconds)
  def get_wait_time(self):
    return Config.get_general_value("BrowserWaitTime", "0")

# Get the timeout from config.
# @return The timeout time (in milliseconds)
  def get_timeout_time(self):
    return Config.get_general_value("BrowserTimeout", "0")

# Get browser size from config.
# @return The browser size
  def get_browser_size(self):
    return Config.get_value_for_section(SELENIUM_SECTION, "BrowserSize", "MAXIMIZE")