
# raise ValueError("Error Happened")

class ValidationError(ValueError):
    pass

class PhoneValidationError(ValidationError):
    def __init__(self, phone):
        if len(phone) < 10:
            super().__init__("Phone is too short")
        elif len(phone) > 10:
            super().__init__("Phone is too long")

class LoginValidationError(ValidationError):
    pass
        

try:
    raise PhoneValidationError("1235457657565756576")
# except LoginValidationError
except PhoneValidationError:
    print("Phone is not valid")
except ValidationError:
    print("Value is not valid")
