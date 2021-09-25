from PollModule import PollModule
from SarcasmModule import SarcasmModel as SarcasmModule
from StatsModule import StatsModule
from Connect4Module import Connect4

states = {
    "sarcasm" : SarcasmModule(), 
    "stats" : StatsModule(),
    "connect4" : Connect4(),
    "poll" : PollModule(),
}