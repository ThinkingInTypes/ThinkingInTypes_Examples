from dataclasses import dataclass


@dataclass
class FibonacciRatio:
    sequence_length: int

    def generate_fibonacci(self) -> list[int]:
        fib = [1, 1]
        for _ in range(2, self.sequence_length):
            fib.append(fib[-1] + fib[-2])
        return fib

    def calculate_relative_growth(
        self, fib: list[int]
    ) -> list[float]:
        growth_rates = []
        for prev, current in zip(fib[:-1], fib[1:]):
            growth_rates.append(current / prev)
        return growth_rates

    def show_stabilization(self):
        fib_sequence = self.generate_fibonacci()
        growth_rates = self.calculate_relative_growth(
            fib_sequence
        )

        print(
            f"{'Step':>4} | {'Fib Number':>10} | {'Rel. Growth':>12}"
        )
        print("-" * 33)
        for i, (num, rate) in enumerate(
            zip(fib_sequence[1:], growth_rates), start=1
        ):
            print(f"{i:4d} | {num:10d} | {rate:12.8f}")


if __name__ == "__main__":
    fib_ratio = FibonacciRatio(sequence_length=20)
    fib_ratio.show_stabilization()
