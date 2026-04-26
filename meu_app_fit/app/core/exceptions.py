from fastapi import HTTPException, status

class AppException(HTTPException): # Criamos uma classe de exceção personalizada que herda de HTTPException, para padronizar a estrutura das respostas de erro em nossa API.
    def __init__(self, status_code: int, code: str, message: str):

        super().__init__(
            status_code=status_code, 
            detail= {
                "error": {
                    "code": code,
                    "message": message
                }
            }
    )

class UnauthorizedException(AppException):
    def __init__(self, message: str = "Unauthorized"):
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            code="AUTH_INVALID_CREDENTIALS",
            message=message
        )

class BadRequestException(AppException):
    def __init__(self, message: str = "Bad Request"):
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            code="BAD_REQUEST",
            message=message
        )

class NotFoundException(AppException):
    def __init__(self, message: str = "Not Found"):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            code="RESOURCE_NOT_FOUND",
            message=message
        )

class DatabaseException(AppException):
    def __init__(self, message: str = "Database Error"):
        super().__init__(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            code="DATABASE_ERROR",
            message="Database not ready"
        )