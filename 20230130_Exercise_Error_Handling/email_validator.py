# Top-level domain (TLD)
import re

valid_tld = {"com", "bg", "net", "org"}
pattern = r"([\w+\.]{4,}@[a-z]+\.[a-z]{2,3})\b"

email = input()


class MustContainAtSymbolError(Exception):
    pass


class MoreThanOneAtSymbolsError(Exception):
    pass


class NameTooShort(Exception):
    pass


class InvalidDomainError(Exception):
    pass


while email:

    result = re.findall(pattern, email)

    if result:

        print("Email is valid")

    else:

        if "@" not in email:
            raise MustContainAtSymbolError("Email must contain '@'!")

        #  checking for more than one @ symbols
        if email.count("@") > 1:
            raise MoreThanOneAtSymbolsError("Email can't contain more than one '@' symbols!")

        # looking for shorter than 4 characters username
        if len(email.split("@")[0]) < 4:
            raise NameTooShort("Name must be more than 4 characters")

        # checking for valid TLD in the set with Top-level domains
        if not set(email.split(".")[-1]).issubset(valid_tld):
            raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

        if not (email.split(".")[-1]):
            raise IndexError

    email = input()

# test inputs:

# abc@abv.bg

# peter@gmail.com
# petergmail.com

# peter@gmail.hotmail
