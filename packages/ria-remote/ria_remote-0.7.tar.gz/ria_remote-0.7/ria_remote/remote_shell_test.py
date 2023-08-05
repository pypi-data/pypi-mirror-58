from datalad.support.sshconnector import SSHManager
import subprocess
import threading
from queue import Queue, Empty
from io import StringIO, BufferedReader, BufferedWriter, BufferedRWPair, BufferedRandom, BytesIO


class NonBlockingStreamReader(object):

    def __init__(self, stream):
        """
        Parameter
        ---------
        stream: the stream to read from.
                (i.e. a process' stdout or stderr)
        """

        self._s = stream
        self._q = Queue()

        def _populateQueue(stream, queue):
            """
            Collect lines from 'stream' and put them in 'quque'.
            """

            while True:
                content = stream.read1()
                if content:
                    queue.put(content)
                else:
                    raise UnexpectedEndOfStream

        self._t = threading.Thread(target=_populateQueue, args=(self._s, self._q))
        self._t.daemon = True
        self._t.start()

    def readline(self, timeout=None):
        try:
            return self._q.get(block=timeout is not None,
                               timeout=timeout)
        except Empty:
            return None


class UnexpectedEndOfStream(Exception):
    pass


class RemoteShellWrapper(object):

    def __init__(self):
        ssh = SSHManager().get_connection('datalad-test')
        ssh.open()

        # start remote shell
        cmd = ['ssh'] + ssh._ctrl_options + [ssh.sshri.as_str()]
        print("Start command: {}".format(' '.join(cmd)))
        self.proc = subprocess.Popen(cmd, stderr=subprocess.PIPE, stdout=subprocess.PIPE, stdin=subprocess.PIPE)

        self.stdout_reader = NonBlockingStreamReader(self.proc.stdout)
        self.stderr_reader = NonBlockingStreamReader(self.proc.stderr)


        #
        # #
        # self._stdout_buffer = BytesIO()
        # self._stdout_thread = threading.Thread(target=self._readerthread,
        #                                        args=(self.proc.stdout, self._stdout_buffer))
        # self._stdout_thread.daemon = True
        # self._stdout_thread.start()
        #
        # self._stderr_buffer = BytesIO()
        # self._stderr_thread = threading.Thread(target=self._readerthread,
        #                                        args=(self.proc.stderr, self._stderr_buffer))
        # self._stderr_thread.daemon = True
        # self._stderr_thread.start()
        #
        # self._stdin_buffer = BytesIO()
        # self._stdin_thread = threading.Thread(target=self._writerthread,
        #                                       args=(self.proc.stdin, self._stdin_buffer))
        # self._stdin_thread.daemon = True
        # self._stdin_thread.start()

    def _readerthread(self, fh, buffer):
        print("--------------------------")
        print("DEBUG: fh: {}".format(type(fh)))
        print("DEBUG: buffer: {}".format(type(buffer)))
        print("DEBUG: buffer.closed: {}".format(buffer.closed))
        while not buffer.closed:
            b = fh.read1()
            print("read: {}".format(b))
            buffer.write(b)

    def _writerthread(self, fh, buffer):
        print("--------------------------")
        print("DEBUG: fh: {}".format(type(fh)))
        print("DEBUG: buffer: {}".format(type(buffer)))
        print("DEBUG: buffer.closed: {}".format(buffer.closed))
        while not buffer.closed:
            print("try writing to stdin")
            b = buffer.read1()
            if b:
                print("write: {}".format(b))
                fh.write(b)

    def __del__(self):
        print("end shell")
        self.proc.stdin.write(b"exit\n")
        #self.proc.stdin.flush()
        exitcode = self.proc.wait(timeout=0.5)
        if exitcode is None:  # timed out
            self.proc.terminate()


# def filler(buffer):
#     print("start filler")
#     while True:
#         print("command")
#         buffer.write(b"echo some\n")
#         #buffer.flush()


shell = RemoteShellWrapper()
from time import sleep

sleep(1)


while not shell.stdout_reader._q.empty():
    print("stdout: %s" % shell.stdout_reader.readline().decode())
while not shell.stderr_reader._q.empty():
    print("stderr: %s" % shell.stderr_reader.readline().decode())

print("writing to stdin")
shell.proc.stdin.write(b"uname -a\n")
shell.proc.stdin.flush()

sleep(1)

while not shell.stdout_reader._q.empty():
    print("stdout: %s" % shell.stdout_reader.readline().decode())
while not shell.stderr_reader._q.empty():
    print("stderr: %s" % shell.stderr_reader.readline().decode())
