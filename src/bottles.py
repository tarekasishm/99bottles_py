from typing import Dict


class Bottles:
    def verse(
        self,
        verse_number: int,
    ) -> str:
        default_verse: str = f"{verse_number} bottles of beer on the wall, {verse_number} bottles of beer.\n" + (
            f"Take one down and pass it around, {verse_number - 1} bottles of beer on the wall."
        )

        verses: Dict[int, str] = {
            2: f"{verse_number} bottles of beer on the wall, {verse_number} bottles of beer.\n" + (
                f"Take one down and pass it around, {verse_number - 1} bottle of beer on the wall."
            ),
            1: f"{verse_number} bottle of beer on the wall, {verse_number} bottle of beer.\n" + (
                f"Take it down and pass it around, no more bottles of beer on the wall."
            ),
            0: f"No more bottles of beer on the wall, no more bottles of beer.\n" + (
                f"Go to the store and buy some more, 99 bottles of beer on the wall."
            ),
        }
 
        return verses.get(verse_number, default_verse)

    def verses(
        self,
        max: int,
        min: int,
    ) -> str:
        return "\n\n".join([
            self.verse(verse_number) for verse_number in range(max, min - 1, -1)
        ])

    def song(self) -> None:
        return self.verses(99, 0)
