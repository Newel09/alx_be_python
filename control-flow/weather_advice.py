"""
Instructions:

Prompt User for Weather Input:

Ask the user to input the current weather from a predefined set of conditions: sunny, rainy, or cold.
Use the prompt: What's the weather like today? (sunny/rainy/cold):.
Provide Clothing Recommendations:

Based on the user’s input, your program will recommend different types of clothing:
If the weather is “sunny”, recommend: Wear a t-shirt and sunglasses.
If the weather is “rainy”, recommend: Don't forget your umbrella and a raincoat.
If the weather is “cold”, recommend: Make sure to wear a warm coat and a scarf.
Include an else statement that handles unexpected input by printing: Sorry, I don't have recommendations for this weather.
Output the Recommendation:

Print the clothing recommendation based on the weather condition provided by the user.
"""
# define possible inputs.
#weather = ("sunny", "rainy", "cold")
while True:
    Weather = input("What's the weather like today? (sunny/rainy/cold): ").lower() # .lower() to convert to any case.

    if Weather == "sunny":
      print(f"Wear a t-shirt and sunglasses.") # Print this is the weather is sunny.

    elif Weather == "rainy":
      print(f"Don't forget your umbrella and a raincoat.")

    elif Weather == "cold":
      print(f"Make sure to wear a warm coat and a scarf.")

    else:
      print(f"Sorry, I don't have recommendations for this weather.")
      break
  