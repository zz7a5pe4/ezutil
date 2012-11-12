#!/usr/bin/python

#import cmd2 as cmd
import cmd
import os

class HelloWorld(cmd.Cmd):
    """Simple command processor example."""
    
    FRIENDS = [ 'Alice', 'Adam', 'Barbara', 'Bob' ]
    prompt = '% '
    intro = "Simple command processor example." 
    def do_greet(self, person):
        "Greet the person"
        if person and person in self.FRIENDS:
            greeting = 'hi, %s!' % person
        elif person:
            greeting = "hello, " + person
        else:
            greeting = 'hello'
        print greeting

    def help_greet(self):
        print '\n'.join([ 'greet [person]',
                           'Greet the named person',
                           ])
    
    def complete_greet(self, text, line, begidx, endidx):
        if not text:
            completions = self.FRIENDS[:]
        else:
            completions = [ f
                            for f in self.FRIENDS
                            if f.startswith(text)
                            ]
        return completions
 
    def do_shell(self, line):
        "Run a shell command"
        print "running shell command:", line
        output = os.popen(line).read()
        print output
        self.last_output = output

    def do_exit(self, line):
        return True
    def do_EOF(self, line):
        return True   
    def postloop(self):
        print

if __name__ == '__main__':
    HelloWorld().cmdloop()
