import dataclasses
import enum
from datetime import datetime, date


class Hobby(enum.Enum):
    sports = "Sports"
    reading = "Reading"
    music = "Music"


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    mobile_number: str
    date_of_birth: datetime.date
    subjects: list[str]
    hobbies: list[str]
    picture: str
    address: str
    state: str
    city: str


student = User('Test_Name', 'Test_Last_Name', 'test@gmail.com', "Male", '8800555353', date(2000, 12, 11),
               ['Computer Science'],
               [Hobby.music.value], 'foto.jpg', 'Test_Adress, 9', 'NCR', 'Delhi')
