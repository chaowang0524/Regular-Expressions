import re

string = "The Euro STOXX 600 index, which tracks all stock markets across Europe including the FTSE, fell by 11.48% – the worst day since it launched in 1998. The panic selling prompted by the coronavirus has wiped £2.7tn off the value of STOXX 600 shares since its all-time peak on 19 February."

# `{}` are a repetition operator in regex

result_4 = re.findall(
    r"\w{4}", string
)  # matches four consecutives letters/digits in the string
print(result_4)

result_four_letter_words = re.findall(
    r"\b\w{4}\b", string
)  # `\b` for boundaries. It matches the four-letter words/digits in the string
print(result_four_letter_words)

result_3_5 = re.findall(
    r"\b\w{3,5}\b", string
)  # words that three characters but no more than five
print(result_3_5)

result_3_ = re.findall(r"\b\w{3,}\b", string)  # words at least three characters
print(result_3_5)

number = "12312378976413246512316897966895378456123"
result_digits = re.search(
    r"\d{3,6}", number
)  # matches the first 3-6 digits in the string, greedy
print(result_digits)

# convert it to non-greedy
result_digits_non_greedy = re.search(
    r"\d{3,6}?", number
)  # add `?` to make it non-greedy
print(result_digits_non_greedy)
