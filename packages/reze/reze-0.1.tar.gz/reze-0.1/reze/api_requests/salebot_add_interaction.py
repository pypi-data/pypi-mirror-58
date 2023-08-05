class SalebotAddInteraction:
    def __init__(self, user_id, tag, cat_id, event, item_id=None, value=None, created_time=None):
        """
        Required parameters
        """
        self.method = "POST"
        self.path = "/api/v1/salebot/interactions"

        self.userId = user_id
        self.tag = tag
        self.catId = cat_id
        self.event = event
        self.itemId = item_id
        self.value = value
        self.createdTime = created_time

    def get_body_parameters(self):
        """
            Values of body parameters as a dictionary (name of parameter: value of the parameter).
        """
        p = dict()
        p['userId'] = self.userId
        p['tag'] = self.tag
        p['catId'] = self.catId
        p['event'] = self.event
        if self.itemId is not None:
            p['itemId'] = self.itemId
        if self.value is not None:
            p['value'] = self.value
        if self.createdTime is not None:
            p['createdTime'] = self.createdTime
        return p
