from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from sleeper.enum.TransactionStatus import TransactionStatus
from sleeper.enum.TransactionType import TransactionType
from sleeper.model.DraftPick import DraftPick
from sleeper.model.FAABTransaction import FAABTransaction
from sleeper.model.TransactionSettings import TransactionSettings


@dataclass(kw_only=True)
class Transaction:
    adds: list[dict[str, int]]
    consenter_ids: list[int]
    created: int
    creator: str
    draft_picks: list[DraftPick]
    drops: list[dict[str, int]]
    roster_ids: list[int]
    settings: TransactionSettings
    status: TransactionStatus
    status_updated: int
    transaction_id: str
    type: TransactionType
    waiver_budget: list[FAABTransaction]
    leg: int
    metadata: Any  # not sure what this is

    @staticmethod
    def from_dict(transaction_dict: dict) -> Transaction:
        return Transaction(
            type=TransactionType.from_str(transaction_dict.get("type")),
            transaction_id=transaction_dict.get("transaction_id"),
            status_updated=transaction_dict.get("status_updated"),
            status=TransactionStatus.from_str(transaction_dict.get("status")),
            settings=TransactionSettings.from_dict(transaction_dict.get("settings")),
            roster_ids=transaction_dict.get("roster_ids"),
            leg=transaction_dict.get("leg"),
            adds=transaction_dict.get("adds"),
            drops=transaction_dict.get("drops"),
            draft_picks=DraftPick.from_dict_list(transaction_dict.get("draft_picks")),
            creator=transaction_dict.get("creator"),
            created=transaction_dict.get("created"),
            consenter_ids=transaction_dict.get("consenter_ids"),
            waiver_budget=FAABTransaction.from_dict_list(transaction_dict.get("waiver_budget")),
            metadata=transaction_dict.get("metadata"),
        )

    @staticmethod
    def from_dict_list(transaction_dict_list: list) -> list[Transaction]:
        transactions = list()
        for transaction_dict in transaction_dict_list:
            transactions.append(Transaction.from_dict(transaction_dict))
        return transactions

    def to_dict(self) -> dict:
        return {
            "adds": self.adds if self.adds is not None else [],
            "consenter_ids": self.consenter_ids if self.consenter_ids is not None else [],
            "created": self.created,
            "creator": self.creator,
            "draft_picks": [draft_pick.to_dict() for draft_pick in self.draft_picks] if self.draft_picks is not None else [],
            "drops": self.drops if self.drops is not None else [],
            "roster_ids": self.roster_ids if self.roster_ids is not None else [],
            "settings": self.settings.to_dict() if self.settings is not None else None,
            "status": self.status.value if self.status is not None else None,
            "status_updated": self.status_updated,
            "transaction_id": self.transaction_id,
            "type": self.type.value if self.type is not None else None,
            "waiver_budget": [faab.to_dict() for faab in self.waiver_budget] if self.waiver_budget is not None else [],
            "leg": self.leg,
            "metadata": self.metadata,
        }
