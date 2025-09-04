from facture.invoice.port import DraftInvoice, DraftLine
from facture.invoice.use_case.add_line_to_invoice import AddLineToInvoice
from tests.fixtures import InvoiceRepositoryForTest


def test_add_line_to_invoice() -> None:
    invoice_repository = InvoiceRepositoryForTest()
    invoice_repository.feed(DraftInvoice(invoice_key="draft_1", customer_key="customer_1", lines=[]))
    sut = AddLineToInvoice(invoice_repository=invoice_repository)

    sut.execute(invoice_key="draft_1", item_key="item_1", quantity=1, price=100.0)

    assert invoice_repository.all_invoices() == {
        "draft_1": DraftInvoice(invoice_key="draft_1", customer_key="customer_1", lines=[
            DraftLine(item_key="item_1", quantity=1, price=100.0)])}
