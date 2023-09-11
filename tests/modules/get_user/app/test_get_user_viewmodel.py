from src.modules.get_user.app.get_user_viewmodel import GetUserViewModel
from src.shared.domain.entities.user import User


class Test_GetUserViewModel:
    def test_get_user_viewmodel(self):
        user = User(
            name="Mateus",
            agency="0000",
            account="12345-6",
            current_balance=1000.00
        )

        userViewModel = GetUserViewModel(user).to_dict()

        expected = {
            "name": "Mateus",
            "agency": "0000",
            "account": "12345-6",
            "current_balance": 1000.00
        }

        return userViewModel == expected