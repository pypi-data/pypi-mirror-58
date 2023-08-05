import re
import logging


class Rule:
    def __init__(self, name: str, funct: object) -> object:
        self.name = name
        self.funct = funct

    def run(self, x) -> bool:
        logging.debug("running rule {} on {}".format(self.name, x))
        return self.funct(x)


no_error = Rule("Check that dictionary json does not have error",
                lambda x: x and (type(x) != dict or "error" not in x))


type_str = Rule("Type is string", lambda x: x is not None and type(x) == str)
type_int = Rule("Type is integer", lambda x: x is not None and type(x) == int)
type_bool = Rule("Type is boolean", lambda x: x is not None and type(x) == bool)  # check not None first
type_dct = Rule("Type is dictionary", lambda x: x is not None and type(x) == dict)
type_lst = Rule("Type is list", lambda x: x is not None and type(x) == list)
type_float = Rule("Type is float", lambda x: x is not None and type(x) in [int, float])

type_url = Rule("Check url exists/ valid with https://www.",
                lambda x: x is not None and len(re.findall(r"^https://www\.(.+)\.(.+)", str(x))) > 0)
type_https = Rule("Check url exists/ valid with http", lambda x: x is not None and len(re.findall(r"^https://(.+)\.(.+)", str(x))) > 0)
type_domain = Rule("Check for exists/ valid domain", lambda x: x is not None and len(re.findall(r"(.+)\.(.+)", str(x))) > 0)
type_date = Rule("Check for exists/ valid date format", lambda x: x is not None and x)  # TODO: update this!
type_ticker = Rule("Check ticker exists/ consists of letters and possible dot",
                   lambda x: x is not None and re.findall(r"^\w+(\.)?\w+", str(x)))

non_empty_field = Rule("Check given field is non-empty", lambda x: x is not None and x)
not_none = Rule("Check field is not None", lambda x: x is not None)

frequency_name = Rule("Check valid frequency name",
                      lambda x: x is not None and x in ["instant", "daily", "weekly", "monthly", "quarterly", "yearly"])


def has_field(field_name):  # uses string name (field in x)
    return Rule("Has field `{}`".format(field_name), lambda x: x is not None and field_name in x)


def in_field(field_names):  # uses string name (x in in fields)
    return Rule("Within fields `{}`".format(field_names), lambda x: x is not None and x in field_names)


def len_eq(number):
    return Rule("Has field length `{}`".format(number), lambda x: x is not None and len(x) == number)


def len_gt(number):
    return Rule("Has field length greater than `{}`".format(number), lambda x: x is not None and len(x) > number)


def len_lt(number):
    return Rule("Has field length less than `{}`".format(number), lambda x: x is not None and len(x) < number)


def gte(number):
    return Rule("Is greater than or equal to `{}`".format(number), lambda x: x is not None and x >= number)


def lte(number):
    return Rule("Is less than or equal to `{}`".format(number), lambda x: x is not None and x <= number)


def matches_url(field_name):
    return Rule("Has url for `{}`".format(field_name), lambda x: x is not None and matches_url_funct(field_name, x))


def matches_url_funct(field, url):
    return len(re.findall(r"https://(www\.)?{name}\.com.*".format(name=field.name), str(url))) > 0
