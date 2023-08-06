from __future__ import annotations

from typing import List, Dict
from enum import IntEnum, unique


@unique
class OfferType(IntEnum):
    HIGH = 0
    NORMAL = 1
    LOW = 2

    def __str__(self):
        return str(self.value)


class Offer(object):
    """docstring for Round."""

    def __init__(self):
        super(Offer, self).__init__()

        self.type: OfferType = OfferType.NORMAL
        self.accepted: bool = False
        self.amount: int = 0

    def load(self, obj: Dict):
        self.type = obj.get('type', OfferType.NORMAL)
        self.accepted = obj.get('accepted', False)
        self.amount = obj.get('amount', 0)

    def save(self) -> Dict:
        offer_obj = {}
        offer_obj['type'] = self.type
        offer_obj['accepted'] = self.accepted
        offer_obj['amount'] = self.amount

        return offer_obj


def load(obj: Dict) -> List[Offer]:
    offers = []
    for offer_obj in obj:
        offer = Offer()
        offer.load(offer_obj)
        offers.append(offer)
    return offers


def save(offers: List[Offer]) -> List:
    obj = []
    for offer in offers:
        obj.append(offer.save())
    return obj
