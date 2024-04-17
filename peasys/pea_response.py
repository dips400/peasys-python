class PeaResponse:
    '''
    Implements the concept of response in the case of a query executed on the database 
    of an AS/400 server by a object. PeaResponse is general and should be use when none other subclasses apply.
    '''

    def __init__(self, has_succeeded, sql_message, sql_state) -> None:
        '''
        Initialize a new instance of the PeaResponse class.
        
        Args
        ------
            has_succeeded (bool):
                Boolean set to true if the query has correctly been executed.
            sql_message (str):
                SQL message return from the execution of the query.
            sql_state (str):
                SQL state return from the execution of the query.
        '''
        self._has_succeeded = has_succeeded
        self._sql_message = sql_message
        self._sql_state = sql_state

    @property
    def has_succeeded(self) -> bool:
        '''
        Boolean set to true if the query has correctly been executed.
        '''
        return self._has_succeeded
    
    @property
    def sql_message(self) -> str:
        '''
        SQL message return from the execution of the query.
        '''
        return self._sql_message
    
    @property
    def sql_state(self) -> str:
        '''
        SQL state return from the execution of the query.
        '''
        return self._sql_state

class PeaCreateResponse(PeaResponse):
    '''
    Implements the concept of response in the case of a CREATE SQL query executed on the database 
    of an AS/400 server by a object.
    '''

    def __init__(self, has_succeeded, sql_message, sql_state, database_name, index_name, table_schema) -> None:
        '''
        Initialize a new instance of the PeaCreateResponse class.
        
        Args
        -----
            has_succeeded (bool):
                Boolean set to true if the query has correctly been executed.
            sql_message (str):
                SQL message return from the execution of the query.
            sql_state (str):
                SQL state return from the execution of the query.
            database_name (str):
                Name of the database if the SQL create query creates a new database.
            index_name (str):
                Name of the index if the SQL create query creates a new index.
            table_schema (dict):
                Schema of the table if the SQL create query creates a new table.
        '''
        super().__init__(has_succeeded, sql_message, sql_state)

        self._database_name = database_name
        self._index_name = index_name
        self._table_schema = table_schema

    @property
    def database_name(self) -> str:
        '''
        Name of the database if the SQL create query creates a new database.
        '''
        return self._database_name
    
    @property
    def index_name(self) -> str:
        '''
        Name of the index if the SQL create query creates a new index.
        '''
        return self._index_name
    
    @property
    def table_schema(self) -> None:
        '''
        Schema of the table if the SQL create query creates a new table.
        '''
        return self._table_schema

class PeaAlterResponse(PeaResponse):
    '''
    Implements the concept of response in the case of a ALTER SQL query executed on the database 
    of an AS/400 server by a object.
    '''

    def __init__(self, has_succeeded, sql_message, sql_state, table_schema) -> None:
        '''
        Initialize a new instance of the PeaAlterResponse class.
        
        Args
        -----
            has_succeeded (bool):
                Boolean set to true if the query has correctly been executed.
            sql_message (str):
                SQL message return from the execution of the query.
            sql_state (str):
                SQL state return from the execution of the query.
            database_name (str):
                Name of the database if the SQL create query creates a new database.
            index_name (str):
                Name of the index if the SQL create query creates a new index.
            table_schema (dict):
                Schema of the table if the SQL create query creates a new table.
        '''
        super().__init__(has_succeeded, sql_message, sql_state)

        self._table_schema = table_schema

    @property
    def table_schema(self) -> None:
        '''
        Schema of the table if the SQL create query creates a new table.
        '''
        return self._table_schema

class PeaDropResponse(PeaResponse):
    '''
    Implements the concept of response in the case of a DROP SQL query executed on the database 
    of an AS/400 server by a object.
    '''

    def __init__(self, has_succeeded, sql_message, sql_state) -> None:
        '''
        Initialize a new instance of the PeaDropResponse class.
        
        Args
        -----
            has_succeeded (bool):
                Boolean set to true if the query has correctly been executed.
            sql_message (str):
                SQL message return from the execution of the query.
            sql_state (str):
                SQL state return from the execution of the query.
        '''
        super().__init__(has_succeeded, sql_message, sql_state)

class PeaSelectResponse(PeaResponse):
    '''
    Implements the concept of response in the case of a SELECT SQL query executed on the database 
    of an AS/400 server by a object.
    '''

    def __init__(self, has_succeeded, sql_message, sql_state, result, row_count, columns_name) -> None:
        '''
        Initialize a new instance of the PeaSelectResponse class.
        
        Args
        -----
            has_succeeded (bool):
                Boolean set to true if the query has correctly been executed.
            sql_message (str):
                SQL message return from the execution of the query.
            sql_state (str):
                SQL state return from the execution of the query.
            result (dict):
                Results of the query in the form of an Dictionary where the columns' name are the key and 
                the values are the elements of this column in the SQL table.
            row_count (int):
                Represents the number of rows that have been retreived by the query.
            columns_name (list):
                List representing the name of the columns in the order of the SELECT query.
        '''
        super().__init__(has_succeeded, sql_message, sql_state)

        self._result = result
        self._row_count = row_count
        self._columns_name = columns_name

    @property
    def result(self) -> dict:
        '''
        Results of the query in the form of an Dictionary where the columns' name are the key and 
                the values are the elements of this column in the SQL table.
        '''
        return self._result
    
    @property
    def row_count(self) -> int:
        '''
        Represents the number of rows that have been retreived by the query.
        '''
        return self._row_count
    
    @property
    def columns_name(self) -> list:
        '''
        List representing the name of the columns in the order of the SELECT query.
        '''
        return self._columns_name

