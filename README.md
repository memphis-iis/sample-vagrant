sample-vagrant README
======================

A small sample application that uses Vagrant for setup.

A Vagrantfile has been supplied so that you can use vagrant to run this application
in a virtual machine. The virtual machine abstracts away the various setup steps
you need to get a testable version of your application running, and it allows you
to continue to use whatever code editors and other tools you like in your current
operating system. We'll cover the few one-time steps you need to perform so that you
can use vagrant, a one-time setup for this project, and the common development
activities that you'll want to know about

Using this repository
------------------------

Instructions follow for using this simple demo. If you already understand Vagrant,
then you can just copy the Vagrantfile, and .provisioning_script.sh, make the changes
you need, and start working. If you've never used Vagrant before, you can proceed with
the information below to get it set up and working for this small application.

One-Time Setup for Vagrant
-------------------------------

 * Install git if you haven't already (which you already have since this is on GitHub)
 * Install VirtualBox if you haven't already: 
   [https://www.virtualbox.org/wiki/Downloads](https://www.virtualbox.org/wiki/Downloads)
 * Install vagrant if you havent' already: 
   [https://www.vagrantup.com/downloads.html](https://www.vagrantup.com/downloads.html)

One-Time Setup for an application
----------------------------------

Now that you have vagrant and virtual box installed, you need to get the application
set up for development. If you haven't already, you need to clone the code
repository. From your command prompt, clone the repository and then enter the new]
directory:

    $ git clone https://github.com/memphis-iis/sample-vagrant.git
    $ cd sample-vagrant

Now you're ready to use vagrant to set up your development environment. First,
we'll ask vagrant to download a "box"; this is a "base" image that we use as a
starting point. Assuming that you're in the sample-vagrant directory that we
clonedabove:

    $ vagrant box add ubuntu/trusty64

This will download a virtual machine image. ***WARNING:*** this may take a while,
but you should only need to do this once. If for some reason it should fail (which
may happen if you have an intermittent internet connection), you can just repeat
the command.

Now we will have vagrant configure and start the virtual machine. Again, from the
directory you created above:

    $ vagrant up

This will start the virtual machine. Since this is the first time you've actually
started it, a provisioning scripting will run. This script will take some time
since it will doing a variety of things, including downloading and installing
software. If this step fails and you are given an error message, the safest way
to restart is to destroy the virtual machine and start over:

    $ vagrant destroy
    $ vagrant up

Note that you can also re-initialize your virtual machine to it "original" state
this way if you want to discard any changes you've made to the virtual machine's
environment.

When everything is finished, you're ready to begin development.

Typical Startup for Development
--------------------------------

Typically, you want to change files inside the project, then run the application
and test your changes. Note that this means that you are changing code, committing
changes with Git, etc on your "host" operating system where you are comfortable with
the available tools. The vagrant guest "box" is for testing (or demonstrating)
your changes.

When using vagrant, you first open a command prompt (or terminal), navigate to the
application directory, and use vagrant to run your virtual machine:

    $ cd sample-vagrant
    $ vagrant up

***HINT:*** This should look familiar - `vagrant up` was the final setup step
we used in our one-time setup above. However, it should run much faster now since
the virtual machine has already been created and provisioned.

Once the virtual machine starts up, you can connect to it and run code. Assuming
that you're still in the same command prompt that you opened above:

    $ vagrant ssh

*ssh is in the git/bin directory and may need to be added to path manually

The command prompt should look different now: you are at a shell prompt in the
virtual machine. Since your application repository is shared with the VM, you can
just `cd` into it to start the application.

    $ cd workspace
    $ ./run.sh
    
Ports for the application and MongoDB are already shared. Once you've started
the application (after you've run `./run.sh` as above), you can connect from
your host operating system at 
[http://localhost:3000/](http://localhost:3000/)

You can also connect to the MongoDB instance with your tool of choice (for instance,
Robomongo) on your host operating system connecting to `localhost` at port `30017`.
Note that inside the virtual machine, the port for MongoDB is the default `27017`.

As has been implied above, the general idea is that you edit source code, look at
data, test the application, commit code to the repository, etc. in your host
operating system. The vagrant-controlled virtual machine is where you execute the
project in a suitable environment for testing.

When you're done with development
----------------------------------------

Once you are done developing, you should shut down your environment cleanly. If
you still have mofacts running, stop it with CTRL+C. Then you can exit the SSH
session by entering `exit` at the command prompt in the virtual machine. After
you exit, you should be back your host environment where you originally entered
`vagrant ssh`. From here you can stop the virtual machine:

    $ vagrant halt

This is fine for the end of a development session, but if you want to completely
remove the virtual machine from your computer you can destroy it:

    $ vagrant destroy
    
This is a fairly low risk activity, since you can always run `vagrant up` to
recreate the virtual machine for you.
