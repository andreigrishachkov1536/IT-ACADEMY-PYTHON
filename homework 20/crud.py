from sqlalchemy import select
from sqlalchemy.orm import Session

from db import engine
from models import User, Order

def create_user(name, email):
    with Session(engine) as session:

        existing_user = session.scalar(select(User).where(User.email == email))

        if existing_user:
            print("Пользователь с таким email уже существует.")
            return

        user = User(
            name=name,
            email=email
        )

        session.add(user)
        session.commit()

        print("Пользователь успешно создан.")


def get_users():
    with Session(engine) as session:
        users = session.scalars(select(User)).all()

        return users


def get_user_by_id(user_id):
    with Session(engine) as session:
        user = session.get(User, user_id)
        return user


def create_order(user_id, product):
    with Session(engine) as session:
        user = session.get(User, user_id)

        if not user:
            print("Пользователь не найден.")
            return

        order = Order(
            product=product,
            status="Новый",
            user_id=user_id
        )

        session.add(order)
        session.commit()

        print("Заказ успешно создан.")


def get_orders():
    with Session(engine) as session:
        orders = session.scalars(select(Order)).all()
        return orders


def get_user_orders(user_id):
    with Session(engine) as session:
        orders = session.scalars(select(Order).where(Order.user_id == user_id)).all()

        return orders


def update_order_status(order_id, new_status):
    with Session(engine) as session:
        order = session.get(Order,order_id)

        if not order:
            print("Заказ не найден.")
            return

        order.status = new_status

        session.commit()

        print("Статус заказа изменён.")


def delete_order(order_id):
    with Session(engine) as session:
        order = session.get(Order,order_id)

        if not order:
            print("Заказ не найден.")
            return

        session.delete(order)
        session.commit()

        print("Заказ удалён.")


def find_order(order_id):
    with Session(engine) as session:
        order = session.get(Order,order_id)

        return order