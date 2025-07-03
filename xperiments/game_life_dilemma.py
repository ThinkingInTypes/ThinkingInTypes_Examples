# game_life_dilemma_textual_fallback.py

from dataclasses import dataclass, field
from random import choice, randint
from typing import Self
import numpy as np
from textual.app import App, ComposeResult
from textual.widgets import Static
from textual.containers import Container
from textual.timer import Timer

C = 0  # Cooperate
D = 1  # Defect
T, R, P, S = 5, 3, 1, 0

PAYOFF_MATRIX = {
    (C, C): (R, R),
    (C, D): (S, T),
    (D, C): (T, S),
    (D, D): (P, P),
}


@dataclass
class Cell:
    alive: bool = False
    strategy: int = field(default_factory=lambda: choice([C, D]))
    score: int = 0

    def play(self, other: Self) -> None:
        if not self.alive or not other.alive:
            return
        s1, s2 = PAYOFF_MATRIX[(self.strategy, other.strategy)]
        self.score += s1
        other.score += s2


@dataclass
class GameOfLifeIPD:
    size: int
    seed_prob: float = 0.2
    grid: np.ndarray = field(init=False)

    def __post_init__(self) -> None:
        self.grid = np.array([
            [Cell(alive=(randint(0, 100) < self.seed_prob * 100)) for _ in range(self.size)]
            for _ in range(self.size)
        ])

    def neighbors(self, x: int, y: int) -> list[tuple[int, int]]:
        deltas = [-1, 0, 1]
        return [
            ((x + dx) % self.size, (y + dy) % self.size)
            for dx in deltas
            for dy in deltas
            if dx != 0 or dy != 0
        ]

    def iterate(self) -> None:
        for row in self.grid:
            for cell in row:
                cell.score = 0

        for x in range(self.size):
            for y in range(self.size):
                cell = self.grid[x, y]
                for nx, ny in self.neighbors(x, y):
                    cell.play(self.grid[nx, ny])

        new_grid = np.empty_like(self.grid, dtype=object)

        for x in range(self.size):
            for y in range(self.size):
                cell = self.grid[x, y]
                neighbors = [self.grid[nx, ny] for nx, ny in self.neighbors(x, y)]
                live_neighbors = [n for n in neighbors if n.alive]
                n_live = len(live_neighbors)

                if cell.alive:
                    if n_live in (2, 3):
                        strategy = max([cell, *live_neighbors], key=lambda c: c.score).strategy
                        new_grid[x, y] = Cell(alive=True, strategy=strategy)
                    else:
                        new_grid[x, y] = Cell(alive=False)
                else:
                    if n_live == 3:
                        strategy = max(live_neighbors, key=lambda c: c.score).strategy
                        new_grid[x, y] = Cell(alive=True, strategy=strategy)
                    else:
                        new_grid[x, y] = Cell(alive=False)

        self.grid = new_grid

    def to_unicode_grid(self) -> str:
        return "\n".join(
            "".join(
                "🟦" if cell.alive and cell.strategy == C else
                "🟥" if cell.alive else
                "⬛"
                for cell in row
            )
            for row in self.grid
        )


class LifeDilemmaApp(App):
    BINDINGS = [("q", "quit", "Quit")]

    def __init__(self, size: int = 20, delay: float = 0.25) -> None:
        super().__init__()
        self.game = GameOfLifeIPD(size)
        self.delay = delay
        self.timer: Timer | None = None

    def compose(self) -> ComposeResult:
        self.output = Static("")
        self.output.styles.height = "auto"
        yield Container(self.output)

    def on_mount(self) -> None:
        self.timer = self.set_interval(self.delay, self.update_display)

    def update_display(self) -> None:
        self.game.iterate()
        self.output.update(self.game.to_unicode_grid())


if __name__ == "__main__":
    LifeDilemmaApp(size=30, delay=0.15).run()
