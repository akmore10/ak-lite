from enum import Enum
from typing import Any

class StatementTypes(Enum):
    STATEMENT_INSERT = "insert"
    STATEMENT_SELECT = "select"

    def getValues(self):
        return self.value
    
class Statement:
    def __init__(self):
        self.type = None
    def setType(self,statementType : StatementTypes):
        self.type = statementType

