from dataclasses import dataclass, replace


@dataclass
class DraftInvoice:
    invoice_key: str
    customer_key: str
    lines: list


class InvoiceRepositoryForTest:
    def __init__(self):
        self._invoices = {}

    def all_invoices(self) -> list[DraftInvoice]:
        return self._invoices

    def feed(self, invoice):
        self._invoices[invoice.invoice_key] = invoice

    def save(self, invoice: DraftInvoice) -> None:
        self._invoices[invoice.invoice_key] = invoice

    def by_id(self, invoice_key: str) -> DraftInvoice:
        return self._invoices[invoice_key]


class CreateInvoice:
    def __init__(self, invoice_repository: InvoiceRepositoryForTest) -> None:
        self._invoice_repository = invoice_repository

    def execute(self, customer_key: str) -> None:
        self._invoice_repository.save(DraftInvoice(invoice_key="draft_1", customer_key=customer_key, lines=[]))


def test_create_invoice_for_a_customer() -> None:
    # GIVEN
    invoice_repository = InvoiceRepositoryForTest()
    sut = CreateInvoice(invoice_repository=invoice_repository)

    # WHEN
    sut.execute(customer_key="customer_1")

    # THEN
    assert invoice_repository.all_invoices() == {
        "draft_1": DraftInvoice(invoice_key="draft_1", customer_key="customer_1", lines=[])
    }


class AddLineToInvoice:
    def __init__(self, invoice_repository: InvoiceRepositoryForTest):
        self._invoice_repository = invoice_repository

    def execute(self, invoice_key: str, item_key: str, quantity: int, price: float):
        invoice = self._invoice_repository.by_id(invoice_key)

        self._invoice_repository._invoices = [replace(invoice, lines=[
            DraftLine(item_key=item_key, quantity=quantity, price=price)
        ])]


@dataclass()
class DraftLine:
    item_key: str
    quantity: int
    price: float


def test_add_line_to_invoice() -> None:
    invoice_repository = InvoiceRepositoryForTest()
    invoice_repository.feed(DraftInvoice(invoice_key="draft_1", customer_key="customer_1", lines=[]))
    sut = AddLineToInvoice(invoice_repository=invoice_repository)

    sut.execute(invoice_key="draft_1", item_key="item_1", quantity=1, price=100.0)

    assert invoice_repository.all_invoices() == [DraftInvoice(invoice_key="draft_1", customer_key="customer_1", lines=[
        DraftLine(item_key="item_1", quantity=1, price=100.0)])]
