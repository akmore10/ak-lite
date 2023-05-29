from Frontend.Types.Statement import Statement,StatementTypes
from FrontendErrorHandling.CommandExceptions import CommandNotFound

class PrepareStatement:
    def __init__(self):
        self.statement = Statement()
    def prepare_statement(self , statement):
        if statement == "insert":
            self.statement.setType(StatementTypes.STATEMENT_INSERT)
            return self.statement
        if statement == "select":
            self.statement.setType(StatementTypes.STATEMENT_SELECT)
            return self.statement
        raise CommandNotFound("The command is not available in this version.")