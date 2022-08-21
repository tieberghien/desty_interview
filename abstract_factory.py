from abc import ABC, abstractmethod
import typing as tg

class QueryRunner(ABC):
    @abstractmethod
    def get_number(self, configuration: tg.Dict) -> tg.Union[int, float]:
        """Returns an integer or a float. Note that if this function was actually 
        implemented, the number would be the return value of the database cal. However
        in this case, we simply return an integer for one DAO."""
        pass


class MongoDbQueryRunner(QueryRunner):
    def get_number(self, configuration: tg.Dict) -> tg.Union[int, float]:
        return 1


class BigQueryQueryRunner(QueryRunner):
    def get_number(self, configuration: tg.Dict) -> tg.Union[int, float]:
        return 2


class MySqlQueryRunner(QueryRunner):
    def get_number(self, configuration: tg.Dict) -> tg.Union[int, float]:
        return 3


class AbstractFactory(ABC):
    def get_dao(self, database: str) -> tg.Optional[QueryRunner]:
        """Returns a QueryRunner instance"""
        factories = {
            "mongodb": MongoDbQueryRunner(),
            "bigquery": BigQueryQueryRunner(),
            "mysql": MySqlQueryRunner(),
        }

        try:
            factory = factories[database]
        except KeyError:
            print(f"{database} query runner not implemented yet.")
            return

        return factory
        