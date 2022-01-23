#!/usr/bin/python
import psycopg2
import os

class sqlconnector:
    def connect(sql):
        """ Connect to the PostgreSQL database server """
        conn = None
        try:
            # connect to the PostgreSQL server
            print('Connecting to the PostgreSQL database...')
            conn = psycopg2.connect("postgresql://ari:QBZ4q2HGlKraftg3kTt62g@free-tier14.aws-us-east-1.cockroachlabs.cloud:26257/defaultdb?sslmode=verify-full&options=--cluster%3Dcheery-moth-36")
            # create a cursor
            cur = conn.cursor()

            # execute a statement
            cur.execute(sql)
            rows = cur.fetchall()
            conn.commit()

        # close the communication with the PostgreSQL
            cur.close()
            return rows
        finally:
            if conn is not None:
                conn.close()
                print('Database connection closed.')
