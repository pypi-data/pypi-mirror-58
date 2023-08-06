"""Models for key nouns in Skrate, namely tricks, attempts, games."""
import datetime
import random
from typing import Any, List, Mapping, Optional

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import text

from skrate import game_logic

# Our app database
db = SQLAlchemy()

# Game feed parameters
_GAME_FEED_LENGTH = 4


def init_db_connec(app: Flask) -> None:
    """Connect to persistence layer for Skrate app.
    
    Args:
        app: The Flask web server application object

    """
    db.init_app(app)


def create_db_tables(app: Flask) -> None:
    """Create or update table schemas based on models defined in this file.

    Args:
        app: The Flask web server application object

    """
    with app.app_context():
        db.create_all()


def drop_db_tables(app: Flask) -> None:
    """Drop all tables, useful in test (ensure URI contains TEST).

    Args:
        app: The Flask web server application object

    Raises:
        ValueError: if you try to run this on production config

    """
    if not "test" in app.config["SQLALCHEMY_DATABASE_URI"]:
        raise ValueError("drop_all() only permitted on test db, use psql.")
    with app.app_context():
        db.drop_all()


class Trick(db.Model):  # type: ignore
    """A type of trick (i.e., kickflip) - **NOT** a specific attempt of one."""

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False)
    attempts = db.relationship("Attempt", backref="trick", lazy=True)


class Attempt(db.Model):  # type: ignore
    """An attempt at a trick, with landed or not result."""

    id = db.Column(db.Integer, primary_key=True)
    trick_id = db.Column(db.Integer, db.ForeignKey("trick.id"), nullable=False)
    game_id = db.Column(db.Integer, db.ForeignKey("game.id"))
    user = db.Column(db.String(16), nullable=False)  # Note can be past_<user>
    landed = db.Column(db.Boolean, nullable=False)
    time_of_attempt = db.Column(db.DateTime, default=datetime.datetime.utcnow)


class Game(db.Model):  # type: ignore
    """A single game of SKATE against your past self."""

    id = db.Column(db.Integer, primary_key=True)
    attempts = db.relationship("Attempt", backref="game", lazy=True)
    user = db.Column(db.String(16), nullable=False)
    start_time = db.Column(db.DateTime, default=datetime.datetime.utcnow)


def record_attempt(app: Flask, user: str, trick_id: int, landed: bool,
                   game_id: Optional[int]) -> None:
    """Record an attempt by user (or fake attempt as part of a game)

    Args:
        app: The Flask web server application object
        user: the user attempting the trick (may be past_someone)
        trick_id: id of the trick being attempted
        landed: whether or not it was landed successfully
        game_id: id of which game it's part of, if any

    """
    with app.app_context():
        att = Attempt(trick_id=trick_id,
                      game_id=game_id,
                      user=user,
                      landed=landed)
        db.session.add(att)
        db.session.commit()
        app.logger.info("Committed new attempt with id %s", att.id)


def opponent_response_if_any(app: Flask, user: str,
                             game_id_if_any: Optional[int]) -> bool:
    """If in an ongoing game (not completed), past self needs to respond.

    Args:
        app: the Flask web server application object
        user: the name of the current user (not past_ self)
        game_id_if_any: integer game id if we're in one

    Returns:
        Whether or not the game is ongoing

    """
    if game_id_if_any is None:
        return False

    with app.app_context():
        game = Game.query.filter_by(id=game_id_if_any).one()
        game_state = get_game_state(game.attempts, user)
        if not game_state.is_ongoing():
            return False

        # Opponent to choose a trick - if on a challenge, must be same
        trick_to_try = game_state.challenging_move_id
        if trick_to_try is None:
            # If not on a challenge, logic is do user's best trick next
            trick_to_try = game_logic.game_trick_choice(
                app, user, game_state.trick_ids_used_up, db)

        # Figure whether opponent lands
        odds = game_logic.get_odds(app, user, trick_to_try, db)
        land = random.uniform(0, 1) <= odds
        record_attempt(app, "past_" + user, trick_to_try, land, game_id_if_any)

        # Refresh game with any opponent attempt above, and see if game is finished
        game_updated = Game.query.filter_by(id=game_id_if_any).one()
        game_state_updated = get_game_state(game_updated.attempts, user)
        return game_state_updated.is_ongoing()


