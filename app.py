import os

def main():
    name = os.getenv("USERNAME", "Guest")
    print(f"Hello, {name}!")

if __name__ == "__main__":
    main()
