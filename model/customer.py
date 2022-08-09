from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class Customer(BaseModel):
    clientID: int
    fullName: Optional[str]
    status: Optional[str]
    mobileNo: Optional[str]
    officeName: Optional[str]

    def __init__(self, clientID, fullName, mobileNo, officeName, status):
        super().__init__(clientID = clientID, fullName = fullName, mobileNo = mobileNo, officeName = officeName, status = status)
