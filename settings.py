from envparse import env


default_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3MiOiJvayIsImlhdCI6MTU1Mzg1OTMyMH0.Oepp68IgF-i7HaCwhQELHRyrmWPllpUPobMzySz0Q1M'
SECRET_KEY = env.str('SECRET_KEY', default='12345')
DB_SERVICE_URL = env.str('DB_SERVICE_URL', default='http://176.99.11.253/db/api/')
AUTH_TOKEN = env.str('AUTH_TOKEN', default=default_token)
