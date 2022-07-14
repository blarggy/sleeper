from sleeper.api.APIClient import APIClient
from sleeper.model.User import User
from sleeper.util.ConfigReader import ConfigReader


class UserAPIClient(APIClient):
    __USER_ROUTE = ConfigReader.get("api", "user_route")
    __USERS_ROUTE = ConfigReader.get("api", "users_route")
    __LEAGUE_ROUTE = ConfigReader.get("api", "league_route")

    @classmethod
    def get_user(cls, *, username: str = None, user_id: str = None) -> User:
        if username is None and user_id is None:
            raise ValueError("Must pass 'username' or 'user_id'.")
        user_arg = username if username is not None else user_id
        url = cls._build_route(cls.__USER_ROUTE, f"{user_arg}")
        return User.from_dict(cls._get(url))

    @classmethod
    def get_users_in_league(cls, *, league_id: str) -> list[User]:
        url = cls._build_route(cls.__LEAGUE_ROUTE, league_id, cls.__USERS_ROUTE)
        return User.from_dict_list(cls._get(url))
