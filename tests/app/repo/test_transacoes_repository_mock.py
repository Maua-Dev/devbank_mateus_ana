import pytest
from src.app.entities.transacoes import Transacoes
from src.app.repo.transacoes_repository_mock import ItemRepositoryMock


class Test_ItemRepositoryMock:
    def test_get_all_transactions(self):
        repo = ItemRepositoryMock()

        transacoes = repo.get_all_transactions()

        expected_transacoes = repo.transacoes

        assert transacoes == expected_transacoes