class PeaUpdateResponse(PeaResponse):
    '''
    Implements the concept of response in the case of a UPDATE SQL query executed on the database 
    of an AS/400 server by a object.
    '''

    def __init__(self, has_succeeded, sql_message, sql_state, row_count) -> None:
        '''
        Initialize a new instance of the PeaUpdateResponse class.
        
        Args
        -----
            has_succeeded (bool):
                Boolean set to true if the query has correctly been executed.
            sql_message (str):
                SQL message return from the execution of the query.
            sql_state (str):
                SQL state return from the execution of the query.
            row_count (int):
                Represents the number of rows that have been retreived by the query.
        '''
        super().__init__(has_succeeded, sql_message, sql_state)

        self._row_count = row_count

    @property
    def row_count(self) -> int:
        '''
        Represents the number of rows that have been retreived by the query.
        '''
        return self._row_count

class PeaDeleteResponse(PeaResponse):
    '''
    Implements the concept of response in the case of a DELETE SQL query executed on the database 
    of an AS/400 server by a object.
    '''

    def __init__(self, has_succeeded, sql_message, sql_state, row_count) -> None:
        '''
        Initialize a new instance of the PeaDeleteResponse class.
        
        Args
        -----
            has_succeeded (bool):
                Boolean set to true if the query has correctly been executed.
            sql_message (str):
                SQL message return from the execution of the query.
            sql_state (str):
                SQL state return from the execution of the query.
            row_count (int):
                Represents the number of rows that have been retreived by the query.
        '''
        super().__init__(has_succeeded, sql_message, sql_state)

        self._row_count = row_count

    @property
    def row_count(self) -> int:
        '''
        Represents the number of rows that have been retreived by the query.
        '''
        return self._row_count

class PeaInsertResponse(PeaResponse):
    '''
    Implements the concept of response in the case of a INSERT SQL query executed on the database 
    of an AS/400 server by a object.
    '''

    def __init__(self, has_succeeded, sql_message, sql_state, row_count) -> None:
        '''
        Initialize a new instance of the PeaInsertResponse class.
        
        Args
        -----
            has_succeeded (bool):
                Boolean set to true if the query has correctly been executed.
            sql_message (str):
                SQL message return from the execution of the query.
            sql_state (str):
                SQL state return from the execution of the query.
            row_count (int):
                Represents the number of rows that have been retreived by the query.
        '''
        super().__init__(has_succeeded, sql_message, sql_state)

        self._row_count = row_count

    @property
    def row_count(self) -> int:
        '''
        Represents the number of rows that have been retreived by the query.
        '''
        return self._row_count

class PeaCommandResponse:
    '''
        Represents the concept of response in the case of an OS/400 command executed on the database of an AS/400 server by a PeaClient object.
    '''
    
    def __init__(self, has_succeeded, warnings) -> None:
        '''
        Initialize a new instance of the PeaCommandResponse class.
            
        Args
        -----
            has_succeeded (bool):
                Boolean set to true if the command has correctly been executed meaning that no CPFxxxx was return. Still, description messages 
                    can be return along with CP*xxxx.
            warnings (list of string):
                List of warnings that results form the command execution. Errors are of the form : CP*xxxx Description of the warning.
        '''
        self._has_succeeded = has_succeeded
        self._warnings = warnings
        
    @property
    def has_succeeded(self) -> bool:
        '''
        Boolean set to true if the command has correctly been executed meaning that no CPFxxxx was return.
        '''
        return self._has_succeeded
    
    @property
    def warnings(self) -> list:
        '''
        List of warnings that results form the command execution. Errors are of the form : CP*xxxx Description of the warning.
        '''
        return self._warnings
       
 
class ColumnInfo:
    '''
        ColumnInfo is used to represent the informations about one column in the table in case the user want to retrieve the table's schema.
    '''
    
    def __init__(self, column_name, ordinal_position, data_type, length, numeric_scale, is_nullable, is_updatable, numeric_precision) -> None:
        '''
        Initialize a new instance of ColumnInfo class.
            
        Args
        -----
            column_name (str):
                Name of the column.
            ordinal_position (int):
                Ordinal position of the column.
            data_type (str):
                Type of data accepted by the column.
            length (int):
                Length of the data.
            numeric_scale (int):
                Numeric scale if data is of type numeric.
            is_nullable (bool):
                True is the field is nullable.
            is_updatable (bool):
                True is the field is updatable.
            numeric_precision (int):
                Numeric precision if data s=is of type numeric.
        '''
        self._column_name = column_name
        self._ordinal_position = ordinal_position
        self._data_type = data_type
        self._length = length
        self._numeric_scale = numeric_scale
        self._is_nullable = is_nullable
        self._is_updatable = is_updatable
        self._numeric_precision = numeric_precision

    @property
    def column_name(self) -> str:
        '''
        Name of the column.
        '''
        return self._column_name
    
    @property
    def ordinal_position(self) -> int:
        '''
        Ordinal position of the column.
        '''
        return self._ordinal_position
    
    @property
    def data_type(self) -> str:
        '''
        Type of data accepted by the column.
        '''
        return self._data_type
    
    @property
    def length(self) -> int:
        '''
        Length of the data.
        '''
        return self._length
    
    @property
    def numeric_scale(self) -> int:
        '''
        Numeric scale if data is of type numeric.
        '''
        return self._numeric_scale
    
    @property
    def is_nullable(self) -> bool:
        '''
        True is the field is nullable.
        '''
        return self._is_nullable
    
    @property
    def is_updatable(self) -> bool:
        '''
        True is the field is updatable.
        '''
        return self._is_updatable
    
    @property
    def numeric_precision(self) -> int:
        '''
        Numeric precision if data s=is of type numeric.
        '''
        return self._numeric_precision
