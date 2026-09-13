from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str] = mapped_column(String(100))

    email: Mapped[str] = mapped_column(String(150),unique=True)

    orders: Mapped[list["Order"]] = relationship(back_populates="user")

    def __str__(self):
        return (
            f"ID: {self.id} | "
            f"Имя: {self.name} | "
            f"Email: {self.email}"
        )


class Order(Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(primary_key=True)

    product: Mapped[str] = mapped_column(String(200))

    status: Mapped[str] = mapped_column(String(50),default="Новый")

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"),nullable=False)

    user: Mapped["User"] = relationship(back_populates="orders")

    def __str__(self):
        return (
            f"ID заказа: {self.id} | "
            f"Товар: {self.product} | "
            f"Статус: {self.status} | "
            f"ID пользователя: {self.user_id}"
        )