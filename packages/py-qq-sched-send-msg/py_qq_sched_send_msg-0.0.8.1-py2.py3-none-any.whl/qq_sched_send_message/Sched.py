from apscheduler.schedulers.blocking import BlockingScheduler


class Schedar:
    schedar = BlockingScheduler()

    @classmethod
    def add_task(cls, func, id, time):
        Schedar.schedar.add_job(func, "interval", seconds=time, id=id)

    @classmethod
    def run(cls):
        Schedar.schedar.start()

    @classmethod
    def remove(cls, id):
        Schedar.schedar.remove_job(id)
