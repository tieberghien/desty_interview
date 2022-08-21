from abstract_factory import AbstractFactory

# the user selected these values in webpage
query_runner_name = "bigquery"
query_options = {
    "sql_statemant": "select count(*) as the_number from `orders`",
    "return_value": "the_number",
}

# then the application van use this code to query for a number
factory = AbstractFactory()
query_runner = factory.get_dao(query_runner_name)

result = query_runner.get_number(query_options)

# the value of result would then be 2
assert result == 2

query_runner_name = "mysql"
query_runner = factory.get_dao(query_runner_name)
result = query_runner.get_number(query_options)

assert result == 3

query_runner_name = "notimplemented"
query_runner = factory.get_dao(query_runner_name)
