import re

tweet = "Get ready for #PythonChallenge! Join us on 18/12 and 19/12 for a weekend full coding and debbuging, exploration and inspiration and collaboration https://www.python.org/challenge."

tweet1 = re.sub(r'\d+', '', tweet)
print(tweet1)

tweet2 = re.sub(r'https\S+', '', tweet1)
tweet3 = re.sub(r'www\S+', '', tweet2)
print(tweet3)

tweet4 = re.sub(r'#[A-Za-z0-9]+', '',tweet3)
print(tweet4)
final_output = re.sub('[/!,]+', '', tweet4)
print(final_output)