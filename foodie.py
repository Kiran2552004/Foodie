import typer
from peewee import *
from shop.models import create_tables
from shop.services.authentication import UserSession, AuthenticationService
from shop.services.restaurant import RestaurantService
from shop.exceptions import ShopYooExit

from shop.commands import restaurant, users, cart, order

app = typer.Typer()

user_session = users.user_session
auth = users.auth

app.add_typer(users.app, name="users")
app.add_typer(restaurant.app, name="restaurant")
app.add_typer(cart.app, name="cart")
app.add_typer(order.app, name="order")


if __name__ == "__main__":
    create_tables()
    with user_session:
        try:
            auth.load_session()
            app()
        except Exception as e:
            pass
