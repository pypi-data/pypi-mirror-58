from __future__ import print_function

import csv
import hashlib
import os.path
import re
import time
from collections import OrderedDict
from zipfile import ZIP_DEFLATED, ZipInfo, ZipFile
import tempfile
from wheel.cli import WheelError
from wheel.util import urlsafe_b64decode, as_unicode, native, urlsafe_b64encode, as_bytes, StringIO

# Non-greedy matching of an optional build number may be too clever (more
# invalid wheel filenames will match). Separate regex for .dist-info?
WHEEL_INFO_RE = re.compile(
    r"""^(?P<namever>(?P<name>.+?)-(?P<ver>.+?))(-(?P<build>\d[^-]*))?
     -(?P<pyver>.+?)-(?P<abi>.+?)-(?P<plat>.+?)\.whl$""",
    re.VERBOSE)


def get_zipinfo_datetime(timestamp=None):
    # Some applications need reproducible .whl files, but they can't do this without forcing
    # the timestamp of the individual ZipInfo objects. See issue #143.
    timestamp = int(os.environ.get('SOURCE_DATE_EPOCH', timestamp or time.time()))
    return time.gmtime(timestamp)[0:6]
import os, sys
from tkinter import *
from tkinter.filedialog import *
try:
    import tkinter as tk  # for python 3
except:
    import Tkinter as tk  # for python 2
import pygubu
wheel_file = None
class WheelFile(ZipFile):
    """A ZipFile derivative class that also reads SHA-256 hashes from
    .dist-info/RECORD and checks any read files against those.
    """

    _default_algorithm = hashlib.sha256

    def __init__(self, file, mode='r', dist=''):
        basename = os.path.basename(file)
        self.parsed_filename = WHEEL_INFO_RE.match(basename)

        ZipFile.__init__(self, file, mode, compression=ZIP_DEFLATED, allowZip64=True)

        self.dist_info_path = dist
        self.record_path = self.dist_info_path + '/RECORD'
        self._file_hashes = OrderedDict()
        self._file_sizes = {}
        if mode == 'r':
            # Ignore RECORD and any embedded wheel signatures
            self._file_hashes[self.record_path] = None, None
            self._file_hashes[self.record_path + '.jws'] = None, None
            self._file_hashes[self.record_path + '.p7s'] = None, None

            # Fill in the expected hashes by reading them from RECORD
            try:
                record = self.open(self.record_path)
            except KeyError:
                raise WheelError('Missing {} file'.format(self.record_path))

            with record:
                for line in record:
                    line = line.decode('utf-8')
                    path, hash_sum, size = line.rsplit(u',', 2)
                    if hash_sum:
                        algorithm, hash_sum = hash_sum.split(u'=')
                        try:
                            hashlib.new(algorithm)
                        except ValueError:
                            raise WheelError('Unsupported hash algorithm: {}'.format(algorithm))

                        if algorithm.lower() in {'md5', 'sha1'}:
                            raise WheelError(
                                'Weak hash algorithm ({}) is not permitted by PEP 427'
                                .format(algorithm))

                        self._file_hashes[path] = (
                            algorithm, urlsafe_b64decode(hash_sum.encode('ascii')))

    def open(self, name_or_info, mode="r", pwd=None):
        def _update_crc(newdata, eof=None):
            if eof is None:
                eof = ef._eof
                update_crc_orig(newdata)
            else:  # Python 2
                update_crc_orig(newdata, eof)

            running_hash.update(newdata)
            if eof and running_hash.digest() != expected_hash:
                raise WheelError("Hash mismatch for file '{}'".format(native(ef_name)))

        ef = ZipFile.open(self, name_or_info, mode, pwd)
        ef_name = as_unicode(name_or_info.filename if isinstance(name_or_info, ZipInfo)
                             else name_or_info)
        if mode == 'r' and not ef_name.endswith('/'):
            if ef_name not in self._file_hashes:
                raise WheelError("No hash found for file '{}'".format(native(ef_name)))

            algorithm, expected_hash = self._file_hashes[ef_name]
            if expected_hash is not None:
                # Monkey patch the _update_crc method to also check for the hash from RECORD
                running_hash = hashlib.new(algorithm)
                update_crc_orig, ef._update_crc = ef._update_crc, _update_crc

        return ef

    def write_files(self, base_dir):
        logger.info("creating '%s' and adding '%s' to it", self.filename, base_dir)
        deferred = []
        for root, dirnames, filenames in os.walk(base_dir):
            # Sort the directory names so that `os.walk` will walk them in a
            # defined order on the next iteration.
            dirnames.sort()
            for name in sorted(filenames):
                path = os.path.normpath(os.path.join(root, name))
                if os.path.isfile(path):
                    arcname = os.path.relpath(path, base_dir)
                    if arcname == self.record_path:
                        pass
                    elif root.endswith('.dist-info'):
                        deferred.append((path, arcname))
                    else:
                        self.write(path, arcname)

        deferred.sort()
        for path, arcname in deferred:
            self.write(path, arcname)

    def write(self, filename, arcname=None, compress_type=None):
        with open(filename, 'rb') as f:
            st = os.fstat(f.fileno())
            data = f.read()

        zinfo = ZipInfo(arcname or filename, date_time=get_zipinfo_datetime(st.st_mtime))
        zinfo.external_attr = st.st_mode << 16
        zinfo.compress_type = ZIP_DEFLATED
        self.writestr(zinfo, data, compress_type)

    def writestr(self, zinfo_or_arcname, bytes, compress_type=None):
        try:
            zinfo_or_arcname = zinfo_or_arcname.replace('\\', '/')
        except:
            pass
        ZipFile.writestr(self, zinfo_or_arcname, bytes, compress_type)
        fname = (zinfo_or_arcname.filename if isinstance(zinfo_or_arcname, ZipInfo)
                 else zinfo_or_arcname)
        logger.info("adding '%s'", fname)
        if fname != self.record_path:
            hash_ = self._default_algorithm(bytes)
            self._file_hashes[fname] = hash_.name, native(urlsafe_b64encode(hash_.digest()))
            self._file_sizes[fname] = len(bytes)

    def close(self):
        # Write RECORD
        if self.fp is not None and self.mode == 'w' and self._file_hashes:
            data = StringIO()
            writer = csv.writer(data, delimiter=',', quotechar='"', lineterminator='\n')
            writer.writerows((
                (
                    fname,
                    algorithm + "=" + hash_,
                    self._file_sizes[fname]
                )
                for fname, (algorithm, hash_) in self._file_hashes.items()
            ))
            writer.writerow((format(self.record_path), "", ""))
            zinfo = ZipInfo(native(self.record_path), date_time=get_zipinfo_datetime())
            zinfo.compress_type = ZIP_DEFLATED
            zinfo.external_attr = 0o664 << 16
            self.writestr(zinfo, as_bytes(data.getvalue()))

        ZipFile.close(self)
