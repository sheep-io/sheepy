class HttpError(Exception):
    def __init__(self, status_code, message):
        self.status_code = status_code
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"HttpError: {self.status_code} - {self.message}"

def handle_http_error(status_code):
    error_messages = {
        400: "Bad Request: The server could not understand the request.",
        401: "Unauthorized: Authentication is required.",
        403: "Forbidden: You do not have permission to access this resource.",
        404: "Not Found: The requested resource could not be found.",
        500: "Internal Server Error: The server encountered an error.",
        503: "Service Unavailable: The server is not ready to handle the request."
    }
    return error_messages.get(status_code, "An unexpected error occurred.")
