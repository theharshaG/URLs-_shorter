import random
import string

urls = {}

while True:
    print("\n1. Shorten URL")
    print("2. Retrieve URL")
    print("3. Show All")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        long_url = input("Enter long URL: ")

        code = ''.join(random.choices(string.ascii_letters + string.digits, k=5))

        urls[code] = long_url

        print("Short URL: short.ly/" + code)

    elif choice == "2":
        code = input("Enter short code: ")

        if code in urls:
            print("Original URL:", urls[code])
        else:
            print("URL not found")

    elif choice == "3":
        for code, url in urls.items():
            print(f"{code} -> {url}")

    elif choice == "4":
        print("Bye..")
        break

    else:
        print("Invalid choice")
