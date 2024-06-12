from functions import *

# აპლიკაციის მთავარი მენიუ.

def main():
    load_users_from_csv()
    
    while True:
        print("\nGym Registration System")
        print("1. Register User")
        print("2. Display Users")
        print("3. Delete User")
        print("4. Distribution of Users by Age Category")
        print("5. Distribution of Users by Age Category and Region")
        print("6. Distribution of Users by Age Category and branch")
        print("7. Gender Distribution Display")
        print("8. Display Gender Distribution by Region")
        print("9. Display Gender Distribution by Branch")
        print("10. Calculate and Display Total Revenue by Branch")
        print("11. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            user = create_user()
            register_user(user)
        elif choice == '2':
            print("\nCurrent User Database:")
            display_users()
        elif choice == '3':
            personal_number = input("Enter the personal number of the user to delete: ")
            delete_user_by_personal_number(personal_number)
        elif choice == '4':
            count_and_display_users_by_age_category()
        elif choice == '5':
            count_and_display_users_by_age_category_region()
        elif choice == '6':
            count_and_display_users_by_age_category_branch()
        elif choice == '7':
            display_gender_distribution()
        elif choice == '8':
            display_gender_distribution_by_region()
        elif choice == '9':
            display_gender_distribution_by_branch()
        elif choice == '10':
            calculate_and_display_revenue_by_branch()
        elif choice == '11':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()     