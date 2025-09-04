from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass()
class DraftLine:
    item_key: str
    quantity: int
    price: float


@dataclass
class DraftInvoice:
    invoice_key: str
    customer_key: str
    lines: list[DraftLine]


class InvoiceRepositoryPort(ABC):
    @abstractmethod
    def save(self, invoice: DraftInvoice) -> None: ...

    @abstractmethod
    def by_id(self, invoice_key: str) -> DraftInvoice: ...


