from gluon.storage import Storage
settings = Storage()

settings.migrate = True
settings.title = 'Chaosmentors'
settings.subtitle = ''
settings.author = 'Marco Gaib'
settings.author_email = 'marco.gaib@auticare.de'
settings.keywords = ''
settings.description = 'This is the subscription System for the Chaosmentors-project.'
settings.layout_theme = 'Default'
settings.database_uri = 'sqlite://storage.sqlite'
settings.security_key = 'b1ce81fd-e497-4656-a749-a37116883fc1'
settings.email_server = 'localhost'
settings.email_sender = 'contact@chaosmentors.org'
settings.email_login = ''
settings.login_method = 'local'
settings.login_config = ''
settings.plugins = []
settings.license = XML('<a href="http://www.gnu.org/licenses/gpl-3.0.en.html" target="_new">GPL</a>')
