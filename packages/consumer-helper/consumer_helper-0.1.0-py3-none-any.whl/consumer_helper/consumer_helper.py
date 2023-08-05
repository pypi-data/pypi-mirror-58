import threading

from confluent_kafka import Consumer


class ConsumeLoop:
    instance_list = []

    def __init__(self, consumer: Consumer, on_message: callable, on_exit: callable = None):
        self.consumer = consumer
        self.on_message = on_message
        self.on_exit = on_exit
        self.loop_thread = threading.Thread(target=self.loop)
        self.loop_stop = False
        ConsumeLoop.instance_list.append(self)
        # self.loop_thread.setDaemon(True)

    @staticmethod
    def stop_all_loop(signum, frame):
        for instance in ConsumeLoop.instance_list:
            instance.stop()

    def loop(self):
        while not self.loop_stop:
            msg = self.consumer.poll(1)
            self.on_message(msg)
        if self.on_exit:
            self.on_exit()
        try:
            self.consumer.commit()
            self.consumer.close()
        except RuntimeError:
            pass

    def run(self, blocking=False):
        self.loop_thread.start()
        if blocking:
            self.loop_thread.join()

    def stop(self, sync=False):
        self.loop_stop = True
        if sync:
            self.loop_thread.join()

    def __del__(self):
        if self.loop_thread.is_alive():
            self.loop_thread.join()
