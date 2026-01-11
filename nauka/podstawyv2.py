from pydantic import BaseModel, EmailStr, Field

class User(BaseModel):
    name: str
    email: EmailStr
    id: int = Field(gt=0)  # Dajemy to zamiast osobnej funkcji z dekoratorem

user=User(name="michal",email="email@wp.pl",id=1)
print(user)

