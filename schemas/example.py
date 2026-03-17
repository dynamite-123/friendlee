from pydantic import BaseModel

class ExampleBase(BaseModel):
    name: str
    description: str | None = None

class ExampleCreate(ExampleBase):
    pass

class Example(ExampleBase):
    id: int

    class Config:
        from_attributes = True
