from ..base import SellAPI


class NegotiationAPI(SellAPI):
    api_name = 'negotiation'
    resource = ''


class FindEligibleItems(NegotiationAPI):
    method_type = 'GET'
    url_postfix = 'find_eligible_items'
    allowed_query_params = ['limit', 'offset']


class SendOfferToInterestedBuyers(NegotiationAPI):
    method_type = 'POST'
    url_postfix = 'send_offer_to_interested_buyers'
