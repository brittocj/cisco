### A basic HTTP web application using Python Django DRF web framework.

- Following endpoints are available:
 - ping 
    method: POST
Accepts a body containing a url key and corresponding link, ie {‘url’: ‘ https://www.foobar.com‘}; This route should send a GET request to that endpoint, ignoring SSL for simplicity, and return the payload of that request as the response for the route.
 -  info
    method: GET 
Returns hardcoded status of {“Receiver”: “Cisco is the best!”}
  - apidoc
  method GET
  Returns API documentation on Swagger.

##### Clone the repo and follow the below instructions to run the web application: 
 - Use pipenv to install requiremnts for the Python Django web application.
 - And run the application in pipenv shell from basic_http directory.
 - Use ./manage.py runserver
 
- Demo available at: http://www.simplysmile.in/cisco/
