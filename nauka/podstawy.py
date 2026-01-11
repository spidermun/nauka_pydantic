from pydantic import BaseModel, EmailStr,Field,field_validator


class User(BaseModel):
    name: str
    email: EmailStr
    id: int

# user_data = {
#     'name': "michal",
#     "email": "email@wp.pl",
#     "id": 12
# }

    @field_validator("id")
    def validate_id(cls,value):
        if value <= 0:
            raise ValueError(f"Musi byc wieksze od {value}")
        return value




user=User(name="michal",email="email@wp.pl",id=1)
print(user)



# user = User(**user_data) # ** to operator rozpakowowania warto pamietac !!
#
# print(user.name)
# print(user.email)
# print(user.id)