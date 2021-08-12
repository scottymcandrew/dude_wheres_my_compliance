# Dude, where's my Prisma Cloud Compliance?

This application is designed to *drive over to Prisma Cloud to obtain the latest and greatest of compliance coverage.

# *REMEMBER* to generate a self-signed certificate (or better yet, a _real_ one) e.g.

`openssl req -x509 -newkey rsa:4096 -nodes -subj "/C=UK/ST=Scotland/L=Edinburgh/O=IT/CN=myhost.example.com" -out cert.pem -keyout key.pem -days 365`

Also, set your environment variables, because of course, I wasn't silly enough to hard-code them ;-) e.g.

`export PC_KEY='blah'`
`export PC_SECRET='blahblah'`

[Include your API endpoint]
(https://prisma.pan.dev/api/cloud/api-urls):
`export PC_API_EP='https://api.eu.prismacloud.io'`

.....
*Geddit??? ;-)

# Install & Run

This is a Python Flask application so you of course need to run this within a Python environment.

- Install the packages in requirements.txt `pip3 install -r requirements.txt`
- Run the app `python3 ./app.py`

# Links and Other Fun Stuff

This app is a front end / client for accessing the Prisma Cloud API.
If you would like to add functionality or indeed just explore the API, firstly here is the
[API Reference](https://prisma.pan.dev/api/cloud/)

Even cooler, and this is what I used to make up this awesome app, use [Postman](https://www.postman.com/) and
download the Prisma Cloud Collection over [here](https://github.com/PaloAltoNetworks/pcs-postman).

**Pro Tip**: On postman, when you make a request to an API, over on the right there's a code button.
Click that, and it will give you the codified version, for all sorts of languages. Obviously for this
simply click Python - Requests and you can build functionalty into this app with almost zero coding aptitude!