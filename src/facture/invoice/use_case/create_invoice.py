from facture.invoice.port import InvoiceRepositoryPort, DraftInvoice


class CreateInvoice:
    def __init__(self, invoice_repository: InvoiceRepositoryPort) -> None:
        self._invoice_repository = invoice_repository

    def execute(self, customer_key: str) -> None:
        self._invoice_repository.save(DraftInvoice(invoice_key="draft_1", customer_key=customer_key, lines=[]))
