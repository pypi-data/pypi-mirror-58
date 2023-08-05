from .helpers import django_service, flask_service, start_super_jopi_infra

# Services
CLI_SERVICE_SPLASH = """
    ___________     __    __          
    \__    ___/___ |  | _|  | ______  
      |    | /    \|  |/ /  |/ /    \ 
      |    |(  []  )    <|    <  []  )
      |____| \____/|__|_ \__|_ \____/ 
                        \/    \/      
"""

FLASK = "flask"
DJANGO = "django"
SUPER_JOPI = 'super-jopi'
AVAILABLE_TEMPLATES = {FLASK: flask_service, DJANGO: django_service}
AVAILABLE_INFRA = {SUPER_JOPI: start_super_jopi_infra}
