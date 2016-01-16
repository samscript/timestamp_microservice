This my solution for Timestamp Microservice.

I elected to use python 2.7 with 2 available 3rd party libraries:
    -dateparser
        it deals with natural language date entries
    -bottle
        it deals with web API service
        
        
Examples: https://timestamp-microservice-samscript.c9users.io/datetime/86400
        Response:  {"unix": "86400", "natural": "January 2, 1970"}