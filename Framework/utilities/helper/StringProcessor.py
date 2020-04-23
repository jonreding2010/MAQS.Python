class StringProcessor:
# Creates a string based on the arguments. If no args are applied, then we want to just return the message
# @param message The message being used
# @param args    The arguments being used
# @return A final string
  def safe_formatter(self, message, args):
    try: 
      return ''.join(message, args);
    except Exception:
        str_list = []
        str_list.append("Message: " + message)
        str_list.append("");
        str_list.append(" Arguments: ");
              
        argument_list = []
        for arg in args:
             argument_list.append(arg.toString() + " ")
             
        str_list.append(argument_list.join) 
    return ''.join(str_list)
  
# Gets a string of a nested exception list
# @param e Exception to print as string</param>
# return A string of the Exceptions with stack trace</returns>

  def safe_exception_formatter(self, e):
      sb = []
      return get_exception(e, sb)

# Recursive function to grab the inner exceptions
# @param ex Exception to look into</param>
# @param sb String builder to build the string</param>
# @param level Recursive level for spacing of logs</param>
# return A string with the exceptions</returns>
  def get_exception(self, ex, sb, level = 0):
        return " "
        '''
      spaces = new string(' ', level);
      sb.Append($"{Environment.NewLine}{spaces}{ex.Message}{(ex.StackTrace == null ? "" : $"{Environment.NewLine}{spaces}{ex.StackTrace}")}");
      if (ex is AggregateException && (ex as AggregateException).InnerExceptions.Count > 0)
        for var exception in (ex as AggregateException).InnerExceptions)
          {
              GetException(exception, sb, level + 1);
          }
      }
      else if (ex.InnerException != ""):
          GetException(ex.InnerException, sb, level + 2)

      return sb.ToString();
      '''