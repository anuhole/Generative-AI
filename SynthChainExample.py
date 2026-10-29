from faker import Faker

fake = Faker('en-IN')

for i in range(5):
    print(f"User {i+1}")
    print(" Name    :",fake.name())
    print(" Email   :",fake.email())
    print(" Phone   :",fake.phone_number())
    print(" Address :",fake.address())
    print(" Android :", fake.android_platform_token())



   
