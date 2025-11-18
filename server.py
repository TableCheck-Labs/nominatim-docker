"""
Custom Nominatim server wrapper with health endpoint
"""
import falcon
from nominatim_api.server.falcon.server import run_wsgi

class HealthResource:
    """Health check endpoint that always returns 200"""
    
    def on_get(self, req, resp):
        """
        Handle GET requests to /health
        Always returns 200 OK with service status
        """
        resp.status = falcon.HTTP_200
        resp.content_type = 'application/json'
        resp.text = '{"status":"online","service":"nominatim"}'

def get_application():
    """
    Get the Nominatim application with added health endpoint
    """
    # Get the base Nominatim application
    app = run_wsgi()
    
    # Add health endpoint
    health = HealthResource()
    app.add_route('/health', health)
    
    return app

# This is what Gunicorn will call
def run_wsgi():
    """Entry point for Gunicorn"""
    return get_application()

