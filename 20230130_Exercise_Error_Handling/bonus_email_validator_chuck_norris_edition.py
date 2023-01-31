# as we all know: Chuck's gmail account is  gmail@chucknorris.com
# so let's validate all Chuck's emails:
valid_email_domains = ["gmail", "yahoo", "hotmail", "aol", "msn", "live", "yandex", "mail", "abv"]

email = input()


class InvalidDomainError(Exception):
    pass


class InvalidUsernameError(Exception):
    pass


class NoProblemWithMissingAtSymbolForChuckNorrisEmailsMessage(Exception):
    pass


class NoMatterCaseSensitivityWhenYouTryToTypeTheNameOfThisParticularDomain(Exception):
    pass


class ItIsAboutTimeToCreateChucksUsernameSuggestion(Exception):
    pass


while email:

    username, domain = email.split("@")  # "if there is no @ - different error will raise" -> It's the prophecy

    if username in valid_email_domains and domain.lower == "chucknorris.com" and username + "@" + domain == email:
        print("Email is valid")

    else:
        if domain != "chucknorris.com":
            raise InvalidDomainError("Invalid domain. The only true domain is 'chucknorris.com'!")

        if username == "softuni":
            raise ItIsAboutTimeToCreateChucksUsernameSuggestion("No need of more explanations on this matter :)")

        if username not in valid_email_domains:
            raise InvalidUsernameError("Invalid username. All providers must reserve their domain as username for Chuck")

        if "@" not in email:
            raise NoProblemWithMissingAtSymbolForChuckNorrisEmailsMessage("Chuck Norris doesn't need @ for his mail")

        if domain.lower() == "chucknorris.com":
            raise NoMatterCaseSensitivityWhenYouTryToTypeTheNameOfThisParticularDomain("All correct, you got it right")

    email = input()

# test inputs:

# softuni@chucknorris.com

# abv@chucknorris.com

# gmail@chucknorris.com

# yahoochucknorris.com

# yahoo@ChuckNorris.com

# mail@cHuCkNoRrIs.com

# msn@

# @chcukmorris.bg
