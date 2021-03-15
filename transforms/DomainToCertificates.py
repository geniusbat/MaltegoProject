from maltego_trx.transform import DiscoverableTransform
import Request
from maltego_trx.entities import Phrase


class DomainToCertificates(DiscoverableTransform):
    """
    Receive DNS name from the client, and resolve to IP address.
    """

    @classmethod
    def create_entities(cls, request, response):
        #Get the requested domain
        domain = request.Value
        #Create the request from the domain
        request = Request.Request("https://crt.sh/?CN=" + str(domain) + "&output=json")
        #Get the result
        results = request.getCertificatesFromText()
        #For each result in the list, create an entity and add properties
        for element in results:
            #Add entity
            entity = response.addEntity(Phrase, domain)
            #Get properties and make them string if necessary
            id = str(element[0])
            name = element[1]
            issuerName = element[2]
            issuerId = str(element[3])
            expiryDate = str(element[4])
            #Add properties to the entity
            entity.addProperty("id", "id", "strict", id)
            entity.addProperty("name", "name", "loose", name)
            entity.addProperty("issuerName", "issuerName", "loose", issuerName)
            entity.addProperty("issuerId", "issuerId", "strict", issuerId)
            entity.addProperty("expiryDate", "expiryDate", "loose", expiryDate)
