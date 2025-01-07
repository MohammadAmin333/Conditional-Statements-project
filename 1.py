def summer_activity(temperature):  
    if temperature >= 90:  
        return "It's really hot! How about going to the beach?"  
    elif 70 <= temperature < 90:  
        return "Perfect weather for a picnic in the park!"  
    elif 50 <= temperature < 70:  
        return "A nice day for a hike or a bike ride."  
    else:  
        return "It's quite cool! Maybe stay in and read a book."  

# Example usage  
try:  
    user_temperature = float(input("Enter the current temperature in Fahrenheit: "))  
    activity = summer_activity(user_temperature)  
    print(activity)  
except ValueError:  
    print("Please enter a valid number.")  