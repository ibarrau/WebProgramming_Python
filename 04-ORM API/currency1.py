import requests

def main():
    res = requests.get("https://data.fixer.io/api/latest?base=USD&symbols=EUR")
    if res.status_code != 200:
        raise Exception("ERROR: API request unsuccessful.")
    data = res.json()
    code = data["error"]["code"]
    print(f"The api fails and the code error is: {code}.")

def main_two():
    base = input("First Currency: ")
    other = input("Other Currency: ")
    res = requests.get("https://data.fixer.io/api/latest", 
        params = {"base":base, "symbols":other} )
    
    if res.status_code != 200:
        raise Exception("ERROR: API request unsuccessful.")
    
    data = res.json()
    code = data["error"]["code"]
    print(f"The api fails and the code error is: {code}.")

if __name__ == "__main__":
    main_two()
