import json
import psycopg2
from psycopg2 import Error
import psycopg2.extras

def lambda_handler(event, context):
    try:
        connection = psycopg2.connect(user="docker",
                                    password="docker",
                                    host="host.docker.internal",
                                    port="5432",
                                    database="SongData")

        #cursor = connection.cursor()
        cursor = connection.cursor(cursor_factory = psycopg2.extras.RealDictCursor)
        print(connection.get_dsn_parameters(), "\n")
        
        select_query = f"""SELECT song_title, artist_name, breakout_name, breakout_metric1 FROM song_data WHERE breakout_name = %s 
                          AND breakout_metric1 > %s"""
               
        cursor.execute(select_query, (event["m"], event["n"]))
        songs = cursor.fetchall()

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
            "songs" : json.dumps(songs)
        }),
    }

    
    

