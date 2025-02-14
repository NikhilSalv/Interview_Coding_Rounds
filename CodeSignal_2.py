"""Your task is to implement a simulation of a
change directory command. This command changes the current
working directory to the specified one.
The initial working directory is root i.e. / . You are given a list of cd commands
commands
There are multiple options for command arguments.
• cd / - changes the working directory to the root directory.
• cd. - stays in the current directory.
• cd .. - moves the working directory one level up. In the root directory, cd..
does nothing.
• cd < subdirectory> - moves to the specified subdirectory within the current working directory.
< subdirectory> is a string consisting of only lowercase English"""

"""Example
For
commands = ["cd users", "cd codesignal", "cd ..", "cd admin"]
the output should be solution (commands) = '/users/admin' """

def Solution(array):
  path_stack = []
  for command in array:
    if command == "cd ..":
      pass
    elif command == "cd .":
      continue
    elif command == "cd /":
      path_stack = []
    else:
      directory = command.split(" ")[1]
      path_stack.append(command)

return "/" + "/".join("path_stack")


if __name__ == "__main__":
  commands = ["cd users", "cd codesignal", "cd ..", "cd admin"]
  print(Solution(commands))
