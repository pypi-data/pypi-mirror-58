from .consumer_helper import ConsumeLoop
import signal

signal.signal(signal.SIGTERM, ConsumeLoop.stop_all_loop)
