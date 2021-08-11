# Dude, where's my Prisma Cloud Compliance?

This application is designed to *drive over to Prisma Cloud to obtain the latest and greatest of compliance coverage.

# *REMEMBER* to generate a self-signed certificate (or better yet, a _real_ one) e.g.

`openssl req -x509 -newkey rsa:4096 -nodes -subj "/C=UK/ST=Scotland/L=Edinburgh/O=IT/CN=myhost.example.com" -out cert.pem -keyout key.pem -days 365`

Also, set your environment variables, because of course, I wasn't silly enough to hard-code them ;-) e.g.

`export PC_KEY='blah'`
`export PC_SECRET='blahblah'`

.....
*Geddit??? ;-)

# Install & Run

This is a Python Flask application so you of course need to run this within a Python environment.

- Install the packages in requirements.txt `pip3 install -r requirements.txt`
- Run the app `python3 ./app.py`