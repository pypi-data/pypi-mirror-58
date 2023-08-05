import logging


class Check:
    """
    Takes a list of DataObject and runs the function on the entire list
    """
    def __init__(self, name: str, funct) -> None:
        self.name = name
        self.funct = funct

    def run(self, data_lst, metadata=None) -> bool:
        logging.debug("running check {}".format(self.name))
        return self.funct(data_lst, metadata)


class CheckEach(Check):
    """
    Takes a list of DataObject and runs the function on each DataObject within the list
    """
    def __init__(self, name: str, funct) -> None:
        super().__init__(name, funct)

    def run(self, data_lst, metadata) -> bool:
        logging.debug("running check all {}".format(self.name))
        for obj in data_lst:
            ok = self.funct(obj, metadata)
            if ok:
                continue
            logging.debug("check {} failed with object date {} and value {}"
                          .format(self.name, obj.date.value, obj.number.value))
            return False
        return True
