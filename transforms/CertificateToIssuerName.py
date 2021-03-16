from maltego_trx.transform import DiscoverableTransform
from maltego_trx.entities import Phrase


class CertificateToIssuerName(DiscoverableTransform):
    @classmethod
    def create_entities(cls, request, response):
        entity = response.addEntity(Phrase, "Issuer name")
        try:
            issuerName = request.getProperty("issuerName")
            entity.addProperty("issuerName", "issuerName", "loose", issuerName)
        except ValueError:
            entity.addProperty("issuerName", "issuerName", "loose", "N/A")
