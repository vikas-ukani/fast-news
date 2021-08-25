
from pydantic.fields import Field, Required
from datetime import datetime
from pydantic import BaseModel
from typing import Optional


class NewsCreate(BaseModel):
    title: str = Field(None, title="Title for your news",
                       max_length=100, min_length=5, Required=True)
    description: str = Field(None, title="A long description for your news",
                             min_length=10, max_length=500, Required=True)
    slug: str = Field(
        None, title="A unique text for get an deteils of current news.", Required=True)
    isPublished: bool = Field(
        None, title='A boolean value for this news', default_value=True, Required=False)
    price: Optional[float] = Field(
        None, title='Price to get access this news, Paid', default_value=0, Required=False)
    createdAt: datetime = Field(
        None, title="Date time while creting this news", default_value=datetime.now(), Required=False)
