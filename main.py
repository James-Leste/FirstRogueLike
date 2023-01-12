import tcod

from actions import EscapeAction, MovementAction
from input_handler import EventHandler


def main() -> None:
    # Size of the window
    screen_width = 80
    screen_height = 50

    player_x = int(screen_width / 2)
    player_y = int(screen_height / 2)

    # import the tile set file 材质
    tileset = tcod.tileset.load_tilesheet(
        "characters.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )

    # add a event handler
    event_handler = EventHandler()

    # define context 上下文
    with tcod.context.new_terminal(
            screen_width,  # width
            screen_height,  # height
            tileset=tileset,  # tile set
            title="Dungeon",  # title of the window
            vsync=True,
    ) as context:

        # root_console is the game itself
        root_console = tcod.Console(screen_width, screen_width, order="F")

        # Game loop which never ends
        while True:
            root_console.print(x=player_x, y=player_y, string="@")  # define the location of @

            context.present(root_console)  # put the game on the window

            root_console.clear()

            for event in tcod.event.wait():
                action = event_handler.dispatch(event)

                if action is None:
                    continue

                if isinstance(action, MovementAction):
                    player_x += action.dx
                    player_y += action.dy

                elif isinstance(action, EscapeAction):
                    raise SystemExit()


if __name__ == "__main__":
    main()
