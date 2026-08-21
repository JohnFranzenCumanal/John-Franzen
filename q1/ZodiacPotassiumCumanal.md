# Activity 3: Implementing Selection Structure - Chinese Zodiac Sign

## Requirements

This code requirement focuses on implementation of the basics of Python based on the learning resource given.

1. Create a `zodiacSectionLN.py` file with the following:
   - Ask the user to enter a year of birth. The baseline year is 1900.
   - Validate user input so it should not be earlier than 1900.
   - If the user enters an invalid year, display an appropriate message then stop the program.
   - Otherwise, determine the Chinese zodiac sign based on the year of birth, starting from 1900. Note: a zodiac sign recurs every 12 years.
   - Only consider the year of birth.

2. Test and run the code before submitting.
3. Document the exercise in the GitHub portfolio.

## Code

```python
#Fuction for grouping the code
def zodiac():
    #A list for all 12 Chinese Zodiac Signs
    zodiac_sign = ['Rat (鼠 / Shǔ)',
    'Ox (牛 / Niú)',
    'Tiger (虎 / Hǔ)',
    'Rabbit (兔 / Tù)',
    'Dragon (龙 / Lóng)',
    'Snake (蛇 / Shé)',
    'Horse (马 / Mǎ)',
    'Goat (羊 / Yáng)',
    'Monkey (猴 / Hóu)',
    'Rooster (鸡 / Jī)',
    'Dog (狗 / Gǒu)',
    'Pig (猪 / Zhū)']
    #asks the user for its birthyear
    year = int(input("Enter your birthyear:"))
    #The code will not accept a year below 1900
    if year < 1900:
        print("Invalid year, it should not be earlier than 1900")
        #Return so the invalid year message and the zodiac sign don't get mixed up together
        return
    #The formula, finding out what index on the list is the year given by the user
    a = (year - 1900 ) % 12
    print(f"Your Chinese Zodiac Sign is: {zodiac_sign[a]}")
    #Return the year value so it goes back to the outer year variable
    return year
#storing the return and calling the function 
year = zodiac()

```
## Output Screenshots

![Invalid Year Output](ZodiacPotassiumCumanal_invalid.jpg)




![Valid Year Output](ZodiacPotassiumCumanal_valid.jpg)
