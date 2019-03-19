#!/usr/bin/env python3

import os
import sys
import shutil
import subprocess
import tarfile

edges = ['vc-b1-edge1-A', 
         'vc-b1-edge1-B',
         'vc-b3-edge1-A',
         'vc-b3-edge1-B',
         'vc-b2-edge1',
         'vc-b4-edge1',
         'vc-b5-edge1',
          ]
gateways = ['vc-gateway-1', 'vc-gateway-2']

tmux_contents = '''set-option -g prefix C-a
unbind-key C-b
bind-key C-a last-window
'''

gdbinit_contents = '''set non-stop on
set print pretty on
set pagination off

define _br
        break vc_pkt_print_track
        disable
        commands
                pkt_bmap_dump pkt->bmap
                continue
        end
end
'''

executable_name = os.path.basename(__file__)
lxc_root = '/var/lib/lxc/%s/rootfs'

def touch(fname, times=None):
    print ("Touching file: ", fname)
    with open(fname, 'a'):
        os.utime(fname, times)

def copy_file(src, dst, debug=False):
    print ("Copying", src, 'to', dst)
    if not debug:
        #shutil.copy (src, dst)
        subprocess.run(["cp", "-f", src, dst])

def debug_binaries(nodes, binary_name):
    path = lxc_root + "/opt/vc/sbin/" + binary_name
    for i in nodes:
        print ("Node: ", i)
        subprocess.run(["ls", "-la", path%i])
        subprocess.run(["ls", "-la", path%i+'.orig'])
        if os.path.exists(path%i+'.fix'):
            subprocess.run(["ls", "-la", path%i+'.fix'])

def _install_binaries(binary_name, nodes, src_prefix=None, dst_prefix=None):
    if src_prefix is None and dst_prefix is None:
        print ("Ignore copying same file")
        return

    src = dst = lxc_root + '/opt/vc/sbin/' + binary_name
    if src_prefix: src += src_prefix
    if dst_prefix: dst += dst_prefix

    for i in nodes:
        copy_file(src%i, dst%i)

def install_binaries(binary_name, nodes):
    binary_to_copy = '/root/' + binary_name
    fixed_binary = lxc_root + '/opt/vc/sbin/' + binary_name + '.fix'

    # Copy binary as binary.fix
    if os.path.exists(binary_to_copy):
        for i in nodes:
            copy_file(binary_to_copy, fixed_binary%i)
        os.remove(binary_to_copy)

    _install_binaries(binary_name, nodes, src_prefix='.fix', dst_prefix=None)

def install_orig_binaries(binary_name, nodes):
    _install_binaries(binary_name, nodes, src_prefix='.orig', dst_prefix=None)

def backup_orig_binaries(binary_name, nodes):
    _install_binaries(binary_name, nodes, src_prefix=None, dst_prefix='.orig')

def initial_setup():
    os.chdir('/root')

    # Backup the original binaries
    backup_orig_binaries('edged', edges)
    backup_orig_binaries('gwd', gateways)

    # Create tmux file
    with open('.tmux.conf', 'w') as output:
        output.write(tmux_contents)

    # Create gdbinit file in all the edges
    for i in edges:
        with open((lxc_root + '/root/.gdbinit')%i, 'w') as output:
            output.write(gdbinit_contents)


def extract_binaries():
    print ("Extracting binaries ...")
    tar = tarfile.open("/root/bin.tar.xz", "r:xz")
    tar.extractall()
    tar.close()
    os.remove("/root/bin.tar.xz")
    shutil.move("./build/x86_64/bin/edged", ".")
    shutil.move("./build/x86_64/bin/gwd", ".")
    shutil.rmtree("./build")
    print ("Extracted successfully !!!\n\n")
    pass

def main():
    # Initial setup
    orig_marker = '/root/.setup.done'
    if not os.path.exists(orig_marker):
        print ("Setting up edge for first time ...")
        initial_setup()
        touch(orig_marker) # Create a marker
        return

    # Install original files
    if 'orig' in sys.argv or 'ori' in sys.argv:
        install_orig_binaries('edged', edges)
        install_orig_binaries('gwd', gateways)
    elif 'debug' in sys.argv:
        debug_binaries(edges, 'edged')
        debug_binaries(gateways, 'gwd')
    else:
        # Install compiled binary files
        if os.path.exists('/root/bin.tar.xz'):
            extract_binaries()
        install_binaries('edged', edges)
        install_binaries('gwd', gateways)

if __name__ == '__main__':
    main()
