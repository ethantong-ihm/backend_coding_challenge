import json
import csv
import psycopg2
from psycopg2 import Error

def lambda_handler(event, context):
    try:
        connection = psycopg2.connect(user="docker",
                                    password="docker",
                                    host="host.docker.internal",
                                    port="5432",
                                    database="SongData")

        cursor = connection.cursor()
        print(connection.get_dsn_parameters(), "\n")

        with open('song_data.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            
            next(csv_reader)
            for row in csv_reader:
                insert_query = f""" INSERT INTO song_data (artist_name, song_title, non_overnight_replays, station_replays, 
                                                        market_replays, breakout_name, breakout_metric1, breakout_metric2,
                                                        breakout_metric3, breakout_metric4, breakout_metric5, breakout_metric6,
                                                        breakout_metric7, breakout_metric8, breakout_metric9) 
                                                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                                                        ON CONFLICT DO NOTHING
                                                        """
                                              
                cursor.execute(insert_query, tuple(row))
                connection.commit()
        
    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)

    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Function run successful",
            # "location": ip.text.replace("\n", "")
        }),
    }
