from abc import ABC, abstractmethod
import typing as tg


class QueryRunner(ABC):
    db: str = ""

    @abstractmethod
    def get_number(self, configuration: tg.Dict) -> tg.Union[int, float]:
        """Returns an integer or a float. Note that if this function was actually
        implemented, the number would be the return value of the database cal. However
        in this case, we simply return an integer for one DAO."""
        pass


class MongoDbQueryRunner(QueryRunner):
    db: str = "mongodb"

    def get_number(self, configuration: tg.Dict) -> tg.Union[int, float]:
        return 1


class BigQueryQueryRunner(QueryRunner):
    db: str = "bigquery"

    def get_number(self, configuration: tg.Dict) -> tg.Union[int, float]:
        return 2


class MySqlQueryRunner(QueryRunner):
    db: str = "mysql"

    def get_number(self, configuration: tg.Dict) -> tg.Union[int, float]:
        return 3


class AbstractFactory(ABC):
    def get_dao(self, database: str) -> tg.Optional[QueryRunner]:
        """Returns a QueryRunner instance"""
        factories: tg.List[tg.Type[QueryRunner]] = QueryRunner.__subclasses__()
        for factory in factories:
            if factory.db == database:
                return factory()  # type: ignore

        print(f"{database} query runner not implemented yet.")
        return None
