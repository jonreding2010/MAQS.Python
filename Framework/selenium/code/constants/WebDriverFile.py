from enum import Enum

class WebDriverFile(Enum):
# The Chrome driver file.
  CHROME = "chromedriver"
  
# The Firefox driver file.  
  FIREFOX = "geckodriver"
  
# The Internet Explorer driver file.
  IE = "IEDriverServer"
  
# The Edge driver file.
  EDGE = "MicrosoftWebDriver"