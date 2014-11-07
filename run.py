from eve import Eve
from os import walk, path

#from tendo import singleton
#me = singleton.SingleInstance()

app = Eve()

extra_dirs = ['./',]
extra_files = extra_dirs[:]
for extra_dir in extra_dirs:
    for dirname, dirs, files in walk(extra_dir):
        for filename in files:
            filename = path.join(dirname, filename)
            if path.isfile(filename):
                extra_files.append(filename)

if __name__ == '__main__':
    app.run(debug=True,extra_files=extra_files)