from facture.invoice.port import DraftInvoice
from facture.invoice.use_case.create_invoice import CreateInvoice
from tests.fixtures import InvoiceRepositoryForTest


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
