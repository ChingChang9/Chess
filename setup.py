import cx_Freeze

executables = [cx_Freeze.Executable("chess.py")]

cx_Freeze.setup(
    name = "Ching's Chess Game",
    author = "Ching Chang",
    author_email = "chingtheprogrammer@icloud.com",
    version = "0.1",
    license = "GNU General Public License v3.0",
    options = {"build_exe": {"packages": ["pygame"],
    "include_files": ["License.txt", "GNU GENERAL PUBLIC LICENSE V3.0.txt",
    "images/aura.png", "images/blackBishop.png", "images/blackKing.png",
    "images/blackKnight.png", "images/blackPawn.png", "images/blackQueen.png",
    "images/blackRook.png","images/chessBoard.jpg", "images/gameIcon.png",
    "images/speaker_off.png", "images/speaker_on.png", "images/whiteBishop.png",
    "images/whiteKing.png", "images/whiteKnight.png", "images/whitePawn.png",
    "images/whiteQueen.png", "images/whiteRook.png", "sounds/boi.wav",
    "sounds/kahoot.wav", "sounds/ohh.wav", "sounds/oof.wav",
    "sounds/queen_dead.wav"]}},
    executables = executables
)