def warn():
    from tkinter import messagebox
    messagebox.showinfo('warning!!!', 'plz first select an wheel file as target file')
def show(msg, title=''):
    from tkinter import messagebox
    messagebox.showinfo(title, msg)
from wheel import wheelfile as whl
def save_file(*args, **kwargs):
    global wheel_file
    file = asksaveasfilename(defaultextension = '.whl',
                filetypes = [('wheel files', '.whl'), ('all files', '.*'),])
    if not file.endswith('.whl'):
        file += '.whl'
    try:
        open(file, 'w+').close()
        
    except:
        os.remove(file)
        file = file.replace('.whl', '-0.0.0-py3.py2-none-any.whl')
    with open(file, 'w+') as fh:
        pass
    wheel_file = WheelFile(file, mode='w')
def all_dict(dictory, exceptions=None, file_types=None, maps=True, files=True, print_data=False):
    import os
    global ti
    ti = ''
    data = []
    string_data = ''
    e = exceptions
    if 'list' in str(type(e)) or e == None:
        pass
    else:
        raise TypeError('expected a list but got a %s' % type(e))
    e = file_types
    if 'list' in str(type(e)) or e == None:
        pass
    else:
        raise TypeError('expected a list but got a %s' % type(e))
    
    print_ = print_data
    
    for dirname, dirnames, filenames in os.walk(dictory):
        # print path to all subdirectories first.
        if maps:
            for subdirname in dirnames:
                dat = os.path.join(dirname, subdirname)
                data.append(dat)
                string_data = string_data + '\n' + dat
                if print_:
                    print(dat)

        # print path to all filenames.
        if files:
            for filename in filenames:
                s = False
                fname_path = filename
                file = fname_path.split('.', 1)
                no = int(len(file) - 1)
                file_type = '/*.' + str(file[-1])
                ti += file_type
                if not e == None:
                    for b in range(0, len(e)):
                        if e[b] == file_type:
                            s = True
                            
                if e == None:
                    s = True
                if s:
                    s = False   
                            
                    dat = os.path.join(dirname, filename)
                    data.append(dat)
                    string_data = string_data + '\n' + dat
                    if print_:
                        
                        print(dat)
        

        # Advanced usage:
        # editing the 'dirnames' list will stop os.walk() from recursing into there.
        if not exceptions == None:
            
            for ip in range(0, int(len(exceptions))):
                exception = exceptions[ip]
                
                if exception in dirnames:
                    # don't go into any .git directories.
                    dirnames.remove(exception)
    
    for dire in data:
        yield dire
