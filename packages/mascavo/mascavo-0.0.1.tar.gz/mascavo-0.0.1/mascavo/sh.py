import os
import subprocess
import logging


def clean(stream):
    try:
        return [line.decode("utf-8").replace('\n', '') for line in stream]
    except UnicodeDecodeError:
        return [line.decode("ISO-8859-1").replace('\n', '') for line in stream]


def sh(command, stdin=None):
    """
    Executa um comando sh passando stdin como entrada do comando
    :param command: comando
    :param stdin: entrada
    :return: saída do comando
    """
    if stdin:
        read, write = os.pipe()
        os.write(write, stdin.encode())
        os.close(write)
    else:
        read = None

    process = subprocess.Popen(
        command,
        shell=True,
        stdin=read,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    output = process.stdout.readlines()
    error = process.stderr.readlines()

    output = clean(output)
    error = clean(error)
    result = output + error

    # loglevel = logging.info if not len(error) else logging.warning
    loglevel = logging.info
    loglevel(
        "command = `%s`\n"
        "output = '%s'"
        % (command, result)
    )

    return output + error


def incremental_output(command):
    import subprocess
    import shlex
    # TODO: adicionar essa implementação no comando sh

    process = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE)
    full_output = []
    while True:
        output = process.stdout.readline()
        if output == b'' and process.poll() is not None:
            break
        if output:
            print(output.strip())
            full_output += [output.strip()]
    rc = process.poll()
    return [line.decode('utf-8') for line in full_output]
