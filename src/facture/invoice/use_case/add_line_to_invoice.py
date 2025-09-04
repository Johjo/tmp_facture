from dataclasses import replace

from facture.invoice.port import InvoiceRepositoryPort, DraftLine


class AddLineToInvoice:
    def __init__(self, invoice_repository: InvoiceRepositoryPort):
        self._invoice_repository = invoice_repository

    def execute(self, invoice_key: str, item_key: str, quantity: int, price: float) -> None:
        invoice = self._invoice_repository.by_id(invoice_key)

        self._invoice_repository.save(replace(invoice, lines=[
            DraftLine(item_key=item_key, quantity=quantity, price=price)
        ]))