from tkinter.filedialog import *
Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
from tkinter import simpledialog as dia
def askstr(msg):
    return dia.askstring('input box', msg)
def explorer_dict(dialog=askopenfilename, **kwargs):
    filename = dialog(**kwargs) # show an "Open" dialog box and return the path to the selected file
    if dialog == askopenfilename:
        path_split = filename.split('\\')
        le = int(len(path_split) - 1)
        file = path_split[le]
        path_list = list()
        index = -1
        while index < le:
            index += 1
            path_list.append(path_split[index])
        path = ''.join(path_list)
    else:
        file = ''
        path = filename
        path_list=[]
    return {'filepath': filename, 'file': file, 'path': path,\
            'path_list': path_list, 'list': [file, filename, path, path_list]}
def add_folder(*args, **kwargs):
    global wheel_file
    if wheel_file == None:
        print('please select first an file to write the wheel in')
        warn()
        return
    file = explorer_dict(dialog=askdirectory)['filepath']
    for i in all_dict(file, maps=False):
        path = i.replace(file, '')
        data = open(i, 'rb').read()
        wheel_file.writestr(path, data)
    show('succes fully added folder to wheel file', 'succes')
def add_file(*args, **kwargs):
    global wheel_file
    if wheel_file == None:
        print('please select first an file to write the wheel in')
        warn()
        return
    file = explorer_dict()['filepath']
    delete = askstr('''you have now filepath: %s. do you want to keep the whole file path typ then: None
if you want to have only the file name typ: filename
else if you want to delete just a part of the path you typ the part of the path you want to delete''' % file)
    if delete.lower() == 'none':
        path = file
    elif delete.lower() == 'filename':
        path = os.path.basename(file)
    else:
        path = file.replace(delete, '')
    with open(file, 'rb') as fh:
        data = fh.read()
    wheel_file.writestr(file, data)
    show('succes added file to wheel file', 'succes')
def add_files(*args, **kwargs):
    global wheel_file
    if wheel_file == None:
        print('please select first an file to write the wheel in')
        warn()
        return
    file = explorer_dict(dialog=askopenfilenames)['filepath']
    for i in file:
        delete = askstr('''you have now filepath: %s. do you want to keep the whole file path typ then: None
if you want to have only the file name typ: filename
else if you want to delete just a part of the path you typ the part of the path you want to delete''' % i)
        if delete.lower() == 'none':
            path = file
        elif delete.lower() == 'filename':
            path = os.path.basename(file)
        else:
            path = file.replace(delete, '')
        data = open(i, 'rb').read()
        wheel_file.writestr(path, data)
    show('succes added files to wheel file', 'succes')
def close():
    global wheel_file
    if wheel_file == None:
        print('please select first an file to write the wheel in')
        warn()
        return
    wheel_file.close()
    wheel_file = None
    print('closed')
    show('safed file succes', 'closed')
def read():
    file_ = askopenfilename()
    data = open(file_, 'rb').read()
    with open('temp.zip', 'wb') as fh:
        fh.write(data)
        file_ = fh.name
    import time
    time.sleep(1)
    wheelfile = ZipFile(file_, 'r')
    wheelfile = wheelfile
    end_dir = askdirectory()
    if not os.path.isdir(end_dir):
        os.mkdir(end_dir)
    files = wheelfile.namelist()
    for file in files:
        logger.info('extracting: %s' % file)
        wheelfile.extract(file, end_dir)
        logger.info('extracted: %s' % file)
    wheelfile.close()
    os.remove(file_)
    logger.info(('%s files extracted to %s' % (str(len(files)), end_dir), 'succes'))
    show('%s files extracted to %s' % (str(len(files)), end_dir), 'succes')
