import requests

def fetch_random_user_freeapi():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)
    data = response.json()
    

    if (data["success"] and "data" in data):
        user_data = data["data"]

        username = user_data["login"]["username"]
        password = user_data["login"]["password"]
        city = user_data["location"]["city"]
        country = user_data["location"]["country"]

        return username,password,country,city
    else:
        raise Exception("[Error] Failed to fetch!")
        

value = fetch_random_user_freeapi()


def main():
    try: 
        username, password, country, city = fetch_random_user_freeapi()
        print(f"Username: {username}, \npassword: {password}, \nCity: {city}, \nCountry: {country} ")
    except Exception as e: 
        print(str(e))
        
    finally:
        pass

if __name__ == "__main__":
    main()