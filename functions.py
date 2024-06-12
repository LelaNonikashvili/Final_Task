import csv
import datetime

# ვქმნით იუზერის კლასს (განვსაზღვრავთ იუზერის ყველა ატრიბუტს, რაც გვსურს რომ რეგისტრაციისას მივანიჭოთ იუზერს და მეთოდებს, რისი საშუალებითაც, 
# რეგისტრაციისას მითითებული დაბადების თარიღით, იუზერს ავტომატუმატურად მიენიჭება ასაკი და ჩვენ მიერ წინასწარ განსაზღვრული ასაკობრივი 
# კატეგორიებიდან ერთ-ერთი.)

class User:
    def __init__(self, personal_number, first_name, last_name, date_of_birth, gender, phone_number, region, subscription_branch, subscription_fee):
        self.personal_number = personal_number
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.phone_number = phone_number
        self.region = region
        self.subscription_branch = subscription_branch
        self.subscription_fee = subscription_fee
        self.age = self.calculate_age()
        self.age_category = self.assign_age_category()
    
    def __str__(self):
        return (f"Personal Number: {self.personal_number}, First Name: {self.first_name}, Last Name: {self.last_name}, "
                f"Date of Birth: {self.date_of_birth}, Age: {self.age}, Age Category: {self.age_category}, "
                f"Gender: {self.gender}, Phone Number: {self.phone_number}, "
                f"Region: {self.region}, Subscription Branch: {self.subscription_branch}, "
                f"Subscription Fee: {self.subscription_fee} GEL")

    def calculate_age(self):
        today = datetime.date.today()
        return today.year - self.date_of_birth.year - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))

    def assign_age_category(self):
        age = self.age
        if age < 18:
            return "<18"
        elif 18 <= age <= 25:
            return "18-25"
        elif 26 <= age <= 35:
            return "26-35"
        elif 36 <= age <= 45:
            return "36-45"
        else:
            return ">46"

# წინასწარ განვსაზღვრეთ რეგიონები და შესაბამისი ფილიალები, სადაც გვაქვს სპორტდარბაზები.
regions = {
    "tbilisi": ["saburtalo", "isani", "gldani"],
    "kvemo kartli": ["rustavi"],
    "samegrelo": ["zugdidi"],
    "imereti": ["kutaisi"],
    "kakheti": ["telavi"]
}

# ფუნქცია ახალი იუზერის დარეგისტრირებისთვის. თითოეული პარამეტრისთვის გვაქვს შესაბამისი შეზღუდვა, არასწორი ფორმატით მონაცემის შეყვანის შემთხვევაში.
def create_user():
    while True:
        personal_number = input("Enter personal number: ")
        if personal_number.isdigit() and len(personal_number) == 11:
            break
        else:
            print("Invalid personal number. It must be 11 numeric characters.")

    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")

    while True:
        date_of_birth = input("Enter date of birth (YYYY-MM-DD): ")
        try:
            date_of_birth = datetime.datetime.strptime(date_of_birth, "%Y-%m-%d").date()
            break
        except ValueError:
            print("Invalid date format. Please enter the date in YYYY-MM-DD format.")

    while True:
        gender = input("Enter gender (male/female): ").lower()
        if gender in ["male", "female"]:
            gender = gender.capitalize()
            break
        else:
            print("Invalid gender. Please enter 'male' or 'female'.")

    while True:
        phone_number = input("Enter phone number: ")
        if phone_number.isdigit() and len(phone_number) == 9 and phone_number.startswith('5'):
            break
        else:
            print("Invalid phone number format. Try again!")

    #დარეგისტრირებისას შეგვიძლია მხოლოდ იმ რეგიონების სახელის შეყვანა, რაც წინასწარ განვსაზღვრეთ.
    print("Select region of the country:")
    for region in regions:
        print(region.title())
    while True:
        region = input("Enter region: ").lower()
        if region in regions:
            break
        else:
            print("Invalid region. Please select a valid region.")

    # დარეგისტრირებისას შეგვიძლია მხოლოდ იმ ფილიალების სახელის შეყვანა, რაც წინასწარ განვსაზღვრეთ.
    print(f"Select branch in {region.title()}:")
    for branch in regions[region]:
        print(branch.title())
    while True:
        subscription_branch = input("Enter subscription branch: ").lower()
        if subscription_branch in regions[region]:
            break
        else:
            print(f"Invalid branch for {region.title()}. Please select a valid branch.")

    #კომპანის აქვს სამი ტიპის აბონიმენტი. რეგისტრაციისას უნდა მიეთითოს ერთ-ერთი.
    print("Select subscription fee:")
    subscription_options = {
        "1": "100 GEL (three days a week, during daytime hours)",
        "2": "150 GEL (three days a week at any time of the day)",
        "3": "250 GEL (unlimited access)"
    }
    for key, value in subscription_options.items():
        print(f"{key}: {value}")
    while True:
        subscription_choice = input("Enter the number corresponding to the subscription option: ")
        if subscription_choice in subscription_options:
            subscription_fee = { "1": 100, "2": 150, "3": 250 }[subscription_choice]
            break
        else:
            print("Invalid choice. Please select a valid subscription option.")

    return User(personal_number, first_name, last_name, date_of_birth, gender, phone_number, region.title(), subscription_branch.title(), subscription_fee)

