import re
import itertools

mandatoryFields = [
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid",
]


def validateField(field):
    val = field["value"]
    code = field["code"]
    if code == "byr":
        if not 1920 <= int(val) <= 2002:
            return False
    elif code == "iyr":
        if not 2010 <= int(val) <= 2020:
            return False

    elif code == "eyr":
        if not 2020 <= int(val) <= 2030:
            return False

    elif code == "hgt":
        unit = val[-2:]
        if unit == "cm":
            if not 150 <= int(val[:-2]) <= 193:
                return False
        elif unit == "in":
            if not 59 <= int(val[:-2]) <= 76:
                return False
        else:
            return False
    elif code == "hcl":
        rest = re.findall("[a-f,0-9]", val[1:])
        if not (val[0] == "#" and len(val) == 7 and len(rest) == 6):
            return False
    elif code == "ecl":
        keys = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

        if not (len(val) == 3 and (val in keys)):
            return False

    elif code == "pid":
        rest = re.findall("[0-9]", val)
        if not (len(rest) == 9 and len(val) == 9):
            return False
    return True


def isValidPassport(onlyFields):
    def f(fields):
        # Check if all mandatory fields are present
        if len(list(filter(lambda field: field in list(map(lambda x: x["code"], list(fields))), mandatoryFields))) == len(
                mandatoryFields
        ):
            # Early return if only checking if mandatory fields are present
            if onlyFields == True:
                return True

            if False in list(map(lambda field: validateField(field), fields)):
                return False

            return True
        else:
            return False
    return f


def countValidPassports(passports, onlyFields=False):
    return sum(map(isValidPassport(onlyFields), passports))


if __name__ == "__main__":
    f = open("day4Input.txt", "r")
    data = [x.replace("\n", " ").split(" ")
            for x in f.read().strip().split("\n\n")]
    f.close()

    passports = list(
        map(
            lambda data: list(
                map(lambda elem: {"code": elem[:3], "value": elem[4:]}, data)
            ),
            data
        )
    )

    print("A: ", countValidPassports(passports.copy(), onlyFields=True))

    print("B: ", countValidPassports(passports.copy(), onlyFields=False))
