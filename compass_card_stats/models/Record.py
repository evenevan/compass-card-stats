from dataclasses import dataclass
from datetime import datetime, time


@dataclass(frozen=True)
class Record:
    date_time: datetime
    transaction: str
    product: str
    line_item: str
    amount: float
    balance_details: float
    journey_id: int
    location_display: str
    transaction_time: time

    @classmethod
    def from_csv(
        cls,
        date_time,
        transaction,
        product,
        line_item,
        amount,
        balance_details,
        journey_id,
        location_display,
        transaction_time,
        *_,
    ):
        print(amount, float(amount.replace("$", "")))
        return cls(
            date_time=datetime.strptime(date_time, "%b-%d-%Y %I:%M %p"),
            transaction=transaction,
            product=product,
            line_item=line_item,
            amount=float(amount.replace("$", "")),
            balance_details=float(balance_details.replace("$", "")),
            journey_id=journey_id,
            location_display=location_display,
            transaction_time=datetime.strptime(transaction_time, "%I:%M %p").time(),
        )
