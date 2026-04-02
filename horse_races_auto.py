import mysql.connector
import random
import time
import logging

# Configure logging
logging.basicConfig(filename='horse_races.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Database connection details
DB_HOST = 'sql109.infinityfree.com'
DB_USER = 'if0_41280387'
DB_PASSWORD = 'eEQsb29X6JmYla'
DB_NAME = 'if0_41280387_dgb_infinity'

try:
    connection = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )
    cursor = connection.cursor()

    while True:
        start_time = time.strftime('%Y-%m-%d %H:%M:%S')
        end_time = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(time.time() + 20))
        winning_horse = random.choice(['red', 'blue'])

        # Insert a new horse race record
        race_query = "INSERT INTO horse_races (start_time, end_time, winning_horse) VALUES (%s, %s, %s)"
        race_data = (start_time, end_time, winning_horse)
        cursor.execute(race_query, race_data)
        connection.commit()
        logging.info(f'Race created: start_time={start_time}, end_time={end_time}, winning_horse={winning_horse}')
        time.sleep(random.randint(20, 30))  # Wait for a random period between 20 and 30 seconds

except mysql.connector.Error as e:
    logging.error(f'Error connecting to MySQL Platform: {e}')

finally:
    if connection:
        cursor.close()
        connection.close()  
