import cgi
import os

import wsgiref.handlers
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.api import mail

class Form(webapp.RequestHandler):
    def post(self):
        template_values = self.request.params
        path_email = os.path.join(os.path.dirname(__file__), 'apply.email')

        message = mail.EmailMessage(sender='hcurrie@gmail.com',
                            subject='[ECWZ Website] Application to Assist',
                            to = 'hamish@currie.to',
                            body = template.render(path_email, template_values))
        message.send()

        path_html = os.path.join(os.path.dirname(__file__), 'apply.html')
        self.response.out.write(template.render(path_html, template_values))

def main():
    application = webapp.WSGIApplication([('/apply.php', Form), ],
				    debug=True)
    wsgiref.handlers.CGIHandler().run(application)

if __name__ == "__main__":
    main()
