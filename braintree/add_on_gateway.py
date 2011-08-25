import braintree
from braintree.add_on import AddOn
from braintree.resource_collection import ResourceCollection

class AddOnGateway(object):
    def __init__(self, gateway):
        self.gateway = gateway
        self.config = gateway.config

    def all(self):
        response = self.config.http().get("/add_ons/")
        modifications = {"modification": response["modifications"]}
        return [AddOn(self.gateway, item) for item in ResourceCollection._extract_as_array(modifications, "modification")]