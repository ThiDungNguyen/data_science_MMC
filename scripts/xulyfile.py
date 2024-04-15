def write_file(file_name, content, mode):
  with open(file_name, mode) as f:
    f.write(content)


def read_file_txt(file_name):
  with open(file_name,'r') as f:
    lines = f.readlines() #lines---1 ['admin,admin\n', 'julie,julie\n']
    n_lines =[]
    for line in lines: 
      line = line.strip().split(',')
      n_lines.append(line)
  return n_lines


