from __future__ import annotations

import datetime
from typing import List, Dict
from enum import IntEnum, unique

import gefragt_gejagt.question
import gefragt_gejagt.offer as offer


DEFAULT_OFFER_HIGH_FACTOR = 3
DEFAULT_OFFER_LOW_FACTOR = 0.2


@unique
class RoundType(IntEnum):
    PLAYER = 1
    FINAL = 2

    def __str__(self):
        return str(self.value)


class Round(object):
    def __init__(self):
        super(Round, self).__init__()

        self.id: int
        self.won: bool = False
        self.type: RoundType = RoundType.PLAYER
        self.finalTime: List[Dict] = []
        self.player: Player = None
        self.team: Team = None
        self.questions: List[Question] = []
        self.offers: List[Offer] = []
        self.correctionOffset: int = 0

    @property
    def level(self) -> int:
        levels = []
        for player in self.players:
            levels.append(player.level)
        return max(levels)

    @property
    def acceptedOffer(self) -> Offer:
        for offer in self.offers:
            if offer.accepted:
                return offer
        return None

    @property
    def correctAnswersChaser(self) -> int:
        count = 0
        for question in self.questions:
            if question.answerChaser == 0 and (
                    question.type == gefragt_gejagt.question.QuestionType.CHASE or (
                    self.team is not None and question.type == gefragt_gejagt.question.QuestionType.SIMPLE)):
                count += 1
            elif self.team is not None and question.type == gefragt_gejagt.question.QuestionType.SIMPLE and question.answerPlayer == 0 and question.answerChaser is not None:
                count -= 1
        return count

    @property
    def correctAnswersPlayer(self) -> int:
        count = 0
        for question in self.questions:
            if (self.type == RoundType.PLAYER and question.answerPlayer == 0 and question.type == gefragt_gejagt.question.QuestionType.CHASE) or (
                    self.type == RoundType.FINAL and question.answerPlayer == 0 and question.answerChaser is None and question.type == gefragt_gejagt.question.QuestionType.SIMPLE):
                count += 1
        return count

    @property
    def playerStartOffset(self) -> int:
        if self.type == RoundType.FINAL:
            return len(self.team.qualified_players)
        else:
            if len(self.offers) != 0:
                if self.offers[0].accepted:
                    return 2
                if self.offers[2].accepted:
                    return 4
            return 3

    @property
    def questionsLeftForPlayer(self) -> int:
        return 7 - self.correctAnswersPlayer - self.playerStartOffset

    @property
    def chaserFinalWon(self) -> boolean:
        return self.correctAnswersChaser >= (
            self.playerStartOffset +
            self.correctAnswersPlayer)

    @property
    def timePassed(self):
        lastStarted = None
        passedTime = datetime.timedelta()

        if not len(self.finalTime):
            return 0
        for timespan in self.finalTime:
            if not timespan.get('end'):
                lastStarted = timespan['start']
            else:
                passedTime += timespan['end'] - timespan['start']

        if lastStarted:
            return passedTime + (datetime.datetime.now() - lastStarted)
        else:
            return passedTime

    def setup_offers(self, points: int):
        high_offer = offer.Offer()
        high_offer.type = offer.OfferType.HIGH
        high_offer.amount = round(
            points * DEFAULT_OFFER_HIGH_FACTOR)

        normal_offer = offer.Offer()
        normal_offer.type = offer.OfferType.NORMAL
        normal_offer.amount = points

        low_offer = offer.Offer()
        low_offer.type = offer.OfferType.LOW
        low_offer.amount = round(
            points * DEFAULT_OFFER_LOW_FACTOR)

        self.offers = [
            high_offer,
            normal_offer,
            low_offer
        ]

    def load(self, obj: Dict, game):
        self.id = obj['id']
        self.won = obj.get('won', False)
        self.type = obj.get('type', RoundType.PLAYER)
        self.correctionOffset = obj.get('correctionOffset', 0)

        if obj.get('offers'):
            self.offers = gefragt_gejagt.offer.load(obj['offers'])
        if obj.get('team'):
            self.team = game.get_team_by_id(obj['team']['id'])
        if obj.get('player'):
            self.player = game.get_player_by_id(obj['player']['id'])
        if obj.get('questions'):
            questions = []
            for question_obj in obj['questions']:
                question = game.get_question_by_id(question_obj['id'])
                questions.append(question)
            self.questions = questions

        if obj.get('finalTime'):
            for span in obj.get('finalTime'):
                if span.get('end'):
                    self.finalTime.append({'start': datetime.datetime.fromisoformat(
                        span['start']), 'end': datetime.datetime.fromisoformat(span['end'])})
                else:
                    self.finalTime.append(
                        {'start': datetime.datetime.fromisoformat(span['start'])})

    def save(self) -> Dict:
        round_obj = {}
        round_obj['id'] = self.id
        round_obj['won'] = self.won
        round_obj['type'] = self.type
        if self.player:
            round_obj['player'] = self.player.save()
        if self.team:
            round_obj['team'] = self.team.save()
        round_obj['questions'] = gefragt_gejagt.question.save(self.questions)
        round_obj['offers'] = offer.save(self.offers)
        if self.acceptedOffer:
            round_obj['acceptedOffer'] = self.acceptedOffer.save()

        round_obj['correctAnswersChaser'] = self.correctAnswersChaser
        round_obj['correctAnswersPlayer'] = self.correctAnswersPlayer
        round_obj['playerStartOffset'] = self.playerStartOffset
        round_obj['questionsLeftForPlayer'] = self.questionsLeftForPlayer
        round_obj['correctionOffset'] = self.correctionOffset

        round_obj['finalTime'] = []
        for span in self.finalTime:
            if span.get('end'):
                round_obj['finalTime'].append(
                    {'start': span['start'].__str__(), 'end': span['end'].__str__()})
            else:
                round_obj['finalTime'].append(
                    {'start': span['start'].__str__()})

        return round_obj


def load(obj: Dict, game) -> List[Round]:
    rounds = []
    for round_obj in obj:
        round = Round()
        round.load(round_obj, game)
        rounds.append(round)
    return rounds


def save(rounds: List[Round]) -> List:
    obj = []
    for round in rounds:
        obj.append(round.save())
    return obj
