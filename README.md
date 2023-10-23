# Rest-API-SQL
Design and implement an API to load csv files into a SQL using chunks and this information must be retrieved for other APIs and grouped by certain criteria.

## Requirements
Python 3.5.2+

## Running in local
To run the server, please execute the following from the root directory:

```bash
# install libraries
pip3 install -r requirements.txt

# run app
python3 main.py
```
and open your browser to here:

```
http://127.0.0.1:9091/apidocs/
```
First run the route POST `\load-data` to populate the tables

## Running with Docker

To run the server on a Docker container, please execute the following from the root directory:

```bash
# building the image
docker build -t api_trips .

# starting up a container
docker run -p 9091:9091 api_trips
```
and open your browser to here:

```
http://127.0.0.1:9091/apidocs/
```
First run the route POST `\load-data` to populate the tables.

## Structure Folder
```
├───api
│   └───controllers     -> routes for the api with their logics
├───database            -> fucntions for model and database
├───csv_files           -> files input
├───swagger_ui          -> json file Swagger desing
├───database.db         -> database created
├───Dockerfile          -> configurations for dockerfile
├───requirements.txt    -> libreries used
└───main.py             -> run app
```