# მომხმარებლების მონაცემთა ბაზა
user_database = []

# აღნიშნული ფუნქციით, ავტომატურად ვინახავთ იუზერების მონაცემებს CSV ფაილში.
def save_user_to_csv(user):
    with open('user_database.csv', mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([user.personal_number, user.first_name, user.last_name, user.date_of_birth, user.age, user.age_category, user.gender, user.phone_number, user.region, user.subscription_branch, user.subscription_fee])


def load_users_from_csv():
    try:
        with open('user_database.csv', mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                user = User(
                    personal_number=row['Personal Number'],
                    first_name=row['First Name'],
                    last_name=row['Last Name'],
                    date_of_birth=datetime.datetime.strptime(row['Date of Birth'], "%Y-%m-%d").date(),
                    gender=row['Gender'],
                    phone_number=row['Phone Number'],
                    region=row['Region'],
                    subscription_branch=row['Subscription Branch'],
                    subscription_fee=float(row['Subscription Fee'])
                )
                user_database.append(user)
    except FileNotFoundError:
        initialize_csv()
    except KeyError:
        print("CSV file headers do not match the expected format.")
        initialize_csv()

def initialize_csv():
    with open('user_database.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Personal Number', 'First Name', 'Last Name', 'Date of Birth', 'Age', 'Age Category', 'Gender', 'Phone Number', 'Region', 'Subscription Branch', 'Subscription Fee'])

def write_all_users_to_csv():
    initialize_csv()  
    with open('user_database.csv', mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for user in user_database:
            writer.writerow([user.personal_number, user.first_name, user.last_name, user.date_of_birth, user.age, user.age_category, user.gender, user.phone_number, user.region, user.subscription_branch, user.subscription_fee])

# აღნიშნული ფუნქციით, დარეგისტრირებული მომხმარებელი ემატება იუზერების ბაზაში.
def register_user(user):
    user_database.append(user)
    save_user_to_csv(user)
    print("User registered successfully.")
    

# დარეგისტრირებული მომხმარებლების ჩვენების ფუნქცია.
def display_users():
    if not user_database:
        print("No users registered yet.")
    else:
        for user in user_database:
            print(user)

# იუზერის წაშლის ფუნქცია ბაზიდან, რაც წასაშლელი იუზერის პირადი ნომრის შეყვანას მოგვთხოვს.
def delete_user_by_personal_number(personal_number):
    global user_database
    user_database = [user for user in user_database if user.personal_number != personal_number]
    write_all_users_to_csv()
    print(f"User with personal number {personal_number} has been deleted.")

# ვითვლით, ჯამურად, ყველა ფილიალში, მომხმარებლების პროცენტულ განაწილებას, ჩვენ მიერ წინასწარ განსაზღვრული ასაკობრივი კატეგორიების მიხედვით.
def count_and_display_users_by_age_category():
    age_categories = {
        "<18": 0,
        "18-25": 0,
        "26-35": 0,
        "36-45": 0,
        ">46": 0
    }
    total_users = len(user_database)
    for user in user_database:
        age_categories[user.age_category] += 1
    
    print("\nUser count by age category (Total):")
    for category, count in age_categories.items():
        percentage = (count / total_users) * 100 if total_users != 0 else 0
        print(f"{category}: {count} ({percentage:.2f}%)")

# ვითვლით მომხმარებლების პროცენტულ განაწილებას ასაკობრივი კატეგორიების მიხედვით თითოეული რეგიონისთვის.
def count_and_display_users_by_age_category_region():
    print("\nUser count by age category in each region:")
    for region in regions:
        age_categories = {
            "<18": 0,
            "18-25": 0,
            "26-35": 0,
            "36-45": 0,
            ">46": 0
        }
        total_users = sum(1 for user in user_database if user.region.lower() == region)
        for user in user_database:
            if user.region.lower() == region:
                age_categories[user.age_category] += 1
        
        print(f"\nRegion: {region.title()}")
        for category, count in age_categories.items():
            percentage = (count / total_users) * 100 if total_users != 0 else 0
            print(f"{category}: {count} ({percentage:.2f}%)")

# ვითვლით მომხმარებლების პროცენტულ განაწილებას ასაკობრივი კატეგორიების მიხედვით თითეული ფილიალისთვის.
def count_and_display_users_by_age_category_branch():
    print("\nUser count by age category in each branch:")
    for region_branches in regions.values():
        for branch in region_branches:
            age_categories = {
                "<18": 0,
                "18-25": 0,
                "26-35": 0,
                "36-45": 0,
                ">46": 0
            }
            total_users = sum(1 for user in user_database if user.subscription_branch.lower() == branch)
            for user in user_database:
                if user.subscription_branch.lower() == branch:
                    age_categories[user.age_category] += 1
            
            print(f"\nBranch: {branch.title()}")
            for category, count in age_categories.items():
                percentage = (count / total_users) * 100 if total_users != 0 else 0
                print(f"{category}: {count} ({percentage:.2f}%)")

#ვითვლით, ჯამურად, ყველა ფილიალში, მომხმარებლების პროცენტულ განაწილებას სქესის მიხედვით.
def display_gender_distribution():
    total_users = len(user_database)
    gender_distribution = {
        "Male": sum(1 for user in user_database if user.gender == "Male"),
        "Female": sum(1 for user in user_database if user.gender == "Female")
    }

    print("\nGender Distribution:")
    print(f"Total Users: {total_users}")
    for gender, count in gender_distribution.items():
        percentage = (count / total_users) * 100 if total_users != 0 else 0
        print(f"{gender}: {count} ({percentage:.2f}%)")

# ვითვლით მომხმარებლების პროცენტულ განაწილებას სქესის მიხედვით თითოეული რეგიონისთვის.
def display_gender_distribution_by_region():
    print("\nGender Distribution by Region:")
    for region in regions:
        total_users = sum(1 for user in user_database if user.region.lower() == region)
        gender_distribution = {
            "Male": sum(1 for user in user_database if user.region.lower() == region and user.gender == "Male"),
            "Female": sum(1 for user in user_database if user.region.lower() == region and user.gender == "Female")
        }

        print(f"\nRegion: {region.title()}")
        print(f"Total Users: {total_users}")
        for gender, count in gender_distribution.items():
            percentage = (count / total_users) * 100 if total_users != 0 else 0
            print(f"{gender}: {count} ({percentage:.2f}%)")


# ვითვლით მომხმარებლების პროცენტულ განაწილებას სქესის მიხედვით თითოეული ფილიალისთვის.
def display_gender_distribution_by_branch():
    print("\nGender Distribution by Branch:")
    for region_branches in regions.values():
        for branch in region_branches:
            total_users = sum(1 for user in user_database if user.subscription_branch.lower() == branch)
            gender_distribution = {
                "Male": sum(1 for user in user_database if user.subscription_branch.lower() == branch and user.gender == "Male"),
                "Female": sum(1 for user in user_database if user.subscription_branch.lower() == branch and user.gender == "Female")
            }

            print(f"\nBranch: {branch.title()}")
            print(f"Total Users: {total_users}")
            for gender, count in gender_distribution.items():
                percentage = (count / total_users) * 100 if total_users != 0 else 0
                print(f"{gender}: {count} ({percentage:.2f}%)")

# თითოეული იუზერის მიერ არჩეული აბონიმენტის ღირებულების მიხედვით, ვითვლით ფილიალების ჯამურ შემოსავალს.
def calculate_and_display_revenue_by_branch():
    branch_revenue = {branch.title(): 0 for region in regions for branch in regions[region]}

    for user in user_database:
        branch_revenue[user.subscription_branch] += user.subscription_fee

    print("\nTotal Revenue by Branch:")
    for branch, revenue in branch_revenue.items():
        print(f"{branch.title()}: {revenue} GEL")

  