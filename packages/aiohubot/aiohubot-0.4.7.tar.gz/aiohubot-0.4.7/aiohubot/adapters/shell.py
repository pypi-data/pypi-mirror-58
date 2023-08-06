import sys
import time
from os import environ
from cmd import Cmd
from asyncio import run_coroutine_threadsafe
from threading import Thread, Event

from aiohubot.plugins import Adapter, TextMessage


class Shell(Adapter):
    _ansi = "\x1b[1;33m%s\x1b[0m"

    def send(self, envelope, *strings):
        print(self._ansi % "reply> ", end="")
        if strings:
            print(*[self._ansi % s for s in strings], sep="\n")
        else:
            print(self._ansi % "are you joking?")
            print(envelope)

    def emote(self, envelope, *strings):
        return [self.send(envelope, f"* {s}") for s in strings]

    def reply(self, envelope, *strings):
        msgs = [f"{envelop['user'].name}: {s}" for s in strings]
        return self.send(envelope, *msgs)

    def run(self):
        cli = Cli()
        cli.prompt = f"{self.robot.name}> "
        cli.robot = self.robot
        cli.shell, cli._loop = self, self._loop
        self.cli = cli
        self.th = Thread(target=cli.cmdloop)
        self.th.start()
        return self.emit("connected")

    def shutdown(self):
        self.robot.shutdown()
        return sys.exit(0)


class Cli(Cmd):
    evt = Event()

    def do_msg(self, msg):
        user_id = environ.get("HUBOT_SHELL_USER_ID", "1")
        username = environ.get("HUBOT_SHELL_USER_NAME", "Shell")
        user = self.robot.brain.user_for_id(user_id,
                                            **dict(name=username, room="Shell"))
        coro = self.shell.receive(TextMessage(user, msg, "message_id"))
        f = run_coroutine_threadsafe(coro, loop=self._loop)
        f.add_done_callback(lambda f: self.evt.set())
        self.evt.wait()
        self.evt.clear()
        self.lastcmd = ""

    def do_quit(self, msg):
        print("\n*** Exiting ... ***\n")
        return True

    def do_EOF(self, msg):
        print()
        return self.do_quit(msg)

    def postloop(self):
        self._loop.call_later(0, self.shell.shutdown)

    do_exit = do_quit


use = Shell
