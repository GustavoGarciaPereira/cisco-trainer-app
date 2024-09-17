# app/models.py
from sqlalchemy import Table, Column, Integer, String
from .database import metadata

questions = Table(
    "questions",
    metadata,
    Column("id", Integer, primary_key=True, nullable=False),
    Column("question", String, nullable=False),
    Column("option_a", String, nullable=False),
    Column("option_b", String, nullable=False),
    Column("option_c", String, nullable=False),
    Column("option_d", String, nullable=False),
    Column("correct_option", String, nullable=False),
)

scores = Table(
    "scores",
    metadata,
    Column("id", Integer, primary_key=True, nullable=False),
    Column("score", Integer, nullable=False),
    Column("timestamp", String, nullable=False),
)