def start_game(app: Flask, user: str) -> int:
    """Start a new game of SKATE with current user, return game_id.

    Args:
        app: the Flask web server application object
        user: the name of the current user

    """
    with app.app_context():
        game = Game(attempts=[], user=user)
        db.session.add(game)
        db.session.commit()
        app.logger.info("Started new game with id %s", game.id)

    return game.id


def get_trick_view_params(user: str, trick: Trick) -> Mapping[str, Any]:
    """Get parameters to render landing page view of trick and stats on it.

    Args:
        user: the currente Skrate user
        trick: the Trick object representing the type of trick

    """

    user_attempts = Attempt.query.filter_by(user=user,
                                            trick_id=trick.id).count()
    user_lands = Attempt.query.filter_by(user=user,
                                         trick_id=trick.id,
                                         landed=True).count()
    return {
        "attempts": user_attempts,
        "lands": user_lands,
        "name": trick.name,
        "id": trick.id
    }


def get_all_trick_infos(app: Flask, user: str) -> List[Mapping[str, Any]]:
    """Get list of all trick infos and user stats on them, ordered by land rate.
    
    Args:
        app: the Flask server application object
        user: user current logged in in session

    """
    all_tricks = Trick.query.all()
    trick_odds_dict = game_logic.get_odds_lookup_dict(app, user, db)
    tricks_sorted = sorted(all_tricks,
                           key=lambda trick: trick_odds_dict[trick.id],
                           reverse=True)
    return [get_trick_view_params(user, trick) for trick in tricks_sorted]


def get_skate_letters_colors(score: int) -> List[Mapping[str, str]]:
    """Get list of elements for render like {"letter": "S", "color" white"}.

    Args:
        score: integer from 0-5 indicating how many letters earned.

    """
    return [{
        "color": "black" if i < score else "white",
        "letter": letter
    } for i, letter in enumerate(game_logic.LETTERS)]


def get_latest_game_params(app: Flask, user: str,
                           game_id: int) -> Mapping[str, Any]:
    """Get parameters to render the game view.

    Args:
        app: the server flask application object
        user: current user
        game_id: current game id

    """
    with app.app_context():
        latest_game = Game.query.filter(Game.user == user, Game.id == game_id) \
                .order_by(Game.start_time).first()
        if latest_game is None:
            turn_lines = [{
                "classes": "list-group-item",
                "text": "Hit 'New Game' to play!"
            }]
            letters_colors = {
                "new": get_skate_letters_colors(0),
                "past": get_skate_letters_colors(0)
            }
        else:
            # This utilizes the actual game rules to generate output so far
            game_state = get_game_state(latest_game.attempts, user)
            turn_lines = [{
                "classes": "list-group-item " + msg.msg_type,
                "text": msg.msg_text
            } for msg in game_state.status_feed]
            letters_colors = {
                "new": get_skate_letters_colors(game_state.user_score),
                "past": get_skate_letters_colors(game_state.opponent_score)
            }

        return {"turn_lines": turn_lines, "letters_colors": letters_colors}


def get_game_state(attempts: List[Attempt],
                   user_name: str) -> game_logic.GameState:
    """Calculate the game state given ordered list of attempts.

    Args:
        attempts: the attempts by either user in this game
        user_name: the user name logged in as

    """
    # Bit wasteful to do this each time want it, but still plenty fast
    sorted_attempts = sorted(attempts, key=lambda a: a.time_of_attempt)

    # Sanity check, confirm alternating turns starting with user
    assert all(a.user == user_name
               for a in sorted_attempts[::2]), game_logic._TURN_FAULT
    assert all(a.user != user_name
               for a in sorted_attempts[1::2]), game_logic._TURN_FAULT

    # Build up state and return it... note if no attempts yet that's ok
    game_state = game_logic.GameState(user_name)
    for attempt in sorted_attempts:
        if game_state.apply_attempt(attempt.trick_id, attempt.trick.name,
                                    attempt.landed, attempt.user):
            break

    return game_state
