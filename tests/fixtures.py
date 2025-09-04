from facture.invoice.port import InvoiceRepositoryPort, DraftInvoice


class InvoiceRepositoryForTest(InvoiceRepositoryPort):
    def __init__(self) -> None:
        self._invoices : dict[str, DraftInvoice] = {}

    def all_invoices(self) -> dict[str, DraftInvoice]:
        return self._invoices

    def feed(self, invoice: DraftInvoice) -> None:
        self._invoices[invoice.invoice_key] = invoice

    def save(self, invoice: DraftInvoice) -> None:
        self._invoices[invoice.invoice_key] = invoice

    def by_id(self, invoice_key: str) -> DraftInvoice:
        return self._invoices[invoice_key]
