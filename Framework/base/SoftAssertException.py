
class SoftAssertException(Exception):

# Initializes a new instance of the <see cref="SoftAssertException" /> class
        
        # Call the base class constructor with the parameters it needs
        # super(ValidationError, self).__init__(message)

        # Now for your custom code...
        # self.errors = errors

# Initializes a new instance of the SoftAssertException class
# @param message The message that describes the error
    def __init__(self, message):
        super(message)

# Initializes a new instance of the SoftAssertException
# @param message The message that describes the error
# @param innerException The exception that is the cause of the current exception
    def __init__(self, message, innerException): 
        super(message, innerException)


# Initializes a new instance of the SoftAssertException
# @param info The serialization information object that holds the serialized object data about the exception being thrown
# @param context The serialization streaming context
    def __init__(self, info, context): 
        super(info, context)
