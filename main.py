from global_connection import connection
from fastmcp import FastMCP
import ast

mcp = FastMCP("MySQL Operations")

@mcp.tool()
def select(table_name, columns="*", where_clause=None, where_values=None):
    """
    Dynamically fetch records from any MySQL table.

    Args:
        table_name (str): The name of the table to query.
        columns (str or list): Columns to select (default "*"). Use list for multiple.
        where_clause (str, optional): WHERE clause to filter rows (e.g., "id = %s").
        where_values (list, optional): Values to bind in the WHERE clause.

    Returns:
        list[tuple]: List of rows fetched from the table.
        str: Error message if the operation fails.
    """
    if not connection:
        return "No database connection."

    try:
        cursor = connection.cursor()
        column_str = ", ".join(columns) if isinstance(columns, list) else columns

        query = f"SELECT {column_str} FROM {table_name}"
        if where_clause:
            query += f" WHERE {where_clause}"

        cursor.execute(query, where_values or [])
        rows = cursor.fetchall()
        return rows
    except Exception as e:
        return f"Error during select: {e}"


@mcp.tool()
def insert(table_name, column_names, values):
    """
    Insert data dynamically into any specified table in a MySQL database.

    Args:
        table_name (str): The name of the table where the data will be inserted.
        column_names (list[str]): A list of column names corresponding to the values.
        values (list[Any]): A list of values to insert, matching the order of column_names.

    Returns:
        None. Prints a success message if the insert is successful, or an error message if it fails.
    """
    if not connection:
        return "No database connection."

    try:

        # Convert string to list if necessary
        if isinstance(column_names, str):
            column_names = ast.literal_eval(column_names)
        if isinstance(values, str):
            values = ast.literal_eval(values)

        cursor = connection.cursor()

        # Dynamically construct SQL query
        columns = ", ".join(column_names)
        placeholders = ", ".join(["%s"] * len(values))

        query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"

        # Execute
        cursor.execute(query, values)
        connection.commit()

        return f"Inserted into `{table_name}` successfully."
    except Exception as e:
        return f"Error during insert: {e}"


@mcp.tool()
def update(table_name, update_data, where_clause, where_values):
    """
    Dynamically update records in any MySQL table.

    Args:
        table_name (str): The name of the table to update.
        update_data (dict): Dictionary of columns to update with their new values.
        where_clause (str): The WHERE clause to filter which rows to update (e.g., "id = %s").
        where_values (list): Values to bind in the WHERE clause.

    Returns:
        str: Success or error message.
    """
    if not connection:
        return "No database connection."

    try:

        # Convert string to list if necessary
        if isinstance(where_values, str):
            where_values = ast.literal_eval(where_values)


        cursor = connection.cursor()

        set_clause = ", ".join([f"{col} = %s" for col in update_data.keys()])
        query = f"UPDATE {table_name} SET {set_clause} WHERE {where_clause}"

        values = list(update_data.values()) + where_values

        cursor.execute(query, values)
        connection.commit()

        return f"Updated rows in `{table_name}` successfully."
    except Exception as e:
        return f"Error during update: {e}"


@mcp.tool()
def delete(table_name, where_clause, where_values):
    """
    Dynamically delete records from any MySQL table.

    Args:
        table_name (str): The name of the table from which to delete.
        where_clause (str): The WHERE clause to filter which rows to delete (e.g., "id = %s").
        where_values (list): Values to bind in the WHERE clause.

    Returns:
        str: Success or error message.
    """
    if not connection:
        return "No database connection."

    try:
        # Convert string to list if necessary
        if isinstance(where_values, str):
            where_values = ast.literal_eval(where_values)

        cursor = connection.cursor()
        query = f"DELETE FROM {table_name} WHERE {where_clause}"

        cursor.execute(query, where_values)
        connection.commit()

        return f"Deleted rows from `{table_name}` successfully."
    except Exception as e:
        return f"Error during delete: {e}"


@mcp.tool()
def get_all_table_names():
    """
    Retrieve a list of all table names from the connected MySQL database.

    Returns:
        list[str]: A list containing the names of all tables in the database.
        str: An error message if the operation fails or if there's no database connection.
    """
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("SHOW TABLES")
            tables = cursor.fetchall()
            return [table[0] for table in tables]
        except Exception as e:
            return f"Error fetching table names: {e}"

@mcp.tool()     
def get_column_names(table_name):
    """
    Retrieve the column names and their details for a specified table.

    Args:
        table_name (str): The name of the table to describe.

    Returns:
        list[str]: A list containing the names of all columns in the specified table.
        str: An error message if the operation fails or if there's no database connection.
    """
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute(f"DESCRIBE {table_name}")
            columns = cursor.fetchall()
            return [column[0] for column in columns]
        except Exception as e:
            return f"Error describing table '{table_name}':", e



# print (get_all_table_names())