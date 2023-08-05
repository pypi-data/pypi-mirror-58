class SalebotItemsToItem:
    def __init__(self, tag, count=None):
        """
        Required parameters
        """
        self.method = "POST"
        self.path = "/api/v1/salebot/itemstoitem"

        self.tag = tag
        self.count = count

    def get_body_parameters(self):
        """
            Values of body parameters as a dictionary (name of parameter: value of the parameter).
        """
        p = dict()

        p['tag'] = self.tag
        if self.count is not None:
            p['count'] = self.count

        return p
