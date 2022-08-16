 # iHeartMedia - Music Lab - Data Code Challenge

## Data Processing
Create an AWS Lambda Function named `ProcessSongData` to process data from a CSV file and write it to a local Postgres container.
1. Use AWS SAM YAML template to create and run the lambda function locally.
    - https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-resource-function.html
    - https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/what-is-sam.html
2. Write this function in Python 3.9
3. Use [this DockerHub image](https://hub.docker.com/_/postgres) to run Postgres container.
4. `song_data.csv` can be stored anywhere as long as it can be accesssed by the reviewers when they run your Python code.
5. Come up with a table design to store `song_data.csv` and write it to Postgres (you can use `psycopg2` or any database adapter library you'd like).
6. Write documentation in `README.md` on your design decisions and instructions on how to run your code. 

## API
Build an AWS API Gateway with lambda integration to query  from the local Postgres and return JSON responses.
1. Use AWS SAM YAML template to create the 2 lambda functions.
    - https://docs.aws.amazon.com/lambda/latest/dg/services-apigateway-tutorial.html
    - https://docs.aws.amazon.com/lambda/latest/dg/services-apigateway-template.html
2. Write these functions in JavaScript using Node 14.
3.  Write a lambda named `GetAllSongTitles`:
    - Return an unordered and distinct list of song titles from DB
    - Path `/get-all-song-Titles`
    - Method `Get`
    - Your response object should look like
        ```JSON
        {
            "SongTitles": ["Shape Of You", "Bad Habits", ...] 
        }
        ```
4. Write a lambda named `GetQualifiedSongs`:
    - Return a distinct list of songs that have `BreakoutName = m` and `POP > n` (*m* and *n* are arguments/params/variables)
    -  Path `get-qualified-songs`
    - Method `Post` with a request body that looks like:
        ```JSON
            {
                "BreakOutName": "Total"
                "PopGreaterThan": 70
            }
        ```
    - Your response object should look like
        ```JSON
            {
                "Songs": [
                    {
                        "SongTitle": "Shape Of You",
                        "Artist": "SHEERAN ED",
                        "BreakoutName": "Total",
                        "POP": 70
                    },
                    ...
                ]
            }
        ```

5. Write instructions on how to run your code. Other types of documentation are not required for this API.

## Important Requirement Notes:
- **Reviewers will run your code based on your instructions.**
- **Code quality, performance, and documentation matter.**