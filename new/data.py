import yaml

users = [
    {
        "userid":1,
        "username":"abc",
        "email":"abc@xyz.com",
        "password":"abc@test"
    },
    {
        "userid":2,
        "username":"def",
        "email":"def@xyz.com",
        "password":"def@test"
    },
    {
        "userid":3,
        "username":"mno",
        "email":"mno@xyz.com",
        "password":"mno@test"
    }
]

advisors = [
    {
        "advid":1,
        "name":"Advisor1",
        "pic":"Advisor1_image"
    },
    {
        "advid":2,
        "name":"Advisor2",
        "pic":"Advisor2_image"
    },
    {
        "advid":3,
        "name":"Advisor3",
        "pic":"Advisor3_image"
    }
]

bookings = []

with open("new/user.yaml", 'w') as userfile:
    data = yaml.dump(users, userfile)
    print(data)
    print("Write successful")
    userfile.close()

with open("new/test.yaml", 'w') as advisorfile:
    data = yaml.dump(advisors, advisorfile)
    print(data)
    print("Write successful")
    advisorfile.close()

with open("new/booking.yaml", 'w') as bookingfile:
    data = yaml.dump(bookings, bookingfile)
    print(data)
    print("Write successful")
    bookingfile.close()