from enum import Enum

class TestResultType(Enum):
# The test passed.
  PASS = "PASS"

# The test failed.

  FAIL = "FAIL"

# The test was inconclusive.
  INCONCLUSIVE = "INCONCLUSIVE"

# The test was skipped.
  SKIP = "SKIP"


# The test had an unexpected result.
  OTHER = "OTHER"