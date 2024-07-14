RESOURCE_DOES_NOT_EXIST_MESSAGE = "Requested resource does not exist"
RESOURCE_ALREADY_EXIST = "Resource with that name already exist"


class NoResourceValue(Exception):
    pass


class WrongUrlResourceNotFound(Exception):
    pass


class DataParserNotFound(Exception):
    pass
