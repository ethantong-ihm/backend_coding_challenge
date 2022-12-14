 # iHeartMedia - Music Lab - Data Code Challenge

## Data Processing
Create an AWS Lambda Function named `ProcessSongData` to process data from a CSV file and write it to a local Postgres container.
1. Use AWS SAM YAML template to create and run the lambda function locally.
    - [SAM overview](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/what-is-sam.html)
    - [Create a lambda function from SAM template](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-resource-function.html)
    - [SAM CLI commands](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-command-reference.html)
    - [invoke local lambda with SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-cli-command-reference-sam-local-invoke.html)
2. Write this function using Python 3.9 or Node 14.
3. Use [this DockerHub image](https://hub.docker.com/_/postgres) to run Postgres container.
4. `song_data.csv` can be stored anywhere as long as it can be accessed by the reviewers when they run your code.
5. Understand the structure of `song_data.csv` and come up with a relational database design.
6. Write the data to Postgres (you can use any database adapter library). This writing process should be idempotent. If the lambda is invoked multiple times with the same same csv input, the output should also be the same.
7. Write documentation in `README.md` on your design decisions and instructions on how to run your code.

## API
Build an AWS API Gateway with lambda integration to query from the local Postgres and return a JSON response.
1. Use AWS SAM YAML template to create and run the API Gateway with lambda function locally.
    - [Create API Gateway + Lambda from SAM template](https://docs.aws.amazon.com/lambda/latest/dg/services-apigateway-template.html)
    - [Run local API Gateway with SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-cli-command-reference-sam-local-start-api.html)

2. Write these functions using Python 3.9 or Node 14.
3. Write a lambda named `GetQualifiedSongs`:
    - Return a distinct list of songs that have `BreakoutName = m` and `BreakoutMetric1 > n` (*m* and *n* are variables)
    - Path: `get-qualified-songs`.
    - Method: `Post`.
    - The request body should contain `BreakoutName` and `BreakoutMetric1` parameters.
    - The response body should contain `SongTitle`, `Artist`, `BreakoutName`, and `BreakoutMetric1`.
4. Write instructions on how to run your code. Other types of documentation are not required for this API.
5. Feel free to extend this with TypeScript, GraphQL, or unit test cases but this is completely optional.

## Important Requirement Notes:
- **Reviewers will run your code based on your instructions.**
- **Code quality, performance, and documentation matter.**