import zipfile
def con():
    global wheel_file
    if wheel_file == None:
        print('please select first an file to write the wheel in')
        warn()
        return
    file = explorer_dict(defaultextension = '.zip',
                filetypes = [('Zip files', '.zip'), ('all files', '.*'),])['filepath']
    import zipfile
    import shutil
    widgets.info.config(text='opening selected zip file...')
    zipper = zipfile.ZipFile(file)
    end_dir = 'uhfdsidsuifsdhiaufhdiashvishsuyfgibwucfW'
    try:
        shutil.rmtree(end_dir)
    except:
        pass
    os.mkdir(end_dir)
    zipper.extractall(path=end_dir)
    zipper.close()
    for i in all_dict(end_dir, maps=False):
        widgets.info.config('fprocessing file: {i}')
        path = i.replace(file, '')
        path = i.replace(end_dir, '')
        data = open(i, 'rb').read()
        wheel_file.writestr(path, data)
    close()
    widgets.info.config(text='removing temp dictory...')
    for i in range(100):
        try:
            shutil.rmtree(end_dir)
        except:
            pass
    widgets.info.config(text='done!')
    import time
    time.sleep(1)
    show('succes fully converted zip to wheel', 'succes')
def conz():
    file = explorer_dict(defaultextension = '.whl',
                filetypes = [('wheel files', '.whl'), ('all files', '.*'),])['filepath']
    import zipfile
    import shutil
    global widgets
    widgets.info.config(text='opening selected wheel file')
    zipper =  zipfile.ZipFile(file)
    end_dir = 'uhfdsidsuifsdhiaufhdiashvishsuyfgibwucfW'
    try:
        shutil.rmtree(end_dir)
    except:
        pass
    os.mkdir(end_dir)
    zipper.extractall(path=end_dir)
    zipper.close()
    file = explorer_dict(dialog=asksaveasfilename, defaultextension = '.zip',
                filetypes = [('zip files', '.zip'), ('all files', '.*'),])['filepath']
    open(file, 'w+').close()
    en = zipfile.ZipFile(file, 'w')
    for i in all_dict(end_dir, maps=False):
        widgets.info.config(text=f'processing file: {i}')
        path = i.replace(file, '')
        path = i.replace(os.path.abspath('\\' + end_dir), '')
        data = open(i, 'rb').read()
        en.writestr(path, data)
    en.close()
    widgets.info.config(text='deleting temp dictory...')
    for i in range(100):
        try:
            shutil.rmtree(end_dir)
        except:
            pass
    widgets.info.config(text='status: done!')
    import time
    time.sleep(1)
    widgets.info.config(text='None')
    show('succes fully converted zip to wheel', 'succes')
from tkinter import *

class Application:
    def __init__(self):

        
        root = Tk(className='wheel build')
        root.geometry('400x300')
        def get_button(button):
            assert isinstance(button, str), str(f'excpected an string but got an {type(button)}')
            return widgets[button.lower()]
        global widgets
        class my_class(dict):
            def __init__(self):
                dict.__init__(self)
        widgets = my_class()
        btn = Button(root, text='add folder', command=add_folder)
        btn.place(x='0',y='0')
        widgets['add folder'] = btn
        btn = Button(root, text='add file', command=add_file)
        btn.place(x=70,y=0)
        widgets['add file'] = btn
        btn = Button(root, text='target file', command=save_file)
        btn.place(x=140,y=0)
        widgets['target file'] = btn
        btn = Button(root, text='save', command=close)
        btn.place(x=0,y=40)
        widgets['save'] = btn
        btn = Button(root, text='add files', command=add_files)
        btn.place(x=70,y=40)
        widgets['add files'] = btn
        btn = Button(root, text='extract wheel file', command=read)
        btn.place(x=140,y=40)
        widgets['extract wheel file'] = btn
        btn = Button(root, text='convert zip to whl', command=con)
        btn.place(x=0, y=80)
        widgets['convert zip to whl'] = btn
        btn = Button(root, text='convert whl to zip', command=conz)
        btn.place(x=140, y=80)
        widgets['convert whl to zip'] = btn
        label = Message(root, text='first you need to select a file.\n you do that when you press the button target file.\n then you can choise add an folder, files or one file.\n if you have choise everything you want you just press the save button to close the file')
        label.place(x=0,y=120)
        widgets['help'] = label
        label = Label(root, text='info:')
        label.place(x=0, y=250)
        widgets['working on...'] = label
        global mesg
        label = Text(root)
        
        label.place(x=50, y=250, width=550,height=20)
        widgets.info = label
        widgets.info = label
        global info
        class log():
            def __init__(self, label):
                self.master = label
            def info(self, *args):
                global mesg
                self.master.delete('1.0',END)
                self.master.insert(END, ''.join(args))
                print(''.join(args))
            def update(self):
                self.master.mark_set(INSERT, END)
                self.master.update()
                self.master.update_idletasks()
        global logger
        logger = log(widgets.info)
        info = 'info'
        def update():
            logger.update()
            root.after(10, update)
        root.geometry('700x300')
        root.after(50, update)
        root.mainloop()
def main():
    app = Application()
if __name__ == '__main__':
    main()


