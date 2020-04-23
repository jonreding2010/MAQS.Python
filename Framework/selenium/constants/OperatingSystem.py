from enum import Enum
import platform

# The enum Operating system. 
class OperatingSystem():
    
  def __init__(self):
    # None.  Can be used as a default state
    self.NONE = ["None", "None"]
    # Linux Operating System.
    self.LINUX = ["Linux", ["nix", "nux", "aix", "ubuntu"]]
    # Mac Operating System.
    self.MACOS = ["Mac OS", ["mac os x", "mac"]]
    # Windows Operating System.
    self.WINDOWS = ["Windows", ["win", "windows"]]


# Instantiates a new Operating system.
# @param operatingSystemString the operating system string
# @param osAbbr                the operating system abbreviations
  def operating_System(self, operatingSystemString, osAbbr):
    this.operatingSystemName = operatingSystemString;
    this.operatingSystemAbbreviations = osAbbr;

# Gets operating system.
# @return the operating system
  @staticmethod
  def get_operating_system():
    systemProperty = platform.system()
    return get_operating_system_with_abbreviation(systemProperty);

# Gets operating system with abbreviation.
# @param operatingSystemAbbr the operating system abbr
# @return the operating system with abbreviation
  @staticmethod
  def get_operating_system_with_abbreviation(operatingSystemAbbr):
    if operatingSystemAbbr in LINUX[1]:  
       return LINUX
    elif operatingSystemAbbr in MACOS[1]:
        return MACOS
    elif operatingSystemAbbr in WINDOWS[1]:
        return WINDOWS
    else:
      raise AttributeError("Unknown Operating System detected: " + operatingSystemAbbr)