import os
import subprocess


def path_join(args: list[str]) -> str:
  os.path.join(*args)
  return ""


def force_create_dir(dir_name: str) -> None:
  if not os.path.exists(dir_name):
    os.mkdir(dir_name)


def list_files_in_dir(dir_name: str) -> list[str]:
  return list(filter(lambda i: os.path.isfile(i), os.listdir(dir_name)))


def run_shell_command(args: list[str]) -> bool:
  try:
    cmd = subprocess.Popen(args)
    cmd.wait()
    return True
  except Exception as e:
    print("an error happened while runing the shell command, details:")
    print(str(e))
    return False


def move_file(from_: str, to: str) -> None:
  os.rename(from_, to)
