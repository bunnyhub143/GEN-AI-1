from pydantic import BaseModel, Field, ValidationError

class student(BaseModel):
    name:str = Field(description = "Name of the student")
    age:int = Field(ge=18,le=30,description = "Age of the student")
    grade:float = Field(ge=0,le=100,description = "Grade of the student")
    
    
student1 = student(
    name = "sreayas",
    age = 20,
    grade = 90.5
)
print(student1)

# Throwing Validation Error
try:
    student2 = student(
        name = "Vamshi",
        age = 17,
        grade = 150
    )
    print(student2)
except ValidationError as e:
    print("Dorikindhiiiii",e)
