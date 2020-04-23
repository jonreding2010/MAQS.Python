from Framework.utilities.helper import StringProcessor
from ctypes import FormatError
from binascii import Error
from argparse import ArgumentError
from Framework.selenium.constants import BrowserType, SeleniumConfig, RemoteBrowserType, WebDriverFile
from selenium import webdriver
from pathlib import Path
import os

# The type Web driver factory.
class WebDriverFactory:
      
  WINDOW_MAX = "MAXIMIZE"
  
# Gets default browser.
# @return the default browser
# @throws Exception the exception
  @staticmethod
  def get_default_browser():
    return get_browser_with_default_configuration(SeleniumConfig.get_browser_type());

# Gets browser with default configuration.
# @param browser the browser
# @return the browser with default configuration
# @throws Exception the exception
  @staticmethod
  def get_browser_with_default_configuration(browser):
    size = SeleniumConfig.get_browser_size()
    try:
        if browser == BrowserType.IE:
          return get_internet_explorer_driver(get_default_internet_explorer_options(), size);
        elif browser == BrowserType.FIREFOX:
          return get_firefox_driver(get_default_firefox_options(), size);
        elif browser == BrowserType.CHROME:
          return get_chrome_driver(get_default_chrome_options(), size);
        elif browser == BrowserType.HEADLESS_CHROME:
          return get_headless_chrome_driver(get_default_headless_chrome_options(size));
        elif browser == BrowserType.EDGE:
          return get_edge_driver(get_default_edge_options(), size);
        elif browser == BrowserType.REMOTE:
          return webdriver.RemoteWebDriver(SeleniumConfig.getHubUrl(), get_default_remote_options())
        else:
           raise ArgumentError(StringProcessor.safeFormatter("Browser type '%s' is not supported", browser));
    except Exception as e:
      # Log that something went wrong
      raise Error("Your web driver may be out of date or unsupported. " + e.message)

# Gets default chrome options.
# @return the default chrome options
  @staticmethod
  def get_default_chrome_options():
    chromeOptions = webdriver.ChromeOptions();
    chromeOptions.addArguments("test-type");
    chromeOptions.addArguments("--disable-web-security");
    chromeOptions.addArguments("--allow-running-insecure-content");
    chromeOptions.addArguments("--disable-extensions");
    return chromeOptions

# Gets default headless chrome options.
# @return the default headless chrome options
  @staticmethod
  def get_default_headless_chrome_options():
    return get_default_headless_chrome_options(WINDOW_MAX);

# Gets default headless chrome options.
# @param size the size
# @return the default headless chrome options
  @staticmethod
  def get_default_headless_chrome_options(size):
    headlessChromeOptions = webdriver.ChromeOptions();
    headlessChromeOptions.addArguments("test-type");
    headlessChromeOptions.addArguments("--disable-web-security");
    headlessChromeOptions.addArguments("--allow-running-insecure-content");
    headlessChromeOptions.addArguments("--disable-extensions");
    headlessChromeOptions.addArguments("--no-sandbox");
    headlessChromeOptions.addArguments("--headless");
    headlessChromeOptions.addArguments(get_headless_window_size_string(size));
    return headlessChromeOptions;

# Gets default internet explorer options.
# @return the default internet explorer options
  @staticmethod
  def get_default_internet_explorer_options():
    options = webdriver.InternetExplorerOptions();
    options.ignoreZoomSettings()
    return options

# Gets default firefox options.
# @return the default firefox options
  @staticmethod
  def get_default_firefox_options():
    firefoxOptions = webdriver.FirefoxOptions()
    firefoxOptions.setProfile(webdriver.FirefoxProfile())
    return firefoxOptions

# Gets default edge options.
# @return the default edge options
  @staticmethod
  def get_default_edge_options():
    edgeOptions = webdriver.EdgeOptions()
    edgeOptions.setPageLoadStrategy(webdriver.PageLoadStrategy.NORMAL.toString())
    return edgeOptions;

# Gets chrome driver.
# @param chromeOptions the chrome options
# @return the chrome driver
  @staticmethod
  def get_chrome_driver(chromeOptions):
    return get_chrome_driver(chromeOptions, WINDOW_MAX)

