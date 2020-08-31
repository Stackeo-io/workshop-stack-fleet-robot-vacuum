import unittest

from app.api.graphql_engine import GraphqlEngine


class TestGraphqlEngine(unittest.TestCase):
    def setUp(self):
        self._tested = GraphqlEngine()

    def test_schema_should_not_raise_error(self):
        # As the code is using `gql()` method, it will
        # raise an exception if the schema is not valid
        #
        # this test is an easy way to validate our
        # graphql schema on continuous integration
        self._tested.schema()

if __name__ == '__main__':
    unittest.main()
