# sam-with-postgres

## Getting Started

### Prerequisits
In order to run this container docker will need to be installed

Windows : https://docs.docker.com/desktop/install/windows-install/
Linux : https://docs.docker.com/desktop/install/linux-install/

Python3.9 : https://www.python.org/downloads/release/python-390/

SAM CLI : https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install-windows.html


### Instructions
1. Go to  `Song-Data` directory
2. In the terminal run `docker compose up` to create the postgres database and song_data table
3. Run `sam build` to build the project
3. Run `sam local invoke ProcessSongData` to fill the postgres table
4. Run `sam local start-api` to start the api gateway


#### Notes 
To make it easier to authenticate I hardcoded the username and password. If this was a real project I would leverage AWS Secrets Manager to retrieve creds