# Gets chrome driver.
# @param chromeOptions the chrome options
# @param size          the size
# @return the chrome driver
  @staticmethod
  def get_chrome_driver(chromeOptions, size):
    get_driver_location(WebDriverFile.CHROME.getFileName())
    driver = webdriver.ChromeDriver(chromeOptions);
    driver.setBrowserSize(driver, size);
    return driver;

# Gets headless chrome driver.
# @param headlessChromeOptions the headless chrome options
# @return the headless chrome driver
  @staticmethod
  def get_headless_chrome_driver(headlessChromeOptions):
    get_driver_location(WebDriverFile.CHROME.getFileName())
    return webdriver.ChromeDriver(headlessChromeOptions)

# Gets firefox driver.
# @param firefoxOptions the firefox options
# @param size           the size
# @return the firefox driver
  @staticmethod
  def get_firefox_driver(firefoxOptions, size):
    webdriver.get_driver_location(WebDriverFile.FIREFOX.getFileName())
    driver = webdriver.FirefoxDriver(firefoxOptions);
    driver.setBrowserSize(driver, size);
    return driver

# Gets edge driver.
# @param edgeOptions the edge options
# @param size        the size
# @return the edge driver
  @staticmethod
  def get_edge_driver(edgeOptions, size):
    driverLocation = webdriver.getDriverLocation(WebDriverFile.EDGE.getFileName(),
        get_windows_edge_driver_location(WebDriverFile.EDGE.getFileName()));

    # If we can't find an installed edge driver, look in the normal places
    if len(driverLocation) == 0:
      driverLocation = get_driver_location(WebDriverFile.EDGE.getFileName());
      
    driver = webdriver.EdgeDriver(edgeOptions);
    driver.setBrowserSize(driver, size);
    return driver

# Gets internet explorer driver.
# @param internetExplorerOptions the internet explorer options
# @param size                    the size
# @return the internet explorer driver
  @staticmethod
  def get_internet_explorer_driver(internetExplorerOptions, size):
    get_driver_location(WebDriverFile.IE.getFileName())
    driver = webdriver.InternetExplorerDriver(internetExplorerOptions);
    driver.setBrowserSize(driver, size);
    return driver;

# Gets default remote options.
# @return the default remote options
  @staticmethod
  def get_default_remote_options():
    remoteBrowser = SeleniumConfig.get_remote_browser_type();
    remotePlatform = SeleniumConfig.get_remote_platform();
    remoteBrowserVersion = SeleniumConfig.get_remote_browser_version()
    capabilities = SeleniumConfig.get_remote_capabilities_as_objects()
    return get_remote_options(remoteBrowser, remotePlatform, remoteBrowserVersion, capabilities)

# Gets remote options.
# @param remoteBrowser the remote browser
# @return the remote options
  @staticmethod
  def get_remote_options(remoteBrowser):
    return get_remote_options(remoteBrowser, "", "", None);

# Gets remote options.
# @param remoteBrowser      the remote browser
# @param remoteCapabilities the remote capabilities
# @return the remote options
  @staticmethod
  def get_remote_options(remoteBrowser, remoteCapabilities):
    return get_remote_options(remoteBrowser, "", "", remoteCapabilities);

# Gets remote options.
# @param remoteBrowser        the remote browser
# @param remotePlatform       the remote platform
# @param remoteBrowserVersion the remote browser version
# @param remoteCapabilities   the remote capabilities
# @return the remote options
  @staticmethod
  def get_remote_options(remoteBrowser, remotePlatform, remoteBrowserVersion, remoteCapabilities):  
    if remoteBrowser == RemoteBrowserType.IE:
        options = webdriver.InternetExplorerOptions()
    elif remoteBrowser == RemoteBrowserType.FIREFOX:
        options = webdriver.FirefoxOptions()
    elif remoteBrowser == RemoteBrowserType.CHROME:
        options = webdriver.ChromeOptions()
    elif remoteBrowser == RemoteBrowserType.EDGE:
        options = webdriver.EdgeOptions()
    elif remoteBrowser == RemoteBrowserType.SAFARI:
        options = webdriver.SafariOptions()
    else:
        raise Exception(StringProcessor.safeFormatter("Remote browser type " + remoteBrowser + " is not supported"))

    # Add a platform setting if one was provided
    if (remotePlatform != "" and "platform" not in remoteCapabilities):
      remoteCapabilities.put("platform", remotePlatform)

    # Add a remote browser setting if one was provided
    if (remotePlatform != "" and "platform" not in remoteCapabilities):
      remoteCapabilities.put("version", remoteBrowserVersion)

    # Add additional capabilities to the driver options
    set_driver_options(options, remoteCapabilities);
    return options;

