import yaml

users = [
    {
        "userid":"userid1",
        "username":"abc",
        "email":"abc@xyz.com",
        "password":"abc@test"
    },
    {
        "userid":"Userid2",
        "username":"def",
        "email":"def@xyz.com",
        "password":"def@test"
    },
    {
        "userid":"Userid3",
        "username":"mno",
        "email":"mno@xyz.com",
        "password":"mno@test"
    }
]

advisors = [
    {
        "id":"Advisorid1",
        "name":"Advisor1",
        "pic":"Advisor1_image"
    },
    {
        "id":"Advisorid2",
        "name":"Advisor2",
        "pic":"Advisor2_image"
    },
    {
        "id":"Advisorid3",
        "name":"Advisor3",
        "pic":"Advisor3_image"
    }
]

bookings = []

with open("user.yaml", 'w') as userfile:
    data = yaml.dump(users, userfile)
    print(data)
    print("Write successful")
    userfile.close()

with open("test.yaml", 'w') as advisorfile:
    data = yaml.dump(test, advisorfile)
    print(data)
    print("Write successful")
    advisorfile.close()

with open("booking.yaml", 'w') as bookingfile:
    data = yaml.dump(booking, bookingfile)
    print(data)
    print("Write successful")
    bookingfile.close()