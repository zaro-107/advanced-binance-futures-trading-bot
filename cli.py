import typer

from rich.console import Console
from rich.table import Table

from bot.services.execution_service import (
    ExecutionService
)

from bot.core.logger import error_logger

app = typer.Typer()

console = Console()

@app.command()
def trade(
    symbol: str,
    side: str,
    order_type: str,
    quantity: float,
    price: float = None,
    stop_price: float = None
):

    try:

        console.print(
            "\n[bold yellow]Placing Order...[/bold yellow]\n"
        )

        response = ExecutionService.place_trade(
            symbol=symbol,
            side=side,
            order_type=order_type,
            quantity=quantity,
            price=price,
            stop_price=stop_price
        )

        table = Table(title="Order Response")

        table.add_column("Field")
        table.add_column("Value")

        table.add_row(
            "Order ID",
            str(response.get("orderId"))
        )

        table.add_row(
            "Symbol",
            str(response.get("symbol"))
        )

        table.add_row(
            "Status",
            str(response.get("status"))
        )

        table.add_row(
            "Executed Qty",
            str(response.get("executedQty"))
        )

        table.add_row(
            "Avg Price",
            str(response.get("avgPrice"))
        )

        console.print(table)

        console.print(
            "\n[bold green]Order Successful[/bold green]"
        )

    except Exception as e:

        error_logger.error(str(e))

        console.print(
            f"\n[bold red]Error:[/bold red] {e}"
        )

if __name__ == "__main__":

    app()