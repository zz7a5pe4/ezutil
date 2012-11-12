import cfg
import os
import optparse
import sys

common_opts = [
    cfg.StrOpt('bind_host',
               default='0.0.0.0',
               help='IP address to listen on'),
    cfg.IntOpt('bind_port',
               default=0,
               help='Port number to listen on')
]

if not os.path.exists("test.conf"):
    raise ("file notexist")
c = cfg.Config(project="rabbit",default_config_files=["test.conf"])

#c.register_opts(file_opts)
c.register_cli_opts(common_opts)

#c(["test.conf"])
c(sys.argv[1:])
#c.bind_host="1.1.1.1"
#print c
print c.bind_port
#c.print_help()