# Sets driver options.
# @param driverOptions          the driver options
# @param additionalCapabilities the additional capabilities
  @staticmethod
  def set_driver_options(driverOptions, additionalCapabilities):
    # If there are no additional capabilities just return
    if (additionalCapabilities == None):
      return;
      
    for key, value in additionalCapabilities:
      if (value == ""):
        driverOptions.setCapability(key, value)

# Sets browser size.
# @param webDriver the web driver
# @param size      the size
  @staticmethod
  def set_browser_size(webDriver, size):
    size = size.upper

    if (size.equals(WINDOW_MAX)):
      webDriver.manage().window().maximize();
    elif (size != "DEFAULT"):
      webDriver.manage().window().setSize(extract_dimension_from_string(size));

# Gets headless window size string.
#  @param size the size
# @return the headless window size string
  @staticmethod
  def get_headless_window_size_string(size):
    if (size == WINDOW_MAX or  size == "DEFAULT"):
      # If we need a string default to 1920 by 1080
      return "window-size=1920,1080";
    else:
      dimension = extract_dimension_from_string(size);
      return "window-size=" + dimension.width + "," + dimension.height

# Extract dimension from string dimension.
# @param size the size
# @return the dimension
  @staticmethod
  def extract_dimension_from_string(size):
    sizes = size.split("[xX]");

    if (size.upper != "X" or len(sizes) != 2):
      raise ValueError("Browser size is expected to be in an expected format: 1920x1080")

    try:
      width = sizes[0]
      height = sizes[1]
      return width, height
    except Error:
      raise FormatError("Length and Width must be a string that is an integer value: 400x400")

# Gets driver location.
# @param driverFile the driver file
# @return the driver location
  @staticmethod
  def get_driver_location(driverFile):
    return get_driver_location(driverFile, "", True)

# Gets driver location.
# @param driverFile      the driver file
# @param defaultHintPath the default hint path
# @return the driver location
  @staticmethod
  def get_driver_location(driverFile, defaultHintPath):
    return get_driver_location(driverFile, defaultHintPath, True)

# Gets driver location.
# @param driverFile      the driver file
# @param defaultHintPath the default hint path
# @param mustExist       the must exist
# @return the driver location
  @staticmethod
  def get_driver_location(driverFile, defaultHintPath, mustExist):
    # Get the hint path from the config
    hintPath = SeleniumConfig.get_driver_hint_path()

    # Try the hint path first
    if (hintPath != "" and Path.get(hintPath, driverFile).toFile().exists()):
      return hintPath;
  
    # Try the default hint path next
    if (defaultHintPath != "" and Path.get(defaultHintPath, driverFile).toFile().exists()):
      return Path.get(defaultHintPath).toString();

    # Try the test location
    #path = Path.get(File("").getAbsolutePath());
    path = os.path.abspath("")
    testLocation = path.getParent().toString();
    if (Path.get(testLocation, driverFile).toFile().exists()):
      return testLocation;

    # Try resources
    classLoader = WebDriverFactory.__class__;
    url = classLoader.getResource(driverFile);
    if (url != ""):
      file = url.getPath()
      return file.getParent()

    # We didn't find the web driver so throw an error if we need to know where it is
    if (mustExist):
      raise TimeoutError(StringProcessor.safeFormatter("Unable to find driver for " +  driverFile))
    return ""
  
# Gets windows edge driver location.
# @param file the file
# @return the windows edge driver location
  @staticmethod
  def get_windows_edge_driver_location(file):    
    # edgeDriverFolder = "Microsoft Web Driver"
    edgeDriverFolder = WebDriverFile.EDGE

    path = Path.get(os.getenv("ProgramW6432"), edgeDriverFolder, file);
    if (path.toFile().isFile()):
      return path.getParent().toString();

    path = Path.get(os.getenv("ProgramFiles(x86)"), edgeDriverFolder, file);
    if (path.toFile().isFile()):
      return path.getParent().toString()

    path = Path.get(os.getenv("ProgramFiles"), edgeDriverFolder, file);
    if (path.toFile().isFile()):
      return path.getParent().toString() 
    return ""