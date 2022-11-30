import pandas

d = pandas.DataFrame()

d = pandas.DataFrame(
    [
        ["Andy", 46, "Engineer"],
        ["Jane", 33, "Nurse"],
        ["Robert", 21, "Student"],
        ["Maria", 30, "Student"],
    ],
    columns=[
        "Name",
        "Age",
        "Occupation",
    ],
    index=["ID1", "ID2", "ID3", "ID4"],
)
