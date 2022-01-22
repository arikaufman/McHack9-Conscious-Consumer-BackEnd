#!/usr/bin/python
import psycopg2
import os

def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(os.environ['postgresql://ari:QBZ4q2HGlKraftg3kTt62g@free-tier14.aws-us-east-1.cockroachlabs.cloud:26257/defaultdb?sslmode=verify-full&options=--cluster%3Dcheery-moth-36'])
        # create a cursor
        cur = conn.cursor()

	    # execute a statement
        cur.execute("SELECT * FROM companies")
        rows = cur.fetchall()
        conn.commit()
        for row in rows:
            print(row)

	# close the communication with the PostgreSQL
        cur.close()
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


if __name__ == '__main__':
    connect()

