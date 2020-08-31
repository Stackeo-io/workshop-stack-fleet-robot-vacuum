import io
import os

from ariadne import make_executable_schema, gql
from graphql import GraphQLSchema

from app.api.type_resolver.query import query


class GraphqlEngine:

    def __init__(self):
        self.types = []
        self.registry_types()

    def schema(self) -> GraphQLSchema:
        types = self.types
        return make_executable_schema(self._load_schema(), types)

    def registry_types(self):
        self.types.append(query)

    def _load_schema(self) -> str:
        script_directory_path = os.path.dirname(os.path.realpath(__file__))
        schema_path = os.path.join(script_directory_path, "schema", "main.graphql")
        with io.open(schema_path) as file_pointer:
            schema_content = gql(file_pointer.read())

        return schema_content
