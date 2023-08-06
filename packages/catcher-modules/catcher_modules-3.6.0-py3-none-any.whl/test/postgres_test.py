from os.path import join

import psycopg2
from catcher.core.runner import Runner

from test.abs_test_class import TestClass


class PostgresTest(TestClass):
    def __init__(self, method_name):
        super().__init__('postgres', method_name)

    @property
    def conf(self):
        return "dbname=test user=test host=localhost password=test port=5433"

    @property
    def connection(self):
        return psycopg2.connect(self.conf)

    def setUp(self):
        super().setUp()
        with self.connection as conn:
            cur = conn.cursor()
            cur.execute("CREATE TABLE test (id serial PRIMARY KEY, num integer);")
            cur.execute("insert into test(id, num) values(1, 1);")
            cur.execute("insert into test(id, num) values(2, 2);")
            conn.commit()
            cur.close()

    def tearDown(self):
        super().tearDown()
        with self.connection as conn:
            cur = conn.cursor()
            cur.execute("DROP TABLE test;")
            conn.commit()
            cur.close()

    def test_read_simple_query(self):
        self.populate_file('test_inventory.yml', '''
        postgres:
            dbname: test
            user: test
            password: test
            host: localhost
            port: 5433
        ''')

        self.populate_file('main.yaml', '''---
            steps:
                - postgres:
                    request:
                        conf: '{{ postgres }}'
                        query: 'select count(*) from test'
                    register: {documents: '{{ OUTPUT }}'}
                - check:
                    equals: {the: '{{ documents }}', is: 2}
            ''')
        runner = Runner(self.test_dir, join(self.test_dir, 'main.yaml'), join(self.test_dir, 'test_inventory.yml'))
        self.assertTrue(runner.run_tests())

    def test_str_conf(self):
        self.populate_file('test_inventory.yml', '''
        postgres: 'test:test@localhost:5433/test'
        ''')

        self.populate_file('main.yaml', '''---
                steps:
                    - postgres:
                        request:
                            conf: '{{ postgres }}'
                            query: 'select count(*) from test'
                        register: {documents: '{{ OUTPUT }}'}
                    - check:
                        equals: {the: '{{ documents }}', is: 2}
                ''')
        runner = Runner(self.test_dir, join(self.test_dir, 'main.yaml'), join(self.test_dir, 'test_inventory.yml'))
        self.assertTrue(runner.run_tests())

    def test_write_simple_query(self):
        self.populate_file('main.yaml', '''---
                steps:
                    - postgres:
                        request:
                            conf: 'test:test@localhost:5433/test'
                            query: 'insert into test(id, num) values(3, 3);'
                ''')
        runner = Runner(self.test_dir, join(self.test_dir, 'main.yaml'), None)
        self.assertTrue(runner.run_tests())
        response = self.get_values('test')
        self.assertEqual([(1, 1), (2, 2), (3, 3)], response)

    def test_read_with_variables(self):
        self.populate_file('main.yaml', '''---
                variables:
                    pg_conf: 'test:test@localhost:5433/test'
                steps:
                   - echo: {from: '{{ RANDOM_INT }}', register: {num: '{{ OUTPUT }}'}} 
                   - echo: {from: '{{ RANDOM_INT }}', register: {id: '{{ OUTPUT }}'}} 
                   - postgres:
                        actions: 
                            - request:
                                conf: '{{ pg_conf }}'
                                query: 'insert into test(id, num) values({{ id }}, {{ num }});'
                            - request:
                                conf: '{{ pg_conf }}'
                                query: select * from test where id={{ id }}
                              register: {document: '{{ OUTPUT }}'}
                   - check: 
                        equals: {the: '{{ document[1] }}', is: '{{ num }}'} 
                ''')
        runner = Runner(self.test_dir, join(self.test_dir, 'main.yaml'), None)
        self.assertTrue(runner.run_tests())
