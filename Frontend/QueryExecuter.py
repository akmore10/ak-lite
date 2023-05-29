from ErrorHandling.CommandExceptions import CommandNotFound
from Frontend.QueryBuild import PrepareStatement
from Frontend.Types.Statement import StatementTypes

class QueryExecuter:
    @staticmethod
    def execute(command , local_vars):
        prepareObj = PrepareStatement()
        try:
            result = prepareObj.prepare_statement(command)
            if result.type == StatementTypes.STATEMENT_INSERT:
                print("Inside the Insert")
            if result.type == StatementTypes.STATEMENT_SELECT:
                print("Inside the Select")
        except CommandNotFound as e:
            print(e.message)