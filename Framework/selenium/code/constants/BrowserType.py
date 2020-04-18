from enum import Enum

class BrowserType(Enum):
    
# Chrome web browser.
  CHROME = "CHROME"

# Edge web browser.
  EDGE = "EDGE"

# Firefox web browser.
  FIREFOX = "FIREFOX"

# Chrome web browser - run headless.
  HEADLESS_CHROME = "HEADLESS_CHROME"

# IE web browser.
  IE = "IE"

# Remote web browser - Used when executing on Grid or cloud based provides like Sauce Labs.   
  REMOTE = "REMOTE"
